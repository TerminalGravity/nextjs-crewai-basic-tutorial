This document describes the structure of models used in our application. 

First, we define a model named `NamedUrl`. This model consists of two fields:
- `name`: This field stores a string that represents the name.
- `url`: This field stores a string that represents the URL.

Next, we define a model named `PositionInfo`. This model is composed of several fields:
- `company`: This field stores a string that represents the company's name.
- `position`: This field stores a string that represents the position's title.
- `name`: This field stores a string that represents the name of the individual.
- `blog_articles_urls`: This field stores a list of strings, each representing a URL to a blog article.
- `youtube_interviews_urls`: This field stores a list of `NamedUrl` objects, each representing a YouTube interview with its name and URL.

Lastly, we define a model named `PositionInfoList`. This model contains a single field:
- `positions`: This field stores a list of `PositionInfo` objects, representing a collection of position information.

