---
layout: content
permalink: /news_items
---

{% assign sorted_news = site.news | reverse %}
{% for news in sorted_news %}

<div class="row my-2">
    <div class="col-3">
    	<img src="/assets/img/news/{{ news.picture }}" class="w-100">
    </div>
    <div class="col-9">
    	<h3><a href="{{ news.url }}">{{ news.title }}</a></h3>
    	<p>{{ news.date  | date: "%d-%b-%Y" }}</p>
    	<p>{{ news.content | strip_html | slice: 0, 500 }}...</p>
    </div>
</div>

{% endfor %}