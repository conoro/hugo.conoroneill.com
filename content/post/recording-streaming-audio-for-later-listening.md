---
title: "Recording Streaming Audio for later listening"
slug: "recording-streaming-audio-for-later-listening"
date: "2005-05-17T22:36:00+00:00"
tags:
id: 84
comment: false
---

<div style="clear:both;"></div>I've been trying to figure out how to record streaming audio so I can listen to it later (and start/stop when I like). Actually it's specifically for [The Hitchhiker's Guide to the Galaxy Quandary Phase](http://www.bbc.co.uk/radio4/hitchhikers/). I didn't really enjoy the last radio series and the repeats of the TV series aren't that great either. But it became a technical challenge that I wanted to get to the bottom of. I finally cracked it today. Note that the solution below will not work behind some corporate firewalls but seems to work fine on my NATed setup on a Linksys Wireless Router at home.

Download MPlayer for Windows and all the codecs.

[http://www2.mplayerhq.hu/MPlayer/releases/win32-beta/MPlayer-mingw32-1.0pre7.zip](http://www2.mplayerhq.hu/MPlayer/releases/win32-beta/MPlayer-mingw32-1.0pre7.zip)

[http://www2.mplayerhq.hu/MPlayer/releases/codecs/windows-all-20050412.zip](http://www2.mplayerhq.hu/MPlayer/releases/codecs/windows-all-20050412.zip)

Unzip MPlayer and unzip the codecs.Copy the unzipped codecs to the codecs sub-dir of the mplayer dir.

Open a command prompt in the Mplayer dir and type:

mplayer -dumpfile hitchhikers.ra -dumpstream rtsp://rmv8.bbc.net.uk/radio4/hitchhikers/hitchhikers.ra

It streams in realtime so it'll take 30 mins to download.

Listen to ram file later at your leisure using realplayer (or the nifty stripped down, bloat-free [Real Alternative](http://www.codecguide.com/about_real.htm))

Do that once a week to get each new episode.

Don't try this with VLC. I spent ages trying to get it to work before I realised it doesn't support realaudio!<div style="clear:both; padding-bottom: 0.25em;"></div>
