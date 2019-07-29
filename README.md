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

`API Endpoints`

* GET all comments
`http://127.0.0.1:8000/api/v1/comments/`

* POST comments
`http://127.0.0.1:8000/api/v1/comments/`
`{"comment_text": "Great_product", "orders": 2, "user": 1, "active": "true"}`

* POST replies
`http://127.0.0.1:8000/api/v1/comments/`
`{"comment_text": "Great_product", "orders": 2, "user": 1, "active": "true", "parent": 18}`



