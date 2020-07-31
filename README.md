# Django REST Framework File Upload Example

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.0-brightgreen.svg)](https://djangoproject.com)
[![Django Rest Framework Version](https://img.shields.io/badge/djangorestframework-3.11-brightgreen.svg)](https://www.django-rest-framework.org/)

## Running the Project Locally

First, clone the repository to your local machine:

```bash
https://github.com/anuragal/apiserver.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

## The API endpoints 

### Get the mock list of all questions
**127.0.0.1:8000/list/

### Upload file to server
**127.0.0.1:8000/sync/

To run the API in postman select option like below

![](https://github.com/anuragal/apiserver/blob/master/readme_images/postman_sync.png)

## License

The source code is released under the [MIT License](https://github.com/sibtc/drf-jwt-example/blob/master/LICENSE).
