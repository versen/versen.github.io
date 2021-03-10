#!/bin/python3
import argparse
import base64
import json
import locale
import os
from urllib import request, parse


def get_members(token, list_id, segment_id=None, count=999):
  """Collect members in a list or segment using Mailchimp API"""

  api_key, server = token.split('-')
  segment = f'/segments/{segment_id}' if segment_id else ''
  url = f'https://{server}.api.mailchimp.com/3.0/lists/{list_id}{segment}/members?count={count}'
  
  req = request.Request(url)
  base64string = base64.b64encode(bytes('user:%s' % api_key,'ascii'))
  req.add_header('Authorization', 'Basic %s' % base64string.decode('utf-8'))

  res = request.urlopen(req)
  res_dict = json.loads(res.read())
  return {'count': res_dict['total_items'], 'members': res_dict['members']}


def get_member_info(m):
  """Derive name and affiliation from a Mailchimp member dictionary."""

  # get full name
  name = f'{m["merge_fields"]["FNAME"]} {m["merge_fields"]["LNAME"]}'
  
  # treat affiliation(s)
  affiliation = ''
  m["merge_fields"]["AFFIL1"] = m["merge_fields"]["AFFIL1"].strip()
  m["merge_fields"]["AFFIL2"] = m["merge_fields"]["AFFIL2"].strip()
  
  if m["merge_fields"]["AFFIL1"] not in (None, '', 'a', 'N/A'):
    affiliation = f'*{m["merge_fields"]["AFFIL1"]}*'
  
  if m["merge_fields"]["AFFIL2"] not in (None, '', 'a', 'N/A'):
    if affiliation:
      affiliation += f' and *{m["merge_fields"]["AFFIL2"]}*'
    else:
      affiliation = f'*{m["merge_fields"]["AFFIL2"]}*'

  # member text
  if affiliation:
    return name + ', ' + affiliation
  else:
    return name


def generate_list_md(total_members, visible_members):
  """Create the text for the file list.md from Mailchimp list of members."""

  template = '---\nlayout: content\npermalink: /users\n---\n\n'
  template += f'VERSEN currently has **{total_members}** members.\n\n'
  template += f'The following members allowed us to share their information.\n\n'
  
  for m in visible_members:
    # skip exceptional cases
    if m["merge_fields"]["LNAME"] == 'Abc':
      continue
    
    template += f'- {get_member_info(m)}\n'

  return template


if __name__ == "__main__":
  locale.setlocale(locale.LC_ALL, '')
  
  parser = argparse.ArgumentParser(description='Update list of visible VERSEN members using Mailchimp.')
  parser.add_argument('-k', '--api-key', 
    default=os.environ.get('VERSEN_MC_KEY'),
    help='Mailchimp API key (e.g., a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9a9-us1).\nCan be set using the environment variable VERSEN_MC_KEY.')
  parser.add_argument('-o', '--output', 
    default=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'content', 'members', 'list.md'), 
    help='Default: <root>/content/members/list.md')
  
  args = parser.parse_args()
  if not args.api_key:
    print('Error: api-key not set.\n')
    parser.print_help()
    exit(0)
  
  visible_members = get_members(token=args.api_key, list_id='5228435632', segment_id='3577467', count=999)
  invisible_members = get_members(token=args.api_key, list_id='5228435632', segment_id='3577471', count=1)
  total_members = visible_members['count'] + invisible_members['count']
  visible_members['members'].sort(key=lambda m: locale.strxfrm(m["merge_fields"]["FNAME"]))
  
  with open(args.output, 'w') as f:
    text = generate_list_md(total_members=total_members, visible_members=visible_members['members'])
    f.write(text)
