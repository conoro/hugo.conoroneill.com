---
title: "Announcing Bandon Flood Early Warning System on Twitter"
slug: "announcing-bandon-flood-early-warning-system-on-twitter"
date: "2011-11-16T17:18:13+00:00"
tags:
id: 1234
comment: false
---

I'm a big fan of the [Bandon FEWS system](http://www.bandonfloodwarning.ie/) which sends an SMS when the river at the bridge hits a certain level. It must be a life-saver for many businesses and people in the town.

[![](https://s3-eu-west-1.amazonaws.com/conoroneill.com/wp-content/uploads/2011/11/fews1.png "fews1")](https://s3-eu-west-1.amazonaws.com/conoroneill.com/wp-content/uploads/2011/11/fews1.png)

I have had a few thoughts on other things we could do with that live river-level data for the community. Web-apps, Twitter integration, Analytics, Trends etc etc.

However, despite several communications, I have been unable to get any response from Cork County Council about getting access to the live data. All the OpenData initiatives around the world (including Ireland) are obviously passing them by.

Even something as simple as a Twitter Account could be useful and interesting. So I created one called [@BandonFEWS](https://twitter.com/#!/bandonfews). Of course then I had to get at the data despite the CoCo's silence. I dug around the Bandon Flood Warning site but it is built in such a way that the data is not machine visible or scrapable.

[![](https://s3-eu-west-1.amazonaws.com/conoroneill.com/wp-content/uploads/2011/11/fews2.png "fews2")](https://s3-eu-west-1.amazonaws.com/conoroneill.com/wp-content/uploads/2011/11/fews2.png)

I discussed this problem with fellow tech-person Gordon Murray of [Murrion Software](http://www.murrion.ie/) just up the road in Carrigadrohid and of course he had a solution!

Gordon's company has a very smart SMS service which can both send SMSes and receive them in order to act upon them. By signing up his service's "phone" number to the FEWS SMS alerts, he can then do something with them. In this case, he takes the SMS, interprets it and then posts it automatically to the @BandonFEWS Twitter account.

Nice one Gordon! If you have any need of inbound or outbound SMS services, [give him a shout](http://twitter.com/murrion).

Now if only Cork CoCo would give us access to all of the live data, we could do some really interesting things for the community for free. Anyone got any influence in there to make this happen?
