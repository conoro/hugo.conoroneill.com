---
title: "Philips USB Speaker Hell means Cisco becomes the Google of my living room?"
slug: "philips-usb-speaker-hell-means-cisco-become-the-google-of-my-living-room"
date: "2005-11-18T21:25:50+00:00"
tags:
id: 183
comment: false
---

The speakers on the Acer Laptop are a bit puny, particularly for playing DVDs. Unfortunately, the machine does not have a line out, so I decided to get a pair of USB speakers. I didn't need anything particularly special and they had to be just a bog-standard stereo pair due to lack of space. A bit of browsing on Dabs brought up the[ Philips DGX220 Speakers](http://www.dabs.com/ProductView.aspx?QuickLinx=3H8N) at a nice n cheap &pound;23\. 
I received them a few weeks back and was happy to discover that they need no special drivers - XP just handles them out of the box.

Except it didn't.

Weeks of fiddling ensued with no success. The USB composite device would be found and the drivers would load, causing the power light to come on but the install of the USB Audio Drivers always failed with "cannot find suitable drivers for device". Nights of googling produced nothing. These are obviously not a popular product as there are almost no links to them anywhere.

I tried everything - install, uninstall, direct connect, hub connect, scour the philips site, scour all the USB sites. But to no avail.

This evening I had one final go. The various discussions of USB speakers in general all indicated that I had to have usbaudio.sys in C:\WINDOWS\system32\drivers. I didn't but I did find a copy in C:\WINDOWS\ServicePackFiles\i386, so I copied that over. But that was not enough because I needed an INF file to allow Windows to install the driver and there did not appear to be any file called usbaudio.inf anywhere. A bit more googling brought up a discussion of a Siemens M34A Cordless Audio thingy. Totally unrelated to my speakers but one guy mentioned the use of a file called wdma_usb.inf in C:\WINDOWS\inf. Of course I did not have that either. But I did find wdma_usbinf.bak. Why the hell is that there? Who knows. I renamed it to wdma_usb.inf, unplugged and replugged the speaker and went through the install process, obviosuly picking the "manual route" and pointed the device install wizard to the INF file, annnnnnd, it worked!

For gods sake, PCs will never become ubiquitous with their own spot in the living room as long as rubbish like this happens. When I co-founded Advanticus back in 2002, it was on the basis that we were heading into the era of digital convergence where the consumer electronics guys like Sony and Matsushita would deliver on the vision rather than the PC manufacturers. We were just a bit early. 

Cisco obviously believe it too as they have just [dished out $5.3 Billion for Scientific Atlanta](http://www.forbes.com/technology/2005/11/18/cisco-scientific-atlanta-takeover-cx_ck_1118cisco.html). If only Sony and Co would get their act together, they would leave Microsoft/Dell/Intel/HP and their buddies in the dust. However due to  their obsession with DRM (and look what a fine mess that just got Sony into) and controlling the consumer, maybe the winner for living room space will come from left-field and we'll all be converged on our Cisco Home Centers in 3 years time. I've just realised that the Linksys purchase was probably the first step in this. 

Ye know, the tech news worlds blinkered focus on Google/Yahoo/Microsoft/Web2.0 may cause them to miss the huge elephant in the room. Maybe it is time to dip my toe back in the cruel world of the stock market and put more money where my mouth is.

A Few Links: [GMSV](http://blogs.siliconvalley.com/gmsv/2005/11/_cisco_prefers_.html), [Light Reading](http://www.lightreading.com/document.asp?doc_id=84450).

[tags]philips, speakers, usb, cisco, scientific atlanta, convergence, web 2.0, sony, drm[/tags] 
