---
toc: true
---

## Installation
```sh
git clone https://github.com/WINGS-UHM/O-RAN.git
cd O-RAN/NearRT-RIC
```
The following scripts are prepared for installing `kubespray` and `docker` based kubernetes cluster for deploying the Near RT-RIC
```yaml
NEAR-RT-RIC/
├── nginx.sh                            # setup nginx service for hosting dashboards (grafana, kubernetes)
├── kubespray.sh                        # setup a single node kubspray cluster with calico and metallb
├── kube-extra.sh                       # extra setups for setting up dashboard and nfs volumes for influxdb
├── fix-dns.sh                          # fixes dns/internet disconnection if setup breaks nameserver 
├── get-env.sh                          # helper funtion to export import ric-plt ips
└── install_common_templates_to_helm.sh # Modified common templates script to remove root access dependency
```

## NGINX Setup
`nginx.sh` sets up and installs NGINX and configures a simple reverse proxy with basic authentication to securely expose the Kubernetes dashboard proxy running on the local machine.

The proxy forwards requests from a public port to the local kubectl proxy service. The script uses a default username and password for convenience in closed lab environments. Users may change these credentials if the service is exposed outside the local network.

```sh
sudo htpasswd -cb /etc/nginx/htpasswd admin admin123
```

## Kubernetes Cluster Deployment
`kubespray.sh` script deploys a single-node Kubernetes cluster using Kubespray, with the following components enabled:

- Calico – Kubernetes networking (CNI)
- MetalLB – LoadBalancer support for bare-metal environments
- Helm – Kubernetes package manager
- Metrics Server – basic cluster metrics

**Users Should modify following parameters according to their environment.**
 - **Add your local Node IP Address in**
    ```sh 
    NODE_IP="${NODE_IP:-192.168.50.103}" # This will be the eno1, eth0 interface of your host PC, also make sure this IP will be static on router.
    ```
 - **Change Ansible username to the username of host pc**
    ```sh
    ANSIBLE_USER="${ANSIBLE_USER:-admin}" 
    ```
    Replace `admin` with the username of the host machine that will run the deployment.
 - **Network Interface for Calico**
    ```sh
    CALICO_IFACE="${CALICO_IFACE:-eno1}" 
    ```
    Interface name should be your internet interface name usually `eno1/eth0`
 - **Metallb IP Pool**
    
    This IP range should be removed from the **router's DHCP allocation** to prevent conflicts with other devices on the network.
    MetalLB assigns addresses from this range to Kubernetes services requiring external nodes access.
    ```sh
    METALLB_POOL="${METALLB_POOL:-192.168.50.245-192.168.50.246}"
    ```

## Additional Kubernetes Services

`kube-extra.sh` script installs additional services on top of the Kubernetes cluster, including:

- a local kubectl proxy system service for dashboard access
- an admin service account and login token
- an exported kubeconfig file
- an optional local Docker registry
- an optional NFS dynamic storage provisioner
- the Headlamp Kubernetes UI

Users should modify the following parameters according to their environment.

 - **Local Docker registry**
    
    Leave this enabled only if a local registry is required for storing xApp images. If a registry already exists in the environment, this can be disabled.
    ``` sh
    DO_LOCAL_REGISTRY="${DO_LOCAL_REGISTRY:-1}"
    REGISTRY_BIND_IP="${REGISTRY_BIND_IP:-127.0.0.1}"
    REGISTRY_PORT="${REGISTRY_PORT:-5000}"
    ```
    If registry access is needed from other machines, replace `127.0.0.1` with the host machine IP.
 - **NFS Provisioner**

    Certain ORAN RIC services require persistent NFS storage access if the system already has a NFS provisoner this can be disabled.
    ```sh
    DO_NFS_PROVISIONER="${DO_NFS_PROVISIONER:-1}"
    NFS_SERVER_IP="${NFS_SERVER_IP:-192.168.50.103}"
    NFS_EXPORT_PATH="${NFS_EXPORT_PATH:-/export/k8s}"
    NFS_MOUNT_OPTIONS="${NFS_MOUNT_OPTIONS:-nfsvers=3}"
    ```
    If left enabled 
    - Set `NFS_SERVER_IP` to the IP of the Host Machine.

    - Set `NFS_EXPORT_PATH` to the exported NFS directory.
  
## Installation
After making the modifications, run the scripts in the following order.

```sh
sudo chmod +x *.sh
./nginx.sh
./kubespray.sh
./kube-extra.sh
```
{% include notification.html message="Do not run the scripts as `sudo` or `root`.

The scripts internally use `sudo` only where required. Running them as root may break permissions and prevent access for the normal user." %}
