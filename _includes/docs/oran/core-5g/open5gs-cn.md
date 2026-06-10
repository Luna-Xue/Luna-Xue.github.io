## Deploying Core Network

We deploy the core network using the Docker images provided in the `ocudu` library from `open5gs`

```sh
cd ocudu/docker
docker compose -f docker-compose.yml up --build 5gc
```
{% include notification.html status="is-info" message="You can change the visible network name on COTS devices, edit the `NETWORK_NAME_FULL` and `NETWORK_NAME_SHORT` in `ocudu/docker/open5gs/open5gs.env` file." %}

Additionally you can also launch the grafana dashboard for metrics monitoring using 

```sh
docker compose -f docker-compose.yml -f docker-compose.ui.yml up --build 5gc
```
The dashboard will be hosted at `localhost:3300` and the WebUI with subscriber database will be at `localhost:9999`. 

## Configuring UE Subscriber Entries

The `subscriber_db.csv` file stores UE subscription information in the following format:
```csv
Name,IMSI,Key,OP_Type,OP/OPc,AMF,QCI,IP_alloc
```
Each entry corresponds to a single UE. The values for `IMSI`, `Key`, `OP_Type`, `OP/OPc`, and `AMF` must match the parameters programmed onto the SIM card. The `Name` field is only used as a human-readable identifier and is ignored by the HSS. `QCI` specifies the default bearer QoS class, while `IP_alloc` assigns a static IP address to the UE.

When provisioning multiple test UEs, a common approach is to increment the `IMSI`, `Key`, and `IP_alloc` values by one for each additional subscriber while keeping the remaining fields unchanged. This simplifies the creation of multiple UE profiles while maintaining unique subscriber identities and IP assignments.

The output below shows two provisioned UE entries in `ocudu/docker/open5gs/subscriber_db.csv`:


```bash
S23U,001010123456780,00112233445566778899AABBCCDDEEFF,opc,63BFA50EE6523365FF14C1F45F88737D,8000,9,10.45.1.2
A22,001010123456781,00112233445566778899AABBCCDDEEFF,opc,63BFA50EE6523365FF14C1F45F88737D,8000,9,10.45.1.3
```


Here, `S23U` and `A22` are simply human-readable labels used to identify the corresponding UEs. Each UE is assigned a unique `IMSI` and static IP address, while the remaining parameters are configured according to the SIM profile.

The maximum number of UEs that can be assigned IP addresses is determined by the UE address pool configured in the core network. In the default Open5GS configuration, the pool is defined as `10.45.0.1/16`, corresponding to the subnet `10.45.0.0/16`. This provides an address space of approximately 65,534 usable UE IP addresses. The available range can be increased or reduced by modifying the subnet mask to suit the deployment requirements.
