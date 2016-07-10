---
title: "Bandon Flood (FEWS) Open Data Now Available "
slug: "bandon-flood-fews-open-data-now-available"
date: "2011-11-17T15:56:30+00:00"
tags:
id: 1241
---

I was thrilled to get such positive feedback about the [@BandonFEWS](http://twitter.com/BandonFEWS) Twitter account yesterday. Thanks again to [Gordon](http://twitter.com/murrion) for doing all the actual work whilst I basked in the glory :-) It was even better considering how sick I am with a nasty tummy bug. The bug means I can do little useful work for the past few days. But I can play with code.

One fantastic outcome from [yesterday's blogpost](http://conoroneill.com/2011/11/16/announcing-bandon-flood-early-warning-system-on-twitter/) was John Handelaar and others pointing out that I'd given up too easily on trying to extract the river level data from the [Bandon FEWS web-site](http://www.bandonfloodwarning.ie/). And it turns out they were right. A small amount of messing around and I was able to extract out the water level and the date/time.

I've been meaning to do more with [Google Fusion Tables](http://www.google.com/fusiontables/Home/) for ages and this seemed like a good opportunity. It's like a Google Docs online spreadsheet but with knobs on. So  you can populate, query, visualise etc using an API. I decided to use that to make the FEWS data available to everyone. Of course then I ran into the horror that is OAuth2\. But a fair bit of messing and stomach cramps later, and I got that working too.

So we now have [the hourly Bandon river level data available](https://www.google.com/fusiontables/DataSource?docid=103YIcARoxuaWT7NfZ8mVBzY554sF_3ONYC1N3DE) to use for whatever purpose your fiendish minds can come up with. I'm thinking trends, analytics, charts, maps, mashups with weather data, other alerting methods (email, Twitter DMs, iPhone Alerts), a Facebook Fan Page, widgets for other Bandon-related sites. What other ideas do you all have?

<iframe width="500px" height="300px" scrolling="no" frameborder="no" src="http://www.google.com/fusiontables/embedviz?gco_allowHtml=true&gco_displayAnnotations=true&gco_wmode=opaque&gco_chartArea=%7B%22top%22%3A%2230%22%7D&containerId=gviz_canvas&rmax=250&q=select+col1%2C+col0+from+2191951+&qrs=where+col1+%3E%3D+&qre=+and+col1+%3C%3D+&qe=+order+by+col1+asc&viz=GVIZ&t=TIMELINE&width=500&height=300"></iframe>

If you want to embed that live graph on your own site or blog, just paste this code in:

[javascript]
&lt;iframe width= 500px  height= 300px  scrolling= no  frameborder= no  src= http://www.google.com/fusiontables/embedviz?gco_allowHtml=trueandgco_displayAnnotations=trueandgco_wmode=opaqueandgco_chartArea=%7B%22top%22%3A%2230%22%7DandcontainerId=gviz_canvasandrmax=250andq=select+col1%2C+col0+from+2191951+andqrs=where+col1+%3E%3D+andqre=+and+col1+%3C%3D+andqe=+order+by+col1+ascandviz=GVIZandt=TIMELINEandwidth=500andheight=300 &gt;&lt;/iframe&gt;
[/javascript]

You can export the data to CSV and play with it offline in Excel etc or you can go fancy and query it live over the API.

e.g. this API call grabs all of the data in one go (you can test with your browser): [https://fusiontables.googleusercontent.com/fusiontables/api/query?sql=SELECT+ROWID,+riverlevel,+datetime+FROM+2191951](https://fusiontables.googleusercontent.com/fusiontables/api/query?sql=SELECT+ROWID,+riverlevel,+datetime+FROM+2191951)

But of course you will be able to do far more complex queries than that, once we have a decent body of data. See the [Google Fusion Tables Guide here](http://code.google.com/apis/fusiontables/docs/developers_guide.html).

Note that I was forced to use that awkward date format to make the timeline feature in Fusion Tables work correctly.

I don't know if anyone wants the data or will find a use for it but this first step was critical to enabling them to do so. Hopefully this will be a trigger for others to liberate locked-in non-private data on other public sector sites.

Or it could be an opportunity for County Councils to take this tough time we are all living in, where Capex projects are few and far between, and start a [Data Liberation Project](http://www.dataliberation.org/) in every Council department in the country. Nothing I did over the past 24hrs cost a single solitary cent apart from people's time. And based on recent conversations with old college friends, time is one thing a lot of Council Engineers have on their hands. If any Council people are interested in reading more they should have a look at the links [in this post](http://www.web2ireland.org/2011/01/17/the-ireland-api/) I did at the start of the year.

Comments? Thoughts? Improvements?

&nbsp;
