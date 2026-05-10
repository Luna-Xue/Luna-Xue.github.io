## OCUDU Installation

Install the required build tools

```sh
sudo apt-get install cmake make gcc g++ pkg-config libmbedtls-dev libsctp-dev libyaml-cpp-dev libgtest-dev
```

Install `ZMQ` for simulations
```sh 
sudo apt-get install libzmq3-dev
```

Install the `OCUDU` using the following commands
```sh
# Install OCUDU with ZMQ-enabled
git clone https://gitlab.com/ocudu/ocudu.git
cd ocudu
mkdir build
cd build
cmake ../ -DENABLE_EXPORT=ON -DENABLE_ZEROMQ=ON 
make -j $(nproc)
make test -j $(nproc)
sudo make install
```

{% include notification.html status="is-info" message="Data Plane Development Kit ([**DPDK**](https://www.dpdk.org/about/)) is an optional requirement useful when running **4x4 MIMO configurations** or **High Bandwidth Configurations**. Follow the [**DPDK installation guide**](https://ocudu-docs-604e90.gitlab.io/user_manual/tutorials/dpdk/) if required." %}