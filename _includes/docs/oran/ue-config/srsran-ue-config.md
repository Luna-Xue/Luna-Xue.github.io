
---
toc: true
---
## srsRAN UE
The USRP-based UE setup is included here mainly for PoC validation and initial testing. It can be useful for basic bring-up checks, RF sanity testing, and early experimentation, but it should not be treated as the preferred UE option for complete 5G SA testbed operation.

Much of the USRP UE development was originally tied to the older srsRAN 4G stack, and 5G SA support remains limited. As noted in the official OCUDU documentation, COTS UEs or commercial UE solutions such as Amarisoft are preferred for more complete and reliable 5G SA testing.

### Limitations

The current srsUE implementation has several limitations when running in 5G SA mode:

- Limited to 15 kHz subcarrier spacing, which means only FDD bands can be used.
- Limited to 5, 10, 15, or 20 MHz channel bandwidth.
- Handover is not supported.

Due to these constraints, the USRP-based UE path is best viewed as a lightweight experimental option, while COTS UE and Amarisoft-based setups are better suited for full testbed validation.

## Installation

Install the required build dependencies:

```sh
sudo apt-get install build-essential cmake libfftw3-dev libmbedtls-dev libboost-program-options-dev libconfig++-dev libsctp-dev
```

### Install srsGUI

`srsGUI` provides real-time channel quality visualization. The WINGS-UHM fork includes updated dependency support for the current testbed setup.
```sh
git clone https://github.com/WINGS-UHM/srsGUI.git
cd srsGUI
mkdir build
cd build
cmake ../
make 
```

### Install srsRAN 4G
The WINGS-UHM `srsRAN_4G` fork is used for 5G-SA visualization support in this setup.
```sh
git clone https://github.com/WINGS-UHM/srsRAN_4G.git
cd srsRAN_4G
mkdir build
cd build
cmake ../
make
make test
```

Install the built binaries and generate the default user configuration files:
```sh
sudo make install
srsran_install_configs.sh user
```

## Deploying srsUE

Due to limitations only FDD bands can be used you can download the config [here](https://docs.srsran.com/projects/project/en/latest/_downloads/900a04eeabbe80c1bb9f3e571afaa804/ue_rf.conf).

### RF configuration

Update the `[rf]` section to configure the USRP radio parameters according to your SDR. If an external reference is used, set the corresponding clock source in `device_args`.

```conf
[rf]
freq_offset = 0
tx_gain = 50
rx_gain = 40
srate = 23.04e6
nof_antennas = 1

device_name = uhd
device_args = clock=external    # Supported [default, internal, external, gpsdo]
time_adv_nsamples = auto
```

### Disable LTE carrier

In the `[rat.eutra]` section, disable the LTE carrier so that the UE operates only with the 5G NR carrier.

```conf
[rat.eutra]
dl_earfcn = 2850
nof_carriers = 0
```

### Configure NR carrier

Configure the `[rat.nr]` section for 5G SA operation. The NR band, ARFCN, and PRB values should match the gNB configuration.

```conf
[rat.nr]
bands = 3
nof_carriers = 1
max_nof_prb = 106
nof_prb = 106
```

The `max_nof_prb` and `nof_prb` values must be selected according to the configured channel bandwidth:

|   BW | PRBs |
| ---: | ---: |
|    5 |   25 |
|   10 |   52 |
|   15 |   79 |
|   20 |  106 |

Additionally change the `gui` option to `true` for visualizations.
```conf
[gui]
enable = true
```

### Launch srsUE
```sh
sudo -E srsUE <config-file>
# e.g. sudo -E srsUE ue_rf.conf
```