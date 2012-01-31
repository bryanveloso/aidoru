# アイドル (Aidoru)

Make the idols come to you over HTTP. That is the point, isn't it?

## Usage

Fetch a random idol:

    $ curl http://aidoru-bomb.herokuapp.com/random
    {
      "idol": "http://26.media.tumblr.com/tumblr_luz0q1X7AQ1r6j9k4o1_400.gif"
    }

Bomb idols (the `count` argument is optional, by default 5 idols are bombed):

    $ curl http://aidoru-bomb.herokuapp.com/bomb?count=5
    {
      "idols": [
        "http://24.media.tumblr.com/tumblr_lv4p1smS6I1r6j9k4o1_250.gif",
        "http://30.media.tumblr.com/tumblr_lxpdfl8cvS1r6j9k4o1_400.gif",
        "http://27.media.tumblr.com/tumblr_luz4a5t80W1r6j9k4o1_400.gif",
        "http://28.media.tumblr.com/tumblr_lxpdglIuBY1r6j9k4o2_400.gif",
        "http://24.media.tumblr.com/tumblr_ly37wbKxSD1r6j9k4o2_400.gif"
      ]
    }

Count how many idols we have:

    $ curl http://aidoru-bomb.herokuapp.com/count
    {
      "count": 382
    }

## Notes

Because using Tumblr's API is a bit like pulling teeth, to "release early" I
scraped all of the image URLs from a blog and put them in `images.py`. This
isn't ideal for updating and I'd actually like to USE the API, you know, for
more blogs and more GIFs. All of that is forthcoming once I've jumped off
enough bridges to deal with Tumblr.

## Special Thanks

I'd like to extend my gratitude to these fine sites:

* http://aigaki.tumblr.com/
* http://fyeahrokkies.tumblr.com/
