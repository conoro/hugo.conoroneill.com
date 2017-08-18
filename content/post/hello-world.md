---
title: So long WordPress. Hello Hexo.
slug: "hello-world"
date: "2015-03-05T08:48:46+00:00"
tags:
id: 1
comment: false
---
I've been blogging longer than the average bear, with my first post wayyyy back in 2001 on Blogger. I moved to WordPress in 2005 and did a huge amount of stuff with it both personally and professionally until 2013. 

But, like many people, I've had it with WordPress. Pretty much every WP blog I either ran or had some dealings with, has been hacked. Whether through security-hole-riddled plugins, xmlrpc.php or other bugs in WP. I just don't have the time to constantly update eveything and hope it's alright. The botnets relentlessly trying to login to all of the blogs and managing to mini-DDoS me on a regular basis are just the pooh on the cake.

So over the past 2 years I've moved most of my blogs and sites to static setups. Good old HTML, CSS and JS without a whiff of PHP or MySQL. This has been a huge success for me and I simply don't have to worry about any of those sites. I've popped the images up on S3 for performance too.

My tool of choice for all of this has been [Harp](http://harpjs.com/) and I've been happy with it apart from the very long generation time with each new post on [conoroneill.net](http://conoroneill.net). Basically it re-generates the entire site for every new post/page. And with close to 1000 posts there, that takes 5+ minutes even on an 8-core machine (presumably because it's doing them all sequentially).

So when it came time to kill my last install of WordPress here on conoroneill.com, I decided to see what else was out there in the "Node.js Static Site Generation Tool" world. And I quickly found [Hexo](http://hexo.io/).

![Hexo](https://s3-eu-west-1.amazonaws.com/conoroneill.com/wp-content/uploads/2015/03/hexo.png)

Hexo is a fairly new static blogging platform from Taiwan that seems to have built a community very quickly. It is very easy to use/setup and has import tools for the usual suspects including WordPress. The latter had a one-line bug which I fixed and they have merged already. Getting all of the old posts from WordPress involved taking the export file from WP and running it through the Hexo migration tool a few times and making some fixes. It found a few problems like dodgy markup from old WP plugins and a crazy number of categories/tags. A bit ot search/replace fixing in Notepad++ sorted that out and I got a clean import working with very little effort.

I love how quickly it generates static pages and the general ease of use and configuration but obviously you have to be comfortable using Command Line tools and editing Markdown if you want to use it. However, if you are sick of the WP treadmill, it may be a solution for you too.


  
