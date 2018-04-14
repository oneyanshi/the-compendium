The Compendium 
============================== 
The Compendium is a computer science capstone about other computer science capstones completed during the spring semester of 2018 at American University. 

More specifically, it is a content management system built using [Wagtail](https://wagtail.io/), which uses the Django framework. This project not only includes the 'look' of the frontend but also the 'look' for the administration side. For those interested in seeing the code and/or developing, please continue reading on. 

## Installation

You must have (https://www.python.org/downloads/)[Python] and (https://pip.pypa.io/en/latest/installing.html)[pip] installed. Additionally, I recommend using (https://virtualenv.pypa.io/en/latest/installation.html)[virtualenv] to separate development environments.   

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