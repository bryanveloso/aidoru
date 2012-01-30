# アイドル (Aidoru)

Make the idols come to you over HTTP. That is the point, isn't it?

## Usage

Fetch a random idol:

    $ curl http://aidoru-bomb.herokuapp.com/random
    {
      "idol": "http://26.media.tumblr.com/tumblr_luz0q1X7AQ1r6j9k4o1_400.gif"
    }

Bomb idols:

    $ curl http://aidoru-bomb.herokuapp.com/bomb
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
