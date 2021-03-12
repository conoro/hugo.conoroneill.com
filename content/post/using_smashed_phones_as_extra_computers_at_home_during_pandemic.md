+++
Categories = []
Description = "Many four year old Android phones are supercomputers you can use as a desktop computer."
Tags = []
draft = false
date = "2021-03-12T10:17:32+00:00"
title = "Using smashed phones as extra computers at home during the pandemic"
slug = "using_smashed_phones_as_extra_computers_at_home_during_pandemic"
+++

I've always been interested in maximising the lifetime of electronics. I detest built-in obsolescence and I hate the way computers are becoming impossible to upgrade or repair yourself. Apple is the absolute worst culprit in this area and their actions result in others following their terrible example.

Apple's logic is that phones and computers should be like TVs and no-one ever upgrades or repairs their TV. Except, we used to. I still remember the RTV Rentals man coming to our house to replace the tuner in our TV as the existing one couldn't handle the signal of my new ZX Spectrum. 1970s/1980s TVs were modular so it was only a few minutes work. We need to go back to that.

At my most extreme, I recently upgraded the aforementioned 39-year-old ZX Spectrum to have HDMI-out. It has been loading games from SD cards for several years.

![ZX Spectrum](/images/2021/03/spectrum.jpg)


["Right to repair moves forward for your broken devices. But campaigners want to go much further"](https://www.techrepublic.com/article/right-to-repair-moves-forward-for-your-broken-devices-but-campaigners-want-to-go-much-further/)

I also love using cheap electronics to do powerful things. This is why I adore the [Raspberry Pi](https://www.raspberrypi.org/) and [Arduino](https://www.arduino.cc/) ecosystems so much. If you can imagine it, you can probably do it with a few Euro and some combination of those plus cheap modules from Aliexpress. Things I have built recently using this approach (and will blog soon) include a cloud-connected CO2 monitor and a cloud-connected oil tank monitor.

Related to this, one challenge I know many families have had during these pandemic lock-downs is access to computers for all their kids. Obviously the easiest solution for many people is to get a great Chromebook for approx €200 but not everyone can afford that.

How many of those people have smashed phones in a drawer that you suspect are still working? 

![Smashed S8](/images/2021/03/smashed.jpg)


I have a completely smashed four year old Samsung Galaxy S8+. Its own screen mostly stays black but sometimes flickers on and off. I dropped it at the start of the Chicago Marathon in 2018 due to the exhaustion of [Aer Lingus's flight from hell](https://conoroneill.com/2018/10/15/flight-ei123-and-the-death-of-the-aer-lingus-brand/). When I got home, I was informed that [a] Vodafone had never applied the phone insurance policy to the S8+ when I had upgraded to it so [b] It would cost €320 to get a new screen. After telling them politely to get fucked (seems to be a recurring thing with me and Vodafone), I promptly bought a cheap new Huawei Honor Play instead. Great phone. The S8+ sat in a drawer until I decided to try this experiment.

I'm pretty sure the vast majority of non-techie people don't realise that any modern smartphone is a supercomputer in their pocket. And, depending on the model, is more that capable of being a desktop replacement for many common tasks. And I don't just mean schoolwork. You could easily build an entire web application or website with this setup.

And it's doable for as little as €35. Let me show you how.

You have two possible approaches depending on the age and capabilities of your phone. 

## Option 1 - A USB-C phone
The easiest way requires a relatively modern Android phone with a USB-C charging connector. That's the one which works either way around. I have successfully tested this with a two-year old Huawei P30 Pro and that smashed Galaxy S8+.

Literally all you need to do is to go to a site like Amazon UK or a store like Currys/PCWorld and buy a few things:

* A USB Mouse
* A USB Keyboard
* A USB-C Hub with HDMI-out
* A HDMI cable (if you don't have a spare)

The cheapest decent Mouse/Keyboard combo I found on Amazon was this [Asus U2000](https://www.amazon.co.uk/gp/product/B075R9TH9H/). It cost me £10.82!! Both keyboard and mouse are shockingly good. In the past I have also bought some no-name wireless keyboard/mouse sets for < £20 on Amazon and they have been pretty rubbish. But wireless is a little bit handier for a lot of people.

The cheapest good suitable USB-C hub I found on Amazon was this [Ablewe 5 in 1](https://www.amazon.co.uk/gp/product/B07YWWZJ65/) for £18.99. Again I was really surprised by the quality.

Note that the price of each item comes in under the new Brexity customs and excise limits. If you have (or know someone who has) Amazon Prime, definitely do it as separate free-delivery orders.

TBH that's the hardest bit done.

![Setup](/images/2021/03/setup.jpg)


Assembly is a matter of plugging your phone's charger into the power-in on the hub. Plug the keyboard and mouse into the USB sockets on the hub. Plug the HDMI cable into the HDMI socket on the hub and plug the other end into your TV. Then turn on the phone and plug the hub into its charging port.


Some phones require you to pick an option in the display settings to use the external monitor but most will just immediately mirror their screen to the TV. Huawei phones have a fantastic desktop mode where everything on the TV is in full-screen and you get a Microsoft Windows type user experience. My Samsung S8+ is a bit crappier where all the apps fill the screen, but the main home screen doesn't. A minor annoyance.

![Huawei Desktop](/images/2021/03/huawei.jpg)


Yes, this does involve using your TV if you don't have a spare monitor. But hey, my entire generation learned how to use computers this way!

Right, so you now have a supercomputer with a keyboard, mouse and screen, what can you do? Wait a second, I want to tell you about option 2.

## Option 2 - A micro-USB phone
If you have an older or cheaper Android phone that has a classic micro-USB charger (the type you always try to plug in the wrong way around), you *might* be in luck.

In this case what you need to do is:

* Check if your TV has Google Chromecast built-in
* If it does, you need to test it with your phone before trying anything else. Install [Google Home](https://play.google.com/store/apps/details?id=com.google.android.apps.chromecast.app&hl=en_IE&gl=US) on your phone and follow the instructions for mirroring your phone on the TV. If it works then skip to the mouse/keyboard purchase instructions below.
* If you don't have Chromecast on the TV but it does have Screen Mirroring or Miracast, check in the settings of your phone whether it also has Screen Mirroring or Miracast. Follow the phone instructions for setting it up.
* If you have neither on your TV, then you can consider buying a Chromecast device. They are [€39 with free delivery in Ireland](https://store.google.com/ie/product/chromecast). But before you do, install Google Home on your phone to confirm that it is compatible (most phones are). Chromecast also lets you display Netflix, RTE Player, YouTube and Eir Sports on your TV via your phone's internet connection.


Now that you have the display piece sorted, you need to get input working. On these phones, you need the following:

* A USB Keyboard and Mouse (see Option 1 above for the details on that)
* A cheap USB Hub [like this one](https://www.amazon.co.uk/Sabrent-4-Port-Individual-Switches-HB-UMLS/dp/B00BWF5U0M/)
* A cheap USB OTG adapter [like this one](https://www.amazon.co.uk/TECHGEAR-Adapter-Compatible-Samsung-Galaxy/dp/B00G1KQE76/)

In this case, plug the keyboard and mouse into the hub and plug the hub into the phone using the OTG adapter. You should be able to use the keyboard and mouse to control the phone now.

The two big drawbacks of this compared to option 1 are the screen mirroring, which can be slow, and the inability to charge the phone whilst you are using it.

Note I've tested this on a cheap <€80 Nokia 2.2 phone and it worked perfectly.

![Nokia 2.2](/images/2021/03/nokia.jpg)


So back to the question, what can I do with this setup? Lots!!

## Using your phone as a computer
The most obvious things you can do with the phone, now that it's connected to a big screen and has decent input devices, are as follows:

* Zoom / Skype / Google Meet / Webex / GotoMeeting / Microsoft Teams. But better, easier.
* Google Docs / Sheets / Drive on a decent sized screen and with keyboard/mouse navigation
* Chrome web browsing in "Desktop Mode" so you don't get stuck with mobile versions of sites
* Full GMail and Google Calendar via browser
* Decent YouTube, obvs
* Firefox web browsing in Desktop Mode if you don't like Chrome
* Faster typing etc on general messaging like SMS, Signal, WhatsApp

So basically anything you normally do but a lot easier.

## Online software development
But wait, there's more. An ever increasing number of software development tools and environments are now available in the browser. The days of having to install horrendous monstrosities like Eclipse are going away. This is just a selection for the curious and there are many more.

* [Glitch](https://glitch.com/) - This needs to be much better known. It's a really cool online environment for building and re-mixing WebApps and web-sites in your browser.

![Glitch](/images/2021/03/glitch.jpg)

* [GitHub Codespaces](https://github.com/features/codespaces) - I still don't have access to this (pretty please GitHub) but I'm really looking forward to it. Microsoft Visual Studio Code and lots more in the browser. 

* [Espruino](https://www.espruino.com/) - This is a brilliant way of using JavaScript on low-power devices like Bluetooth badges and watches. If you want to get into the world of IoT, have a look.

![Espruino](/images/2021/03/espruino.jpg)

* [Arduino Online IDE](https://store.arduino.cc/digital/create) - The classic educational IoT platform is now available online too. Arduino is how most people start with IoT and it has a massive ecosystem of hardware and software. But it can be a bit daunting to get started.

* [Microsoft MakeCode](https://www.microsoft.com/en-us/makecode?rtc=1) - Wow, I only recently discovered this. An online environment for building games, IoT, Lego, Minecraft etc etc. Totally worth a try.

![Make Code](/images/2021/03/makecode.jpg)

## Termux for local development
You want even more? How about a full-blown Linux environment on your phone where you can run Python. Node.js and a ton of other standard software development tools? You can even build and run a web-server on your phone! And interact fully with GitHub etc.

To do this, you need to install [Termux](https://termux.com/). This taps into the underlying Linux kernel on your phone to provide a protected "old-school" command line environment. It's crazy good! 

I've even installed youtube-dl using it and downloaded YouTube videos for offline watching on flights (remember flying?).

But this comes with a big warning. Termux is no longer available on the Play Store for technical reasons. You need to use an alternative additional app store called [F-Droid](https://f-droid.org/packages/com.termux/). If you are not comfortable doing that, stop here and just enjoy all the other features I've listed above. If you are comfortable, install from the link above (after enabling "allow installation of apps from unknown sources" on your phone).

![Termux](/images/2021/03/termux1.jpg)

You can then run the Termux terminal and install Linux apps using commands like:

```bash
pkg install python
pkg install nodejs
pkg install youtube-dl
pkg install emacs
pkg install nano
pkg install git
```

I won't dig into any more details on that but suffice to say that the classic node.js `hello world` web server can be implemented and run on your phone. Which is mad.

```javascript
const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

```

![Termux 2](/images/2021/03/termux2.jpg)


Or run the legendary text editor, [GNU Emacs](https://www.gnu.org/software/emacs/), which I first tried on a multi-thousand-dollar Sun Workstation in the 90s.

![Emacs](/images/2021/03/emacs.jpg)

## But but but what about iPhones?
It seems to be possible but I haven't done it. [This adapter](https://www.amazon.co.uk/Lightening-Adapter-Digital-Converter-Compatible-White/dp/B0872Y1NH2) looks like what you need. It provides HDMI and USB connectors for £25 and can probably be used with a cheap combination wireless keyboard and mouse. 

There is also a Termux type app for iOS called [a-Shell](https://apps.apple.com/us/app/a-shell/id1473805438) which lets you run Unix commands on your phone.

Let me know if you try it and it works for you. 


## In closing
I'm not going to claim this is the ideal solution to anything but it's an option for some people and it's also a fun experiment to see what's possible with devices that maybe spend most of their time on Twitter, Snapchat or TikTok.

If you find it useful or you know of other interesting things that are possible with phones outside of media, let us know.



