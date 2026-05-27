---
toc: true
---
## Installation

This page sets up the local Python environment and the xApp onboarder tools used later for packaging and deploying xApps to the Near-RT RIC.

### Python xApp Framework

Install virtual environment support and create an isolated Python workspace for xApp development.

```sh
sudo apt install python3-venv
python -m venv .venv
source .venv/bin/activate
```

Install the Python xApp framework module inside the active virtual environment.

```sh
pip install ricxappframe
```

### Chart Repository

The xApp onboarder needs a Helm chart repository where generated xApp charts can be stored. The command below starts a local ChartMuseum instance on port `8090`.

```sh
docker run --rm -u 0 -it -d -p 8090:8080 -e DEBUG=1 -e STORAGE=local -e STORAGE_LOCAL_ROOTDIR=/charts -v $(pwd)/charts:/charts chartmuseum/chartmuseum:latest
```

Set the chart repository URL so the onboarder can publish charts to the local repository.

```sh
export CHART_REPO_URL=http://0.0.0.0:8090
```

### xApp Onboarder

Clone the onboarder repository and install its Python requirements.

```sh
git clone https://github.com/WINGS-UHM/xapp_onboarder.git
cd xapp_onboarder
pip install -r requirements.txt
```

Install the onboarder package into the active Python environment.

```sh
pip install .
```

This provides the `dms_cli` tool used for onboarding, installing, and managing xApps on the Near-RT RIC.
