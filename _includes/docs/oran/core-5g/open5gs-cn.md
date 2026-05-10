## Deploying Core Network

We deploy the core network using the Docker images provided in the `ocudu` library from `open5gs`

```sh
cd ocudu/docker
docker compose -f docker-compose.yml up --build 5gc
```

Additionally you can also launch the grafana dashboard for metrics monitoring using 

```sh
docker compose -f docker-compose.yml -f docker-compose.ui.yml up --build 5gc
```
The dashboard will be hosted at `localhost:3300` and the WebUI with subscriber database will be at `localhost:9999`. New subscribers can be added before launching in the `open5gs/subscriber_db.csv` or from the WebUI after intiating. 