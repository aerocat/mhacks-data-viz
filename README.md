# CryptoBattles


![Alt text](./screenshot.png?raw=true "The final result")
<i> Because everyone likes screenshots </i>

## What is this?
Cryptobattles is a simple hierarchical data visualization of live volumes of certain cryptocurrencies pairs. The data is provided by the public GDAX API (Coinbase), and displayed using D3.js.

## Why the name?
Ideally, the cryptocurrencies should "fight" for the available space, which is fixed. Unfortunately, I found that the volumes provided by the GDAX API don't update as quickly as I thought. Hence, I added a random value to each pair to demonstrate the expected behavior.

## When was this made?
This project was made during MHacks X hackathon, at the  University of Michigan.

## Live Demo
<http://mhacks-180903.appspot.com>.

## Inspiration
Originally, I wanted to create a data visualization project that used Voronoi's regions, because they are freaking cool. By using some kind of live data stream I thought it'd be really cool to see the shapes change in real time. Given the short amount of time available at the hackathon, I ended up using a more boring Treemap instead, since Voronoi’s are not actually best used to represent hierarchical data.

## How I built it
The front end is built using D3.js. The data flowing from the GDAX API (Coinbase) is parsed, filtered and sent to the front end as a JSON object using my own back end endpoint, which I wrote in Flask. Finally, AJAX takes care of updating the chart without having to refresh the page. The entire service is hosted on Google App Engine.

## Challenges I ran into
So many. I had to learn D3.js, Flask and Google App Engine, and I spent countless of hours debugging. Eventually, I discovered that the volume data wasn’t changing as fast as I wanted (thanks GDAX). That’s why I later added a line of Python that randomizes the values at every API call.



