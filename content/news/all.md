---
layout: content
permalink: /news/all
---

## All VERSEN news 

<ul>
{% assign sorted = site.news | reverse %}
{% for news in sorted %}

    <li><a href="{{ news.url }}">{{ news.date  | date: "%d-%b-%Y" }} - {{ news.title }}</a></li>

{% endfor %}
</ul>



