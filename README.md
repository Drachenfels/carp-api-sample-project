CarpApi - Sample Project
========================

## About

Project is a template for working example of carp-api. With examples of many if
not all features that framework delivers. One may expect to see endpoints,
namespaces, versions, dockerised carp-api server, working business logic using
dockerised postgres database with sqlalchemy+alembic combo and finally
configuration sufficient to deployed to google app engine.

## Installation

    `git clone https://github.com/Drachenfels/carp-api-sample-project.git`

## How to start server:

By either:

    `PYTHONPATH=$PWD SIMPLE_SETTINGS=sample_api.settings.base carp_api run`

Or:

    `make server-start`

Second command will launch it through container using docker and
docker-compose. It may be easier in certain environments.

In both cases we should have api serving responses on port 5000.

Try:

    `sensible-browser http://localhost:5000/'

## More documentation

Project home: [Carp-Api](https://github.com/Drachenfels/carp-api)
