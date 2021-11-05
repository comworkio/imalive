# Im Alive API

Just a dummy healthcheck api for your nodes (support armhf for raspberrypi).

It provide a http/restful endpoint that you can use as a healthcheck rule to your loadbalancer and also publish a heartbit in stdout (usefull if you collect it in a log/alerting management system such as elasticstack).

## Table of content

[[_TOC_]]

## Git repositories

* Main repo: https://gitlab.comwork.io/oss/imalive
* Github mirror: https://github.com/idrissneumann/imalive.git
* Gitlab mirror: https://gitlab.com/ineumann/imalive.git

## Image on the dockerhub

The image is available and versioned here: https://hub.docker.com/r/comworkio/imalive-api

## Running with docker-compose

First create your `.env` file from the `.env.example`:

```shell
cp .env.example .env
```

Then replace the values (like the `IMALIVE_NODE_NAME` with your node name). Then:

```shell
$ docker-compose up
```

If you want to test on a raspberrypi or any other ARM device, use this command instead:

```shell
$ docker-compose -f docker-compose-arm.yml up
```
## Endpoints

### Healthcheck

```shell
$ curl localhost:8080/v1/health
{"status": "ok", "time": "2021-11-05T06:55:28.274736", "alive": true, "name": "anode"}
```

### Manifests

```shell
$ curl localhost:8080/v1/manifest 
{"version": "1.0", "sha": "1c7cb1f", "arch": "x86"}
```

## Heartbit

You can change the wait time between two heartbit with the `WAIT_TIME` environment variable (in seconds).
