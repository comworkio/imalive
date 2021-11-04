# Im Alive API

Just a dummy healthcheck api for your nodes (support armhf for raspberrypi).

## Table of content

[[_TOC_]]

## Git repositories

* Main repo: https://gitlab.comwork.io/oss/imalive-api
* Github mirror: https://github.com/idrissneumann/imalive-api.git
* Gitlab mirror: https://gitlab.com/ineumann/imalive-api.git

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
{"status": "ok", "alive": true, "name": "rpirunner8"}
```

### Manifests

```shell
$ curl localhost:8080/v1/manifest 
{"version": "1.0", "sha": "1c7cb1f", "arch": "x86"}
```
