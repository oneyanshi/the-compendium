The Compendium 
============================== 
The Compendium is a computer science capstone about other computer science capstones. This was made during the spring semester of 2018 at American University for CSC-493. 

More specifically, it is a content management system built using [Wagtail](https://wagtail.io/), which uses the Django framework. This project not only includes the 'look' of the frontend but also the 'look' for the administration side. For those interested in seeing the code and/or developing, please continue reading on. 

## Installation

You must have [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/latest/installing.html) installed. 

Additionally, I recommend using [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) to separate development environments.   

After doing the above, you must do the following: 

```$ pip install wagtail ``` 

After, you'll be able to clone the project. 

    git clone git@github.com:oneyanshi/the-compendium.git
    cd the-compendium
    pip install -r requirements.txt 

And then do the following: 

    ./manage.py migrate 
    ./manage.py load_initial_data 
    ./manage.py runserver 

## Development  

I highly recommend on reading up on documentation on Wagtail and how development works. It is "object-oriented," and changes are made by doing migrations. It is **imperative** to use branching when working on this project, otherwise you may do something or lose work that you wanted/didn't want. 

## Deployment 

So what about deployment? Great question! There shouldn't be a reason for me to reinvent the wheel in terms of providing a tutorial, but [this resource works pretty well](https://vix.digital/insights/deploying-wagtail-production/). Something to note is that any static elements will need to be hosted and/or served through different means, but the tutorial discusses options, ranging from Whitenoise to using Amazon S3. 

Additionally, if you would like to host it on Heroku, the directions on [Wagtail's site](https://wagtail.io/blog/wagtail-heroku-2017/) will help.   