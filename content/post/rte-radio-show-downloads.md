---
title: "RTE Radio Show Downloads"
slug: "rte-radio-show-downloads"
date: "2006-02-27T22:41:29+00:00"
tags:
id: 263
comment: false
---

I'm not a radio person so I tend to miss a wealth of interesting programmes, particularly in the evenings. I have only just found out about [Winter Food on RTE1](http://www.rte.ie/radio1/winterfood/) presented by Cork's own Clodagh McKenna. I was very happy to see that recordings of the show (and archives) were available. Unfortunately there are a few problems, but I have solutions to some of them:

[1] The shows are in Real Player rm format rather than MP3\. Luckily my MP3 player is Real Audio on a Palm so it isn't actually a problem for me.

[2] There is no RSS feed for this programme. RTE actually do have RSS feeds for their top level stuff like the news but not fine-grained to enable me to subscribe to updates on Winter Food.

In fact, what the hell is stopping them from going the whole hog and embracing podcasting properly and making all of their programming available via something like Podcast Alley? Today FM do it for Gift Grub on iTunes but obviously we don't want anything which makes people install that dire software on their PCs. They should have a look over at [The Restaurant Guys](http://www.restaurantguysradio.com/sle/rg/) in New Jersey - a food programme on a commercial radio station (WCTC) that is fully setup for MP3 downloads to anyone worldwide.

Does anyone know what RTE's intentions are in this area as a publicly funded broadcaster? It would take minimal capital investment to set this up. I know I'd spend a lot more time listening to RTE programmes if I could dictate when I get to listen to their output on the move.

[3] You can't actually download the files for later listening, you have to listen to them in realtime on your computer. This is the same stupid limitation set by BBC radio which I found a solution for when I wanted to grab the H2G2 broadcasts from last year. Follow my instructions over at [this post ](http://conoroneill.com/2005/05/17/recording-streaming-audio-for-later-listening/)(mainly to do with setting up [MPlayer](http://www2.mplayerhq.hu)), find out when the programme you want was broadcast e.g. February 18th and then download it using MPlayer using a command line in a DOS prompt like the following:

mplayer -dumpfile winterfood20060218.ra -dumpstream rtsp://streaming2.rte.ie/2006/0218/18022006rte-winterfood.rm

Unfortunately this downloads in realtime so it'll take the full half hour to grab but when it is done you'll have a Real Audio file to use to your hearts content.

If you need MP3 then you'll have to grab [LAME from here](http://www.free-codecs.com/Lame_Encoder_download.htm) and copy it to the same dir as MPlayer. Then execute the following two commands:

mplayer winterfood20060218.ra -ao pcm -ao pcm:file=winterfood20060218.wav

lame -f  winterfood20060218.wav winterfood20060218.mp3

Note that the mplayer step above takes up crazy amounts of disk space (3 meg real audio file becoming a multi-gig wav file) and you may run out if you have a small hard drive.

Of course, what would be far better would be a little script which ran once a week and grabbed the latest episode for you and converted it if needed. I'm gonna have a bit of spare time in the next few weeks so I may hack some travesty of a script together and make it available here.

The above instructions apply to any of the RTE programmes which they make available for later listening. You do have to figure out the "path" to the file which you do as follows: right-click on the "listen to this show" link, save it to your desktop, open the smil file in notepad and find the rstp path in that file and use it in place of the rstp link in the command line above. Hardly slick.

[tags]RTE, Winter Food, Clodagh McKenna, MP3, Real Audio, mplayer, Podcasting, BBC, LAME[/tags]
