---
layout: archive
title: "Papers"
permalink: /papers/
author_profile: true
---

You can also find my papers (preprints) on [my arXiv page](https://arxiv.org/a/enomoto_h_1.html).

{% include base_path %}

# Publications

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

# Preprints

{% for post in site.preprints reversed %}
  {% include archive-single.html %}
{% endfor %}
