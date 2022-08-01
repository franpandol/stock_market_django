<h1 align="center">Stock Market Service</h1>

## 📝 Table of Contents

- [Getting Started](#getting_started)
- [Prerequisites](#prerequisites)
- [Test](#tests)
- [Usage](#usage)
- [Obtain API Key](#api_key)
- [Obtain Stock Data](#stock_data)
- [Throttling](#throttling)
- [Built Using](#built_using)
- [Authors](#authors)

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

There are two options:

with Makefile
  - `make install` # will create a new environment with venv, then will install the required dependencies listed in requirements.txt
  - `make run` # will run a development server for the app in localhost:8000

with docker

  - `docker-compose build` # will create the container image
  - `docker-compose up -d` # will start the image, this will run a development server for the app in localhost:8000


### Prerequisites <a name = "prerequisites"></a>

To install and run with `make` you need to have python 3 installed.
To run it with `docker` you need to have `docker` and `docker-compose` installed.


## 🔧 Running the tests <a name = "tests"></a>

`python manage.py test`

## 🎈 Usage <a name="usage"></a>
The app has two endpoints, one to register for a new API key and the other one to get the stock data.

Use `localhost:8000` to run the api in local mode. 
You can also play with the app in the browser by going to https://stock-market-service.pandol.sh/

--------

### Obtain API Key <a name = "api_key"></a>
------------
- url: `https://stock-market-service.pandol.sh/api/v1/api/v1/register/`
- method: POST
- Receives name, last_name and email. Email is unique. 

Example request

`curl --request POST \
  --url https://stock-market-service.pandol.sh/api/v1/register/ \
  --header 'Content-Type: multipart/form-data' \
  --form name=Dave \
  --form last_name=Mustaine \
  --form email=example@email.com`

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
  --header 'Authorization: Token cc7e310f398b3db5544e0cc9688f7fb473b520eb'`

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
-----

- Anonymous users: 100 requests/day
- Authenticated  users: 1000 requests/day

Error message when throttled

`{
	"detail": "Request was throttled. Expected available in 86399 seconds."
}`

## ⛏️ Built Using <a name = "built_using"></a>

- [Django](https://www.djangoproject.com) - Web framework for Python

## ✍️ Authors <a name = "authors"></a>

- [@franpandol](https://github.com/franpandol)
