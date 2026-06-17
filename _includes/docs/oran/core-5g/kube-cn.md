## Deploying Core Network in Kubernetes

Additionally Core Network can also be deployed in the Kubernetes Cluster besides ORAN services.


1. Verify MetalLB IP availability and edit `RECIPE_EXAMPLE/example_recipe_5g_core.yaml`

   ```sh
   cd O-RAN/kube-cn
   kubectl get ipaddresspools -A -o wide
   kubectl get svc -A -o wide | awk 'NR==1 || $3=="LoadBalancer"'
   ```

   ```yml
   open5gs:
   loadBalancerIP: <free-metallb-ip>
   upfAdvertiseIP: <free-metallb-ip>
   ```

2. Verify gNB metrics source:

   ```yml
   metrics:
       wsUrl: <gnb-host-ip>:8001
   ```

3. Build and push images:

   ```sh
   docker build -t registry.local:5000/ocudu/open5gs-5gc:v2.7.6-kube --target open5gs --build-arg OS_VERSION=22.04 --build-arg OPEN5GS_VERSION=v2.7.6 ./open5gs
   docker build -t registry.local:5000/ocudu/telegraf:1.35.0-kube ./telegraf
   docker build -t registry.local:5000/ocudu/grafana:12.0.2-kube --build-arg GF_VERSION=12.0.2 --build-arg LOGO_URL=https://raw.githubusercontent.com/ocudu/OCUDU_Project_docs/main/docs/source/.imgs/logo.png ./grafana
   # Push Images to registry
   docker push registry.local:5000/ocudu/open5gs-5gc:v2.7.6-kube
   docker push registry.local:5000/ocudu/telegraf:1.35.0-kube
   docker push registry.local:5000/ocudu/grafana:12.0.2-kube
   ```

4. Install to Kubernetes:

   ```sh
   ./install -f RECIPE_EXAMPLE/example_recipe_5g_core.yaml
   ```

5. Verify:

   ```sh
   kubectl get pods -n 5g-core -o wide
   kubectl get svc -n 5g-core -o wide
   ```

   <img src="{{"/assets/img/docs/oran/kube-cn.png"  | relative_url }}" 
          alt="cn-in-kube" 
          style="max-width: 100%; height: auto;" />

   {% include notification.html status="is-info" message="Replace the  `addr` field under `cu_cp.amf` in the gNB configuation file with the `EXTERNAL IP` that is set for `open5gs-5gc` service to connect with core network deployment in kubernetes." %}

{:start="6"}
6. Access WebUIs:

   **Open5GS WebUI**: `http://<free-metallb-ip>:9999`.
   For **Grafana** metrics dashboard, install/start the port-forward service:

   ```sh
   sudo cp systemd/5g-core-grafana-portforward.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable --now 5g-core-grafana-portforward.service
   ```

   Then access `http://<HOST-IP>:3400`

   {% include notification.html status="is-warning" message="`<HOST-IP>` is the the IP address for the Host PC and not the above mentioned `<free-metallb-ip>` that is provided to core network service" %}

{:start="7"}
7. View `Core-Network` logs

   ```sh
   kubectl logs -f -n 5g-core -l app.kubernetes.io/component=open5gs-5gc
   ```
