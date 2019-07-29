### Setup instructions

* `git clone` this repo https://github.com/nikhilverma55/comments
* virtualenv -p python3 pyenv --no-site-packages
* Install virtualenv
`https://gist.github.com/frfahim/73c0fad6350332cef7a653bcd762f08d`
* source pyenv/bin/activate
* cd comments
* Install the requirements
`pip install -r requirement.txt`
`python manage.py migrate`
`python manage.py createsuperuser`
`python manage.py runserver 0.0.0.0:8000`



