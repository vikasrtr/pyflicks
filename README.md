# pyFlicks
This is a simple fun project that aims to create a basic Movie Recommender.

# How ?
pyFlicks is based on my efforts to create simple movie recommender in python, using various techniques.

Currently the only algorithm is User-User Collaborative Filtering.

Learn more [on my blog](https://vikasrtr.github.io)

# Why ?
This is an my attempt to implement and play with the recommender algorithms and techniques, i learn and read about.

I started pyFlicks for sole purpose of designing a full-fledged recommender from ground up.

There will thus be continuous improvements in future, including the **ugly interface**

# Usage
pyFlicks is available as a Flask application and based on [MovieLens Dataset](http://grouplens.org/datasets/).

 - Download MovieLens Dataset and extract in `data` folder.
 - Run `generate_dataset.py` to create necessary files from data.
 - To run it simply execute the `run.py` from root:

` >> python3 generate_dataset.py`
` >> python3 run.py`

 - Then open `localhost:5000` in your browser.

## Screenshots
![Rating Interface](https://github.com/vikasrtr/pyflicks/raw/master/screen-1.png)
![Recommendations](https://github.com/vikasrtr/pyflicks/raw/master/screen-2.png)

# Requirements
 - python 3+
 - Numpy
 - Pandas
 - Flask

# Note
You are free to use any of the code in any manner, whatsoever, without any warranty from author.