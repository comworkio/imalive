# Contributions

For the developers you can test your changes on the app by running this command:

```shell
docker-compose -f docker-compose-local.yml up --build --force-recreate 
```

You can also run unit tests by running this command:

```shell
docker-compose -f docker-compose-local.yml up --build --abort-on-container-exit imalive-tests 
```

Then you can try jaegger UI here for the traces: http://localhost:16686

And prometheus for the metrics: http://localhost:9090
