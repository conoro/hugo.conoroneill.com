---
title: "Numb-nut did his permalinks wrong"
slug: "numb-nut-did-his-permalinks-wrong"
date: "2005-11-17T20:49:22+00:00"
tags:
id: 180
comment: false
---

None of my recent posts were appearing on [Planet of the Blogs](http://www.planetoftheblogs.com/) and I assumed they were doing something wrong. So I finally mailed them today and they were able to suss that my RSS feeds were all buggered. Why? Because I cannot read simple bloody instructions. I wanted to change from the normal Wordpress link style for posts (e.g. [http://conoroneill.com/?p=178](http://conoroneill.com/?p=178)) to a more meaningful permalink structure ([http://conoroneill.com/2005/11/17/pork-from-china/](http://conoroneill.com/2005/11/17/pork-from-china/)). What did I do? I copied the sample code and forgot to change it for my site. Nitwit. Thanks lads. But even after fixing, the Atom feed is still bunched. So there goes the next hour or two trying to figure out why.

UPDATE: I just got the Atom feed working too. After a ton of googling, it turns out I had to go into the MySQL DB with PHPMyAdmin and hand edit some of the guid entries in the wp_posts table to fix the screwed up old permalink structure. A bit unimpressed that a simple typo in a setting could bugger up the DB like that. But all is well again in Conor-land.
[tags]potb, rss, planetoftheblogs, wordpress[/tags]
