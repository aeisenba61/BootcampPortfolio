
# News Mood Homework -- Aaron Eisenbarth

## Observation 1:
The BBC and CBS have had generally positive sentiments in their last 100 tweets, whereas NYtimes, Fox News, and CNN have neutral scores. 
## Observation 2:
The most positive sentiment was sent by CBS, whereas the most negative sentiment was sent by Fox News. 
## Observation 3:
In general, CBS sent very few tweets that were negative (less than 10 in 100). 

```python
import tweepy
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.ticker as ticker

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys
consumer_key = "QNfqVUOAkw1qXDiApaMrDxz8R"
consumer_secret = "fb6GcNnA8kIn2745dWItBtAkiwis8me2nSLz5JQQW8YNDEa2W9"
access_token = "1850707158-Y29i1e5Kh6RwUtNznKEwttfCBokaXRY0qqWoGbN"
access_token_secret = "ybhtfHhR5ZLUPQgjUGPGoQbPPDYtWxYIdyPlUK93pzk8i"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```


```python
news_orgs = ['@BBC','@CBS','@CNN','@FoxNews','@nytimes']
```


```python
test = api.user_timeline('@BBC')
print(json.dumps(test, sort_keys=True, indent=4, separators=(',', ': ')))
```

    [
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 20:34:25 +0000 2017",
            "entities": {
                "hashtags": [
                    {
                        "indices": [
                            22,
                            34
                        ],
                        "text": "BigThankYou"
                    },
                    {
                        "indices": [
                            69,
                            75
                        ],
                        "text": "SPOTY"
                    }
                ],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "twitter.com/BBCSport/statu\u2026",
                        "expanded_url": "https://twitter.com/BBCSport/status/942491981758042112",
                        "indices": [
                            76,
                            99
                        ],
                        "url": "https://t.co/xRHVhwEjFP"
                    }
                ],
                "user_mentions": []
            },
            "favorite_count": 9,
            "favorited": false,
            "geo": null,
            "id": 942493204359909376,
            "id_str": "942493204359909376",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": true,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "quoted_status": {
                "contributors": null,
                "coordinates": null,
                "created_at": "Sun Dec 17 20:29:33 +0000 2017",
                "entities": {
                    "hashtags": [],
                    "symbols": [],
                    "urls": [
                        {
                            "display_url": "twitter.com/i/web/status/9\u2026",
                            "expanded_url": "https://twitter.com/i/web/status/942491981758042112",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/QvxSIPRXyU"
                        }
                    ],
                    "user_mentions": []
                },
                "favorite_count": 352,
                "favorited": false,
                "geo": null,
                "id": 942491981758042112,
                "id_str": "942491981758042112",
                "in_reply_to_screen_name": null,
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "is_quote_status": false,
                "lang": "en",
                "place": null,
                "possibly_sensitive": false,
                "retweet_count": 74,
                "retweeted": false,
                "source": "<a href=\"http://www.socialflow.com\" rel=\"nofollow\">SocialFlow</a>",
                "text": "Volunteer Denise Larrad has been named the BBC Get Inspired Unsung Hero award winner.\n\nThanks for all your efforts.\u2026 https://t.co/QvxSIPRXyU",
                "truncated": true,
                "user": {
                    "contributors_enabled": false,
                    "created_at": "Mon Mar 14 09:44:40 +0000 2011",
                    "default_profile": false,
                    "default_profile_image": false,
                    "description": "Official https://t.co/XsBH2P4slh account. Also from @bbc - @bbcmotd @bbcf1 @bbctms @bbctennis @bbcrugbyunion @bbcsnooker & @bbcgetinspired",
                    "entities": {
                        "description": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport",
                                    "expanded_url": "http://www.bbc.co.uk/sport",
                                    "indices": [
                                        9,
                                        32
                                    ],
                                    "url": "https://t.co/XsBH2P4slh"
                                }
                            ]
                        },
                        "url": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport/0/",
                                    "expanded_url": "http://www.bbc.co.uk/sport/0/",
                                    "indices": [
                                        0,
                                        23
                                    ],
                                    "url": "https://t.co/nGZXuvg6cY"
                                }
                            ]
                        }
                    },
                    "favourites_count": 255,
                    "follow_request_sent": false,
                    "followers_count": 7128183,
                    "following": false,
                    "friends_count": 280,
                    "geo_enabled": true,
                    "has_extended_profile": false,
                    "id": 265902729,
                    "id_str": "265902729",
                    "is_translation_enabled": true,
                    "is_translator": false,
                    "lang": "en",
                    "listed_count": 18954,
                    "location": "MediaCityUK, Salford",
                    "name": "BBC Sport",
                    "notifications": false,
                    "profile_background_color": "C0DEED",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/265902729/1511019477",
                    "profile_image_url": "http://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_link_color": "FFD230",
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "profile_text_color": "333333",
                    "profile_use_background_image": true,
                    "protected": false,
                    "screen_name": "BBCSport",
                    "statuses_count": 310853,
                    "time_zone": "London",
                    "translator_type": "none",
                    "url": "https://t.co/nGZXuvg6cY",
                    "utc_offset": 0,
                    "verified": true
                }
            },
            "quoted_status_id": 942491981758042112,
            "quoted_status_id_str": "942491981758042112",
            "retweet_count": 3,
            "retweeted": false,
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
            "text": "Congratulations and a #BigThankYou to Denise. \ud83c\udf89 What an inspiration. #SPOTY https://t.co/xRHVhwEjFP",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 20:31:03 +0000 2017",
            "entities": {
                "hashtags": [
                    {
                        "indices": [
                            86,
                            100
                        ],
                        "text": "Alternativity"
                    }
                ],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "twitter.com/i/web/status/9\u2026",
                        "expanded_url": "https://twitter.com/i/web/status/942492359497011201",
                        "indices": [
                            117,
                            140
                        ],
                        "url": "https://t.co/RLZvnMA8yJ"
                    }
                ],
                "user_mentions": [
                    {
                        "id": 1586183960,
                        "id_str": "1586183960",
                        "indices": [
                            108,
                            115
                        ],
                        "name": "BBC Two",
                        "screen_name": "BBCTwo"
                    }
                ]
            },
            "favorite_count": 10,
            "favorited": false,
            "geo": null,
            "id": 942492359497011201,
            "id_str": "942492359497011201",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 2,
            "retweeted": false,
            "source": "<a href=\"http://www.radian6.com\" rel=\"nofollow\">Radian6 -Social Media Management</a>",
            "text": "Follow the production of a contemporary performance of the nativity unlike any other. #Alternativity 9pm on @BBCTwo\u2026 https://t.co/RLZvnMA8yJ",
            "truncated": true,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 20:29:11 +0000 2017",
            "entities": {
                "hashtags": [
                    {
                        "indices": [
                            70,
                            76
                        ],
                        "text": "SPOTY"
                    }
                ],
                "media": [
                    {
                        "display_url": "pic.twitter.com/flkmCR2TWw",
                        "expanded_url": "https://twitter.com/BBCSport/status/942491537459556353/photo/1",
                        "id": 942491376553529345,
                        "id_str": "942491376553529345",
                        "indices": [
                            107,
                            130
                        ],
                        "media_url": "http://pbs.twimg.com/media/DRRm6ddXkAEBMsq.jpg",
                        "media_url_https": "https://pbs.twimg.com/media/DRRm6ddXkAEBMsq.jpg",
                        "sizes": {
                            "large": {
                                "h": 356,
                                "resize": "fit",
                                "w": 634
                            },
                            "medium": {
                                "h": 356,
                                "resize": "fit",
                                "w": 634
                            },
                            "small": {
                                "h": 356,
                                "resize": "fit",
                                "w": 634
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "source_status_id": 942491537459556353,
                        "source_status_id_str": "942491537459556353",
                        "source_user_id": 265902729,
                        "source_user_id_str": "265902729",
                        "type": "photo",
                        "url": "https://t.co/flkmCR2TWw"
                    }
                ],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "bbc.in/2jZmOAH",
                        "expanded_url": "http://bbc.in/2jZmOAH",
                        "indices": [
                            83,
                            106
                        ],
                        "url": "https://t.co/J5Un4g5oDM"
                    }
                ],
                "user_mentions": [
                    {
                        "id": 265902729,
                        "id_str": "265902729",
                        "indices": [
                            3,
                            12
                        ],
                        "name": "BBC Sport",
                        "screen_name": "BBCSport"
                    },
                    {
                        "id": 113613920,
                        "id_str": "113613920",
                        "indices": [
                            15,
                            29
                        ],
                        "name": "Noel Gallagher",
                        "screen_name": "NoelGallagher"
                    }
                ]
            },
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/flkmCR2TWw",
                        "expanded_url": "https://twitter.com/BBCSport/status/942491537459556353/photo/1",
                        "id": 942491376553529345,
                        "id_str": "942491376553529345",
                        "indices": [
                            107,
                            130
                        ],
                        "media_url": "http://pbs.twimg.com/media/DRRm6ddXkAEBMsq.jpg",
                        "media_url_https": "https://pbs.twimg.com/media/DRRm6ddXkAEBMsq.jpg",
                        "sizes": {
                            "large": {
                                "h": 356,
                                "resize": "fit",
                                "w": 634
                            },
                            "medium": {
                                "h": 356,
                                "resize": "fit",
                                "w": 634
                            },
                            "small": {
                                "h": 356,
                                "resize": "fit",
                                "w": 634
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "source_status_id": 942491537459556353,
                        "source_status_id_str": "942491537459556353",
                        "source_user_id": 265902729,
                        "source_user_id_str": "265902729",
                        "type": "photo",
                        "url": "https://t.co/flkmCR2TWw"
                    }
                ]
            },
            "favorite_count": 0,
            "favorited": false,
            "geo": null,
            "id": 942491890343202817,
            "id_str": "942491890343202817",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 85,
            "retweeted": false,
            "retweeted_status": {
                "contributors": null,
                "coordinates": null,
                "created_at": "Sun Dec 17 20:27:47 +0000 2017",
                "entities": {
                    "hashtags": [
                        {
                            "indices": [
                                56,
                                62
                            ],
                            "text": "SPOTY"
                        }
                    ],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/flkmCR2TWw",
                            "expanded_url": "https://twitter.com/BBCSport/status/942491537459556353/photo/1",
                            "id": 942491376553529345,
                            "id_str": "942491376553529345",
                            "indices": [
                                93,
                                116
                            ],
                            "media_url": "http://pbs.twimg.com/media/DRRm6ddXkAEBMsq.jpg",
                            "media_url_https": "https://pbs.twimg.com/media/DRRm6ddXkAEBMsq.jpg",
                            "sizes": {
                                "large": {
                                    "h": 356,
                                    "resize": "fit",
                                    "w": 634
                                },
                                "medium": {
                                    "h": 356,
                                    "resize": "fit",
                                    "w": 634
                                },
                                "small": {
                                    "h": 356,
                                    "resize": "fit",
                                    "w": 634
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "type": "photo",
                            "url": "https://t.co/flkmCR2TWw"
                        }
                    ],
                    "symbols": [],
                    "urls": [
                        {
                            "display_url": "bbc.in/2jZmOAH",
                            "expanded_url": "http://bbc.in/2jZmOAH",
                            "indices": [
                                69,
                                92
                            ],
                            "url": "https://t.co/J5Un4g5oDM"
                        }
                    ],
                    "user_mentions": [
                        {
                            "id": 113613920,
                            "id_str": "113613920",
                            "indices": [
                                1,
                                15
                            ],
                            "name": "Noel Gallagher",
                            "screen_name": "NoelGallagher"
                        }
                    ]
                },
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/flkmCR2TWw",
                            "expanded_url": "https://twitter.com/BBCSport/status/942491537459556353/photo/1",
                            "id": 942491376553529345,
                            "id_str": "942491376553529345",
                            "indices": [
                                93,
                                116
                            ],
                            "media_url": "http://pbs.twimg.com/media/DRRm6ddXkAEBMsq.jpg",
                            "media_url_https": "https://pbs.twimg.com/media/DRRm6ddXkAEBMsq.jpg",
                            "sizes": {
                                "large": {
                                    "h": 356,
                                    "resize": "fit",
                                    "w": 634
                                },
                                "medium": {
                                    "h": 356,
                                    "resize": "fit",
                                    "w": 634
                                },
                                "small": {
                                    "h": 356,
                                    "resize": "fit",
                                    "w": 634
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "type": "photo",
                            "url": "https://t.co/flkmCR2TWw"
                        }
                    ]
                },
                "favorite_count": 503,
                "favorited": false,
                "geo": null,
                "id": 942491537459556353,
                "id_str": "942491537459556353",
                "in_reply_to_screen_name": null,
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "is_quote_status": false,
                "lang": "en",
                "place": null,
                "possibly_sensitive": false,
                "retweet_count": 85,
                "retweeted": false,
                "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                "text": ".@NoelGallagher singing the Beatles \n\nBeautiful.\n\nWatch #SPOTY live: https://t.co/J5Un4g5oDM https://t.co/flkmCR2TWw",
                "truncated": false,
                "user": {
                    "contributors_enabled": false,
                    "created_at": "Mon Mar 14 09:44:40 +0000 2011",
                    "default_profile": false,
                    "default_profile_image": false,
                    "description": "Official https://t.co/XsBH2P4slh account. Also from @bbc - @bbcmotd @bbcf1 @bbctms @bbctennis @bbcrugbyunion @bbcsnooker & @bbcgetinspired",
                    "entities": {
                        "description": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport",
                                    "expanded_url": "http://www.bbc.co.uk/sport",
                                    "indices": [
                                        9,
                                        32
                                    ],
                                    "url": "https://t.co/XsBH2P4slh"
                                }
                            ]
                        },
                        "url": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport/0/",
                                    "expanded_url": "http://www.bbc.co.uk/sport/0/",
                                    "indices": [
                                        0,
                                        23
                                    ],
                                    "url": "https://t.co/nGZXuvg6cY"
                                }
                            ]
                        }
                    },
                    "favourites_count": 255,
                    "follow_request_sent": false,
                    "followers_count": 7128183,
                    "following": false,
                    "friends_count": 280,
                    "geo_enabled": true,
                    "has_extended_profile": false,
                    "id": 265902729,
                    "id_str": "265902729",
                    "is_translation_enabled": true,
                    "is_translator": false,
                    "lang": "en",
                    "listed_count": 18954,
                    "location": "MediaCityUK, Salford",
                    "name": "BBC Sport",
                    "notifications": false,
                    "profile_background_color": "C0DEED",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/265902729/1511019477",
                    "profile_image_url": "http://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_link_color": "FFD230",
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "profile_text_color": "333333",
                    "profile_use_background_image": true,
                    "protected": false,
                    "screen_name": "BBCSport",
                    "statuses_count": 310853,
                    "time_zone": "London",
                    "translator_type": "none",
                    "url": "https://t.co/nGZXuvg6cY",
                    "utc_offset": 0,
                    "verified": true
                }
            },
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
            "text": "RT @BBCSport: .@NoelGallagher singing the Beatles \n\nBeautiful.\n\nWatch #SPOTY live: https://t.co/J5Un4g5oDM https://t.co/flkmCR2TWw",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 20:19:09 +0000 2017",
            "entities": {
                "hashtags": [
                    {
                        "indices": [
                            37,
                            43
                        ],
                        "text": "SPOTY"
                    }
                ],
                "media": [
                    {
                        "display_url": "pic.twitter.com/WvQYr12Ds7",
                        "expanded_url": "https://twitter.com/BBCSport/status/942488950014447616/photo/1",
                        "id": 942488946495361024,
                        "id_str": "942488946495361024",
                        "indices": [
                            100,
                            123
                        ],
                        "media_url": "http://pbs.twimg.com/media/DRRktAyWkAAt4b-.jpg",
                        "media_url_https": "https://pbs.twimg.com/media/DRRktAyWkAAt4b-.jpg",
                        "sizes": {
                            "large": {
                                "h": 1080,
                                "resize": "fit",
                                "w": 1920
                            },
                            "medium": {
                                "h": 675,
                                "resize": "fit",
                                "w": 1200
                            },
                            "small": {
                                "h": 383,
                                "resize": "fit",
                                "w": 680
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "source_status_id": 942488950014447616,
                        "source_status_id_str": "942488950014447616",
                        "source_user_id": 265902729,
                        "source_user_id_str": "265902729",
                        "type": "photo",
                        "url": "https://t.co/WvQYr12Ds7"
                    }
                ],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "bit.ly/2B3DwcL",
                        "expanded_url": "http://bit.ly/2B3DwcL",
                        "indices": [
                            76,
                            99
                        ],
                        "url": "https://t.co/DQf1YQT4L0"
                    }
                ],
                "user_mentions": [
                    {
                        "id": 265902729,
                        "id_str": "265902729",
                        "indices": [
                            3,
                            12
                        ],
                        "name": "BBC Sport",
                        "screen_name": "BBCSport"
                    }
                ]
            },
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/WvQYr12Ds7",
                        "expanded_url": "https://twitter.com/BBCSport/status/942488950014447616/photo/1",
                        "id": 942488946495361024,
                        "id_str": "942488946495361024",
                        "indices": [
                            100,
                            123
                        ],
                        "media_url": "http://pbs.twimg.com/media/DRRktAyWkAAt4b-.jpg",
                        "media_url_https": "https://pbs.twimg.com/media/DRRktAyWkAAt4b-.jpg",
                        "sizes": {
                            "large": {
                                "h": 1080,
                                "resize": "fit",
                                "w": 1920
                            },
                            "medium": {
                                "h": 675,
                                "resize": "fit",
                                "w": 1200
                            },
                            "small": {
                                "h": 383,
                                "resize": "fit",
                                "w": 680
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "source_status_id": 942488950014447616,
                        "source_status_id_str": "942488950014447616",
                        "source_user_id": 265902729,
                        "source_user_id_str": "265902729",
                        "type": "photo",
                        "url": "https://t.co/WvQYr12Ds7"
                    }
                ]
            },
            "favorite_count": 0,
            "favorited": false,
            "geo": null,
            "id": 942489365200162817,
            "id_str": "942489365200162817",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 105,
            "retweeted": false,
            "retweeted_status": {
                "contributors": null,
                "coordinates": null,
                "created_at": "Sun Dec 17 20:17:30 +0000 2017",
                "entities": {
                    "hashtags": [
                        {
                            "indices": [
                                23,
                                29
                            ],
                            "text": "SPOTY"
                        }
                    ],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/WvQYr12Ds7",
                            "expanded_url": "https://twitter.com/BBCSport/status/942488950014447616/photo/1",
                            "id": 942488946495361024,
                            "id_str": "942488946495361024",
                            "indices": [
                                86,
                                109
                            ],
                            "media_url": "http://pbs.twimg.com/media/DRRktAyWkAAt4b-.jpg",
                            "media_url_https": "https://pbs.twimg.com/media/DRRktAyWkAAt4b-.jpg",
                            "sizes": {
                                "large": {
                                    "h": 1080,
                                    "resize": "fit",
                                    "w": 1920
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "type": "photo",
                            "url": "https://t.co/WvQYr12Ds7"
                        }
                    ],
                    "symbols": [],
                    "urls": [
                        {
                            "display_url": "bit.ly/2B3DwcL",
                            "expanded_url": "http://bit.ly/2B3DwcL",
                            "indices": [
                                62,
                                85
                            ],
                            "url": "https://t.co/DQf1YQT4L0"
                        }
                    ],
                    "user_mentions": []
                },
                "extended_entities": {
                    "media": [
                        {
                            "display_url": "pic.twitter.com/WvQYr12Ds7",
                            "expanded_url": "https://twitter.com/BBCSport/status/942488950014447616/photo/1",
                            "id": 942488946495361024,
                            "id_str": "942488946495361024",
                            "indices": [
                                86,
                                109
                            ],
                            "media_url": "http://pbs.twimg.com/media/DRRktAyWkAAt4b-.jpg",
                            "media_url_https": "https://pbs.twimg.com/media/DRRktAyWkAAt4b-.jpg",
                            "sizes": {
                                "large": {
                                    "h": 1080,
                                    "resize": "fit",
                                    "w": 1920
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "type": "photo",
                            "url": "https://t.co/WvQYr12Ds7"
                        }
                    ]
                },
                "favorite_count": 142,
                "favorited": false,
                "geo": null,
                "id": 942488950014447616,
                "id_str": "942488950014447616",
                "in_reply_to_screen_name": null,
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "is_quote_status": false,
                "lang": "en",
                "place": null,
                "possibly_sensitive": false,
                "retweet_count": 105,
                "retweeted": false,
                "source": "<a href=\"http://www.socialflow.com\" rel=\"nofollow\">SocialFlow</a>",
                "text": "The voting is open for #SPOTY.\n\nIt's time to have your say \u27a1\ufe0f https://t.co/DQf1YQT4L0 https://t.co/WvQYr12Ds7",
                "truncated": false,
                "user": {
                    "contributors_enabled": false,
                    "created_at": "Mon Mar 14 09:44:40 +0000 2011",
                    "default_profile": false,
                    "default_profile_image": false,
                    "description": "Official https://t.co/XsBH2P4slh account. Also from @bbc - @bbcmotd @bbcf1 @bbctms @bbctennis @bbcrugbyunion @bbcsnooker & @bbcgetinspired",
                    "entities": {
                        "description": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport",
                                    "expanded_url": "http://www.bbc.co.uk/sport",
                                    "indices": [
                                        9,
                                        32
                                    ],
                                    "url": "https://t.co/XsBH2P4slh"
                                }
                            ]
                        },
                        "url": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport/0/",
                                    "expanded_url": "http://www.bbc.co.uk/sport/0/",
                                    "indices": [
                                        0,
                                        23
                                    ],
                                    "url": "https://t.co/nGZXuvg6cY"
                                }
                            ]
                        }
                    },
                    "favourites_count": 255,
                    "follow_request_sent": false,
                    "followers_count": 7128183,
                    "following": false,
                    "friends_count": 280,
                    "geo_enabled": true,
                    "has_extended_profile": false,
                    "id": 265902729,
                    "id_str": "265902729",
                    "is_translation_enabled": true,
                    "is_translator": false,
                    "lang": "en",
                    "listed_count": 18954,
                    "location": "MediaCityUK, Salford",
                    "name": "BBC Sport",
                    "notifications": false,
                    "profile_background_color": "C0DEED",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/265902729/1511019477",
                    "profile_image_url": "http://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_link_color": "FFD230",
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "profile_text_color": "333333",
                    "profile_use_background_image": true,
                    "protected": false,
                    "screen_name": "BBCSport",
                    "statuses_count": 310853,
                    "time_zone": "London",
                    "translator_type": "none",
                    "url": "https://t.co/nGZXuvg6cY",
                    "utc_offset": 0,
                    "verified": true
                }
            },
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
            "text": "RT @BBCSport: The voting is open for #SPOTY.\n\nIt's time to have your say \u27a1\ufe0f https://t.co/DQf1YQT4L0 https://t.co/WvQYr12Ds7",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 20:15:19 +0000 2017",
            "entities": {
                "hashtags": [
                    {
                        "indices": [
                            110,
                            116
                        ],
                        "text": "spoty"
                    }
                ],
                "symbols": [],
                "urls": [],
                "user_mentions": [
                    {
                        "id": 265902729,
                        "id_str": "265902729",
                        "indices": [
                            3,
                            12
                        ],
                        "name": "BBC Sport",
                        "screen_name": "BBCSport"
                    }
                ]
            },
            "favorite_count": 0,
            "favorited": false,
            "geo": null,
            "id": 942488400174702592,
            "id_str": "942488400174702592",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "retweet_count": 27,
            "retweeted": false,
            "retweeted_status": {
                "contributors": null,
                "coordinates": null,
                "created_at": "Sun Dec 17 20:14:59 +0000 2017",
                "entities": {
                    "hashtags": [
                        {
                            "indices": [
                                96,
                                102
                            ],
                            "text": "spoty"
                        }
                    ],
                    "symbols": [],
                    "urls": [
                        {
                            "display_url": "twitter.com/i/web/status/9\u2026",
                            "expanded_url": "https://twitter.com/i/web/status/942488314698960896",
                            "indices": [
                                115,
                                138
                            ],
                            "url": "https://t.co/D1FIRT7a11"
                        }
                    ],
                    "user_mentions": []
                },
                "favorite_count": 55,
                "favorited": false,
                "geo": null,
                "id": 942488314698960896,
                "id_str": "942488314698960896",
                "in_reply_to_screen_name": null,
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "is_quote_status": false,
                "lang": "en",
                "place": null,
                "possibly_sensitive": false,
                "retweet_count": 27,
                "retweeted": false,
                "source": "<a href=\"http://www.socialflow.com\" rel=\"nofollow\">SocialFlow</a>",
                "text": "It's time.\n\nWe know the contenders and now you can vote for your favourite.\n\nWho do want to win #spoty? Vote here\u2026 https://t.co/D1FIRT7a11",
                "truncated": true,
                "user": {
                    "contributors_enabled": false,
                    "created_at": "Mon Mar 14 09:44:40 +0000 2011",
                    "default_profile": false,
                    "default_profile_image": false,
                    "description": "Official https://t.co/XsBH2P4slh account. Also from @bbc - @bbcmotd @bbcf1 @bbctms @bbctennis @bbcrugbyunion @bbcsnooker & @bbcgetinspired",
                    "entities": {
                        "description": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport",
                                    "expanded_url": "http://www.bbc.co.uk/sport",
                                    "indices": [
                                        9,
                                        32
                                    ],
                                    "url": "https://t.co/XsBH2P4slh"
                                }
                            ]
                        },
                        "url": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport/0/",
                                    "expanded_url": "http://www.bbc.co.uk/sport/0/",
                                    "indices": [
                                        0,
                                        23
                                    ],
                                    "url": "https://t.co/nGZXuvg6cY"
                                }
                            ]
                        }
                    },
                    "favourites_count": 255,
                    "follow_request_sent": false,
                    "followers_count": 7128183,
                    "following": false,
                    "friends_count": 280,
                    "geo_enabled": true,
                    "has_extended_profile": false,
                    "id": 265902729,
                    "id_str": "265902729",
                    "is_translation_enabled": true,
                    "is_translator": false,
                    "lang": "en",
                    "listed_count": 18954,
                    "location": "MediaCityUK, Salford",
                    "name": "BBC Sport",
                    "notifications": false,
                    "profile_background_color": "C0DEED",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/265902729/1511019477",
                    "profile_image_url": "http://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_link_color": "FFD230",
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "profile_text_color": "333333",
                    "profile_use_background_image": true,
                    "protected": false,
                    "screen_name": "BBCSport",
                    "statuses_count": 310853,
                    "time_zone": "London",
                    "translator_type": "none",
                    "url": "https://t.co/nGZXuvg6cY",
                    "utc_offset": 0,
                    "verified": true
                }
            },
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
            "text": "RT @BBCSport: It's time.\n\nWe know the contenders and now you can vote for your favourite.\n\nWho do want to win #spoty? Vote here https://t.c\u2026",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 20:00:41 +0000 2017",
            "entities": {
                "hashtags": [
                    {
                        "indices": [
                            68,
                            74
                        ],
                        "text": "SPOTY"
                    }
                ],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "twitter.com/BBCSport/statu\u2026",
                        "expanded_url": "https://twitter.com/BBCSport/status/942483836109238272",
                        "indices": [
                            75,
                            98
                        ],
                        "url": "https://t.co/NKYPBDxSpi"
                    }
                ],
                "user_mentions": []
            },
            "favorite_count": 18,
            "favorited": false,
            "geo": null,
            "id": 942484714430107648,
            "id_str": "942484714430107648",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": true,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "quoted_status": {
                "contributors": null,
                "coordinates": null,
                "created_at": "Sun Dec 17 19:57:11 +0000 2017",
                "entities": {
                    "hashtags": [],
                    "symbols": [],
                    "urls": [
                        {
                            "display_url": "twitter.com/i/web/status/9\u2026",
                            "expanded_url": "https://twitter.com/i/web/status/942483836109238272",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/MKdkG2RsrE"
                        }
                    ],
                    "user_mentions": []
                },
                "favorite_count": 1349,
                "favorited": false,
                "geo": null,
                "id": 942483836109238272,
                "id_str": "942483836109238272",
                "in_reply_to_screen_name": null,
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "is_quote_status": false,
                "lang": "en",
                "place": null,
                "possibly_sensitive": false,
                "retweet_count": 418,
                "retweeted": false,
                "source": "<a href=\"http://www.socialflow.com\" rel=\"nofollow\">SocialFlow</a>",
                "text": "What a year it has been for Phil Foden.\n\nHe helped England win the Under-17 World Cup and took the Golden Ball awar\u2026 https://t.co/MKdkG2RsrE",
                "truncated": true,
                "user": {
                    "contributors_enabled": false,
                    "created_at": "Mon Mar 14 09:44:40 +0000 2011",
                    "default_profile": false,
                    "default_profile_image": false,
                    "description": "Official https://t.co/XsBH2P4slh account. Also from @bbc - @bbcmotd @bbcf1 @bbctms @bbctennis @bbcrugbyunion @bbcsnooker & @bbcgetinspired",
                    "entities": {
                        "description": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport",
                                    "expanded_url": "http://www.bbc.co.uk/sport",
                                    "indices": [
                                        9,
                                        32
                                    ],
                                    "url": "https://t.co/XsBH2P4slh"
                                }
                            ]
                        },
                        "url": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport/0/",
                                    "expanded_url": "http://www.bbc.co.uk/sport/0/",
                                    "indices": [
                                        0,
                                        23
                                    ],
                                    "url": "https://t.co/nGZXuvg6cY"
                                }
                            ]
                        }
                    },
                    "favourites_count": 255,
                    "follow_request_sent": false,
                    "followers_count": 7128183,
                    "following": false,
                    "friends_count": 280,
                    "geo_enabled": true,
                    "has_extended_profile": false,
                    "id": 265902729,
                    "id_str": "265902729",
                    "is_translation_enabled": true,
                    "is_translator": false,
                    "lang": "en",
                    "listed_count": 18954,
                    "location": "MediaCityUK, Salford",
                    "name": "BBC Sport",
                    "notifications": false,
                    "profile_background_color": "C0DEED",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/265902729/1511019477",
                    "profile_image_url": "http://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_link_color": "FFD230",
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "profile_text_color": "333333",
                    "profile_use_background_image": true,
                    "protected": false,
                    "screen_name": "BBCSport",
                    "statuses_count": 310853,
                    "time_zone": "London",
                    "translator_type": "none",
                    "url": "https://t.co/nGZXuvg6cY",
                    "utc_offset": 0,
                    "verified": true
                }
            },
            "quoted_status_id": 942483836109238272,
            "quoted_status_id_str": "942483836109238272",
            "retweet_count": 3,
            "retweeted": false,
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
            "text": "Congratulations to Phil Foden, BBC Young Sports Personality 2017. \ud83c\udfc6 #SPOTY https://t.co/NKYPBDxSpi",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 20:00:06 +0000 2017",
            "entities": {
                "hashtags": [],
                "media": [
                    {
                        "display_url": "pic.twitter.com/Twq4JEOOhj",
                        "expanded_url": "https://twitter.com/BBC/status/942484567671308288/photo/1",
                        "id": 942484560817815552,
                        "id_str": "942484560817815552",
                        "indices": [
                            82,
                            105
                        ],
                        "media_url": "http://pbs.twimg.com/media/DRRgtu3WAAAgNx1.jpg",
                        "media_url_https": "https://pbs.twimg.com/media/DRRgtu3WAAAgNx1.jpg",
                        "sizes": {
                            "large": {
                                "h": 1056,
                                "resize": "fit",
                                "w": 1920
                            },
                            "medium": {
                                "h": 660,
                                "resize": "fit",
                                "w": 1200
                            },
                            "small": {
                                "h": 374,
                                "resize": "fit",
                                "w": 680
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "type": "photo",
                        "url": "https://t.co/Twq4JEOOhj"
                    }
                ],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "bbc.in/2nXztZB",
                        "expanded_url": "http://bbc.in/2nXztZB",
                        "indices": [
                            58,
                            81
                        ],
                        "url": "https://t.co/p1vJrJkn6c"
                    }
                ],
                "user_mentions": []
            },
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/Twq4JEOOhj",
                        "expanded_url": "https://twitter.com/BBC/status/942484567671308288/photo/1",
                        "id": 942484560817815552,
                        "id_str": "942484560817815552",
                        "indices": [
                            82,
                            105
                        ],
                        "media_url": "http://pbs.twimg.com/media/DRRgtu3WAAAgNx1.jpg",
                        "media_url_https": "https://pbs.twimg.com/media/DRRgtu3WAAAgNx1.jpg",
                        "sizes": {
                            "large": {
                                "h": 1056,
                                "resize": "fit",
                                "w": 1920
                            },
                            "medium": {
                                "h": 660,
                                "resize": "fit",
                                "w": 1200
                            },
                            "small": {
                                "h": 374,
                                "resize": "fit",
                                "w": 680
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "type": "photo",
                        "url": "https://t.co/Twq4JEOOhj"
                    }
                ]
            },
            "favorite_count": 14,
            "favorited": false,
            "geo": null,
            "id": 942484567671308288,
            "id_str": "942484567671308288",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 4,
            "retweeted": false,
            "source": "<a href=\"http://www.radian6.com\" rel=\"nofollow\">Radian6 -Social Media Management</a>",
            "text": "\ud83c\udfac How Frankenstein and his Creature conquered the movies. https://t.co/p1vJrJkn6c https://t.co/Twq4JEOOhj",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 19:40:55 +0000 2017",
            "entities": {
                "hashtags": [
                    {
                        "indices": [
                            28,
                            34
                        ],
                        "text": "SPOTY"
                    }
                ],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "twitter.com/BBCSport/statu\u2026",
                        "expanded_url": "https://twitter.com/BBCSport/status/942477918478901248",
                        "indices": [
                            35,
                            58
                        ],
                        "url": "https://t.co/U6hBqWvmZq"
                    }
                ],
                "user_mentions": []
            },
            "favorite_count": 76,
            "favorited": false,
            "geo": null,
            "id": 942479739658305536,
            "id_str": "942479739658305536",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": true,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "quoted_status": {
                "contributors": null,
                "coordinates": null,
                "created_at": "Sun Dec 17 19:33:40 +0000 2017",
                "entities": {
                    "hashtags": [
                        {
                            "indices": [
                                22,
                                28
                            ],
                            "text": "SPOTY"
                        }
                    ],
                    "media": [
                        {
                            "display_url": "pic.twitter.com/BzfWueECe0",
                            "expanded_url": "https://twitter.com/BBCSport/status/942477918478901248/video/1",
                            "id": 942477815747772416,
                            "id_str": "942477815747772416",
                            "indices": [
                                29,
                                52
                            ],
                            "media_url": "http://pbs.twimg.com/media/DRRaqtQUQAAqv10.jpg",
                            "media_url_https": "https://pbs.twimg.com/media/DRRaqtQUQAAqv10.jpg",
                            "sizes": {
                                "large": {
                                    "h": 720,
                                    "resize": "fit",
                                    "w": 1280
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "type": "photo",
                            "url": "https://t.co/BzfWueECe0"
                        }
                    ],
                    "symbols": [],
                    "urls": [],
                    "user_mentions": []
                },
                "extended_entities": {
                    "media": [
                        {
                            "additional_media_info": {
                                "description": "BBC One",
                                "embeddable": true,
                                "monetizable": false,
                                "title": "SPOTY 2017"
                            },
                            "display_url": "pic.twitter.com/BzfWueECe0",
                            "expanded_url": "https://twitter.com/BBCSport/status/942477918478901248/video/1",
                            "id": 942477815747772416,
                            "id_str": "942477815747772416",
                            "indices": [
                                29,
                                52
                            ],
                            "media_url": "http://pbs.twimg.com/media/DRRaqtQUQAAqv10.jpg",
                            "media_url_https": "https://pbs.twimg.com/media/DRRaqtQUQAAqv10.jpg",
                            "sizes": {
                                "large": {
                                    "h": 720,
                                    "resize": "fit",
                                    "w": 1280
                                },
                                "medium": {
                                    "h": 675,
                                    "resize": "fit",
                                    "w": 1200
                                },
                                "small": {
                                    "h": 383,
                                    "resize": "fit",
                                    "w": 680
                                },
                                "thumb": {
                                    "h": 150,
                                    "resize": "crop",
                                    "w": 150
                                }
                            },
                            "type": "video",
                            "url": "https://t.co/BzfWueECe0",
                            "video_info": {
                                "aspect_ratio": [
                                    16,
                                    9
                                ],
                                "duration_millis": 31201,
                                "variants": [
                                    {
                                        "content_type": "application/x-mpegURL",
                                        "url": "https://video.twimg.com/amplify_video/942477815747772416/pl/L2fZAH-cTOMF-SAD.m3u8"
                                    },
                                    {
                                        "bitrate": 2176000,
                                        "content_type": "video/mp4",
                                        "url": "https://video.twimg.com/amplify_video/942477815747772416/vid/1280x720/yUI0KjqVAKR3ckfA.mp4"
                                    },
                                    {
                                        "bitrate": 320000,
                                        "content_type": "video/mp4",
                                        "url": "https://video.twimg.com/amplify_video/942477815747772416/vid/320x180/vlfcWYo8-RfAPUcG.mp4"
                                    },
                                    {
                                        "bitrate": 832000,
                                        "content_type": "video/mp4",
                                        "url": "https://video.twimg.com/amplify_video/942477815747772416/vid/640x360/HRTWjFb8-TtjvEjv.mp4"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "favorite_count": 6672,
                "favorited": false,
                "geo": null,
                "id": 942477918478901248,
                "id_str": "942477918478901248",
                "in_reply_to_screen_name": null,
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "is_quote_status": false,
                "lang": "en",
                "place": null,
                "possibly_sensitive": false,
                "retweet_count": 2239,
                "retweeted": false,
                "source": "<a href=\"http://snappytv.com\" rel=\"nofollow\">SnappyTV.com</a>",
                "text": "One Bradley Lowery \u2764\ufe0f #SPOTY https://t.co/BzfWueECe0",
                "truncated": false,
                "user": {
                    "contributors_enabled": false,
                    "created_at": "Mon Mar 14 09:44:40 +0000 2011",
                    "default_profile": false,
                    "default_profile_image": false,
                    "description": "Official https://t.co/XsBH2P4slh account. Also from @bbc - @bbcmotd @bbcf1 @bbctms @bbctennis @bbcrugbyunion @bbcsnooker & @bbcgetinspired",
                    "entities": {
                        "description": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport",
                                    "expanded_url": "http://www.bbc.co.uk/sport",
                                    "indices": [
                                        9,
                                        32
                                    ],
                                    "url": "https://t.co/XsBH2P4slh"
                                }
                            ]
                        },
                        "url": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport/0/",
                                    "expanded_url": "http://www.bbc.co.uk/sport/0/",
                                    "indices": [
                                        0,
                                        23
                                    ],
                                    "url": "https://t.co/nGZXuvg6cY"
                                }
                            ]
                        }
                    },
                    "favourites_count": 255,
                    "follow_request_sent": false,
                    "followers_count": 7128183,
                    "following": false,
                    "friends_count": 280,
                    "geo_enabled": true,
                    "has_extended_profile": false,
                    "id": 265902729,
                    "id_str": "265902729",
                    "is_translation_enabled": true,
                    "is_translator": false,
                    "lang": "en",
                    "listed_count": 18954,
                    "location": "MediaCityUK, Salford",
                    "name": "BBC Sport",
                    "notifications": false,
                    "profile_background_color": "C0DEED",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/265902729/1511019477",
                    "profile_image_url": "http://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_link_color": "FFD230",
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "profile_text_color": "333333",
                    "profile_use_background_image": true,
                    "protected": false,
                    "screen_name": "BBCSport",
                    "statuses_count": 310853,
                    "time_zone": "London",
                    "translator_type": "none",
                    "url": "https://t.co/nGZXuvg6cY",
                    "utc_offset": 0,
                    "verified": true
                }
            },
            "quoted_status_id": 942477918478901248,
            "quoted_status_id_str": "942477918478901248",
            "retweet_count": 20,
            "retweeted": false,
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
            "text": "He will never be forgotten. #SPOTY https://t.co/U6hBqWvmZq",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 19:32:28 +0000 2017",
            "entities": {
                "hashtags": [
                    {
                        "indices": [
                            72,
                            78
                        ],
                        "text": "SPOTY"
                    }
                ],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "twitter.com/BBCSport/statu\u2026",
                        "expanded_url": "https://twitter.com/BBCSport/status/942476355853221888",
                        "indices": [
                            84,
                            107
                        ],
                        "url": "https://t.co/0wtAvD9R97"
                    }
                ],
                "user_mentions": []
            },
            "favorite_count": 98,
            "favorited": false,
            "geo": null,
            "id": 942477613641105408,
            "id_str": "942477613641105408",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": true,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "quoted_status": {
                "contributors": null,
                "coordinates": null,
                "created_at": "Sun Dec 17 19:27:28 +0000 2017",
                "entities": {
                    "hashtags": [],
                    "symbols": [],
                    "urls": [
                        {
                            "display_url": "twitter.com/i/web/status/9\u2026",
                            "expanded_url": "https://twitter.com/i/web/status/942476355853221888",
                            "indices": [
                                116,
                                139
                            ],
                            "url": "https://t.co/kghCOJPCxV"
                        }
                    ],
                    "user_mentions": []
                },
                "favorite_count": 3574,
                "favorited": false,
                "geo": null,
                "id": 942476355853221888,
                "id_str": "942476355853221888",
                "in_reply_to_screen_name": null,
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "is_quote_status": false,
                "lang": "en",
                "place": null,
                "possibly_sensitive": false,
                "retweet_count": 1538,
                "retweeted": false,
                "source": "<a href=\"http://www.socialflow.com\" rel=\"nofollow\">SocialFlow</a>",
                "text": "This year we lost a young boy who touched the lives of millions.\n\nThe sporting world will never forget him and the\u2026 https://t.co/kghCOJPCxV",
                "truncated": true,
                "user": {
                    "contributors_enabled": false,
                    "created_at": "Mon Mar 14 09:44:40 +0000 2011",
                    "default_profile": false,
                    "default_profile_image": false,
                    "description": "Official https://t.co/XsBH2P4slh account. Also from @bbc - @bbcmotd @bbcf1 @bbctms @bbctennis @bbcrugbyunion @bbcsnooker & @bbcgetinspired",
                    "entities": {
                        "description": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport",
                                    "expanded_url": "http://www.bbc.co.uk/sport",
                                    "indices": [
                                        9,
                                        32
                                    ],
                                    "url": "https://t.co/XsBH2P4slh"
                                }
                            ]
                        },
                        "url": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport/0/",
                                    "expanded_url": "http://www.bbc.co.uk/sport/0/",
                                    "indices": [
                                        0,
                                        23
                                    ],
                                    "url": "https://t.co/nGZXuvg6cY"
                                }
                            ]
                        }
                    },
                    "favourites_count": 255,
                    "follow_request_sent": false,
                    "followers_count": 7128183,
                    "following": false,
                    "friends_count": 280,
                    "geo_enabled": true,
                    "has_extended_profile": false,
                    "id": 265902729,
                    "id_str": "265902729",
                    "is_translation_enabled": true,
                    "is_translator": false,
                    "lang": "en",
                    "listed_count": 18954,
                    "location": "MediaCityUK, Salford",
                    "name": "BBC Sport",
                    "notifications": false,
                    "profile_background_color": "C0DEED",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/265902729/1511019477",
                    "profile_image_url": "http://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_link_color": "FFD230",
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "profile_text_color": "333333",
                    "profile_use_background_image": true,
                    "protected": false,
                    "screen_name": "BBCSport",
                    "statuses_count": 310853,
                    "time_zone": "London",
                    "translator_type": "none",
                    "url": "https://t.co/nGZXuvg6cY",
                    "utc_offset": 0,
                    "verified": true
                }
            },
            "quoted_status_id": 942476355853221888,
            "quoted_status_id_str": "942476355853221888",
            "retweet_count": 24,
            "retweeted": false,
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
            "text": "Bradley Lowery has been named the winner of the Helen Rollason Award at #SPOTY 2017 https://t.co/0wtAvD9R97",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 19:30:06 +0000 2017",
            "entities": {
                "hashtags": [
                    {
                        "indices": [
                            58,
                            72
                        ],
                        "text": "TheApprentice"
                    }
                ],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "twitter.com/i/web/status/9\u2026",
                        "expanded_url": "https://twitter.com/i/web/status/942477020650405888",
                        "indices": [
                            113,
                            136
                        ],
                        "url": "https://t.co/GpWayrrVNG"
                    }
                ],
                "user_mentions": [
                    {
                        "id": 160926944,
                        "id_str": "160926944",
                        "indices": [
                            9,
                            20
                        ],
                        "name": "Lord Sugar",
                        "screen_name": "Lord_Sugar"
                    },
                    {
                        "id": 871686942,
                        "id_str": "871686942",
                        "indices": [
                            103,
                            110
                        ],
                        "name": "BBC One",
                        "screen_name": "BBCOne"
                    }
                ]
            },
            "favorite_count": 13,
            "favorited": false,
            "geo": null,
            "id": 942477020650405888,
            "id_str": "942477020650405888",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 2,
            "retweeted": false,
            "source": "<a href=\"http://www.radian6.com\" rel=\"nofollow\">Radian6 -Social Media Management</a>",
            "text": "Tonight, @Lord_Sugar's final candidates go head to head. \n#TheApprentice: The Final. Tonight at 9pm on @BBCOne.\u2026 https://t.co/GpWayrrVNG",
            "truncated": true,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 19:00:02 +0000 2017",
            "entities": {
                "hashtags": [
                    {
                        "indices": [
                            73,
                            86
                        ],
                        "text": "EmployableMe"
                    }
                ],
                "media": [
                    {
                        "display_url": "pic.twitter.com/ULiqwTgXEB",
                        "expanded_url": "https://twitter.com/BBC/status/942469452087439361/video/1",
                        "id": 940903578134294528,
                        "id_str": "940903578134294528",
                        "indices": [
                            101,
                            124
                        ],
                        "media_url": "http://pbs.twimg.com/amplify_video_thumb/940903578134294528/img/TYEkUZPRd0OzOYIi.jpg",
                        "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/940903578134294528/img/TYEkUZPRd0OzOYIi.jpg",
                        "sizes": {
                            "large": {
                                "h": 720,
                                "resize": "fit",
                                "w": 720
                            },
                            "medium": {
                                "h": 720,
                                "resize": "fit",
                                "w": 720
                            },
                            "small": {
                                "h": 680,
                                "resize": "fit",
                                "w": 680
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "type": "photo",
                        "url": "https://t.co/ULiqwTgXEB"
                    }
                ],
                "symbols": [],
                "urls": [],
                "user_mentions": [
                    {
                        "id": 1586183960,
                        "id_str": "1586183960",
                        "indices": [
                            93,
                            100
                        ],
                        "name": "BBC Two",
                        "screen_name": "BBCTwo"
                    }
                ]
            },
            "extended_entities": {
                "media": [
                    {
                        "additional_media_info": {
                            "description": "",
                            "embeddable": true,
                            "monetizable": false,
                            "title": ""
                        },
                        "display_url": "pic.twitter.com/ULiqwTgXEB",
                        "expanded_url": "https://twitter.com/BBC/status/942469452087439361/video/1",
                        "id": 940903578134294528,
                        "id_str": "940903578134294528",
                        "indices": [
                            101,
                            124
                        ],
                        "media_url": "http://pbs.twimg.com/amplify_video_thumb/940903578134294528/img/TYEkUZPRd0OzOYIi.jpg",
                        "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/940903578134294528/img/TYEkUZPRd0OzOYIi.jpg",
                        "sizes": {
                            "large": {
                                "h": 720,
                                "resize": "fit",
                                "w": 720
                            },
                            "medium": {
                                "h": 720,
                                "resize": "fit",
                                "w": 720
                            },
                            "small": {
                                "h": 680,
                                "resize": "fit",
                                "w": 680
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "type": "video",
                        "url": "https://t.co/ULiqwTgXEB",
                        "video_info": {
                            "aspect_ratio": [
                                1,
                                1
                            ],
                            "duration_millis": 150367,
                            "variants": [
                                {
                                    "bitrate": 832000,
                                    "content_type": "video/mp4",
                                    "url": "https://video.twimg.com/amplify_video/940903578134294528/vid/480x480/L4jbTzXWILx7QvrB.mp4"
                                },
                                {
                                    "content_type": "application/x-mpegURL",
                                    "url": "https://video.twimg.com/amplify_video/940903578134294528/pl/oXCi-FTuz2WGDSEn.m3u8"
                                },
                                {
                                    "bitrate": 320000,
                                    "content_type": "video/mp4",
                                    "url": "https://video.twimg.com/amplify_video/940903578134294528/vid/240x240/It2f8-fCufTjmLFB.mp4"
                                },
                                {
                                    "bitrate": 1280000,
                                    "content_type": "video/mp4",
                                    "url": "https://video.twimg.com/amplify_video/940903578134294528/vid/720x720/4WInX8TQ0CIubQEJ.mp4"
                                }
                            ]
                        }
                    }
                ]
            },
            "favorite_count": 37,
            "favorited": false,
            "geo": null,
            "id": 942469452087439361,
            "id_str": "942469452087439361",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 14,
            "retweeted": false,
            "source": "<a href=\"https://studio.twitter.com\" rel=\"nofollow\">Media Studio</a>",
            "text": "'I just want to show people that I'm disabled, but I'm employable.' \u2764\ufe0f\ufe0f\n\n#EmployableMe | Via @BBCTwo https://t.co/ULiqwTgXEB",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 18:00:08 +0000 2017",
            "entities": {
                "hashtags": [],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "twitter.com/i/web/status/9\u2026",
                        "expanded_url": "https://twitter.com/i/web/status/942454376974770176",
                        "indices": [
                            116,
                            139
                        ],
                        "url": "https://t.co/QJUUYFgWhD"
                    }
                ],
                "user_mentions": []
            },
            "favorite_count": 10,
            "favorited": false,
            "geo": null,
            "id": 942454376974770176,
            "id_str": "942454376974770176",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 6,
            "retweeted": false,
            "source": "<a href=\"http://www.radian6.com\" rel=\"nofollow\">Radian6 -Social Media Management</a>",
            "text": "Spending \u00a3100 a month on rent in London secures floor space equivalent to a small garden shed in parts of northern\u2026 https://t.co/QJUUYFgWhD",
            "truncated": true,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 17:44:03 +0000 2017",
            "entities": {
                "hashtags": [],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "twitter.com/i/web/status/9\u2026",
                        "expanded_url": "https://twitter.com/i/web/status/942450333023907840",
                        "indices": [
                            117,
                            140
                        ],
                        "url": "https://t.co/MMZcLeQ0yc"
                    }
                ],
                "user_mentions": [
                    {
                        "id": 471287735,
                        "id_str": "471287735",
                        "indices": [
                            9,
                            21
                        ],
                        "name": "Gary Lineker",
                        "screen_name": "GaryLineker"
                    },
                    {
                        "id": 171404842,
                        "id_str": "171404842",
                        "indices": [
                            23,
                            36
                        ],
                        "name": "Clare Balding",
                        "screen_name": "clarebalding"
                    },
                    {
                        "id": 32916289,
                        "id_str": "32916289",
                        "indices": [
                            41,
                            52
                        ],
                        "name": "Gabby Logan",
                        "screen_name": "GabbyLogan"
                    }
                ]
            },
            "favorite_count": 10,
            "favorited": false,
            "geo": null,
            "id": 942450333023907840,
            "id_str": "942450333023907840",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 6,
            "retweeted": false,
            "source": "<a href=\"http://www.radian6.com\" rel=\"nofollow\">Radian6 -Social Media Management</a>",
            "text": "Tonight, @GaryLineker, @ClareBalding and @GabbyLogan present the 2017 BBC Sports Personality of the Year. 6:45pm on\u2026 https://t.co/MMZcLeQ0yc",
            "truncated": true,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 17:40:59 +0000 2017",
            "entities": {
                "hashtags": [],
                "symbols": [],
                "urls": [],
                "user_mentions": [
                    {
                        "id": 265902729,
                        "id_str": "265902729",
                        "indices": [
                            3,
                            12
                        ],
                        "name": "BBC Sport",
                        "screen_name": "BBCSport"
                    },
                    {
                        "id": 53732896,
                        "id_str": "53732896",
                        "indices": [
                            93,
                            106
                        ],
                        "name": "Tom Daley",
                        "screen_name": "TomDaley1994"
                    },
                    {
                        "id": 42891713,
                        "id_str": "42891713",
                        "indices": [
                            111,
                            123
                        ],
                        "name": "Yasmin Evans",
                        "screen_name": "YasminEvans"
                    }
                ]
            },
            "favorite_count": 0,
            "favorited": false,
            "geo": null,
            "id": 942449558348619777,
            "id_str": "942449558348619777",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "retweet_count": 8,
            "retweeted": false,
            "retweeted_status": {
                "contributors": null,
                "coordinates": null,
                "created_at": "Sun Dec 17 17:30:31 +0000 2017",
                "entities": {
                    "hashtags": [],
                    "symbols": [],
                    "urls": [
                        {
                            "display_url": "twitter.com/i/web/status/9\u2026",
                            "expanded_url": "https://twitter.com/i/web/status/942446925432934402",
                            "indices": [
                                117,
                                140
                            ],
                            "url": "https://t.co/0X7KxKo5Ws"
                        }
                    ],
                    "user_mentions": [
                        {
                            "id": 53732896,
                            "id_str": "53732896",
                            "indices": [
                                79,
                                92
                            ],
                            "name": "Tom Daley",
                            "screen_name": "TomDaley1994"
                        },
                        {
                            "id": 42891713,
                            "id_str": "42891713",
                            "indices": [
                                97,
                                109
                            ],
                            "name": "Yasmin Evans",
                            "screen_name": "YasminEvans"
                        }
                    ]
                },
                "favorite_count": 35,
                "favorited": false,
                "geo": null,
                "id": 942446925432934402,
                "id_str": "942446925432934402",
                "in_reply_to_screen_name": null,
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "is_quote_status": false,
                "lang": "en",
                "place": null,
                "possibly_sensitive": false,
                "retweet_count": 8,
                "retweeted": false,
                "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
                "text": "Strap yourselves in for The SPOTY Social \u2013 we\u2019re LIVE from the red carpet with @TomDaley1994 and @YasminEvans at Sp\u2026 https://t.co/0X7KxKo5Ws",
                "truncated": true,
                "user": {
                    "contributors_enabled": false,
                    "created_at": "Mon Mar 14 09:44:40 +0000 2011",
                    "default_profile": false,
                    "default_profile_image": false,
                    "description": "Official https://t.co/XsBH2P4slh account. Also from @bbc - @bbcmotd @bbcf1 @bbctms @bbctennis @bbcrugbyunion @bbcsnooker & @bbcgetinspired",
                    "entities": {
                        "description": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport",
                                    "expanded_url": "http://www.bbc.co.uk/sport",
                                    "indices": [
                                        9,
                                        32
                                    ],
                                    "url": "https://t.co/XsBH2P4slh"
                                }
                            ]
                        },
                        "url": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport/0/",
                                    "expanded_url": "http://www.bbc.co.uk/sport/0/",
                                    "indices": [
                                        0,
                                        23
                                    ],
                                    "url": "https://t.co/nGZXuvg6cY"
                                }
                            ]
                        }
                    },
                    "favourites_count": 255,
                    "follow_request_sent": false,
                    "followers_count": 7128183,
                    "following": false,
                    "friends_count": 280,
                    "geo_enabled": true,
                    "has_extended_profile": false,
                    "id": 265902729,
                    "id_str": "265902729",
                    "is_translation_enabled": true,
                    "is_translator": false,
                    "lang": "en",
                    "listed_count": 18954,
                    "location": "MediaCityUK, Salford",
                    "name": "BBC Sport",
                    "notifications": false,
                    "profile_background_color": "C0DEED",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/265902729/1511019477",
                    "profile_image_url": "http://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_link_color": "FFD230",
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "profile_text_color": "333333",
                    "profile_use_background_image": true,
                    "protected": false,
                    "screen_name": "BBCSport",
                    "statuses_count": 310853,
                    "time_zone": "London",
                    "translator_type": "none",
                    "url": "https://t.co/nGZXuvg6cY",
                    "utc_offset": 0,
                    "verified": true
                }
            },
            "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
            "text": "RT @BBCSport: Strap yourselves in for The SPOTY Social \u2013 we\u2019re LIVE from the red carpet with @TomDaley1994 and @YasminEvans at Sports Perso\u2026",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 17:30:04 +0000 2017",
            "entities": {
                "hashtags": [],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "twitter.com/i/web/status/9\u2026",
                        "expanded_url": "https://twitter.com/i/web/status/942446812694306817",
                        "indices": [
                            98,
                            121
                        ],
                        "url": "https://t.co/aKVp7FQXRq"
                    }
                ],
                "user_mentions": []
            },
            "favorite_count": 18,
            "favorited": false,
            "geo": null,
            "id": 942446812694306817,
            "id_str": "942446812694306817",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 5,
            "retweeted": false,
            "source": "<a href=\"http://www.radian6.com\" rel=\"nofollow\">Radian6 -Social Media Management</a>",
            "text": "Spare a thought for the brothers whose rare disease means they'll never eat Christmas dinner. \ud83c\udf57\ud83d\udc94\u2026 https://t.co/aKVp7FQXRq",
            "truncated": true,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 17:00:04 +0000 2017",
            "entities": {
                "hashtags": [
                    {
                        "indices": [
                            62,
                            74
                        ],
                        "text": "BluePlanet2"
                    }
                ],
                "media": [
                    {
                        "display_url": "pic.twitter.com/0GXEybNKgt",
                        "expanded_url": "https://twitter.com/BBC/status/942439263043403776/video/1",
                        "id": 940285355449815040,
                        "id_str": "940285355449815040",
                        "indices": [
                            89,
                            112
                        ],
                        "media_url": "http://pbs.twimg.com/amplify_video_thumb/940285355449815040/img/x6JoNzRn4DZWFUwV.jpg",
                        "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/940285355449815040/img/x6JoNzRn4DZWFUwV.jpg",
                        "sizes": {
                            "large": {
                                "h": 720,
                                "resize": "fit",
                                "w": 720
                            },
                            "medium": {
                                "h": 720,
                                "resize": "fit",
                                "w": 720
                            },
                            "small": {
                                "h": 680,
                                "resize": "fit",
                                "w": 680
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "type": "photo",
                        "url": "https://t.co/0GXEybNKgt"
                    }
                ],
                "symbols": [],
                "urls": [],
                "user_mentions": [
                    {
                        "id": 70725281,
                        "id_str": "70725281",
                        "indices": [
                            79,
                            88
                        ],
                        "name": "BBC Earth",
                        "screen_name": "BBCEarth"
                    }
                ]
            },
            "extended_entities": {
                "media": [
                    {
                        "additional_media_info": {
                            "call_to_actions": {
                                "visit_site": {
                                    "url": "http://www.bbcearth.com/blueplanet2"
                                }
                            },
                            "description": "",
                            "embeddable": false,
                            "monetizable": false,
                            "title": ""
                        },
                        "display_url": "pic.twitter.com/0GXEybNKgt",
                        "expanded_url": "https://twitter.com/BBC/status/942439263043403776/video/1",
                        "id": 940285355449815040,
                        "id_str": "940285355449815040",
                        "indices": [
                            89,
                            112
                        ],
                        "media_url": "http://pbs.twimg.com/amplify_video_thumb/940285355449815040/img/x6JoNzRn4DZWFUwV.jpg",
                        "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/940285355449815040/img/x6JoNzRn4DZWFUwV.jpg",
                        "sizes": {
                            "large": {
                                "h": 720,
                                "resize": "fit",
                                "w": 720
                            },
                            "medium": {
                                "h": 720,
                                "resize": "fit",
                                "w": 720
                            },
                            "small": {
                                "h": 680,
                                "resize": "fit",
                                "w": 680
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "type": "photo",
                        "url": "https://t.co/0GXEybNKgt"
                    }
                ]
            },
            "favorite_count": 109,
            "favorited": false,
            "geo": null,
            "id": 942439263043403776,
            "id_str": "942439263043403776",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 64,
            "retweeted": false,
            "source": "<a href=\"https://studio.twitter.com\" rel=\"nofollow\">Media Studio</a>",
            "text": "'If the oceans don't stay healthy, human beings are doomed.'\n\n#BluePlanet2 via @BBCEarth https://t.co/0GXEybNKgt",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 16:38:24 +0000 2017",
            "entities": {
                "hashtags": [
                    {
                        "indices": [
                            19,
                            25
                        ],
                        "text": "SPOTY"
                    },
                    {
                        "indices": [
                            125,
                            131
                        ],
                        "text": "SPOTY"
                    }
                ],
                "symbols": [],
                "urls": [],
                "user_mentions": [
                    {
                        "id": 265902729,
                        "id_str": "265902729",
                        "indices": [
                            3,
                            12
                        ],
                        "name": "BBC Sport",
                        "screen_name": "BBCSport"
                    },
                    {
                        "id": 53732896,
                        "id_str": "53732896",
                        "indices": [
                            85,
                            98
                        ],
                        "name": "Tom Daley",
                        "screen_name": "TomDaley1994"
                    },
                    {
                        "id": 42891713,
                        "id_str": "42891713",
                        "indices": [
                            103,
                            115
                        ],
                        "name": "Yasmin Evans",
                        "screen_name": "YasminEvans"
                    }
                ]
            },
            "favorite_count": 0,
            "favorited": false,
            "geo": null,
            "id": 942433808565055489,
            "id_str": "942433808565055489",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "retweet_count": 13,
            "retweeted": false,
            "retweeted_status": {
                "contributors": null,
                "coordinates": null,
                "created_at": "Sun Dec 17 14:33:00 +0000 2017",
                "entities": {
                    "hashtags": [
                        {
                            "indices": [
                                5,
                                11
                            ],
                            "text": "SPOTY"
                        }
                    ],
                    "symbols": [],
                    "urls": [
                        {
                            "display_url": "twitter.com/i/web/status/9\u2026",
                            "expanded_url": "https://twitter.com/i/web/status/942402252341256192",
                            "indices": [
                                112,
                                135
                            ],
                            "url": "https://t.co/lnuhzxwMuu"
                        }
                    ],
                    "user_mentions": [
                        {
                            "id": 53732896,
                            "id_str": "53732896",
                            "indices": [
                                71,
                                84
                            ],
                            "name": "Tom Daley",
                            "screen_name": "TomDaley1994"
                        },
                        {
                            "id": 42891713,
                            "id_str": "42891713",
                            "indices": [
                                89,
                                101
                            ],
                            "name": "Yasmin Evans",
                            "screen_name": "YasminEvans"
                        }
                    ]
                },
                "favorite_count": 38,
                "favorited": false,
                "geo": null,
                "id": 942402252341256192,
                "id_str": "942402252341256192",
                "in_reply_to_screen_name": null,
                "in_reply_to_status_id": null,
                "in_reply_to_status_id_str": null,
                "in_reply_to_user_id": null,
                "in_reply_to_user_id_str": null,
                "is_quote_status": false,
                "lang": "en",
                "place": null,
                "possibly_sensitive": false,
                "retweet_count": 13,
                "retweeted": false,
                "source": "<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>",
                "text": "It's #SPOTY weekend and what a start to Sunday night we have for you.\n\n@TomDaley1994 and @YasminEvans host The\u2026 https://t.co/lnuhzxwMuu",
                "truncated": true,
                "user": {
                    "contributors_enabled": false,
                    "created_at": "Mon Mar 14 09:44:40 +0000 2011",
                    "default_profile": false,
                    "default_profile_image": false,
                    "description": "Official https://t.co/XsBH2P4slh account. Also from @bbc - @bbcmotd @bbcf1 @bbctms @bbctennis @bbcrugbyunion @bbcsnooker & @bbcgetinspired",
                    "entities": {
                        "description": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport",
                                    "expanded_url": "http://www.bbc.co.uk/sport",
                                    "indices": [
                                        9,
                                        32
                                    ],
                                    "url": "https://t.co/XsBH2P4slh"
                                }
                            ]
                        },
                        "url": {
                            "urls": [
                                {
                                    "display_url": "bbc.co.uk/sport/0/",
                                    "expanded_url": "http://www.bbc.co.uk/sport/0/",
                                    "indices": [
                                        0,
                                        23
                                    ],
                                    "url": "https://t.co/nGZXuvg6cY"
                                }
                            ]
                        }
                    },
                    "favourites_count": 255,
                    "follow_request_sent": false,
                    "followers_count": 7128183,
                    "following": false,
                    "friends_count": 280,
                    "geo_enabled": true,
                    "has_extended_profile": false,
                    "id": 265902729,
                    "id_str": "265902729",
                    "is_translation_enabled": true,
                    "is_translator": false,
                    "lang": "en",
                    "listed_count": 18954,
                    "location": "MediaCityUK, Salford",
                    "name": "BBC Sport",
                    "notifications": false,
                    "profile_background_color": "C0DEED",
                    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/240463705/BBCSportTwitter_backing11.jpg",
                    "profile_background_tile": false,
                    "profile_banner_url": "https://pbs.twimg.com/profile_banners/265902729/1511019477",
                    "profile_image_url": "http://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_image_url_https": "https://pbs.twimg.com/profile_images/897379868014411777/xpJaG4a5_normal.jpg",
                    "profile_link_color": "FFD230",
                    "profile_sidebar_border_color": "C0DEED",
                    "profile_sidebar_fill_color": "DDEEF6",
                    "profile_text_color": "333333",
                    "profile_use_background_image": true,
                    "protected": false,
                    "screen_name": "BBCSport",
                    "statuses_count": 310853,
                    "time_zone": "London",
                    "translator_type": "none",
                    "url": "https://t.co/nGZXuvg6cY",
                    "utc_offset": 0,
                    "verified": true
                }
            },
            "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
            "text": "RT @BBCSport: It's #SPOTY weekend and what a start to Sunday night we have for you.\n\n@TomDaley1994 and @YasminEvans host The #SPOTY Social\u2026",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 16:00:06 +0000 2017",
            "entities": {
                "hashtags": [],
                "media": [
                    {
                        "display_url": "pic.twitter.com/k2DN8HMDzZ",
                        "expanded_url": "https://twitter.com/BBC/status/942424171660922880/photo/1",
                        "id": 942424164706803713,
                        "id_str": "942424164706803713",
                        "indices": [
                            93,
                            116
                        ],
                        "media_url": "http://pbs.twimg.com/media/DRQpyN0X4AEKrak.jpg",
                        "media_url_https": "https://pbs.twimg.com/media/DRQpyN0X4AEKrak.jpg",
                        "sizes": {
                            "large": {
                                "h": 1056,
                                "resize": "fit",
                                "w": 1920
                            },
                            "medium": {
                                "h": 660,
                                "resize": "fit",
                                "w": 1200
                            },
                            "small": {
                                "h": 374,
                                "resize": "fit",
                                "w": 680
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "type": "photo",
                        "url": "https://t.co/k2DN8HMDzZ"
                    }
                ],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "bbc.in/2nWS5sx",
                        "expanded_url": "http://bbc.in/2nWS5sx",
                        "indices": [
                            69,
                            92
                        ],
                        "url": "https://t.co/zMiJLLau4a"
                    }
                ],
                "user_mentions": []
            },
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/k2DN8HMDzZ",
                        "expanded_url": "https://twitter.com/BBC/status/942424171660922880/photo/1",
                        "id": 942424164706803713,
                        "id_str": "942424164706803713",
                        "indices": [
                            93,
                            116
                        ],
                        "media_url": "http://pbs.twimg.com/media/DRQpyN0X4AEKrak.jpg",
                        "media_url_https": "https://pbs.twimg.com/media/DRQpyN0X4AEKrak.jpg",
                        "sizes": {
                            "large": {
                                "h": 1056,
                                "resize": "fit",
                                "w": 1920
                            },
                            "medium": {
                                "h": 660,
                                "resize": "fit",
                                "w": 1200
                            },
                            "small": {
                                "h": 374,
                                "resize": "fit",
                                "w": 680
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "type": "photo",
                        "url": "https://t.co/k2DN8HMDzZ"
                    }
                ]
            },
            "favorite_count": 47,
            "favorited": false,
            "geo": null,
            "id": 942424171660922880,
            "id_str": "942424171660922880",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 11,
            "retweeted": false,
            "source": "<a href=\"http://www.radian6.com\" rel=\"nofollow\">Radian6 -Social Media Management</a>",
            "text": "\ud83c\udf9e Star Wars: Fans shouldn't worry if The Last Jedi gets bad reviews. https://t.co/zMiJLLau4a https://t.co/k2DN8HMDzZ",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 15:00:07 +0000 2017",
            "entities": {
                "hashtags": [],
                "media": [
                    {
                        "display_url": "pic.twitter.com/YP2cqzyJJd",
                        "expanded_url": "https://twitter.com/BBC/status/942409074355920901/photo/1",
                        "id": 942409069222121472,
                        "id_str": "942409069222121472",
                        "indices": [
                            67,
                            90
                        ],
                        "media_url": "http://pbs.twimg.com/media/DRQcDiwXUAAlQy7.jpg",
                        "media_url_https": "https://pbs.twimg.com/media/DRQcDiwXUAAlQy7.jpg",
                        "sizes": {
                            "large": {
                                "h": 1056,
                                "resize": "fit",
                                "w": 1920
                            },
                            "medium": {
                                "h": 660,
                                "resize": "fit",
                                "w": 1200
                            },
                            "small": {
                                "h": 374,
                                "resize": "fit",
                                "w": 680
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "type": "photo",
                        "url": "https://t.co/YP2cqzyJJd"
                    }
                ],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "bbc.in/2ATgu54",
                        "expanded_url": "http://bbc.in/2ATgu54",
                        "indices": [
                            43,
                            66
                        ],
                        "url": "https://t.co/4xTQ8VaPZi"
                    }
                ],
                "user_mentions": []
            },
            "extended_entities": {
                "media": [
                    {
                        "display_url": "pic.twitter.com/YP2cqzyJJd",
                        "expanded_url": "https://twitter.com/BBC/status/942409074355920901/photo/1",
                        "id": 942409069222121472,
                        "id_str": "942409069222121472",
                        "indices": [
                            67,
                            90
                        ],
                        "media_url": "http://pbs.twimg.com/media/DRQcDiwXUAAlQy7.jpg",
                        "media_url_https": "https://pbs.twimg.com/media/DRQcDiwXUAAlQy7.jpg",
                        "sizes": {
                            "large": {
                                "h": 1056,
                                "resize": "fit",
                                "w": 1920
                            },
                            "medium": {
                                "h": 660,
                                "resize": "fit",
                                "w": 1200
                            },
                            "small": {
                                "h": 374,
                                "resize": "fit",
                                "w": 680
                            },
                            "thumb": {
                                "h": 150,
                                "resize": "crop",
                                "w": 150
                            }
                        },
                        "type": "photo",
                        "url": "https://t.co/YP2cqzyJJd"
                    }
                ]
            },
            "favorite_count": 11,
            "favorited": false,
            "geo": null,
            "id": 942409074355920901,
            "id_str": "942409074355920901",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 6,
            "retweeted": false,
            "source": "<a href=\"http://www.radian6.com\" rel=\"nofollow\">Radian6 -Social Media Management</a>",
            "text": "Can good design make food taste better? \ud83e\udd58\ud83d\ude0b https://t.co/4xTQ8VaPZi https://t.co/YP2cqzyJJd",
            "truncated": false,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        },
        {
            "contributors": null,
            "coordinates": null,
            "created_at": "Sun Dec 17 14:00:01 +0000 2017",
            "entities": {
                "hashtags": [],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "twitter.com/i/web/status/9\u2026",
                        "expanded_url": "https://twitter.com/i/web/status/942393950672785408",
                        "indices": [
                            95,
                            118
                        ],
                        "url": "https://t.co/MAwzbO5JUq"
                    }
                ],
                "user_mentions": []
            },
            "favorite_count": 453,
            "favorited": false,
            "geo": null,
            "id": 942393950672785408,
            "id_str": "942393950672785408",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 234,
            "retweeted": false,
            "source": "<a href=\"https://studio.twitter.com\" rel=\"nofollow\">Media Studio</a>",
            "text": "This grandmother is transforming villages by building dams to bring them much-needed water. \ud83d\udca6\u2026 https://t.co/MAwzbO5JUq",
            "truncated": true,
            "user": {
                "contributors_enabled": false,
                "created_at": "Thu Jan 29 08:30:16 +0000 2009",
                "default_profile": false,
                "default_profile_image": false,
                "description": "Our mission is to enrich your life and to inform, educate and entertain you, wherever you are.",
                "entities": {
                    "description": {
                        "urls": []
                    },
                    "url": {
                        "urls": [
                            {
                                "display_url": "bbc.co.uk",
                                "expanded_url": "http://www.bbc.co.uk",
                                "indices": [
                                    0,
                                    22
                                ],
                                "url": "http://t.co/9Yv7DJ1Pmu"
                            }
                        ]
                    }
                },
                "favourites_count": 3594,
                "follow_request_sent": false,
                "followers_count": 1159513,
                "following": false,
                "friends_count": 160,
                "geo_enabled": false,
                "has_extended_profile": false,
                "id": 19701628,
                "id_str": "19701628",
                "is_translation_enabled": false,
                "is_translator": false,
                "lang": "en",
                "listed_count": 9315,
                "location": "TV. Radio. Online",
                "name": "BBC",
                "notifications": false,
                "profile_background_color": "000000",
                "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/459267803640385537/QkzQGfqX.jpeg",
                "profile_background_tile": false,
                "profile_banner_url": "https://pbs.twimg.com/profile_banners/19701628/1512226202",
                "profile_image_url": "http://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/662708106/bbc_normal.png",
                "profile_link_color": "000000",
                "profile_sidebar_border_color": "000000",
                "profile_sidebar_fill_color": "DDEEF6",
                "profile_text_color": "333333",
                "profile_use_background_image": false,
                "protected": false,
                "screen_name": "BBC",
                "statuses_count": 20551,
                "time_zone": "London",
                "translator_type": "regular",
                "url": "http://t.co/9Yv7DJ1Pmu",
                "utc_offset": 0,
                "verified": true
            }
        }
    ]
    


```python
tweet_text = []
org_text = []
date = []
for org in news_orgs:
    for x in range(6):
        public_tweets = api.user_timeline(org,page = x)
        for tweet in public_tweets:
            print(tweet['text'])
            print(tweet['created_at'])
            print(org)
            tweet_text.append(tweet['text'])
            date.append(tweet['created_at'])
            org_text.append(org)
```

    Congratulations and a #BigThankYou to Denise. 🎉 What an inspiration. #SPOTY https://t.co/xRHVhwEjFP
    Sun Dec 17 20:34:25 +0000 2017
    @BBC
    Follow the production of a contemporary performance of the nativity unlike any other. #Alternativity 9pm on @BBCTwo… https://t.co/RLZvnMA8yJ
    Sun Dec 17 20:31:03 +0000 2017
    @BBC
    RT @BBCSport: .@NoelGallagher singing the Beatles 
    
    Beautiful.
    
    Watch #SPOTY live: https://t.co/J5Un4g5oDM https://t.co/flkmCR2TWw
    Sun Dec 17 20:29:11 +0000 2017
    @BBC
    RT @BBCSport: The voting is open for #SPOTY.
    
    It's time to have your say ➡️ https://t.co/DQf1YQT4L0 https://t.co/WvQYr12Ds7
    Sun Dec 17 20:19:09 +0000 2017
    @BBC
    RT @BBCSport: It's time.
    
    We know the contenders and now you can vote for your favourite.
    
    Who do want to win #spoty? Vote here https://t.c…
    Sun Dec 17 20:15:19 +0000 2017
    @BBC
    Congratulations to Phil Foden, BBC Young Sports Personality 2017. 🏆 #SPOTY https://t.co/NKYPBDxSpi
    Sun Dec 17 20:00:41 +0000 2017
    @BBC
    🎬 How Frankenstein and his Creature conquered the movies. https://t.co/p1vJrJkn6c https://t.co/Twq4JEOOhj
    Sun Dec 17 20:00:06 +0000 2017
    @BBC
    He will never be forgotten. #SPOTY https://t.co/U6hBqWvmZq
    Sun Dec 17 19:40:55 +0000 2017
    @BBC
    Bradley Lowery has been named the winner of the Helen Rollason Award at #SPOTY 2017 https://t.co/0wtAvD9R97
    Sun Dec 17 19:32:28 +0000 2017
    @BBC
    Tonight, @Lord_Sugar's final candidates go head to head. 
    #TheApprentice: The Final. Tonight at 9pm on @BBCOne.… https://t.co/GpWayrrVNG
    Sun Dec 17 19:30:06 +0000 2017
    @BBC
    'I just want to show people that I'm disabled, but I'm employable.' ❤️️
    
    #EmployableMe | Via @BBCTwo https://t.co/ULiqwTgXEB
    Sun Dec 17 19:00:02 +0000 2017
    @BBC
    Spending £100 a month on rent in London secures floor space equivalent to a small garden shed in parts of northern… https://t.co/QJUUYFgWhD
    Sun Dec 17 18:00:08 +0000 2017
    @BBC
    Tonight, @GaryLineker, @ClareBalding and @GabbyLogan present the 2017 BBC Sports Personality of the Year. 6:45pm on… https://t.co/MMZcLeQ0yc
    Sun Dec 17 17:44:03 +0000 2017
    @BBC
    RT @BBCSport: Strap yourselves in for The SPOTY Social – we’re LIVE from the red carpet with @TomDaley1994 and @YasminEvans at Sports Perso…
    Sun Dec 17 17:40:59 +0000 2017
    @BBC
    Spare a thought for the brothers whose rare disease means they'll never eat Christmas dinner. 🍗💔… https://t.co/aKVp7FQXRq
    Sun Dec 17 17:30:04 +0000 2017
    @BBC
    'If the oceans don't stay healthy, human beings are doomed.'
    
    #BluePlanet2 via @BBCEarth https://t.co/0GXEybNKgt
    Sun Dec 17 17:00:04 +0000 2017
    @BBC
    RT @BBCSport: It's #SPOTY weekend and what a start to Sunday night we have for you.
    
    @TomDaley1994 and @YasminEvans host The #SPOTY Social…
    Sun Dec 17 16:38:24 +0000 2017
    @BBC
    🎞 Star Wars: Fans shouldn't worry if The Last Jedi gets bad reviews. https://t.co/zMiJLLau4a https://t.co/k2DN8HMDzZ
    Sun Dec 17 16:00:06 +0000 2017
    @BBC
    Can good design make food taste better? 🥘😋 https://t.co/4xTQ8VaPZi https://t.co/YP2cqzyJJd
    Sun Dec 17 15:00:07 +0000 2017
    @BBC
    This grandmother is transforming villages by building dams to bring them much-needed water. 💦… https://t.co/MAwzbO5JUq
    Sun Dec 17 14:00:01 +0000 2017
    @BBC
    Congratulations and a #BigThankYou to Denise. 🎉 What an inspiration. #SPOTY https://t.co/xRHVhwEjFP
    Sun Dec 17 20:34:25 +0000 2017
    @BBC
    Follow the production of a contemporary performance of the nativity unlike any other. #Alternativity 9pm on @BBCTwo… https://t.co/RLZvnMA8yJ
    Sun Dec 17 20:31:03 +0000 2017
    @BBC
    RT @BBCSport: .@NoelGallagher singing the Beatles 
    
    Beautiful.
    
    Watch #SPOTY live: https://t.co/J5Un4g5oDM https://t.co/flkmCR2TWw
    Sun Dec 17 20:29:11 +0000 2017
    @BBC
    RT @BBCSport: The voting is open for #SPOTY.
    
    It's time to have your say ➡️ https://t.co/DQf1YQT4L0 https://t.co/WvQYr12Ds7
    Sun Dec 17 20:19:09 +0000 2017
    @BBC
    RT @BBCSport: It's time.
    
    We know the contenders and now you can vote for your favourite.
    
    Who do want to win #spoty? Vote here https://t.c…
    Sun Dec 17 20:15:19 +0000 2017
    @BBC
    Congratulations to Phil Foden, BBC Young Sports Personality 2017. 🏆 #SPOTY https://t.co/NKYPBDxSpi
    Sun Dec 17 20:00:41 +0000 2017
    @BBC
    🎬 How Frankenstein and his Creature conquered the movies. https://t.co/p1vJrJkn6c https://t.co/Twq4JEOOhj
    Sun Dec 17 20:00:06 +0000 2017
    @BBC
    He will never be forgotten. #SPOTY https://t.co/U6hBqWvmZq
    Sun Dec 17 19:40:55 +0000 2017
    @BBC
    Bradley Lowery has been named the winner of the Helen Rollason Award at #SPOTY 2017 https://t.co/0wtAvD9R97
    Sun Dec 17 19:32:28 +0000 2017
    @BBC
    Tonight, @Lord_Sugar's final candidates go head to head. 
    #TheApprentice: The Final. Tonight at 9pm on @BBCOne.… https://t.co/GpWayrrVNG
    Sun Dec 17 19:30:06 +0000 2017
    @BBC
    'I just want to show people that I'm disabled, but I'm employable.' ❤️️
    
    #EmployableMe | Via @BBCTwo https://t.co/ULiqwTgXEB
    Sun Dec 17 19:00:02 +0000 2017
    @BBC
    Spending £100 a month on rent in London secures floor space equivalent to a small garden shed in parts of northern… https://t.co/QJUUYFgWhD
    Sun Dec 17 18:00:08 +0000 2017
    @BBC
    Tonight, @GaryLineker, @ClareBalding and @GabbyLogan present the 2017 BBC Sports Personality of the Year. 6:45pm on… https://t.co/MMZcLeQ0yc
    Sun Dec 17 17:44:03 +0000 2017
    @BBC
    RT @BBCSport: Strap yourselves in for The SPOTY Social – we’re LIVE from the red carpet with @TomDaley1994 and @YasminEvans at Sports Perso…
    Sun Dec 17 17:40:59 +0000 2017
    @BBC
    Spare a thought for the brothers whose rare disease means they'll never eat Christmas dinner. 🍗💔… https://t.co/aKVp7FQXRq
    Sun Dec 17 17:30:04 +0000 2017
    @BBC
    'If the oceans don't stay healthy, human beings are doomed.'
    
    #BluePlanet2 via @BBCEarth https://t.co/0GXEybNKgt
    Sun Dec 17 17:00:04 +0000 2017
    @BBC
    RT @BBCSport: It's #SPOTY weekend and what a start to Sunday night we have for you.
    
    @TomDaley1994 and @YasminEvans host The #SPOTY Social…
    Sun Dec 17 16:38:24 +0000 2017
    @BBC
    🎞 Star Wars: Fans shouldn't worry if The Last Jedi gets bad reviews. https://t.co/zMiJLLau4a https://t.co/k2DN8HMDzZ
    Sun Dec 17 16:00:06 +0000 2017
    @BBC
    Can good design make food taste better? 🥘😋 https://t.co/4xTQ8VaPZi https://t.co/YP2cqzyJJd
    Sun Dec 17 15:00:07 +0000 2017
    @BBC
    This grandmother is transforming villages by building dams to bring them much-needed water. 💦… https://t.co/MAwzbO5JUq
    Sun Dec 17 14:00:01 +0000 2017
    @BBC
    🦅 North American Golden eagles' migration timing may be shifted out of step with a seasonal boom in food, according… https://t.co/AySNMGlHBK
    Sun Dec 17 13:00:07 +0000 2017
    @BBC
    A coming of age story loved by generations worldwide. ❤️ 
    
    A three-part dramatisation of Louisa May Alcott's… https://t.co/paOdLong8M
    Sun Dec 17 12:33:06 +0000 2017
    @BBC
    RT @bbcthree: The 96-year-old who organises parties to combat loneliness. https://t.co/Ym3vW0r4m5
    Sun Dec 17 12:12:06 +0000 2017
    @BBC
    Our brains are hard-wired to believe things are worse than they really are, researchers found. 
    
    @BBCWorldService e… https://t.co/ntMruWJYZm
    Sun Dec 17 12:00:09 +0000 2017
    @BBC
    'People either leave within a year, or leave in a wooden box.'
    
    It's a strange life on London's Eel Pie Island.… https://t.co/O225QKc5lo
    Sun Dec 17 11:30:08 +0000 2017
    @BBC
    How to make fantastic, crystal-frosted decorations to hang from your Christmas tree. 🎄❄️
    
    + a few extra tips on cre… https://t.co/n004bKOxu4
    Sun Dec 17 11:00:02 +0000 2017
    @BBC
    RT @BBCiPlayer: 😂 Get your #Sundaymorning LOLs right here https://t.co/pxLVRcNWmN https://t.co/u9HOhxhEVG
    Sun Dec 17 10:09:32 +0000 2017
    @BBC
    RT @BBCOne: Two finalists. Only one winner. Who will @Lord_Sugar choose? There’s only one way to find out. #TheApprentice. Tonight, 9pm. ht…
    Sun Dec 17 10:07:38 +0000 2017
    @BBC
    Did you know that the idea of tinsel dates back to 1610 in Nuremberg, Germany? 🎄 https://t.co/DNeXzvOR9G https://t.co/5HF8kE6Z9t
    Sun Dec 17 10:00:05 +0000 2017
    @BBC
    RT @BBCFood: If you make this meringue today, it will keep till Christmas! (If you can resist tempation for that long...) https://t.co/htw4…
    Sun Dec 17 09:51:41 +0000 2017
    @BBC
    RT @BBCTwo: Tonight at 9pm, Banksy teams up with Danny Boyle to stage a nativity play like no other... #TheAlternativity https://t.co/5UbtM…
    Sun Dec 17 09:51:37 +0000 2017
    @BBC
    RT @BBCSport: Bradley Lowery has been named the winner of the Helen Rollason Award at #SPOTY 2017 https://t.co/hgl1bgW4ud https://t.co/iqXs…
    Sun Dec 17 09:51:28 +0000 2017
    @BBC
    From Manchester's piano man to a 12-year-old girl in Cork: 7 buskers who deserved to go viral. 🎶 ✨… https://t.co/Jph8Fn3wL9
    Sun Dec 17 09:33:04 +0000 2017
    @BBC
    Would you have what it takes to sleep rough?
    Via @BBCScotland. https://t.co/iRYAvzcND9
    Sun Dec 17 09:00:02 +0000 2017
    @BBC
    Ever wondered which Star Wars character you would be? Take this quiz to find out! 🎬 💫 https://t.co/jKdOdCA8DI https://t.co/T7eR3wZIwF
    Sun Dec 17 08:33:03 +0000 2017
    @BBC
    Trouble getting to sleep? Waking in the middle of the night? 😴
    
    Here are 10 ways you can improve the quality of you… https://t.co/U4feE4wnhL
    Sun Dec 17 08:00:06 +0000 2017
    @BBC
    RT @BBCOne: The 100 are coming. Watch this space. #AllTogetherNow https://t.co/82RZVHCWFY
    Sat Dec 16 21:41:40 +0000 2017
    @BBC
    RT @bbcstrictly: A moment they'll never forget ✨ RT to send huge congratulations to your #Strictly 2017 winners @mrjoemcfadden and @Mrs_kat…
    Sat Dec 16 21:21:54 +0000 2017
    @BBC
    RT @bbcstrictly: They've done it! Say hello to your #Strictly 2017 champions, @mrjoemcfadden and @Mrs_katjones 🎉 #StrictlyFinal https://t.c…
    Sat Dec 16 20:58:05 +0000 2017
    @BBC
    📟🎶 The Machine Music Quiz: Were these machines really used to make music? https://t.co/J4gryKhGmx https://t.co/mi6WAmMxFs
    Sat Dec 16 20:30:11 +0000 2017
    @BBC
    RT @bbcstrictly: Super troopers. You can't help but smile when @mrjoemcfadden and @Mrs_katjones dance 👏 #StrictlyFinal https://t.co/mJfLIUs…
    Sat Dec 16 20:29:49 +0000 2017
    @BBC
    RT @bbcstrictly: Blackpool comes to Borehamwood 🚋 What a journey it's been for @MissGAtkinson and @AljazSkorjanec #StrictlyFinal https://t.…
    Sat Dec 16 20:18:53 +0000 2017
    @BBC
    RT @bbcstrictly: Leggie McGee is BACK and she's fiercer than ever💃 @thedebbiemcgee @pernicegiovann1 #StrictlyFinal https://t.co/POPGiZyj58
    Sat Dec 16 20:15:23 +0000 2017
    @BBC
    Tonight, @McInTweet is joined by @mermhart and @NiallOfficial! Michael McIntyre's Big Show. 9pm on @BBCOne. 🎉… https://t.co/uXhH65iAgz
    Sat Dec 16 20:04:07 +0000 2017
    @BBC
    RT @bbcstrictly: FAB-U-LOUS! @alexandramusic and @gorkamarquez1 should be very proud of that Jive 🙌 #StrictlyFinal https://t.co/vAi1nNeMS4
    Sat Dec 16 20:03:41 +0000 2017
    @BBC
    'If you blame hipsters for gentrification, you're letting the real culprits off the hook.' ~ @MrNishKumar… https://t.co/qCFKpqZpdg
    Sat Dec 16 20:00:04 +0000 2017
    @BBC
    In Georgian times, they were made out of animal guts and kept in water or milk. This is the history of the condom.… https://t.co/CjNgMyS1sw
    Sat Dec 16 19:33:02 +0000 2017
    @BBC
    RT @bbcstrictly: The Judges' scores are just for guidance. YOU choose the winner of #Strictly 2017! VOTE for free here 👉 https://t.co/NEoUx…
    Sat Dec 16 19:14:48 +0000 2017
    @BBC
    Two Hollywood legends. One bitter #Feud. 
    Feud: Bette and Joan. 9pm on @BBCTwo. 🎬 https://t.co/CmZTvTvdUk https://t.co/vItcfEXHRV
    Sat Dec 16 18:51:01 +0000 2017
    @BBC
    RT @bbcstrictly: What a feeling! Our fabulous #Strictly finalists are SO ready for tonight 🎉 @alexandramusic @gorkamarquez1 @thedebbiemcgee…
    Sat Dec 16 18:42:33 +0000 2017
    @BBC
    'Remember when all emojis were yellow and nobody cared?!' 🤔 😂 @DarrenHarriott #LiveAtTheApollo https://t.co/OA5uXwGAkx
    Sat Dec 16 18:28:01 +0000 2017
    @BBC
    In an attempt to make more organs available for transplant, ministers are proposing a system of 'presumed consent.'… https://t.co/ZLkDwy18qC
    Sat Dec 16 18:00:07 +0000 2017
    @BBC
    Errol survived prostate cancer. Now he’s dedicated to getting as many other men diagnosed as he can. ❤️️
    Via… https://t.co/WJSQGAOpwx
    Sat Dec 16 17:00:05 +0000 2017
    @BBC
    From @IggyPop to @LadyGaga, here are five celebrities who went nude for art. 🙈🖼 https://t.co/zdhTqBPL4Z https://t.co/gu1zNILXTI
    Sat Dec 16 16:00:06 +0000 2017
    @BBC
    A Greek designer has turned objects we use every day into purposely bad designs guaranteed to frustrate.… https://t.co/nxxsQeGncj
    Sat Dec 16 15:00:14 +0000 2017
    @BBC
    From parasitism to the Picts, Melvyn Bragg covered a huge range of subjects in 2017 for @BBCInOurTime. How much do… https://t.co/6n18CQm07n
    Sat Dec 16 14:30:06 +0000 2017
    @BBC
    It turns out that watching videos of stadiums implode is really, really satisfying. 🏟 https://t.co/5VnaJmFszH https://t.co/APvLQT4Tey
    Sat Dec 16 13:30:04 +0000 2017
    @BBC
    'Oh my gosh, Dad Vader?!' 🙊 Mark Hamill is the greatest secret-keeper in the galaxy. #TheGNShow Via @BBCOne https://t.co/Nx5XLT4luu
    Sat Dec 16 13:04:04 +0000 2017
    @BBC
    👓👠 'It's like shoes, for your face.' 😂
    
    #ScotSquad | Via @BBCScotland https://t.co/gAYLTXMX8p
    Sat Dec 16 12:30:06 +0000 2017
    @BBC
    📝🎭 Sitting on a hot drama script? You have until Monday 15 January 2018 to get it in to @BBCwritersroom. 
    More info… https://t.co/29KluumhO8
    Sat Dec 16 11:30:09 +0000 2017
    @BBC
    'It's like going right to the heart of the earth.' 🌋
    Ever wondered what it's like going 600m deep inside an active… https://t.co/HhIuSaWulR
    Sat Dec 16 11:00:05 +0000 2017
    @BBC
    RT @BBCArchive: 1980 was a simpler time for #StarWars sequels, a time when R2-D2 ran over Goldie, Carrie Fisher and Mark Hamill played with…
    Sat Dec 16 10:28:46 +0000 2017
    @BBC
    RT @bbcmusic: “Your slow hands...OOOH!” 😂
    @NiallOfficial joins @McInTweet‘s Big Show tomorrow night at 9pm on @BBCOne 🙌
    #NiallHoran https:/…
    Sat Dec 16 10:28:06 +0000 2017
    @BBC
    RT @BBCScotlandNews: Some of your beautiful pictures of Scotland this week 😍 🏴󠁧󠁢󠁳󠁣󠁴󠁿 https://t.co/XggeF3xTXG https://t.co/tpgXCWCUrD
    Sat Dec 16 10:27:06 +0000 2017
    @BBC
    RT @BBCScotlandNews: Life can be tough if you are a bin lorry worker in the winter  😂 (Put on those  🎧) https://t.co/kBM2RbxQ7M
    Sat Dec 16 10:25:16 +0000 2017
    @BBC
    RT @BBCFood: Top 🔟 festive brunches. From gingerbread pancakes to cinnamon buns and cracking kedgeree 👉 https://t.co/HKbW0sElHC https://t.c…
    Sat Dec 16 10:22:57 +0000 2017
    @BBC
    RT @BBCOne: It’s decision time. Which one of our fabulous four #Strictly finalists will lift the glitterball trophy? It’s all down to you!…
    Sat Dec 16 10:22:29 +0000 2017
    @BBC
    Some think that this mysterious Magritte painting is the beginning of modern art. It inspires a lot more questions… https://t.co/6JRp3IKMw3
    Sat Dec 16 10:00:05 +0000 2017
    @BBC
    Maradona or someone's gran? 😂
    Can you figure out who these celebrity statues are supposed to be?… https://t.co/O5dzezyk3O
    Sat Dec 16 09:30:05 +0000 2017
    @BBC
    'Santa &amp; his wee elves work their butt off all year round for you.' 🎁😂
    Via @BBCTheSocial. https://t.co/kVEOTtxNBV
    Sat Dec 16 09:00:04 +0000 2017
    @BBC
    Unseen for 1000 years: how one man unearthed an astonishing collection of ancient Viking plunder.… https://t.co/yPJTdciVmr
    Sat Dec 16 08:32:03 +0000 2017
    @BBC
    These protein-packed breakfasts will kick-start your metabolism, leave you fuller for longer &amp; keep those mid-morni… https://t.co/UtZGA7Mtmu
    Sat Dec 16 08:00:09 +0000 2017
    @BBC
    RT @BBCFOUR: Only @GeorgeMichael could pull off looking sultry in a hot pink shirt and lemon fingerless gloves. #TOTP https://t.co/UrB1zTm5…
    Fri Dec 15 23:14:58 +0000 2017
    @BBC
    RT @CBeebiesHQ: ❄️THE SNOW QUEEN HAS LEFT! 😯 
    
    But she'll be back... 😱
    
    If you missed the show today it's repeated tomorrow &amp; available on…
    Fri Dec 15 23:14:50 +0000 2017
    @BBC
    RT @bbcstrictly: There's been laughter, there have been tears and world record swivels! Thank you @ZoeTheBall for another unforgettable yea…
    Fri Dec 15 23:14:41 +0000 2017
    @BBC
    RT @BBCSpringwatch: The funniest wildlife photos of 2017 are here and you'll love them
    https://t.co/f3w2huVMVe https://t.co/9n4OYXTtx4
    Fri Dec 15 23:14:34 +0000 2017
    @BBC
    RT @bbceastenders: This Christmas things are set to explode in catastrophic style in Walford. 
    
    #EastEnders​ on @BBCOne​. https://t.co/enCn…
    Fri Dec 15 23:14:30 +0000 2017
    @BBC
    A clairvoyant cat? 🐈 Or a turtle in the know? 🐢
    Animals in Russia are predicting the outcome of @FIFAWorldCup 2018.… https://t.co/M2UEsc61PK
    Fri Dec 15 19:00:01 +0000 2017
    @BBC
    🎞 @KermodeMovie breaks down his top 10 favourite movie moustaches of all time. 👉 https://t.co/JdBuFyC1L8 https://t.co/tPvTZUfQUV
    Fri Dec 15 18:30:17 +0000 2017
    @BBC
    Fragrant, spiced and with a light golden crumb. 
    🍰🎄This is a good last-minute Christmas cake as it doesn’t need tim… https://t.co/MTTRvjAxKP
    Fri Dec 15 18:00:06 +0000 2017
    @BBC
    👶 'Now I know that can sound confusing, but think of a big Kev, but being wee.' 😂
    
    #ScotSquad | via @BBCScotland https://t.co/xgh0LZ1PIi
    Fri Dec 15 17:30:01 +0000 2017
    @BBC
    RT @BBCOne: Get ready for one winning weekend of @BBCOne shows!
    SATURDAY:
    @BBCStrictly final 💃 🕺
    SUNDAY:
    @BBCSPOTY 🏆
    @BBCApprentice final 👉…
    Fri Dec 15 17:03:51 +0000 2017
    @BBC
    Have we finally reached Peak Eyebrow? 🎄
    
    This could be the definitive eyebrow trend of 2017. https://t.co/dl4fF5SNFs https://t.co/0K3PDrMl6t
    Fri Dec 15 17:00:09 +0000 2017
    @BBC
    Heading to the office Christmas party like... #FridayFeeling 💃 https://t.co/PdaaJAmNMZ
    Fri Dec 15 16:45:06 +0000 2017
    @BBC
    Tonight, four modern confectioners recreate the Christmas treats of the past. The Sweet Makers at Christmas. 9pm on… https://t.co/YQrR888v2I
    Fri Dec 15 16:30:05 +0000 2017
    @BBC
    RT @BBCTwo: Two Hollywood superstars. One bitter #Feud. 🎥🌟🎬 https://t.co/tlPJrJxcIz
    Fri Dec 15 14:56:12 +0000 2017
    @BBC
    A brave village girl tries to rescue her friend before he is frozen forever. ❄️ 👑 Watch @CBeebiesHQ's The Snow Quee… https://t.co/lx4e0bCGp0
    Fri Dec 15 14:34:04 +0000 2017
    @BBC
    RT @bbcstrictly: 🚨 FINAL TRAINING ALERT PART 2🚨  Here's a glimpse at the Showdances from @MissGAtkinson &amp; @AljazSkorjanec and @mrjoemcfadde…
    Fri Dec 15 14:34:02 +0000 2017
    @BBC
    Colour. ✅ Light. ✅ Composition. ✅
    📸❄️ Here's how to make your Instagram snow snaps stand out from the crowd. 👉… https://t.co/qGdRsZlMc8
    Fri Dec 15 14:00:09 +0000 2017
    @BBC
    RT @BBCTwo: How will this series of #PeakyBlinders end? 
    
    Here’s @ollyofficial with a Sneaky Peak at the shocking final episode… 😱 https://…
    Fri Dec 15 13:32:45 +0000 2017
    @BBC
    Cat Deely takes @U2's The Edge &amp; Adam Clayton record shopping. 💿🎶
    
    #U2AtTheBBC | Tuesday 9pm | @BBCOne https://t.co/Qf8MLSpvWI
    Fri Dec 15 13:30:02 +0000 2017
    @BBC
    Prince Harry and Meghan Markle's wedding to be held on 19th May 2018, @KensingtonRoyal has announced. ❤️️ 💍… https://t.co/TtMezZ4u0N
    Fri Dec 15 13:17:03 +0000 2017
    @BBC
    Explore the Twelfth Doctor's TARDIS with this stunning 360º interactive tour. 👉 https://t.co/gCn75M80QQ
    #DoctorWho https://t.co/VT2K2TGwxc
    Fri Dec 15 13:00:07 +0000 2017
    @BBC
    RT @bbcpress: You just wouldn't let it lie! Vic &amp; Bob's Big Night Out returns on @BBCFour: https://t.co/4fWS8FgBee https://t.co/17IzTfpjyS
    Fri Dec 15 12:43:54 +0000 2017
    @BBC
    Clown hooves &amp; furry noses - their role as beast of burden for Father Christmas isn’t the only reason to love reind… https://t.co/jziqCYeXme
    Fri Dec 15 12:30:05 +0000 2017
    @BBC
    Snow, floods &amp; fire. 🌨☔️🔥
    Here's what the weather around the world has been doing. 👉 https://t.co/47YzZh6PyP https://t.co/OjIQszmbeQ
    Fri Dec 15 12:00:08 +0000 2017
    @BBC
    RT @BBCOne: A coming of age story loved by generations worldwide. ❤️ 
    Watch out for the three-part dramatisation of Louisa May Alcott's #Li…
    Fri Dec 15 11:44:00 +0000 2017
    @BBC
    RT @BBCSport: Congratulations Roger Federer 👏
    
    He has won the BBC Overseas Sports Personality of the Year for a record fourth time.
    
    👉 http…
    Fri Dec 15 10:03:30 +0000 2017
    @BBC
    RT @BBCR1: Nobody does it better than @Eminem 🙏
    
    Watch him perform Love The Way You Lie with @SkylarGrey for @AnnieMac 👉 https://t.co/dmILB…
    Fri Dec 15 09:58:24 +0000 2017
    @BBC
    RT @bbcmusic: "I think I threw a drumkit into the audience once.." 😆
    Prepare yourself for @U2 At The BBC 
    Coming to @BBCOne: Tuesday 19th D…
    Fri Dec 15 09:57:59 +0000 2017
    @BBC
    This Friday, you won't want to miss this priceless treasure when the I Love Lucy Christmas Special airs at 8/7c on… https://t.co/oyC9YDno00
    Sun Dec 17 17:48:58 +0000 2017
    @CBS
    Get ready for football! Stream NFL on CBS today with #CBSAllAccess. Try 1 week FREE (not available on mobile phones… https://t.co/cNMa11dmza
    Sun Dec 17 15:39:38 +0000 2017
    @CBS
    RT @HawaiiFive0CBS: Was it all a dream? Catch up on the #H50 Fall Finale: https://t.co/PDeOIaDGqu https://t.co/msEijhSSJH
    Sat Dec 16 18:29:05 +0000 2017
    @CBS
    In less than a week, Lucy and Ricky will return to your screens... in full color! Don't miss two back-to-back episo… https://t.co/rtmvB5Cj1D
    Sat Dec 16 12:00:07 +0000 2017
    @CBS
    Do you know all the nominees for Record Of The Year? Get familiar with this year's GRAMMY® Award nominees ahead of… https://t.co/lXDIu1STfq
    Fri Dec 15 20:23:58 +0000 2017
    @CBS
    'Elton John: I'm Still Standing - A GRAMMY® Salute' will celebrate Elton John's legendary career and timeless hits!… https://t.co/6M38jQQpTA
    Fri Dec 15 14:43:08 +0000 2017
    @CBS
    Get to know 2017 Kennedy Center honorees @LLCoolJ, Carmen de Lavallade (@CarmenDances), @GloriaEstefan,… https://t.co/RGe3zqmY08
    Thu Dec 14 19:13:25 +0000 2017
    @CBS
    So close, yet so far away. Which #Survivor Castaways Will Earn Their Spot In The Final Five? More:… https://t.co/efeBVa4p26
    Wed Dec 13 23:20:01 +0000 2017
    @CBS
    RT @BandB_CBS: Take a walk down #BoldandBeautiful memory lane! RT your favorite #Steam moment. https://t.co/kxeD2br8Tc
    Wed Dec 13 18:56:58 +0000 2017
    @CBS
    RT @thegoodfight: Court is back in session. Season 2 of #TheGoodFight premieres March 4, exclusively on CBS All Access: https://t.co/Niu5a8…
    Tue Dec 12 20:34:16 +0000 2017
    @CBS
    Only two weeks until The 40th Annual Kennedy Center Honors air on December 26! Look back on four decades of inspiri… https://t.co/z4J8sfs55V
    Tue Dec 12 19:04:59 +0000 2017
    @CBS
    Mark your calendars! The 53rd Academy Of Country Music Awards will air Sunday, April 15 on CBS!… https://t.co/yYPc5rCiMW
    Tue Dec 12 17:13:52 +0000 2017
    @CBS
    The search is on to find the pro football player with the best off-the-field talent! Vote for your favorite perform… https://t.co/musmVXrRJz
    Mon Dec 11 21:29:33 +0000 2017
    @CBS
    RT @MadamSecretary: No D.C. holiday party is complete without some political persuasion and a covert sting to bust a corrupt senator. 🎄⭐️ S…
    Mon Dec 11 19:05:21 +0000 2017
    @CBS
    Due to NFL overrun, CBS is delayed 8 mins in the following ET &amp; CT markets: Hunstville, AL, Bowling Green, KY, MS,… https://t.co/gbwhgooEQd
    Mon Dec 11 00:26:50 +0000 2017
    @CBS
    Due to NFL overrun CBS is delayed 7 mins in the following ET &amp; CT markets Tampa, Chicago, Maryland, Michigan, Wash… https://t.co/driVgCiX7D
    Mon Dec 11 00:25:54 +0000 2017
    @CBS
    RT @NoActivityCBS: If you want the intel, you get the tickles. 😂 Stream the first 5 episodes of #NoActivity now: https://t.co/Wzq9bVOhGN ht…
    Sun Dec 10 22:49:02 +0000 2017
    @CBS
    RT @startrekcbs: .@albinokid and @wcruz73 are breaking new ground in #StarTrekDiscovery. 🏳️‍🌈 Stream chapter 1 on CBS All Access: https://t…
    Sun Dec 10 22:48:46 +0000 2017
    @CBS
    Don’t miss America’s Game! Stream the Army-Navy game LIVE today at 3PM ET with a FREE trial of #CBSAllAccess:… https://t.co/38udnQj2vs
    Sat Dec 09 18:24:37 +0000 2017
    @CBS
    There's still time before we have to say so long! Catch up with Carol Burnett, her original castmates and special g… https://t.co/WTiK8dzaXO
    Sat Dec 09 01:11:51 +0000 2017
    @CBS
    This Friday, you won't want to miss this priceless treasure when the I Love Lucy Christmas Special airs at 8/7c on… https://t.co/oyC9YDno00
    Sun Dec 17 17:48:58 +0000 2017
    @CBS
    Get ready for football! Stream NFL on CBS today with #CBSAllAccess. Try 1 week FREE (not available on mobile phones… https://t.co/cNMa11dmza
    Sun Dec 17 15:39:38 +0000 2017
    @CBS
    RT @HawaiiFive0CBS: Was it all a dream? Catch up on the #H50 Fall Finale: https://t.co/PDeOIaDGqu https://t.co/msEijhSSJH
    Sat Dec 16 18:29:05 +0000 2017
    @CBS
    In less than a week, Lucy and Ricky will return to your screens... in full color! Don't miss two back-to-back episo… https://t.co/rtmvB5Cj1D
    Sat Dec 16 12:00:07 +0000 2017
    @CBS
    Do you know all the nominees for Record Of The Year? Get familiar with this year's GRAMMY® Award nominees ahead of… https://t.co/lXDIu1STfq
    Fri Dec 15 20:23:58 +0000 2017
    @CBS
    'Elton John: I'm Still Standing - A GRAMMY® Salute' will celebrate Elton John's legendary career and timeless hits!… https://t.co/6M38jQQpTA
    Fri Dec 15 14:43:08 +0000 2017
    @CBS
    Get to know 2017 Kennedy Center honorees @LLCoolJ, Carmen de Lavallade (@CarmenDances), @GloriaEstefan,… https://t.co/RGe3zqmY08
    Thu Dec 14 19:13:25 +0000 2017
    @CBS
    So close, yet so far away. Which #Survivor Castaways Will Earn Their Spot In The Final Five? More:… https://t.co/efeBVa4p26
    Wed Dec 13 23:20:01 +0000 2017
    @CBS
    RT @BandB_CBS: Take a walk down #BoldandBeautiful memory lane! RT your favorite #Steam moment. https://t.co/kxeD2br8Tc
    Wed Dec 13 18:56:58 +0000 2017
    @CBS
    RT @thegoodfight: Court is back in session. Season 2 of #TheGoodFight premieres March 4, exclusively on CBS All Access: https://t.co/Niu5a8…
    Tue Dec 12 20:34:16 +0000 2017
    @CBS
    Only two weeks until The 40th Annual Kennedy Center Honors air on December 26! Look back on four decades of inspiri… https://t.co/z4J8sfs55V
    Tue Dec 12 19:04:59 +0000 2017
    @CBS
    Mark your calendars! The 53rd Academy Of Country Music Awards will air Sunday, April 15 on CBS!… https://t.co/yYPc5rCiMW
    Tue Dec 12 17:13:52 +0000 2017
    @CBS
    The search is on to find the pro football player with the best off-the-field talent! Vote for your favorite perform… https://t.co/musmVXrRJz
    Mon Dec 11 21:29:33 +0000 2017
    @CBS
    RT @MadamSecretary: No D.C. holiday party is complete without some political persuasion and a covert sting to bust a corrupt senator. 🎄⭐️ S…
    Mon Dec 11 19:05:21 +0000 2017
    @CBS
    Due to NFL overrun, CBS is delayed 8 mins in the following ET &amp; CT markets: Hunstville, AL, Bowling Green, KY, MS,… https://t.co/gbwhgooEQd
    Mon Dec 11 00:26:50 +0000 2017
    @CBS
    Due to NFL overrun CBS is delayed 7 mins in the following ET &amp; CT markets Tampa, Chicago, Maryland, Michigan, Wash… https://t.co/driVgCiX7D
    Mon Dec 11 00:25:54 +0000 2017
    @CBS
    RT @NoActivityCBS: If you want the intel, you get the tickles. 😂 Stream the first 5 episodes of #NoActivity now: https://t.co/Wzq9bVOhGN ht…
    Sun Dec 10 22:49:02 +0000 2017
    @CBS
    RT @startrekcbs: .@albinokid and @wcruz73 are breaking new ground in #StarTrekDiscovery. 🏳️‍🌈 Stream chapter 1 on CBS All Access: https://t…
    Sun Dec 10 22:48:46 +0000 2017
    @CBS
    Don’t miss America’s Game! Stream the Army-Navy game LIVE today at 3PM ET with a FREE trial of #CBSAllAccess:… https://t.co/38udnQj2vs
    Sat Dec 09 18:24:37 +0000 2017
    @CBS
    There's still time before we have to say so long! Catch up with Carol Burnett, her original castmates and special g… https://t.co/WTiK8dzaXO
    Sat Dec 09 01:11:51 +0000 2017
    @CBS
    RT @bigbangtheory: It's the biggest best friend breakup of the year... 😱 Stream the latest full episode of #BigBangTheory: https://t.co/iIw…
    Fri Dec 08 23:35:41 +0000 2017
    @CBS
    RT @AmazingRaceCBS: Presenting... the 30th cast of the #AmazingRace! Made up of champions and winners, this is quite literally the most com…
    Thu Dec 07 18:23:03 +0000 2017
    @CBS
    Do you know all the nominees for Song Of The Year? Get familiar with this year's GRAMMY® Award nominees ahead of Mu… https://t.co/I6hhOtfQjb
    Thu Dec 07 12:07:06 +0000 2017
    @CBS
    A new Twilight Zone original series is coming exclusively to CBS All Access in association with @JordanPeele,… https://t.co/fVYnhUASee
    Wed Dec 06 17:32:28 +0000 2017
    @CBS
    RT @SuperiorDonuts: You'll want to check this box! ☑︎ Stream the latest episode of #SuperiorDonuts: https://t.co/h1xhKLCAPl https://t.co/d8…
    Tue Dec 05 19:21:31 +0000 2017
    @CBS
    RT @YoungSheldon: Wondering what it's like behind the scenes of #YoungSheldon? Let star @OfficialRaeganR take you on a tour of the set! htt…
    Tue Dec 05 19:14:00 +0000 2017
    @CBS
    The Kennedy Center Honors recognizes the lifetime contributions of all types of performance artists. Watch the 40th… https://t.co/azF3rW2ptw
    Tue Dec 05 00:54:16 +0000 2017
    @CBS
    RT @YoungSheldon: There's something @elonmusk never told you about @spacex's Falcon 9. 📓  #YoungSheldon https://t.co/bu3W0IC8zN
    Tue Dec 05 00:03:06 +0000 2017
    @CBS
    Just like old times, Carol Burnett bumps up the lights and answers questions from the audience. Catch up on The Car… https://t.co/9r7WI8d1tZ
    Mon Dec 04 20:52:31 +0000 2017
    @CBS
    Star comedian @JimCarrey gets emotional when he expresses his heartfelt thanks to Carol Burnett for her positive in… https://t.co/5QCejBcg5T
    Mon Dec 04 19:22:07 +0000 2017
    @CBS
    Take a trip down memory lane with Carol Burnett for a special tribute you'll never forget. Catch up on The Carol Bu… https://t.co/XBINDav614
    Mon Dec 04 07:14:06 +0000 2017
    @CBS
    RT @JLawlorNY: So, ok...maybe I'm crying at at the #CarolBurnett50 finale with everyone singing her theme song! #ImSoGladWeHadThisTimeToget…
    Mon Dec 04 03:02:00 +0000 2017
    @CBS
    RT @junerenee: A true classic and favorite!! Love #CarolBurnett50 laughed and cried...just like before!
    Mon Dec 04 03:01:09 +0000 2017
    @CBS
    RT if you’ve loved reliving these classic moments during #CarolBurnett50 https://t.co/I1tIWeSlsQ
    Mon Dec 04 02:51:35 +0000 2017
    @CBS
    RT @Mom101: I can't tell you the joy of seeing my 10yo laughing at this. Especially the Tim Conway dentist sketch.  #CarolBurnett50
    Mon Dec 04 02:49:27 +0000 2017
    @CBS
    RT @AdeleAndMike: Thank You for bringing back such wonderful memories, the entire family would gather to watch, and we would then laugh abo…
    Mon Dec 04 02:47:39 +0000 2017
    @CBS
    RT @tessab13: The Siamese Elephants skit on the Carol Burnett show is such a classic and possibly my favorite. Loved Tim Conway! #CarolBurn…
    Mon Dec 04 02:43:14 +0000 2017
    @CBS
    RT @inezpanebianco: @OfficialBPeters and Carol Burnett reminiscing back on the carol burnett show is my idea of a perfect night ❤️ #CarolBu…
    Mon Dec 04 02:26:30 +0000 2017
    @CBS
    What a performance by @OfficialBPeters, @KChenoweth, Carol Burnett, Steve Lawrence, and @StephenAtHome!… https://t.co/DqewQ6ASQp
    Mon Dec 04 02:22:42 +0000 2017
    @CBS
    RT @jonjeffryes: Bob Mackie created 65 costumes a week for The Carol Burnett Show #CarolBurnett50
    Mon Dec 04 02:12:59 +0000 2017
    @CBS
    RT @bmayberry92: Steve Carell with that video submission though! 😂 #carolburnett50
    Mon Dec 04 01:56:26 +0000 2017
    @CBS
    She’s still got it! #CarolBurnett50 https://t.co/zTxZc5zrqP
    Mon Dec 04 01:55:44 +0000 2017
    @CBS
    RT @BobMackie: Our friend Tim Conway never failed to make us laugh #CarolBurnett50
    Mon Dec 04 01:43:24 +0000 2017
    @CBS
    RT @bpeters99: #CarolBurnett50  Am I the Only one with tears in my eyes while I give a standing ovation from my couch? One of the most bril…
    Mon Dec 04 01:33:37 +0000 2017
    @CBS
    RT @SuperJen1117: This show is awesome...Some of the funniest women together on one stage 🙌🏼❤️ #CarolBurnett50
    Mon Dec 04 01:24:51 +0000 2017
    @CBS
    These two are just like sisters ❤️ #CarolBurnett50 https://t.co/EPpyf2kOuV
    Mon Dec 04 01:13:30 +0000 2017
    @CBS
    RT @chattie: Watching #carolburnett50  can’t quit smiling. Brings me memories of watching on Saturday nights with my mom and grandma.
    Mon Dec 04 01:11:57 +0000 2017
    @CBS
    RT @DanRocks98: Settling in for the #CarolBurnett50 special. This lady is comedy gold! A true staple of my childhood.
    Mon Dec 04 01:05:31 +0000 2017
    @CBS
    She’s back! Tune in now to see The Carol Burnett 50th Anniversary Special on CBS and CBS All Access. #CarolBurnett50 https://t.co/HhvRmT5AR0
    Mon Dec 04 01:00:09 +0000 2017
    @CBS
    Due to #NFL football overrun #CBS is delayed 11 min in: 
    Atlanta 
    Baltimore 
    Columbus
    Cleveland 
    Toledo
    Detroit
    Fli… https://t.co/oCkn11yJOR
    Mon Dec 04 00:25:16 +0000 2017
    @CBS
    Relive the laughter and the magic in this star-studded tribute to everyone's favorite classic comedy show. Don't mi… https://t.co/WV6jxBnRAt
    Sun Dec 03 20:00:02 +0000 2017
    @CBS
    Tonight, spend an evening together with Carol Burnett and celebrity friends as they celebrate The Carol Burnett 50t… https://t.co/uH2uM9cJFS
    Sun Dec 03 18:44:14 +0000 2017
    @CBS
    Carol Burnett credits the close-knit cast for the success of her show. Join her and original cast members Vicki Law… https://t.co/1rlNPUS5EJ
    Sun Dec 03 17:32:01 +0000 2017
    @CBS
    Carol Burnett and friends reflect on how the show became an instant classic that's still celebrated today! Join the… https://t.co/lZgVz9XSyM
    Sun Dec 03 13:00:04 +0000 2017
    @CBS
    Tonight, celebrate with Carol Burnett, Vicki Lawrence, Lyle Waggoner &amp; more special guests! Find out how to watch T… https://t.co/Rhm6RJ34u2
    Sun Dec 03 12:00:01 +0000 2017
    @CBS
    Stream Indiana at Michigan LIVE today at 12:30PM ET with a 1-month FREE trial of #CBSAllAccess. Just use promo code… https://t.co/xRem3zSyEQ
    Sat Dec 02 15:55:39 +0000 2017
    @CBS
    Kristin Chenoweth (@KChenoweth) explains why audiences still crave Carol Burnett! Don't miss The Carol Burnett 50th… https://t.co/kM92NTtTfs
    Sat Dec 02 14:30:03 +0000 2017
    @CBS
    Catch up on this amazing lineup of music specials! Here's how to watch Bruno Mars: 24K Magic Live at the Apollo, Th… https://t.co/Jit2CzZJCY
    Sat Dec 02 13:00:07 +0000 2017
    @CBS
    Missed Bruno Mars: 24K Magic Live at the Apollo? Keep up! Watch the full show: https://t.co/itXpGB5gRm #BrunoMars https://t.co/8yyQlC1LML
    Sat Dec 02 12:00:03 +0000 2017
    @CBS
    Reminisce with these classic photos and get ready to relive the magic when The Carol Burnett 50th Anniversary Speci… https://t.co/yJQEzCjoSA
    Fri Dec 01 22:43:05 +0000 2017
    @CBS
    RT @LivinBiblically: In the beginning, there was Chip. And lo! Chip had a revelation. #LivingBiblically is a new comedy premiering Monday,…
    Fri Dec 01 22:15:28 +0000 2017
    @CBS
    Discover these pro football stars' off-the-field talents in MVP: Most Valuable Performer, airing Jan 25 on CBS! Fin… https://t.co/g8jSRW8mQf
    Fri Dec 01 21:00:12 +0000 2017
    @CBS
    Find out when #BigBrother celebrity edition, #AmazingRace, #Survivor, new drama @instinctcbs and new comedy… https://t.co/4Psl74zcCB
    Fri Dec 01 20:17:18 +0000 2017
    @CBS
    Actress @BethBehrs explains why Carol Burnett is her hero! Celebrate her lasting influence with The Carol Burnett 5… https://t.co/Lnt5P9jEu0
    Fri Dec 01 19:32:18 +0000 2017
    @CBS
    RT @instinctcbs: New drama #Instinct, starring @Alancumming, premieres Sunday, March 11 on @CBS! https://t.co/aaL0JXpqav
    Fri Dec 01 18:40:34 +0000 2017
    @CBS
    RT @AmazingRaceCBS: On your marks... #AmazingRace returns Wednesday, January 3! https://t.co/XMSJSUymUZ
    Fri Dec 01 18:16:37 +0000 2017
    @CBS
    RT @CBSBigBrother: Mark. Your. Calendars. The celebrity edition of #BigBrother premieres February 7! https://t.co/nP3Do6jTwM
    Fri Dec 01 18:10:11 +0000 2017
    @CBS
    The Angels await you... catch up on the world's most celebrated fashion show now! Watch the full 2017… https://t.co/xfYDbEzpfX
    Fri Dec 01 14:00:04 +0000 2017
    @CBS
    Comedy stars Amy Poehler, Bill Hader, @MayaRudolph &amp; @TraceeEllisRoss give the legendary Tarzan yell a try- but no… https://t.co/lrrHE2f9Nv
    Fri Dec 01 12:00:03 +0000 2017
    @CBS
    Action-adventure series 'Blood &amp; Treasure' has been picked up for broadcast in Summer 2019: https://t.co/gAjqbF5bYh https://t.co/3cTBH9AKFI
    Fri Dec 01 01:31:30 +0000 2017
    @CBS
    Carol Burnett visited @TheTalkCBS to discuss how she got her start in show business! Watch The Carol Burnett 50th A… https://t.co/EyqmFWZHEC
    Thu Nov 30 21:10:19 +0000 2017
    @CBS
    The world's most beloved fairy tales are reimagined as a dark &amp; twisted psychological thriller in "Tell Me A Story,… https://t.co/CytIswrRj1
    Thu Nov 30 20:54:39 +0000 2017
    @CBS
    RT @RansomCBS: #Ransom star @luke_j_roberts on set in Budapest for Season 2! https://t.co/rgC5ylqSMp
    Thu Nov 30 17:40:02 +0000 2017
    @CBS
    Comic @JayLeno reflects on the major impression Carol Burnett left on him. Celebrate The Carol Burnett 50th Anniver… https://t.co/PIakndHJt1
    Thu Nov 30 17:30:05 +0000 2017
    @CBS
    Watch #BrunoMars perform "That's What I Like" in Bruno Mars: 24K Magic Live at the Apollo: https://t.co/hAFcB9HpE3 https://t.co/I7ZWHdDYCP
    Thu Nov 30 15:00:05 +0000 2017
    @CBS
    Watch #BrunoMars perform "24K Magic" in Bruno Mars: 24K Magic Live at the Apollo: https://t.co/UgD4fC5cS6 https://t.co/iTGKJSbjwY
    Thu Nov 30 12:00:03 +0000 2017
    @CBS
    Missed Bruno Mars: 24K Magic Live at the Apollo Theater? Keep up! Watch the full show: https://t.co/itXpGB5gRm… https://t.co/nkRMIUd2Df
    Thu Nov 30 07:52:09 +0000 2017
    @CBS
    RT @CWatkinsTV: That. Was. Amazing! #BrunoMars
    Thu Nov 30 04:09:55 +0000 2017
    @CBS
    The stage is 🔥🔥 #BrunoMars https://t.co/nykrDH46Bs
    Thu Nov 30 04:00:27 +0000 2017
    @CBS
    RT @anitakearney65: I could watch this all night #Brunomars #BrunosTvSpecial so much fun to watch OMG
    Thu Nov 30 03:59:09 +0000 2017
    @CBS
    Everybody put your hands up! #BrunoMars https://t.co/jU7NyttAqv
    Thu Nov 30 03:55:37 +0000 2017
    @CBS
    RT @Sara_nurse: My 2yr old niece heard @BrunoMars and is now up singing and dancing #BrunosTVSpecial #BrunoMars
    Thu Nov 30 03:51:38 +0000 2017
    @CBS
    RT @AllieNY86: His voice is mesmerizing 
    #BrunoMars
    Thu Nov 30 03:44:54 +0000 2017
    @CBS
    RT @BrunoMars: We love you MARY!!!! ❤️ #BrunosTvSpecial
    Thu Nov 30 03:37:13 +0000 2017
    @CBS
    RT @RDMichelleLNK: Loving a dose of #BrunoMars midweek. So amazing!
    Thu Nov 30 03:35:13 +0000 2017
    @CBS
    We’re only halfway into the show. Get ready for more of your favorite #BrunoMars tunes! https://t.co/BJh0PeX864
    Thu Nov 30 03:33:32 +0000 2017
    @CBS
    When #BrunoMars tells you to pick up the phone, that’s exactly what you do. https://t.co/JZDS26h3lL
    Thu Nov 30 03:23:03 +0000 2017
    @CBS
    RT @MargoSlade: Best way to relax after a hard day of work watching #BrunoMars on #BrunosTVSpecial my heart is the happiest
    Thu Nov 30 03:11:31 +0000 2017
    @CBS
    RT @Tiffany48184: Now that's how you open up a show!!!!! #BrunoMars
    Thu Nov 30 03:09:54 +0000 2017
    @CBS
    RT if you’re ready to party with #BrunoMars!! https://t.co/o4qQoKOzgH
    Thu Nov 30 03:07:20 +0000 2017
    @CBS
    RT @BrunoMars: POP POP!!💥💥 everyone tweet #BrunosTvSpecial! We on!!!! 🍾
    Thu Nov 30 03:06:38 +0000 2017
    @CBS
    RT @Queentassia14: Bruno Mars Live at the Apollo!!!! Yeah I have to wake up at like 4 am for work.... but it's worth it. #BrunoMars #Brunos…
    Thu Nov 30 03:03:15 +0000 2017
    @CBS
    RT @asbstar30: BRUNO #BrunoMars
    Thu Nov 30 03:02:34 +0000 2017
    @CBS
    Get on your feet, and prepare to dance. #BrunoMars is hitting the stage! https://t.co/yOyq8JlMZj
    Thu Nov 30 02:59:59 +0000 2017
    @CBS
    Pop pop, it's showtime! Bruno Mars: 24K Magic Live at the Apollo starts at 10/9c on CBS, or try 1 month FREE of CBS… https://t.co/cpCSYDKieM
    Thu Nov 30 02:45:03 +0000 2017
    @CBS
    Calling all Bruno Mars' lovelies... don't miss Bruno Mars: 24K Magic Live at the Apollo tonight @ 10/9c on CBS &amp; CB… https://t.co/nGOgukLMx9
    Thu Nov 30 00:06:05 +0000 2017
    @CBS
    You'll treasure this special night with #BrunoMars! Find out how to watch Bruno Mars: 24K Magic Live at the Apollo… https://t.co/qF2eRcJLSJ
    Wed Nov 29 23:20:13 +0000 2017
    @CBS
    RT @BrunoMars: Ladies put your hoops on tonight! Fellas break out that good cologne! #BrunosTvSpecial is airing on @CBS! What y’all trynna…
    Wed Nov 29 23:15:24 +0000 2017
    @CBS
    RT @YoungSheldon: Sheldon will do whatever it takes to get his hands on his own computer in tomorrow's all-new episode of #YoungSheldon! ht…
    Wed Nov 29 23:14:57 +0000 2017
    @CBS
    RT @survivorcbs: What drama will ensue on back-to-back episodes of #Survivor tonight? Watch a sneak peek now: https://t.co/LHcxyClSw1 https…
    Wed Nov 29 23:13:40 +0000 2017
    @CBS
    Power outage cripples Atlanta's Hartsfield-Jackson airport https://t.co/Mu2V4Ef0VC https://t.co/11IS2CxwPw
    Sun Dec 17 20:30:03 +0000 2017
    @CNN
    Environmental Protection Agency cuts could risk a public health emergency https://t.co/jXfk42LrP8 https://t.co/wLPi6wEudY
    Sun Dec 17 20:15:08 +0000 2017
    @CNN
    Hundreds have come down with a stomach illness during a Royal Caribbean cruise https://t.co/2QrExbXepY https://t.co/oX168QMPhz
    Sun Dec 17 20:00:25 +0000 2017
    @CNN
    This is how Australia's prime minister went swimming 50 years ago and vanished forever https://t.co/1jTVZN7pxR https://t.co/fJ0XzIv9fp
    Sun Dec 17 19:45:07 +0000 2017
    @CNN
    Lawyers representing the Trump presidential transition have accused special counsel Robert Mueller of 'unlawfully'… https://t.co/3LLmBKgfgT
    Sun Dec 17 19:30:21 +0000 2017
    @CNN
    Ohio Gov. John Kasich, a Republican, says the GOP is "losing the future" by "turning off millennials"… https://t.co/7WFkeq2pS1
    Sun Dec 17 19:15:08 +0000 2017
    @CNN
    The Pentagon has researched the possible existence of UFOs in a once completely classified project that began becau… https://t.co/ZXFJpotwiH
    Sun Dec 17 19:00:19 +0000 2017
    @CNN
    Southern Californnia resident says her neighborhood looks like "a war zone" because of the Thomas Fire, the third-l… https://t.co/EIpQQfBL10
    Sun Dec 17 18:45:04 +0000 2017
    @CNN
    Don't blink — or you'll miss another market milestone. The Dow could top 25,000 any day now. https://t.co/IirtH9usNz https://t.co/wW2YlZTLOz
    Sun Dec 17 18:30:05 +0000 2017
    @CNN
    A landslide in Chile has left 5 dead and 15 missing https://t.co/kuiebZHCJa https://t.co/MGvDcegxkM
    Sun Dec 17 18:15:13 +0000 2017
    @CNN
    "Star Wars: The Last Jedi" had a monster box office opening https://t.co/cMVRZpYUa0 https://t.co/WmlhY3x0WA
    Sun Dec 17 18:00:22 +0000 2017
    @CNN
    Here's what's in the tax bill for homeowners:
    ■ Downsized mortgage interest deduction
    ■ Less reason to itemize
    ■ Li… https://t.co/M66IVaJMkP
    Sun Dec 17 17:45:04 +0000 2017
    @CNN
    Their missions vary greatly: To provide loving homes for orphaned children, feed those in crisis or mend war's psyc… https://t.co/W1XsbAJDGW
    Sun Dec 17 17:30:31 +0000 2017
    @CNN
    "Do I need a British accent?" former President Barack Obama jokes before Prince Harry interviews him for a radio sh… https://t.co/rzrdHHlhmw
    Sun Dec 17 17:22:18 +0000 2017
    @CNN
    Alabama Senator-elect Doug Jones says it's time to move on from the special election, even though Roy Moore won't c… https://t.co/f8FhRyXZeo
    Sun Dec 17 17:00:47 +0000 2017
    @CNN
    UK Prime Minister Theresa May 'will not be derailed' on Brexit https://t.co/7JL1uYtLps https://t.co/wnxnGUW2Kt
    Sun Dec 17 16:45:10 +0000 2017
    @CNN
    Treasury Secretary Steven Mnuchin says he has no reason to think President Trump will fire special counsel Robert M… https://t.co/IiekN4b6P7
    Sun Dec 17 16:30:45 +0000 2017
    @CNN
    Children's health should be more important than tax cuts, writes Dean Obeidallah for @CNNOpinion… https://t.co/PzfT1VwAWI
    Sun Dec 17 16:18:20 +0000 2017
    @CNN
    Bernie Sanders has joined the list of lawmakers calling on President Trump to resign, citing the multiple allegatio… https://t.co/HtlsGzjfnW
    Sun Dec 17 16:00:16 +0000 2017
    @CNN
    A baby born with her heart outside her body has survived three surgeries to insert it back into her chest… https://t.co/MrHTAABsAh
    Sun Dec 17 15:45:12 +0000 2017
    @CNN
    Power outage cripples Atlanta's Hartsfield-Jackson airport https://t.co/Mu2V4Ef0VC https://t.co/11IS2CxwPw
    Sun Dec 17 20:30:03 +0000 2017
    @CNN
    Environmental Protection Agency cuts could risk a public health emergency https://t.co/jXfk42LrP8 https://t.co/wLPi6wEudY
    Sun Dec 17 20:15:08 +0000 2017
    @CNN
    Hundreds have come down with a stomach illness during a Royal Caribbean cruise https://t.co/2QrExbXepY https://t.co/oX168QMPhz
    Sun Dec 17 20:00:25 +0000 2017
    @CNN
    This is how Australia's prime minister went swimming 50 years ago and vanished forever https://t.co/1jTVZN7pxR https://t.co/fJ0XzIv9fp
    Sun Dec 17 19:45:07 +0000 2017
    @CNN
    Lawyers representing the Trump presidential transition have accused special counsel Robert Mueller of 'unlawfully'… https://t.co/3LLmBKgfgT
    Sun Dec 17 19:30:21 +0000 2017
    @CNN
    Ohio Gov. John Kasich, a Republican, says the GOP is "losing the future" by "turning off millennials"… https://t.co/7WFkeq2pS1
    Sun Dec 17 19:15:08 +0000 2017
    @CNN
    The Pentagon has researched the possible existence of UFOs in a once completely classified project that began becau… https://t.co/ZXFJpotwiH
    Sun Dec 17 19:00:19 +0000 2017
    @CNN
    Southern Californnia resident says her neighborhood looks like "a war zone" because of the Thomas Fire, the third-l… https://t.co/EIpQQfBL10
    Sun Dec 17 18:45:04 +0000 2017
    @CNN
    Don't blink — or you'll miss another market milestone. The Dow could top 25,000 any day now. https://t.co/IirtH9usNz https://t.co/wW2YlZTLOz
    Sun Dec 17 18:30:05 +0000 2017
    @CNN
    A landslide in Chile has left 5 dead and 15 missing https://t.co/kuiebZHCJa https://t.co/MGvDcegxkM
    Sun Dec 17 18:15:13 +0000 2017
    @CNN
    "Star Wars: The Last Jedi" had a monster box office opening https://t.co/cMVRZpYUa0 https://t.co/WmlhY3x0WA
    Sun Dec 17 18:00:22 +0000 2017
    @CNN
    Here's what's in the tax bill for homeowners:
    ■ Downsized mortgage interest deduction
    ■ Less reason to itemize
    ■ Li… https://t.co/M66IVaJMkP
    Sun Dec 17 17:45:04 +0000 2017
    @CNN
    Their missions vary greatly: To provide loving homes for orphaned children, feed those in crisis or mend war's psyc… https://t.co/W1XsbAJDGW
    Sun Dec 17 17:30:31 +0000 2017
    @CNN
    "Do I need a British accent?" former President Barack Obama jokes before Prince Harry interviews him for a radio sh… https://t.co/rzrdHHlhmw
    Sun Dec 17 17:22:18 +0000 2017
    @CNN
    Alabama Senator-elect Doug Jones says it's time to move on from the special election, even though Roy Moore won't c… https://t.co/f8FhRyXZeo
    Sun Dec 17 17:00:47 +0000 2017
    @CNN
    UK Prime Minister Theresa May 'will not be derailed' on Brexit https://t.co/7JL1uYtLps https://t.co/wnxnGUW2Kt
    Sun Dec 17 16:45:10 +0000 2017
    @CNN
    Treasury Secretary Steven Mnuchin says he has no reason to think President Trump will fire special counsel Robert M… https://t.co/IiekN4b6P7
    Sun Dec 17 16:30:45 +0000 2017
    @CNN
    Children's health should be more important than tax cuts, writes Dean Obeidallah for @CNNOpinion… https://t.co/PzfT1VwAWI
    Sun Dec 17 16:18:20 +0000 2017
    @CNN
    Bernie Sanders has joined the list of lawmakers calling on President Trump to resign, citing the multiple allegatio… https://t.co/HtlsGzjfnW
    Sun Dec 17 16:00:16 +0000 2017
    @CNN
    A baby born with her heart outside her body has survived three surgeries to insert it back into her chest… https://t.co/MrHTAABsAh
    Sun Dec 17 15:45:12 +0000 2017
    @CNN
    Take a look back at the photos that shaped 2017 https://t.co/FxlEcWRHyZ https://t.co/iE2e4HCytW
    Sun Dec 17 15:30:32 +0000 2017
    @CNN
    Rep. Himes: The President is attacking the FBI; “You have to ask yourself, ‘Why?’” If you're convinced you're innoc… https://t.co/t24I443NcJ
    Sun Dec 17 15:15:29 +0000 2017
    @CNN
    For the first time, eight planets have been found orbiting a distant star, Kepler-90, 2,545 light-years from Earth,… https://t.co/IP3AsLYMco
    Sun Dec 17 15:00:30 +0000 2017
    @CNN
    Sen.-elect Doug Jones of Alabama doesn’t join the several Senate Democrats calling for President Trump to step down… https://t.co/ISuV4fOE4Z
    Sun Dec 17 14:53:00 +0000 2017
    @CNN
    Alabama Sen.-elect Doug Jones: "I'm gonna commit to having a Senate office that reflects the diversity of Alabama.… https://t.co/kwvVAgUrPr
    Sun Dec 17 14:47:00 +0000 2017
    @CNN
    Prince Harry and Meghan Markle will marry on May 19, 2018, Kensington Palace says https://t.co/jVRSRqwYf6 https://t.co/Cu0RUjhsNq
    Sun Dec 17 14:45:10 +0000 2017
    @CNN
    Alabama Sen.-elect Doug Jones on if he considers voting with Republicans on certain issues: “Of course I do”… https://t.co/d5sRr3wJkj
    Sun Dec 17 14:36:00 +0000 2017
    @CNN
    The photos that shaped 2017 https://t.co/0gA9dMQ0VS https://t.co/zPpBl2aZy0
    Sun Dec 17 14:30:20 +0000 2017
    @CNN
    "The war on Christmas is over...it will soon be replaced by the war with North Korea": Saturday Night Live had a sp… https://t.co/kYFbB6vjO9
    Sun Dec 17 14:30:06 +0000 2017
    @CNN
    Alabama Sen.-elect Doug Jones has a message for Roy Moore: "It's time to move on. Alabama has spoken." #CNNSOTU https://t.co/4VLqvsAcFg
    Sun Dec 17 14:20:21 +0000 2017
    @CNN
    Alabama Sen.-elect Doug Jones says the "Mueller investigation is gonna shake down the way it's gonna shake down"… https://t.co/cILeYK7ALg
    Sun Dec 17 14:19:36 +0000 2017
    @CNN
    Treasury Secretary Steve Mnuchin responds to a report that the CDC was given a list of banned words and says that t… https://t.co/zLawSK8Wmr
    Sun Dec 17 14:16:14 +0000 2017
    @CNN
    Climate change in the Northern Arctic is happening so quickly it's forcing NOAA and others to rewrite a data-correc… https://t.co/byM6Hxd4S5
    Sun Dec 17 14:15:07 +0000 2017
    @CNN
    Treasury Secretary Steve Mnuchin on the GOP tax plan: “This is the biggest single change to the tax system in fixin… https://t.co/f8FIBHuklc
    Sun Dec 17 14:08:10 +0000 2017
    @CNN
    Donald Trump won 81% of the vote in this small Kentucky town. But residents aren't waiting on Washington to fix thi… https://t.co/anf0Tgsrid
    Sun Dec 17 14:00:16 +0000 2017
    @CNN
    The vote to roll back #netneutrality rules was slammed by tech giants like Amazon, Facebook and Netflix.
    
    It was ap… https://t.co/MlBOYNJIEA
    Sun Dec 17 13:45:04 +0000 2017
    @CNN
    'The Simpsons' predicted Disney would buy Fox in an episode that aired way back in 1998 https://t.co/wm0VhNdG4E https://t.co/NEaQAwQaMK
    Sun Dec 17 13:30:24 +0000 2017
    @CNN
    Their missions vary greatly: To provide loving homes for orphaned children, feed those in crisis or mend war's psyc… https://t.co/3yhQP4nwcX
    Sun Dec 17 13:15:03 +0000 2017
    @CNN
    Two paintings by Renaissance artist Raphael have been discovered at the Vatican - after being hidden for 500 years https://t.co/0Q5WAB18oX
    Sun Dec 17 13:02:11 +0000 2017
    @CNN
    For the first time, eight planets have been found orbiting a distant star, Kepler-90, 2,545 light-years from Earth,… https://t.co/oI8pyj8IWb
    Sun Dec 17 12:00:16 +0000 2017
    @CNN
    A mother's questions about her son's death leads to a yearlong investigation, revealing serious questions about the… https://t.co/rgl636u6iQ
    Sun Dec 17 11:30:13 +0000 2017
    @CNN
    Take a look back at the photos that shaped 2017 https://t.co/cFC16FkVIg https://t.co/fddQtcB7sI
    Sun Dec 17 11:00:39 +0000 2017
    @CNN
    "I was a healthy 33-year-old, and I'm not going to be a healthy 34-year-old." Ady Barkan, who is battling ALS and c… https://t.co/sxkGLooegP
    Sun Dec 17 10:30:43 +0000 2017
    @CNN
    The political upsets we've seen this year in New Jersey, Virginia and Alabama represent not so much a blue wave as… https://t.co/rD3mvvhJ7V
    Sun Dec 17 10:00:07 +0000 2017
    @CNN
    The vote to roll back #netneutrality rules was slammed by tech giants like Amazon, Facebook and Netflix.
    
    It was ap… https://t.co/15k5EiOhg6
    Sun Dec 17 09:30:12 +0000 2017
    @CNN
    A suicide bomber attacked a church packed with worshipers Sunday in Pakistan, killing 7 people and injuring more th… https://t.co/vPzsVBiI5V
    Sun Dec 17 09:18:08 +0000 2017
    @CNN
    Lisa McNair's sister was killed in the '63 Alabama Baptist Church bombing. Years later, then a US attorney, Doug Jo… https://t.co/zoYFVZy1Qw
    Sun Dec 17 09:01:27 +0000 2017
    @CNN
    Two paintings by Renaissance artist Raphael have been discovered at the Vatican — after being hidden for 500 years… https://t.co/mcaf4lmrpQ
    Sun Dec 17 08:31:42 +0000 2017
    @CNN
    This 500-year-old mystery at the Vatican has finally been solved https://t.co/ObyOTrzUPe https://t.co/uWRgu4N7ZX
    Sun Dec 17 08:00:46 +0000 2017
    @CNN
    A baby born with her heart outside her body has survived three surgeries to insert it back into her chest… https://t.co/t6CXrDVSAR
    Sun Dec 17 07:00:21 +0000 2017
    @CNN
    For the first time, eight planets have been found orbiting a distant star, Kepler-90, 2,545 light-years from Earth,… https://t.co/aTUCnQTFTO
    Sun Dec 17 06:30:09 +0000 2017
    @CNN
    An American diplomat who resigned in disgust last week says she believes the Trump administration is putting Americ… https://t.co/1Dq2ARsv45
    Sun Dec 17 06:00:14 +0000 2017
    @CNN
    Sen. Bernie Sanders has joined the list of lawmakers calling on President Trump to resign, citing the multiple alle… https://t.co/3MIyfb5x8N
    Sun Dec 17 05:30:06 +0000 2017
    @CNN
    These 16 states are running out of funding for CHIP — the Children's Health Insurance Program… https://t.co/WPgDVDGZpQ
    Sun Dec 17 05:00:15 +0000 2017
    @CNN
    'The Simpsons' predicted Disney would buy Fox in an episode that aired way back in 1998 https://t.co/bDaqptIuEM https://t.co/8rPHk2rmJd
    Sun Dec 17 04:30:13 +0000 2017
    @CNN
    For the first time, eight planets have been found orbiting a distant star, Kepler-90, 2,545 light-years from Earth,… https://t.co/tVDa4TuMCf
    Sun Dec 17 04:00:05 +0000 2017
    @CNN
    The vote to roll back #netneutrality rules was slammed by tech giants like Amazon, Facebook and Netflix.
    
    It was ap… https://t.co/az2SFVStfV
    Sun Dec 17 03:30:07 +0000 2017
    @CNN
    People can lie. But the case files may provide clues that will lead to the truth about this teen who was killed by… https://t.co/0z5dikCXjS
    Sun Dec 17 03:00:16 +0000 2017
    @CNN
    President Donald Trump’s private lawyers are slated to meet with special counsel Robert Mueller as soon as next wee… https://t.co/QFcEWWZtoX
    Sun Dec 17 02:45:07 +0000 2017
    @CNN
    A White House senior adviser at the Department of Homeland Security has previously:
    - Promoted birtherism
    - Said Ob… https://t.co/DgqYxZzHb3
    Sun Dec 17 02:30:12 +0000 2017
    @CNN
    This Juilliard musician spends weekend afternoons playing the New York subway. Here's why. https://t.co/kKV62kWP75 https://t.co/QO8z2rrXZ4
    Sun Dec 17 02:01:07 +0000 2017
    @CNN
    An Ohio driver accused of plowing into a crowd protesting a white nationalist rally this summer in Charlottesville,… https://t.co/ewckcxoUep
    Sun Dec 17 01:30:06 +0000 2017
    @CNN
    US Sen. Lindsey Graham said in an interview that he believes there's a 30% chance President Trump will order a firs… https://t.co/7Kd6P4FyTr
    Sun Dec 17 01:00:17 +0000 2017
    @CNN
    Shocking postmortem incisions on her son's body after he was fatally shot by police led this Chicago mom to ask CNN… https://t.co/MkYiifzOUm
    Sun Dec 17 00:30:10 +0000 2017
    @CNN
    Take a look back at the photos that shaped 2017 https://t.co/oPJTHZSN6P https://t.co/TcIPPHyHvG
    Sun Dec 17 00:01:34 +0000 2017
    @CNN
    Hollywood execs name Anita Hill to lead anti-harassment effort https://t.co/sEHjFEufdc https://t.co/94V1tDKgS7
    Sat Dec 16 23:30:07 +0000 2017
    @CNN
    Two paintings by Renaissance artist Raphael have been discovered at the Vatican — after being hidden for 500 years… https://t.co/bIKAhcgJ38
    Sat Dec 16 23:02:27 +0000 2017
    @CNN
    "I wasn’t ready for a woman President." In this small Kentucky town, 81% of voters supported Trump, and most are st… https://t.co/QqtVtwEqi6
    Sat Dec 16 22:46:36 +0000 2017
    @CNN
    This bombshell letter accuses Uber of espionage, hacking and bribery https://t.co/JA9fB7sqPU https://t.co/oHekxtghmY
    Sat Dec 16 22:30:21 +0000 2017
    @CNN
    "This is going to be one of the great gifts to the middle-income people of this country that they've ever gotten fo… https://t.co/ziKsa0Z2xM
    Sat Dec 16 22:17:39 +0000 2017
    @CNN
    "I was a healthy 33-year-old, and I'm not going to be a healthy 34-year-old." Ady Barkan, who is battling ALS and c… https://t.co/FxLUrbM1z8
    Sat Dec 16 22:00:44 +0000 2017
    @CNN
    JUST IN: Democratic Rep. Ruben Kihuen of Nevada won't run for re-election amid sexual harassment allegations… https://t.co/ndz5exdX4W
    Sat Dec 16 21:40:17 +0000 2017
    @CNN
    Morgan Spurlock, the filmmaker behind "Super Size Me," is leaving his production company after detailing his own hi… https://t.co/thCuWlD32R
    Sat Dec 16 21:30:23 +0000 2017
    @CNN
    Ex-wife of NBA player Lorenzen Wright charged in his 2010 slaying https://t.co/hnL5yHeDVL https://t.co/oIuNUTsir7
    Sat Dec 16 21:15:02 +0000 2017
    @CNN
    Susan Bro, mother of Charlottesville victim Heather Heyer, says she has some advice for President Trump: "Stop twee… https://t.co/I4BBtZSeKA
    Sat Dec 16 21:00:24 +0000 2017
    @CNN
    "I'm protecting my child's remains." Susan Bro, mother of Charlottesville victim Heather Heyer, says she has hidden… https://t.co/0uDJfsHhZ6
    Sat Dec 16 20:45:55 +0000 2017
    @CNN
    Two paintings by Renaissance artist Raphael have been discovered at the Vatican — after being hidden for 500 years… https://t.co/Hpnq1nFtMC
    Sat Dec 16 20:31:45 +0000 2017
    @CNN
    "There's no better time than the holiday season to reach out and give back to our communities," former President Ba… https://t.co/r7IxR9VT49
    Sat Dec 16 20:15:30 +0000 2017
    @CNN
    "I wasn’t ready for a woman President." In this small Kentucky town, 81% of voters supported Trump, and most are st… https://t.co/d4qDHtp3xu
    Sat Dec 16 20:01:02 +0000 2017
    @CNN
    "The Simpsons" predicted Disney would buy Fox in an episode that aired way back in 1998 https://t.co/DD6CkCRaMd https://t.co/82C5G8Klun
    Sat Dec 16 19:45:05 +0000 2017
    @CNN
    Their missions vary greatly: To provide loving homes for orphaned children, feed those in crisis or mend war's psyc… https://t.co/l39VG5k5G5
    Sat Dec 16 19:30:18 +0000 2017
    @CNN
    The vote to roll back #netneutrality rules was slammed by tech giants like Amazon, Facebook and Netflix.
    
    It was ap… https://t.co/Jo2LRFCjzh
    Sat Dec 16 19:15:05 +0000 2017
    @CNN
    Chef Mario Batali includes recipe with apology for 'past behavior' https://t.co/gUwvY3Qbsn https://t.co/pe2xYMWPQH
    Sat Dec 16 19:00:13 +0000 2017
    @CNN
    John McCain calls out Trump for his anti-media remarks, saying the President "must understand his harmful rhetoric… https://t.co/EAw9MJzyNd
    Sat Dec 16 18:45:13 +0000 2017
    @CNN
    Russian election date set for March 2018 https://t.co/YnITHxti3M https://t.co/W8jIYpzZ8p
    Sat Dec 16 18:30:03 +0000 2017
    @CNN
    This is what's in the GOP's final tax plan https://t.co/8jIV8m5Hj7 https://t.co/tk7Tnq58EG
    Sat Dec 16 18:15:09 +0000 2017
    @CNN
    What changes to the child tax credit means for families https://t.co/cdMoLgZ6e7 https://t.co/Od3fQvvjRB
    Sat Dec 16 18:00:05 +0000 2017
    @CNN
    "What the hell is going on in Chicago?" President Trump asked in a recent speech.
    
    R&amp;B artist BJ the Chicago Kid co… https://t.co/HMFuhBUp4y
    Sat Dec 16 17:46:55 +0000 2017
    @CNN
    Former President Barack Obama dons a Santa hat and brings holiday cheer to kids in Washington, D.C.… https://t.co/XkkqiVim3J
    Sat Dec 16 17:30:04 +0000 2017
    @CNN
    Journalist Tina Brown suggests "pigs in a blanket" recipe for chef Mario Batali after he posted an online apology f… https://t.co/73bPpwrZMe
    Sat Dec 16 17:16:03 +0000 2017
    @CNN
    These are the 7 words the Trump administration has banned the Centers for Disease Control and Prevention from using… https://t.co/CSxdeIDMJV
    Sat Dec 16 17:00:46 +0000 2017
    @CNN
    President Trump's judge pick demonstrates his utter contempt for the judiciary, writes Paul Callan for @CNNOpinion… https://t.co/Y7sAAIb2zG
    Sat Dec 16 16:45:09 +0000 2017
    @CNN
    Peru's President to face impeachment proceedings https://t.co/i0IXFaQnqS https://t.co/igil5fMd1I
    Sat Dec 16 16:15:13 +0000 2017
    @CNN
    Powerful winds threaten to fuel the Thomas Fire in Southern California https://t.co/7hBaFizVG5 https://t.co/pML5Jpx7RD
    Sat Dec 16 16:00:08 +0000 2017
    @CNN
    It looks like tax reform is already paying off with the GOP base https://t.co/QmbH3Fn88T https://t.co/qQt1CoT1hD
    Sat Dec 16 15:45:04 +0000 2017
    @CNN
    This is how your tuition will be affected by the Republican tax reform bill https://t.co/tDlyW870JU https://t.co/dDMK4Vy1mV
    Sat Dec 16 15:30:05 +0000 2017
    @CNN
    Lindsey Vonn strikes back with Val d'Isere World Cup win https://t.co/nZw6n72zyJ https://t.co/exW5nlfBMb
    Sat Dec 16 15:21:28 +0000 2017
    @CNN
    Former Vanity Fair editor Tina Brown: "The more women we have in positions of authority...the more you're going to… https://t.co/ik1zEeQCcG
    Sat Dec 16 14:51:43 +0000 2017
    @CNN
    Veteran magazine editor Tina Brown on Mario Batali's online apology, amid allegations of sexual assault, which was… https://t.co/wW2fHuDglw
    Sat Dec 16 14:41:15 +0000 2017
    @CNN
    Take a look back at the photos that shaped 2017 https://t.co/ghDtzAzg1F https://t.co/J9LcdAuLo5
    Sat Dec 16 14:30:27 +0000 2017
    @CNN
    .@GroverNorquist: "Every single American who pays taxes will get a rate reduction." https://t.co/3ebaS9P2aZ
    Sun Dec 17 20:44:24 +0000 2017
    @FoxNews
    A sailor meets his child for the first time following the guided-missile cruiser USS Vella Gulf's (CG 72) return to… https://t.co/zSP6Expc1f
    Sun Dec 17 20:44:06 +0000 2017
    @FoxNews
    'Batman' Actor Christian Bale: Trump's America Is 'A Genuine Tragedy' https://t.co/SJkP7EtHEi
    Sun Dec 17 20:41:58 +0000 2017
    @FoxNews
    Readout of @POTUS’s Call with President Vladimir Putin https://t.co/luUFOhF0nj
    Sun Dec 17 20:30:25 +0000 2017
    @FoxNews
    .@CortesSteve: "You can't be pro-employment and anti-employer." https://t.co/FITBh7EuSy
    Sun Dec 17 20:30:05 +0000 2017
    @FoxNews
    .@SenFranken has confirmed he will leave the Senate in early January. https://t.co/1gL5Y32jEO
    Sun Dec 17 20:28:41 +0000 2017
    @FoxNews
    Boy, 10, to get bionic hand in time for Christmas (via @christocarbone @FoxNewsTech)  https://t.co/a3PkN8nE6b
    Sun Dec 17 20:25:00 +0000 2017
    @FoxNews
    .@CortesSteve: "Suddenly Democrats have found religion when it comes to running up the debt even though the Obama a… https://t.co/rNmuzigxmO
    Sun Dec 17 20:21:24 +0000 2017
    @FoxNews
    .@GDouglasJones: "[Roy Moore] is hurting the people of this state." https://t.co/z0pQOBHwM7
    Sun Dec 17 20:20:01 +0000 2017
    @FoxNews
    .@GDouglasJones: "I oppose the building of a wall. I think that's an expense that the taxpayers just don't have to… https://t.co/n1WkRr85RE
    Sun Dec 17 20:15:02 +0000 2017
    @FoxNews
    Power outage at Atlanta airport causes 'pandemonium'
    https://t.co/ytQLhWfv4e
    Sun Dec 17 20:12:38 +0000 2017
    @FoxNews
    North Koreans mark 6th anniversary of Kim Jong Il's death https://t.co/dS7H3bRfWY
    Sun Dec 17 20:10:22 +0000 2017
    @FoxNews
    RT @EricShawnTV: I anchor @FoxNews at 4 &amp; 6 pm ET: Was #Mueller team obtaining @POTUS @realDonaldTrump transition e-mails legal and on the…
    Sun Dec 17 20:10:13 +0000 2017
    @FoxNews
    Man accidentally drops wife's wedding ring in Salvation Army kettle https://t.co/dy3VoQZshr
    Sun Dec 17 20:10:00 +0000 2017
    @FoxNews
    .@KellyannePolls: "The fix was in against @realDonaldTrump from the beginning, and they were pro-Hillary... They ca… https://t.co/B3i5KMHB1j
    Sun Dec 17 20:09:05 +0000 2017
    @FoxNews
    On @WattersWorld, @jessebwatters compared the actions and treatment of @HillaryClinton and @POTUS. https://t.co/YLoAaGzfxJ
    Sun Dec 17 20:03:59 +0000 2017
    @FoxNews
    .@IvankaTrump has expressed her enthusiasm for the GOP tax reform bill, which Treasury Secretary @stevenmnuchin1 to… https://t.co/mUBpk40UrD
    Sun Dec 17 19:59:07 +0000 2017
    @FoxNews
    .@stevenmnuchin1: “I think we could have quarters of 4, 5, 6 percent growth." https://t.co/fMDkBrPbrS https://t.co/sU1riVkR06
    Sun Dec 17 19:58:18 +0000 2017
    @FoxNews
    .@stevenmnuchin1: “I have no doubt” tax reform will pass. https://t.co/fMDkBrPbrS https://t.co/eTfaBi8utP
    Sun Dec 17 19:56:15 +0000 2017
    @FoxNews
    Texas man admits to beheading wife in front of children https://t.co/Ur3kHCCZuu
    Sun Dec 17 19:55:00 +0000 2017
    @FoxNews
    .@GroverNorquist: "Every single American who pays taxes will get a rate reduction." https://t.co/3ebaS9P2aZ
    Sun Dec 17 20:44:24 +0000 2017
    @FoxNews
    A sailor meets his child for the first time following the guided-missile cruiser USS Vella Gulf's (CG 72) return to… https://t.co/zSP6Expc1f
    Sun Dec 17 20:44:06 +0000 2017
    @FoxNews
    'Batman' Actor Christian Bale: Trump's America Is 'A Genuine Tragedy' https://t.co/SJkP7EtHEi
    Sun Dec 17 20:41:58 +0000 2017
    @FoxNews
    Readout of @POTUS’s Call with President Vladimir Putin https://t.co/luUFOhF0nj
    Sun Dec 17 20:30:25 +0000 2017
    @FoxNews
    .@CortesSteve: "You can't be pro-employment and anti-employer." https://t.co/FITBh7EuSy
    Sun Dec 17 20:30:05 +0000 2017
    @FoxNews
    .@SenFranken has confirmed he will leave the Senate in early January. https://t.co/1gL5Y32jEO
    Sun Dec 17 20:28:41 +0000 2017
    @FoxNews
    Boy, 10, to get bionic hand in time for Christmas (via @christocarbone @FoxNewsTech)  https://t.co/a3PkN8nE6b
    Sun Dec 17 20:25:00 +0000 2017
    @FoxNews
    .@CortesSteve: "Suddenly Democrats have found religion when it comes to running up the debt even though the Obama a… https://t.co/rNmuzigxmO
    Sun Dec 17 20:21:24 +0000 2017
    @FoxNews
    .@GDouglasJones: "[Roy Moore] is hurting the people of this state." https://t.co/z0pQOBHwM7
    Sun Dec 17 20:20:01 +0000 2017
    @FoxNews
    .@GDouglasJones: "I oppose the building of a wall. I think that's an expense that the taxpayers just don't have to… https://t.co/n1WkRr85RE
    Sun Dec 17 20:15:02 +0000 2017
    @FoxNews
    Power outage at Atlanta airport causes 'pandemonium'
    https://t.co/ytQLhWfv4e
    Sun Dec 17 20:12:38 +0000 2017
    @FoxNews
    North Koreans mark 6th anniversary of Kim Jong Il's death https://t.co/dS7H3bRfWY
    Sun Dec 17 20:10:22 +0000 2017
    @FoxNews
    RT @EricShawnTV: I anchor @FoxNews at 4 &amp; 6 pm ET: Was #Mueller team obtaining @POTUS @realDonaldTrump transition e-mails legal and on the…
    Sun Dec 17 20:10:13 +0000 2017
    @FoxNews
    Man accidentally drops wife's wedding ring in Salvation Army kettle https://t.co/dy3VoQZshr
    Sun Dec 17 20:10:00 +0000 2017
    @FoxNews
    .@KellyannePolls: "The fix was in against @realDonaldTrump from the beginning, and they were pro-Hillary... They ca… https://t.co/B3i5KMHB1j
    Sun Dec 17 20:09:05 +0000 2017
    @FoxNews
    On @WattersWorld, @jessebwatters compared the actions and treatment of @HillaryClinton and @POTUS. https://t.co/YLoAaGzfxJ
    Sun Dec 17 20:03:59 +0000 2017
    @FoxNews
    .@IvankaTrump has expressed her enthusiasm for the GOP tax reform bill, which Treasury Secretary @stevenmnuchin1 to… https://t.co/mUBpk40UrD
    Sun Dec 17 19:59:07 +0000 2017
    @FoxNews
    .@stevenmnuchin1: “I think we could have quarters of 4, 5, 6 percent growth." https://t.co/fMDkBrPbrS https://t.co/sU1riVkR06
    Sun Dec 17 19:58:18 +0000 2017
    @FoxNews
    .@stevenmnuchin1: “I have no doubt” tax reform will pass. https://t.co/fMDkBrPbrS https://t.co/eTfaBi8utP
    Sun Dec 17 19:56:15 +0000 2017
    @FoxNews
    Texas man admits to beheading wife in front of children https://t.co/Ur3kHCCZuu
    Sun Dec 17 19:55:00 +0000 2017
    @FoxNews
    Bizarre film of @Omarosa surfaces amid White House exit https://t.co/YRKbEmx246
    Sun Dec 17 19:42:01 +0000 2017
    @FoxNews
    .@GDouglasJones: "[Roy Moore] is hurting the people of this state." https://t.co/YXE59SATIs
    Sun Dec 17 19:40:25 +0000 2017
    @FoxNews
    Putin thanks Trump by phone for info that thwarted terror attack, WH confirms (via @josephweber19 @foxnewspolitics)  https://t.co/bbp0zUMv2Z
    Sun Dec 17 19:40:00 +0000 2017
    @FoxNews
    .@GDouglasJones: "I'm going to be a Doug Jones Democrat. I'm going to be looking at issues on both sides. I'm going… https://t.co/RNSfX0soW4
    Sun Dec 17 19:38:43 +0000 2017
    @FoxNews
    .@GDouglasJones: "I do support the DACA program and would love to see that extended." https://t.co/n5CVj3LLm0
    Sun Dec 17 19:36:14 +0000 2017
    @FoxNews
    .@GDouglasJones: "I oppose the building of a wall. I think that's an expense that the taxpayers just don't have to… https://t.co/QaIOT93er5
    Sun Dec 17 19:36:01 +0000 2017
    @FoxNews
    Boy, 10, to get bionic hand in time for Christmas (via @christocarbone) https://t.co/a3PkN8nE6b #FNTech
    Sun Dec 17 19:36:00 +0000 2017
    @FoxNews
    TONIGHT on "Fox Report," @RickLeventhal talks to NYPD Commissioner @NYPDONeill - Tune in at 7p ET on Fox News Chann… https://t.co/QfSSpFEgab
    Sun Dec 17 19:33:34 +0000 2017
    @FoxNews
    .@GDouglasJones: "There's always the opportunity to find common ground." https://t.co/VzsX86iyCg
    Sun Dec 17 19:32:08 +0000 2017
    @FoxNews
    NBC paid off producer who accused Chris Matthews of harassment, report says https://t.co/7KAZqzzaGa
    Sun Dec 17 19:27:58 +0000 2017
    @FoxNews
    North Koreans mark 6th anniversary of Kim Jong Il's death https://t.co/dS7H3bzEyo
    Sun Dec 17 19:26:00 +0000 2017
    @FoxNews
    .@POTUS has used his weekly address to once more call for big changes in U.S. immigration policy. https://t.co/n66orWOPUm
    Sun Dec 17 19:24:08 +0000 2017
    @FoxNews
    .@DrDarrinPorcher on @POTUS: "We've been getting kicked around for years and years and it's about time that someone… https://t.co/u18uwWp0Zu
    Sun Dec 17 19:20:05 +0000 2017
    @FoxNews
    "Wreaths Across America" honored fallen heroes at over 1,000 locations in all 50 states https://t.co/YxRJRQEwXW
    Sun Dec 17 19:15:04 +0000 2017
    @FoxNews
    Civil Air Patrol cadets from the Fredericksburg squadron place a wreath on a headstone at Quantico National Cemeter… https://t.co/oO0UX67M01
    Sun Dec 17 19:10:02 +0000 2017
    @FoxNews
    Texas restaurant's sign depicting blackface caricature sparks outrage https://t.co/fXCPtHiZOI
    Sun Dec 17 19:07:57 +0000 2017
    @FoxNews
    Millionaire heir found guilty of murdering ex-girlfriend, burning her body in an incinerator called 'the eliminator… https://t.co/t1UveLhPtj
    Sun Dec 17 19:06:00 +0000 2017
    @FoxNews
    Hundreds attend funeral of 'abandoned' Vietnam veteran, Purple Heart recipient (via @travfed)  https://t.co/hXBE7dXYEs
    Sun Dec 17 18:56:00 +0000 2017
    @FoxNews
    .@DarrellIssa: "We've got to cleanup... the standards at the FBI and Department of Justice. Get the politics out of… https://t.co/lmGLIaM8BC
    Sun Dec 17 18:43:56 +0000 2017
    @FoxNews
    'Star Wars: The Last Jedi' opens with $220M, 2nd best weekend all-time https://t.co/Evi0lH8lt5
    Sun Dec 17 18:35:00 +0000 2017
    @FoxNews
    TONIGHT: Fox News looks back at the murder case that gripped the nation. Tune in to "Interview With a Monster: The… https://t.co/62SSUe3rs2
    Sun Dec 17 18:32:29 +0000 2017
    @FoxNews
    Obama's WH Ethics Chief 'Stocking Up' For 'When We Take the Streets' Over A Mueller Firing https://t.co/mqacTxxhxh
    Sun Dec 17 18:26:34 +0000 2017
    @FoxNews
    British woman diplomat found murdered; raped and strangled in Lebanon (via @byKatherineLam)  https://t.co/OdEeSIP0Dz
    Sun Dec 17 18:25:36 +0000 2017
    @FoxNews
    Kremlin says Putin thanked Trump for CIA tip on bombings (via @FoxBusiness) https://t.co/0DIyoG0f9z
    Sun Dec 17 18:17:30 +0000 2017
    @FoxNews
    .@RepDavid on the tax bill: "This is going to be really good for the economy but it's also going to be really good… https://t.co/ClJz87rJnB
    Sun Dec 17 18:11:53 +0000 2017
    @FoxNews
    Hundreds attend funeral of 'abandoned' Vietnam veteran, Purple Heart recipient https://t.co/fkRDLgQHAE
    Sun Dec 17 17:58:13 +0000 2017
    @FoxNews
    'Batman' Actor Christian Bale: Trump's America Is 'A Genuine Tragedy' https://t.co/uqPhXJXh1A
    Sun Dec 17 17:41:19 +0000 2017
    @FoxNews
    'Take Them Out In Cuffs': Pirro Doubles Down on FBI 'Consigliere' McCabe, Agent Strzok https://t.co/EN47t2eTAh
    Sun Dec 17 17:28:40 +0000 2017
    @FoxNews
    .@AmbJohnBolton: "I think the fact that Secretary Tillerson is still talking about the possibility of negotiation w… https://t.co/7VstYKL2VD
    Sun Dec 17 17:26:01 +0000 2017
    @FoxNews
    Trump, Putin Spoke Today via Phone https://t.co/TImDRmbx4p
    Sun Dec 17 17:22:14 +0000 2017
    @FoxNews
    Jones supports DACA, says it’s time for GOP opponent Roy Moore to ‘move on’ (via @josephweber19 @FoxNewsSunday)… https://t.co/CML6eL5pMN
    Sun Dec 17 17:15:00 +0000 2017
    @FoxNews
    North Koreans mark 6th anniversary of Kim Jong Il's death https://t.co/zrIsFOn1Fq
    Sun Dec 17 17:07:07 +0000 2017
    @FoxNews
    An airline lounge denied this woman access because she was wearing Uggs https://t.co/Pc9ehPKL4u
    Sun Dec 17 17:01:20 +0000 2017
    @FoxNews
    .@DrDarrinPorcher on @POTUS: "We've been getting kicked around for years and years and it's about time that someone… https://t.co/kkTCLk3BcV
    Sun Dec 17 16:47:01 +0000 2017
    @FoxNews
    .@gen_jackkeane: "The Trump administration is returning America to its leadership role as the indispensable nation… https://t.co/e2zSqSStb2
    Sun Dec 17 16:40:04 +0000 2017
    @FoxNews
    A sailor meets his child for the first time following the guided-missile cruiser USS Vella Gulf's (CG 72) return to… https://t.co/mqEIhMOZV4
    Sun Dec 17 16:33:05 +0000 2017
    @FoxNews
    Boy, 9, locks himself in safe while playing hide-and-seek https://t.co/2nDSbwuxNe
    Sun Dec 17 16:30:57 +0000 2017
    @FoxNews
    .@RepDeSantis: "The question is, what was the FBI doing to inject itself into the campaign?" https://t.co/SYgcBSDZK5
    Sun Dec 17 16:17:05 +0000 2017
    @FoxNews
    .@RepTimRyan: "We have a decrease in taxes for the wealthiest and we're going to borrow about two trillion dollars.… https://t.co/msyM7a3vDZ
    Sun Dec 17 16:08:03 +0000 2017
    @FoxNews
    Autopsies underway for Canadian billionaires found dead, family slams reports of murder-suicide as 'irresponsible' https://t.co/m5x1yh4lVj
    Sun Dec 17 16:00:00 +0000 2017
    @FoxNews
    A.B. Stoddard: "The president should not attack the FBI. He is the Commander in Chief and attacking his own institu… https://t.co/7JBdbdnI3k
    Sun Dec 17 15:57:33 +0000 2017
    @FoxNews
    Mnuchin says 'no doubt' Congress will pass tax reform bill this week (via @josephweber19 @FoxNewsSunday)… https://t.co/5NJIevMla7
    Sun Dec 17 15:50:00 +0000 2017
    @FoxNews
    .@DrDarrinPorcher: "Rooting against the president is equivalent to getting on an airplane and hoping that the plane… https://t.co/6O8MYTWsCm
    Sun Dec 17 15:45:04 +0000 2017
    @FoxNews
    .@DarrellIssa: "We've got to cleanup... the standards at the FBI and Department of Justice. Get the politics out of… https://t.co/33pmcjj8z6
    Sun Dec 17 15:45:00 +0000 2017
    @FoxNews
    OPINION: @GreggJarrett: Special Counsel Robert Mueller is accused of acting in complete disregard for the law and m… https://t.co/tmdkR044k0
    Sun Dec 17 15:38:55 +0000 2017
    @FoxNews
    .@KarlRove: "We don't need to cut the spending, we simply need to restrain it's future growth." #SundayFutures… https://t.co/kkCUvVyDNw
    Sun Dec 17 15:35:00 +0000 2017
    @FoxNews
    .@KarlRove: "The President's approval ratings are dreadful." https://t.co/sHWF2goNV2
    Sun Dec 17 15:29:53 +0000 2017
    @FoxNews
    Bud Cummins: "I believe Bob Mueller is a guy of integrity but he's gonna have to prove it, he's going to have to pr… https://t.co/6v2hKP98ol
    Sun Dec 17 15:27:09 +0000 2017
    @FoxNews
    .@RepKevinBrady on the tax bill: "Tax reform is hard but it's critical." https://t.co/s7pUHQE3qk
    Sun Dec 17 15:23:56 +0000 2017
    @FoxNews
    .@RepKevinBrady on the tax bill: "I think the message to our global competitors... is America is never going to fal… https://t.co/pWH3CcoXEE
    Sun Dec 17 15:11:47 +0000 2017
    @FoxNews
    .@RepKevinBrady on the tax bill: "We are on the one yard line and we intend to punch it in." https://t.co/l6huy4e5Je
    Sun Dec 17 15:03:10 +0000 2017
    @FoxNews
    Suicide bombers attack Pakistan church, killing 8 people, officials say (via @byKatherineLam)  https://t.co/qZUh0PiKuZ
    Sun Dec 17 15:00:31 +0000 2017
    @FoxNews
    On this day in 1903, the first successful engine-powered, manned airplane was flown by Orville and Wilbur Wright. I… https://t.co/kXyyzloBuR
    Sun Dec 17 14:49:11 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@GDouglasJones says he is going to be the kind of senator people can talk to and reason with.
    Sun Dec 17 14:47:29 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@GDouglasJones on @MooreSenate’s refusal to concede in AL special election: I’ve quit trying to figure out what Moore m…
    Sun Dec 17 14:47:26 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@GDouglasJones on what kind of Democratic Senator he hopes to be: I have resisted trying to put labels on myself…I'm go…
    Sun Dec 17 14:47:24 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@GDouglasJones says @POTUS’ phone following his victory was very gracious, and that he is looking forward to meeting hi…
    Sun Dec 17 14:47:21 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@GDouglasJones: I support the #DACA program and would love to see it extended.
    Sun Dec 17 14:47:18 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@GDouglasJones on #DACA: I’ve said I oppose the building of a wall but I do think we can increase border security.
    Sun Dec 17 14:47:15 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@GDouglasJones on tax reform bill: It’s a complicated bill…this is not the simplification process we were all told abou…
    Sun Dec 17 14:47:12 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@GDouglasJones on if he’d vote for tax plan: There’s things I like about it…but my biggest concern is its going to incr…
    Sun Dec 17 14:47:09 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@GDouglasJones on whether he will support @POTUS in his position as a newly-elected senator: There’s always an opportun…
    Sun Dec 17 14:47:06 +0000 2017
    @FoxNews
    .@RepTimRyan: "We need that trillion dollar infrastructure bill that the president promised." https://t.co/V1X76LJU6R
    Sun Dec 17 14:33:24 +0000 2017
    @FoxNews
    .@RepTimRyan: "We have a decrease in taxes for the wealthiest and we're going to borrow about two trillion dollars.… https://t.co/wBkBiZYjzp
    Sun Dec 17 14:31:26 +0000 2017
    @FoxNews
    A sailor meets his child for the first time following the guided-missile cruiser USS Vella Gulf's (CG 72) return to… https://t.co/QmwQWY7mVY
    Sun Dec 17 14:21:54 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@pdoocy with a preview of the tax vote and the effort to avoid a government shutdown. https://t.co/LlxoFF0uq1
    Sun Dec 17 14:21:24 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@stevenmnuchin1 on China: We are in economic competition with China…we want a more balanced and fair trade relationship…
    Sun Dec 17 14:19:02 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@stevenmnuchin1 on @POTUS’ national security strategy: I’ve been working with the president on it, he is excited to giv…
    Sun Dec 17 14:18:59 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@stevenmnuchin1 on @POTUS’ comments yesterday about 6% economic growth: I think we could have quarters of 4, 5, 6% grow…
    Sun Dec 17 14:18:56 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@stevenmnuchin1 on if short-term gov’t funding extension to January is the way to run the government: We will look at r…
    Sun Dec 17 14:15:59 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@stevenmnuchin1 on possibility of gov't shutdown: I can’t rule it out two days before Christmas but I don’t see it occu…
    Sun Dec 17 14:15:52 +0000 2017
    @FoxNews
    Pentagon secretly set up program to investigate UFOs at Harry Reid's urging, reports say https://t.co/IYX1Ldsjti
    Sun Dec 17 14:13:36 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@stevenmnuchin1 on possible new tariffs against China: We will look at where they are, whatever means we need to combat…
    Sun Dec 17 14:13:22 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@stevenmnuchin1 on China engaging in "economic aggression": This isn’t about trade wars, it’s about reciprocal fair tra…
    Sun Dec 17 14:13:20 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@stevenmnuchin1 on passing tax plan: People said we couldn't do it, we will do it and I can't be more excited for @POTU…
    Sun Dec 17 14:08:38 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@stevenmnuchin1 on tax return post cards: Over 90% of Americans are going to fill out their taxes on that postcard or o…
    Sun Dec 17 14:08:36 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@stevenmnuchin1 on simplicity of filing returns in new tax plan: We’re in the process already of designing new forms so…
    Sun Dec 17 14:07:42 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@stevenmnuchin1 on tax reform: “This is a historic event to fix a broken tax system.”
    Sun Dec 17 14:07:40 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@stevenmnuchin1 says pass-through companies are the engine of growth for this country.
    Sun Dec 17 14:06:28 +0000 2017
    @FoxNews
    RT @FoxNewsSunday: .@stevenmnuchin1 says he has no doubt Congress will pass tax reform this week.
    Sun Dec 17 14:06:26 +0000 2017
    @FoxNews
    Kit Harington stars in HBO’s “Gunpowder” as an ancestor who plotted to kill an actual king https://t.co/bj7b2P84Pq
    Sun Dec 17 20:45:05 +0000 2017
    @nytimes
    Opinion: "An emerging religious worldview — “Fox evangelicalism” — is preached from the pulpits of conservative med… https://t.co/Csnahh7cNk
    Sun Dec 17 20:30:09 +0000 2017
    @nytimes
    A power outage at the Atlanta airport, the world's busiest, stranded passengers and left them in the dark https://t.co/LHqCLLCVKQ
    Sun Dec 17 20:22:06 +0000 2017
    @nytimes
    Here are some great stories you may have missed in the rush of the week https://t.co/hVGr3too4s
    Sun Dec 17 20:15:07 +0000 2017
    @nytimes
    President Putin called President Trump to thank him for the work of the CIA in helping prevent an Islamic State att… https://t.co/de1svwADJb
    Sun Dec 17 20:07:03 +0000 2017
    @nytimes
    "The Last Jedi" made the jump to box office hyperspace with the second-biggest opening of all time https://t.co/vNPzfJBDVg
    Sun Dec 17 20:00:10 +0000 2017
    @nytimes
    Europe has many regions with movements that are pushing for more autonomy https://t.co/10LsTQe2Yo
    Sun Dec 17 19:45:04 +0000 2017
    @nytimes
    Families fear a dengue vaccine has turned their children into time bombs, in whom the virus could set off a life-th… https://t.co/LDPYQq6lqf
    Sun Dec 17 19:30:15 +0000 2017
    @nytimes
    “Republicans who voted Democratic, now they’ve discovered they can do it, and the world didn’t come to an end” https://t.co/9rQwUhysGN
    Sun Dec 17 19:15:05 +0000 2017
    @nytimes
    The planned closing sent shock waves through the theater’s community of devotees https://t.co/IVJXMhpTTF
    Sun Dec 17 19:00:14 +0000 2017
    @nytimes
    Decimated by addiction, its heritage at risk, the Cherokee Nation is trying
    to sue pharmacies and distributors https://t.co/IyEwxsMIkK
    Sun Dec 17 18:45:02 +0000 2017
    @nytimes
    Health officials tried to downplay reports that the CDC has been barred from using words like "fetus" or "transgend… https://t.co/uouA11jisf
    Sun Dec 17 18:30:16 +0000 2017
    @nytimes
    All told, 13 million fewer Americans are projected to have health coverage https://t.co/5G7boaf76K
    Sun Dec 17 18:15:08 +0000 2017
    @nytimes
    RT @peterbakernyt: Trump and Putin spoke by phone again, the second time in the last few days. White House says it will provide a readout s…
    Sun Dec 17 18:11:03 +0000 2017
    @nytimes
    Opinion: In the face of hate crimes and anti-LGBTQ laws, travelers are often the most vulnerable https://t.co/pdvj6Jn7Th
    Sun Dec 17 18:00:15 +0000 2017
    @nytimes
    President Trump's lawyer accused the special counsel of improperly obtaining transition emails, a charge Robert Mue… https://t.co/RsOU65qrgX
    Sun Dec 17 17:45:05 +0000 2017
    @nytimes
    “If we treat the dead like garbage, then the living are just walking garbage" https://t.co/02ZcZGJPWY
    Sun Dec 17 17:30:06 +0000 2017
    @nytimes
    RT @nytimesworld: Chile’s presidential election is the first in a series that will alter the political trajectory of Latin America. Voters…
    Sun Dec 17 17:20:41 +0000 2017
    @nytimes
    For women, the burden of caring for children can be so great that many opt to be sterilized. https://t.co/sih8vOdYKk https://t.co/VOkLi9AyNW
    Sun Dec 17 17:11:43 +0000 2017
    @nytimes
    When this baby died, severe malnutrition was listed as the cause of death — rare in Venezuela. “In some public hosp… https://t.co/8Xcc8jnuwX
    Sun Dec 17 17:10:05 +0000 2017
    @nytimes
    Kit Harington stars in HBO’s “Gunpowder” as an ancestor who plotted to kill an actual king https://t.co/bj7b2P84Pq
    Sun Dec 17 20:45:05 +0000 2017
    @nytimes
    Opinion: "An emerging religious worldview — “Fox evangelicalism” — is preached from the pulpits of conservative med… https://t.co/Csnahh7cNk
    Sun Dec 17 20:30:09 +0000 2017
    @nytimes
    A power outage at the Atlanta airport, the world's busiest, stranded passengers and left them in the dark https://t.co/LHqCLLCVKQ
    Sun Dec 17 20:22:06 +0000 2017
    @nytimes
    Here are some great stories you may have missed in the rush of the week https://t.co/hVGr3too4s
    Sun Dec 17 20:15:07 +0000 2017
    @nytimes
    President Putin called President Trump to thank him for the work of the CIA in helping prevent an Islamic State att… https://t.co/de1svwADJb
    Sun Dec 17 20:07:03 +0000 2017
    @nytimes
    "The Last Jedi" made the jump to box office hyperspace with the second-biggest opening of all time https://t.co/vNPzfJBDVg
    Sun Dec 17 20:00:10 +0000 2017
    @nytimes
    Europe has many regions with movements that are pushing for more autonomy https://t.co/10LsTQe2Yo
    Sun Dec 17 19:45:04 +0000 2017
    @nytimes
    Families fear a dengue vaccine has turned their children into time bombs, in whom the virus could set off a life-th… https://t.co/LDPYQq6lqf
    Sun Dec 17 19:30:15 +0000 2017
    @nytimes
    “Republicans who voted Democratic, now they’ve discovered they can do it, and the world didn’t come to an end” https://t.co/9rQwUhysGN
    Sun Dec 17 19:15:05 +0000 2017
    @nytimes
    The planned closing sent shock waves through the theater’s community of devotees https://t.co/IVJXMhpTTF
    Sun Dec 17 19:00:14 +0000 2017
    @nytimes
    Decimated by addiction, its heritage at risk, the Cherokee Nation is trying
    to sue pharmacies and distributors https://t.co/IyEwxsMIkK
    Sun Dec 17 18:45:02 +0000 2017
    @nytimes
    Health officials tried to downplay reports that the CDC has been barred from using words like "fetus" or "transgend… https://t.co/uouA11jisf
    Sun Dec 17 18:30:16 +0000 2017
    @nytimes
    All told, 13 million fewer Americans are projected to have health coverage https://t.co/5G7boaf76K
    Sun Dec 17 18:15:08 +0000 2017
    @nytimes
    RT @peterbakernyt: Trump and Putin spoke by phone again, the second time in the last few days. White House says it will provide a readout s…
    Sun Dec 17 18:11:03 +0000 2017
    @nytimes
    Opinion: In the face of hate crimes and anti-LGBTQ laws, travelers are often the most vulnerable https://t.co/pdvj6Jn7Th
    Sun Dec 17 18:00:15 +0000 2017
    @nytimes
    President Trump's lawyer accused the special counsel of improperly obtaining transition emails, a charge Robert Mue… https://t.co/RsOU65qrgX
    Sun Dec 17 17:45:05 +0000 2017
    @nytimes
    “If we treat the dead like garbage, then the living are just walking garbage" https://t.co/02ZcZGJPWY
    Sun Dec 17 17:30:06 +0000 2017
    @nytimes
    RT @nytimesworld: Chile’s presidential election is the first in a series that will alter the political trajectory of Latin America. Voters…
    Sun Dec 17 17:20:41 +0000 2017
    @nytimes
    For women, the burden of caring for children can be so great that many opt to be sterilized. https://t.co/sih8vOdYKk https://t.co/VOkLi9AyNW
    Sun Dec 17 17:11:43 +0000 2017
    @nytimes
    When this baby died, severe malnutrition was listed as the cause of death — rare in Venezuela. “In some public hosp… https://t.co/8Xcc8jnuwX
    Sun Dec 17 17:10:05 +0000 2017
    @nytimes
    Oriana Caraballo couldn’t bear the pain of watching her kids go hungry. She was about to hang herself, but then she… https://t.co/H5Fsxn0YOG
    Sun Dec 17 17:08:04 +0000 2017
    @nytimes
    Esteban’s mother couldn’t breast-feed him, so a neighbor did it. The baby was rushed to a hospital weighing 4 pound… https://t.co/YkDLVfVqNd
    Sun Dec 17 17:06:29 +0000 2017
    @nytimes
    “Your mamá is here with you, my daughter — and I love you,” Albiannys Castillo told her baby girl. The 5-month-old… https://t.co/o48WDtbtOF
    Sun Dec 17 17:04:49 +0000 2017
    @nytimes
    Kenyerber Aquino Merchán was born healthy: 6 pounds 7 ounces. At 17 months old, he starved to death.… https://t.co/OOiwWFAOTh
    Sun Dec 17 17:03:21 +0000 2017
    @nytimes
    In the last 3 years, Venezuela’s economy has collapsed. Now, hunger grips the nation. https://t.co/sih8vOdYKk https://t.co/Zi3hijwNm0
    Sun Dec 17 17:02:12 +0000 2017
    @nytimes
    “Sometimes they die in your arms just from dehydration.” Children in Venezuela are dying of malnutrition, but the g… https://t.co/aZXotKRtrN
    Sun Dec 17 17:00:04 +0000 2017
    @nytimes
    RT @nytimesarts: Oxford Dictionaries chose "youthquake" as the international Word of the Year. What would your choice be and why? https://t…
    Sun Dec 17 16:52:03 +0000 2017
    @nytimes
    The altitude is called the “death zone” for good reason. Climbing Everest is a formidable feat. The only thing more… https://t.co/IBmjk4b81l
    Sun Dec 17 16:45:13 +0000 2017
    @nytimes
    Since Hurricane Maria steamrollered Puerto Rico, the day-to-day job of digging out has fallen largely to island res… https://t.co/dOsP1VzSlj
    Sun Dec 17 16:30:14 +0000 2017
    @nytimes
    An Australian man was charged with trying to help North Korea sell its missile and other military technology abroad https://t.co/XPRYg37Bwx
    Sun Dec 17 16:15:06 +0000 2017
    @nytimes
    The ACLU is asking a judge to stop the government from preventing 2 undocumented teenagers from seeking abortions https://t.co/ORwKJBNJU8
    Sun Dec 17 16:00:03 +0000 2017
    @nytimes
    He is the fifth member of Congress to step aside in the past 2 weeks as part of the national reckoning over sexual… https://t.co/w7WSZqWs3k
    Sun Dec 17 15:45:06 +0000 2017
    @nytimes
    “I think most Americans would be outraged to know that they are subsidizing sexual predators in the tax code" https://t.co/MODkz4CTEr
    Sun Dec 17 15:30:14 +0000 2017
    @nytimes
    RT @nytvideo: Sequins. Leather. Skates. Our five-video series celebrates dancing around the world, from the asphalt streets of Tokyo to a s…
    Sun Dec 17 15:23:14 +0000 2017
    @nytimes
    Figure out where your taxes are going with our interactive calculator https://t.co/PovzWGL88l
    Sun Dec 17 15:15:06 +0000 2017
    @nytimes
    As the Nigerian military has begun making headway against Boko Haram, people are regaining their social lives, in t… https://t.co/R9djGwNN7Z
    Sun Dec 17 15:00:32 +0000 2017
    @nytimes
    Gift ideas under $50 https://t.co/RGv31K9buB https://t.co/3LxQlsJgud
    Sun Dec 17 14:45:09 +0000 2017
    @nytimes
    RT @NYTmag: “The list was not long for this world, but maybe it lived long enough to prove its point.” — @jennydeluxe https://t.co/AK2PGf2J…
    Sun Dec 17 14:32:04 +0000 2017
    @nytimes
    "I have no idea what I saw. It had no plumes, wings or rotors and outran our F-18s."
    
    But, he added, "I want to fly… https://t.co/GM0fKIt5Fx
    Sun Dec 17 14:20:07 +0000 2017
    @nytimes
    Puerto Rico is bracing for another blow: a foreclosure epidemic that could rival what happened in Detroit https://t.co/n2h5ilVBgD
    Sun Dec 17 14:08:02 +0000 2017
    @nytimes
    RT @NYTSports: Carmelo Anthony returned to Madison Square Garden, where he got a video tribute, hugs, cheers, jeers and only 5 baskets out…
    Sun Dec 17 13:58:14 +0000 2017
    @nytimes
    Kirsten Gillibrand has assumed her place at the head table of the Democrats’ anti-Trump movement https://t.co/rP0KXTe7Bd
    Sun Dec 17 13:30:06 +0000 2017
    @nytimes
    Hisham loved Arkansas and the mosque he founded in town. He thought about how little the vandals understood.
    
    Abrah… https://t.co/t4fRIUl2Gb
    Sun Dec 17 13:10:06 +0000 2017
    @nytimes
    News Analysis: When Saying ‘Yes’ Is Easier Than Saying ‘No’ https://t.co/l9E0RYkk1R
    Sun Dec 17 13:08:08 +0000 2017
    @nytimes
    "It’s authoritarian, the cult of personality. It’s saying that we’re American — and you’re not." https://t.co/rYkFab08ZP
    Sun Dec 17 13:00:20 +0000 2017
    @nytimes
    They lost their country. Then a fire robbed them of even more.
    https://t.co/tEkYlas9Za
    Sun Dec 17 12:40:07 +0000 2017
    @nytimes
    The tax code has long offered rewards for buying rather than renting, an equation that the Republican bill upends https://t.co/VfcMD4F4g4
    Sun Dec 17 12:30:09 +0000 2017
    @nytimes
    La maison la plus chère du monde? Simple babiole pour un prince saoudien https://t.co/Z1A4qY9mfX
    Sun Dec 17 12:21:34 +0000 2017
    @nytimes
    Suicide Bombers Target Pakistan Church Packed With Worshipers https://t.co/NNevzfXoTr
    Sun Dec 17 12:06:49 +0000 2017
    @nytimes
    In a White House where drama and chaos have been prominent, Omarosa Manigault Newman was known for contributing to… https://t.co/Nbr6Oc38Ux
    Sun Dec 17 12:00:14 +0000 2017
    @nytimes
    The Pentagon has acknowledged a secret program to investigate UFOs. It began in 2007 as a pet project of Harry Reid… https://t.co/Sedix2TEdN
    Sun Dec 17 11:30:15 +0000 2017
    @nytimes
    A poll finds that Americans don’t expect their own taxes to decline next year https://t.co/jtx4X9plMX
    Sun Dec 17 11:00:19 +0000 2017
    @nytimes
    Matter: Ancient Penguins Were Giant Waddling Predators https://t.co/N0eIMq0QNo
    Sun Dec 17 10:48:03 +0000 2017
    @nytimes
    Ties: My Husband Died and All I Got Was This Sweatshirt https://t.co/YI9YBBvFeI
    Sun Dec 17 10:45:20 +0000 2017
    @nytimes
    The road to Broadway has rarely been this cold https://t.co/fGvQucVvbO
    Sun Dec 17 10:38:45 +0000 2017
    @nytimes
    "I know I am not the only parent wondering if I can robot-proof my children’s careers" https://t.co/MuQ8osHExk
    Sun Dec 17 10:22:18 +0000 2017
    @nytimes
    How to speak your love briefly. How to heal from trauma. How to stop thinking and start doing. https://t.co/He6GU2yAEN
    Sun Dec 17 10:01:45 +0000 2017
    @nytimes
    RT @jasondhorowitz: In Italy, #MeToo is more like Meh. https://t.co/RwWqQEjVMR
    Sun Dec 17 09:45:13 +0000 2017
    @nytimes
    The gorgeous sapphires found in Canada’s Nunavut territory are made with a unique geological recipe https://t.co/W1SavOe1UG
    Sun Dec 17 09:26:29 +0000 2017
    @nytimes
    ‘S.N.L.’ Takes On Omarosa Resignation (or Firing?) https://t.co/Vzn0k8anG1
    Sun Dec 17 09:09:46 +0000 2017
    @nytimes
    Look, Santa's schedule is very busy https://t.co/CDperLmp2J
    Sun Dec 17 08:58:06 +0000 2017
    @nytimes
    "The world doesn’t stop just because I got sober" https://t.co/UOQpJeR7cv
    Sun Dec 17 08:40:00 +0000 2017
    @nytimes
    Hygge is the Danish concept of coziness. We're here to help you have a hygge winter. https://t.co/tLzUuQwwS3
    Sun Dec 17 08:12:45 +0000 2017
    @nytimes
    Australian Tried to Sell Missile Parts for North Korea, Police Say https://t.co/lC4ZErRyk1
    Sun Dec 17 07:53:42 +0000 2017
    @nytimes
    From “Game of Thrones” to “This Is Us,” The Times’s TV critics each pick some of their favorite hours and half-hours https://t.co/8lBhxKl13m
    Sun Dec 17 07:45:06 +0000 2017
    @nytimes
    Barely a year out of drama school, Jamael Westman was a snob about musicals. Then he tried out to play Hamilton. https://t.co/qW0PmojdZU
    Sun Dec 17 07:27:28 +0000 2017
    @nytimes
    Rex Tillerson reversed course, insisting — as Trump has all along — that the North must stop its nuclear threats https://t.co/qaqVoTVOxR
    Sun Dec 17 07:09:32 +0000 2017
    @nytimes
    Remember hygge? Well, get ready for lykke, lagom and janteloven. https://t.co/wx3wDHRenf
    Sun Dec 17 06:51:35 +0000 2017
    @nytimes
    These are the best. And the crispiest. Make them. You’ll be so happy. https://t.co/OdsgxTImuG
    Sun Dec 17 06:33:22 +0000 2017
    @nytimes
    “The hardest part of being a sibling of a person with cancer is that you’re not able to make them better" https://t.co/CNt9AhsFYO
    Sun Dec 17 06:15:24 +0000 2017
    @nytimes
    The 54 best songs of 2017 https://t.co/54cxC5f6UG
    Sun Dec 17 05:56:55 +0000 2017
    @nytimes
    Gabriel García Márquez’s literary remains may be in Texas, but a new digital project makes his papers available to… https://t.co/avv7B1vs9v
    Sun Dec 17 05:39:00 +0000 2017
    @nytimes
    Our list of the top 10 cheap eats in NYC https://t.co/DcBbnY9dcr
    Sun Dec 17 05:20:36 +0000 2017
    @nytimes
    What are your favorite holiday cookies? Here are ours. https://t.co/VTmOos52hR
    Sun Dec 17 05:04:13 +0000 2017
    @nytimes
    Vigorous Exercise Tied to Macular Degeneration in Men https://t.co/sE5WwQZxZ8
    Sun Dec 17 04:45:23 +0000 2017
    @nytimes
    He drove through the night with his mother’s ashes and her dog, Pistol, in the seat beside him. As he drove, he tal… https://t.co/IvrCnG9Iy1
    Sun Dec 17 04:40:02 +0000 2017
    @nytimes
    Global Health: Six Lessons in Helping African Women Avoid H.I.V. https://t.co/Div1poLihC
    Sun Dec 17 04:23:40 +0000 2017
    @nytimes
    A photographer stumbled upon a “cat night” at a Brooklyn bar. From there, he rode the wave from one cat extravaganz… https://t.co/3BCTO8btr2
    Sun Dec 17 04:19:43 +0000 2017
    @nytimes
    A healthy and delicious dinner idea https://t.co/yLIWeKQcMY
    Sun Dec 17 04:03:27 +0000 2017
    @nytimes
    Sleep vs. exercise?  “That’s a terrible choice,” said one doctor and sleep expert. https://t.co/mrCMSby8q3
    Sun Dec 17 03:47:10 +0000 2017
    @nytimes
    “The message here is 'Trump is going to come and get you — and we support that'"
    https://t.co/uKnskyLof9
    Sun Dec 17 03:30:06 +0000 2017
    @nytimes
    Harry Reid, who retired from Congress this year, said he was proud of The Pentagon's UFO program… https://t.co/lkzlPMs0C4
    Sun Dec 17 03:00:19 +0000 2017
    @nytimes
    Why does the flu virus change so much every year? And why does the vaccine's effectiveness vary so much? https://t.co/9Q2MI3hCz1
    Sun Dec 17 02:40:20 +0000 2017
    @nytimes
    Ask Real Estate: Holiday Tipping: A Fraught Apartment Building Tradition https://t.co/BRao3dZ838
    Sun Dec 17 02:22:12 +0000 2017
    @nytimes
    Here’s what oil drilling looks like in the arctic refuge, 30 years later https://t.co/anigkTALI2 https://t.co/spwLSchEPn
    Sun Dec 17 02:19:31 +0000 2017
    @nytimes
    It's by no means an exhaustive list. So yeah, sorry about that. https://t.co/EuIctsdDrY
    Sun Dec 17 02:03:03 +0000 2017
    @nytimes
    "When scientists say bears are going extinct, I want people to realize what it looks like" https://t.co/e07KS3EG6L
    Sun Dec 17 01:46:12 +0000 2017
    @nytimes
    Come for the cats climbing ropes. Stay for the lesson in cultural understanding. https://t.co/4zPbABcIk2
    Sun Dec 17 01:29:35 +0000 2017
    @nytimes
    Jimmy Fallon was on top of the world. Then came Trump. https://t.co/4skaoqEeby
    
    This was one of our most-read articles this year.
    Sun Dec 17 01:10:07 +0000 2017
    @nytimes
    “Fortunately, it’s something she doesn’t remember,” Shirmira said of entering the shelter system days after her dau… https://t.co/r0EGD6QLFe
    Sun Dec 17 00:40:05 +0000 2017
    @nytimes
    Op-Ed Columnist: A War Trump Won https://t.co/BxvTymlJHs
    Sun Dec 17 00:31:27 +0000 2017
    @nytimes
    Lincoln Plaza Cinema, Renowned Art House Theater, To Close https://t.co/u7Vgi0w3ch
    Sun Dec 17 00:21:51 +0000 2017
    @nytimes
    Scientists are gaining a more refined — and surprising — understanding of the effects of loneliness on health https://t.co/QHlK8zbCR7
    Sun Dec 17 00:21:07 +0000 2017
    @nytimes
    "When is 'not telling' lying?" That age-old question: How much sexual history should we share? https://t.co/AedUIPXS3V
    Sun Dec 17 00:07:03 +0000 2017
    @nytimes
    The program began in 2007 and was largely funded at the request of Harry Reid, who has had a longtime interest in s… https://t.co/uDoTGE8pqY
    Sat Dec 16 23:46:25 +0000 2017
    @nytimes
    The message making its way to Democrats is that the path to victory is through energizing minority communities https://t.co/KrqZW1rZv8
    Sat Dec 16 23:30:06 +0000 2017
    @nytimes
    An analysis of FBI crime data found a 26% increase in bias incidents in the last quarter of 2016 compared with the… https://t.co/q2nceNrpnA
    Sat Dec 16 23:15:04 +0000 2017
    @nytimes
    When Marco Rubio threatened to vote against the tax bill, critics thought he was grandstanding, bluffing or both https://t.co/oLCnK2Zvb5
    Sat Dec 16 23:00:04 +0000 2017
    @nytimes
    The ACLU is asking a judge to stop the government from preventing 2 undocumented teenagers from seeking abortions https://t.co/opM8HhOi2k
    Sat Dec 16 22:45:04 +0000 2017
    @nytimes
    Spoiler alert! For those who have seen "Star Wars: The Last Jedi," let's take a look at some burning questions you… https://t.co/O6TeVS9tne
    Sat Dec 16 22:30:17 +0000 2017
    @nytimes
    


```python
df = pd.DataFrame(
    {'org_text': org_text,
     'tweet_text': tweet_text,
     'date': date
    })
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>org_text</th>
      <th>tweet_text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sun Dec 17 20:34:25 +0000 2017</td>
      <td>@BBC</td>
      <td>Congratulations and a #BigThankYou to Denise. ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sun Dec 17 20:31:03 +0000 2017</td>
      <td>@BBC</td>
      <td>Follow the production of a contemporary perfor...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sun Dec 17 20:29:11 +0000 2017</td>
      <td>@BBC</td>
      <td>RT @BBCSport: .@NoelGallagher singing the Beat...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Sun Dec 17 20:19:09 +0000 2017</td>
      <td>@BBC</td>
      <td>RT @BBCSport: The voting is open for #SPOTY.\n...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Sun Dec 17 20:15:19 +0000 2017</td>
      <td>@BBC</td>
      <td>RT @BBCSport: It's time.\n\nWe know the conten...</td>
    </tr>
  </tbody>
</table>
</div>




```python
compound_list = []
positive_list = []
negative_list = []
neutral_list = []

# Loop through all tweets
for index, row in df.iterrows():

# Run Vader Analysis on each tweet
    df.set_value(index, 'compound', analyzer.polarity_scores(row["tweet_text"])["compound"])
    df.set_value(index, 'pos', analyzer.polarity_scores(row["tweet_text"])["pos"])
    df.set_value(index, 'neu', analyzer.polarity_scores(row["tweet_text"])["neu"])
    df.set_value(index, 'neg', analyzer.polarity_scores(row["tweet_text"])["neg"])

# Add each value to the appropriate list
    #compound_list.append(compound)
    #positive_list.append(pos)
    #negative_list.append(neg)
    #neutral_list.append(neu)
        
#compound_avg = np.mean(compound_list)
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>date</th>
      <th>org_text</th>
      <th>tweet_text</th>
      <th>compound</th>
      <th>pos</th>
      <th>neu</th>
      <th>neg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sun Dec 17 20:34:25 +0000 2017</td>
      <td>@BBC</td>
      <td>Congratulations and a #BigThankYou to Denise. ...</td>
      <td>0.8074</td>
      <td>0.477</td>
      <td>0.523</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sun Dec 17 20:31:03 +0000 2017</td>
      <td>@BBC</td>
      <td>Follow the production of a contemporary perfor...</td>
      <td>0.0000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sun Dec 17 20:29:11 +0000 2017</td>
      <td>@BBC</td>
      <td>RT @BBCSport: .@NoelGallagher singing the Beat...</td>
      <td>0.5994</td>
      <td>0.262</td>
      <td>0.738</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Sun Dec 17 20:19:09 +0000 2017</td>
      <td>@BBC</td>
      <td>RT @BBCSport: The voting is open for #SPOTY.\n...</td>
      <td>0.0000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Sun Dec 17 20:15:19 +0000 2017</td>
      <td>@BBC</td>
      <td>RT @BBCSport: It's time.\n\nWe know the conten...</td>
      <td>0.6249</td>
      <td>0.181</td>
      <td>0.819</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = df.sort_values(by=['org_text','date'],ascending=[True, False])
df2['Tweets Ago'] = df2.groupby(['org_text'])['date'].rank(method='dense',ascending=True)
    
#df2.to_csv('test.csv')
```


```python
for index, i in df2.iterrows():
    if i['org_text'] == '@BBC':
        df2.set_value(index, 'org', 'BBC') 
    elif i['org_text'] == '@nytimes':
        df2.set_value(index, 'org', 'New York Times') 
    elif i['org_text'] == '@CNN':
        df2.set_value(index, 'org', 'CNN')
    elif i['org_text'] == '@FoxNews':
        df2.set_value(index, 'org', 'Fox News')
    elif i['org_text'] == '@CBS':
        df2.set_value(index, 'org', 'CBS')
                      #print(df2['org'].unique())
#print(type(df2['org']))
```


```python
plt.clf()
sns.set(style="whitegrid", palette="muted")
plt.figure(figsize=(12, 10))
# # Incorporate the other graph properties
ax = sns.swarmplot(x = 'Tweets Ago',
                   y = 'compound',
                   data = df2,
                   hue = df2['org'],
                  size = 8)
plt.title("Sentiment Analysis of Media Tweets 12/15/17" ,size=20,weight='bold')
plt.legend(title='Media Sources',fontsize = 12,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlim(100,0)
plt.ylim(-1,1)
plt.xlabel('Tweets Ago', size = 14)
plt.ylabel('Tweet Polarity', size = 14)

x_labels = [0]
adjust = 5
start = 0 
for x in range(20):
    x_labels.append(start + adjust)
    start += adjust

plt.xticks(x_labels,x_labels,rotation='vertical')


# # Save the figure
plt.savefig("Media Sentiment Scatter.png")

# # Show plot
plt.show()
```


    <matplotlib.figure.Figure at 0x18684ac9e80>



![png](output_15_1.png)



```python
df_pivot = pd.pivot_table(df2
                              ,index=['org']
                              ,values = ['compound','pos','neu','neg']
                              ,aggfunc='mean')
df_pivot = df_pivot.reset_index()
df_pivot.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>org</th>
      <th>compound</th>
      <th>neg</th>
      <th>neu</th>
      <th>pos</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BBC</td>
      <td>0.176057</td>
      <td>0.038567</td>
      <td>0.853000</td>
      <td>0.108400</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CBS</td>
      <td>0.381163</td>
      <td>0.011608</td>
      <td>0.828258</td>
      <td>0.160150</td>
    </tr>
    <tr>
      <th>2</th>
      <td>CNN</td>
      <td>-0.026757</td>
      <td>0.086800</td>
      <td>0.841975</td>
      <td>0.071208</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Fox News</td>
      <td>-0.010037</td>
      <td>0.077983</td>
      <td>0.860867</td>
      <td>0.061133</td>
    </tr>
    <tr>
      <th>4</th>
      <td>New York Times</td>
      <td>0.016871</td>
      <td>0.079692</td>
      <td>0.828825</td>
      <td>0.091483</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.clf()
sns.set(style="whitegrid", palette="muted")
plt.figure(figsize=(12, 10))
# # Incorporate the other graph properties
total = float(len(df_pivot['org']))
ax = sns.barplot(x = 'org',
                   y = 'compound',
                   data = df_pivot
                  # hue = df2['org'],
                  # size = 8
                )

for p in ax.patches:
    ax.text(p.get_x() + p.get_width()/2., p.get_height(), "%.2f" % float(p.get_height()), 
            fontsize=12, color='black', ha='center', va='bottom')
    
plt.title("Overall Media Sentiment based on Twitter 12/15/17" ,size=20,weight='bold')
#plt.legend(title='Media Sources',fontsize = 12,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.xlim(-.5,4.5)
plt.ylim(df_pivot['compound'].min() -.1,df_pivot['compound'].max() +.1)
plt.xlabel('', size = 14)
plt.ylabel('Tweet Polarity', size = 14)

#plt.xticks(x_labels,x_labels,rotation='vertical')


# # Save the figure
plt.savefig("Overall Media Sentiment.png")

# # Show plot
plt.show()
```


    <matplotlib.figure.Figure at 0x18684ac44a8>



![png](output_17_1.png)

