# Sleep
I wrote a little program to visualize my sleeping habits. The data is held in a Google Sheet, and the program is written in Python3. The graph is generated with `matplotlib`.

### Motivation
Back in 2021, I read a few articles on the [quantified self](https://en.wikipedia.org/wiki/Quantified_self). The quantified self is to treat one's lifestyle as a numbers game, usually supplemented by analysis or optimization. This wasn't exactly how I wanted to live, but I was interested in tracking *something* from my life, just to see how it would develop long-term. 

I knew I liked studying the sleep tracker on my phone, but it wasn't very accurate as it assumed I would fall asleep before a set bedtime. So, I started tabulating my sleep and wake times on September 21, 2021.

And the habit formed pretty quickly. Here's my chart for 2021, starting on September 21:

Nice, not a day where I slept before midnight. But as a college student, what can I say?

I also calculated some bonus statistics on the side. The shortest sleep during this time period was 5 hours and 45 minutes, on December 30. I was celebrating an early New Year's with friends. The longest sleep was 10 hours and 40 minutes, which actually occurred **three times** in December. Those days I was just being lazy.

On average, I fell asleep at 2:21 AM and woke up at 10:38 AM (I had late classes). Despite these concerning times, I got about 8 hours and 17 minutes of sleep per day, which is healthy, I think. But on the bright side, if I ever moved to California, I would adjust very easily.

### Development

The first problem I had was figuring out how to grab data from a Google Sheet. I knew I could import a Google API, but that felt like using a chainsaw to cut a slice of cake. *All I needed was the data.*

Eventually, I figured out that you could publish a Sheet to the web as a CSV (File -> Share -> Publish to web), then pass the URL to a `pandas` function named `read_csv()`. This was the one-line solution I was looking for.

Another problem was the AM-PM barrier. Say I fall asleep at 11:00 PM and wake up at 7:00 AM (haha). An earlier version of the program incorrectly assumed that both of those times occurred on the *same day*, which meant it plotted a bar from 7:00 AM to 11:00 PM. That's 16 hours of sleep! Which actually isn't unheard of, but I was never a long sleeper.

But 
