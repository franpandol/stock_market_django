<h1 align="center">Stock Market Service or How to present a github repository for a technical challenge</h1>

## 📝 Table of Contents

- [Live Site](#live_site)
- [Getting Started](#getting_started)
- [Prerequisites](#prerequisites)
- [Test](#tests)
- [Usage](#usage)
- [Obtain API Key](#api_key)
- [Obtain Stock Data](#stock_data)
- [Throttling](#throttling)
- [Logging](#logging)
- [TODO & Ideas](#todo)
- [Built Using](#built_using)
- [Authors](#authors)

## Live Site <a name = "live_site"></a>
**https://stock-market-service.pandol.sh/api/v1/**

Deployed in a linux server hosted in DigitalOcean using gunicorn and nginx. The database engine chosen is PostgreSQL taking advantage of the DBAAS (Database as a service) features provided by DigitalOcean.
SSL Certificates by Let's Encrypt are used to secure the site. The site is accessible only through HTTPS. 

<a name = "how_to_use_it" href="#usage">How to use it</a>

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. First clone the repo and then run the following commands:

There are two options with two steps each:

with Makefile
  - Step 1: `make install` # will create a new environment with venv, then will install the required dependencies listed in requirements.txt
  - Step 2: `make run` # will run a development server for the app in localhost:8000

with docker

  - Step 1: `docker-compose build` # will build the image
  - Step 2: `docker-compose up -d` # will start the image, this will run a development server for the app in localhost:8000


For development usage you can change the ALPHAVANTAGE_API_KEY used by the system modifying the file `stock_market/settings/.env.dev` before building the image.

### Prerequisites <a name = "prerequisites"></a>

To install and run with `make` you need to have python 3 installed.
To run it with `docker` you need to have `docker` and `docker-compose` installed.


## 🔧 Running the tests <a name = "tests"></a>

`python manage.py test`


## 🎈 Usage <a name="usage"></a>
The app has two endpoints, one to register for a new API key and the other one to get the stock data. The code for the endpoints can be found in the `api/views.py` file.
The request and data process of ALPHAVANTAGE API is done in `api/services.py`.
The sign up fields validation is made in `authentication/serializers.py`.

Use `localhost:8000` to access the api in local mode. 

**You can also try the app by going to https://stock-market-service.pandol.sh/api/v1/**

--------

### Obtain API Key <a name = "api_key"></a>
------------
- url: `https://stock-market-service.pandol.sh/api/v1/register/`
- method: POST
- Receives name, last_name and email. Email is unique. 

Example request

`curl --request POST \
  --url https://stock-market-service.pandol.sh/api/v1/register/ \
  --header 'Content-Type: multipart/form-data' \
  --form name=Dave \
  --form last_name=Mustaine \
  --form email=examplemail@email.com`

Response
`33cee8a8b96dafasd23bcd38315a0a98f3b821`

------


### Get Stock Data <a name = "stock_data"></a>
------------

- url: `https://stock-market-service.pandol.sh/api/v1/symbol/<str:symbol>/`
- Receives symbol in the url.
- Requires an API key in the header.

Example request

`curl --request GET \
  --url https://stock-market-service.pandol.sh/api/v1/symbol/ibm/ \
  --header 'Authorization: Token f1d263b4fde5550ba0cff55db25042bfe5915063'`

Response

`{
	"last_refreshed": "2022-07-29",
	"close_value": "130.7900",
	"open_value": "129.5200",
	"high_value": "131.0000",
	"low_value": "129.3100",
	"variation_between_last_two_days": 1.5699999999999932
}`



## ⛏️ Throttling <a name = "throttling"></a>

#### Throttling rules

- Anonymous users: 100 requests/day
- Authenticated  users: 1000 requests/day

Error message when throttled

`{
	"detail": "Request was throttled. Expected available in 86399 seconds."
}`

## Logging <a name = "logging"></a>

The class RequestLogMiddleware write a row in a log file called apicalls.log every time a request to the API endpoints is made, listing the request method, the url and the authenticated user.
RequestLogMiddleware is in api/mixins.py

Example 

`[31/Jul/2022 13:56:08] [INFO] [API_REQUEST] GET /api/v1/symbol/ibm/ user@example.com`

`[01/Aug/2022 00:31:01] [INFO] [API_REQUEST] POST /api/v1/register/ AnonymousUser`


## TODO & Ideas <a name = "todo"></a>
- Refactor api/services.py to be able to handle multiple sources of data. Maybe move process_data to a new class Parser to make it more generic.
- Add a new endpoint to get the stock data for a list of symbols.


## ⛏️ Built Using <a name = "built_using"></a>

- [Django](https://www.djangoproject.com) - Web framework for Python
- [Django REST Framework](https://www.django-rest-framework.org) 


## ✍️ Authors <a name = "authors"></a>

- [@franpandol](https://github.com/franpandol)
