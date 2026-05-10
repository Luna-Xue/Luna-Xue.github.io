## Configuration setup

Several of our OTA tested configs are present in the [**configs**](https://github.com/WINGS-UHM/O-RAN/tree/main/configs) folder. OCUDU supports all 3GPP Release 17 bands, the following parameters need to be changed to braodcast at a specific band.


## USRP configuration
The `ru_sdr` block configures the SDR-based radio unit. For USRP-based deployments, OCUDU uses the UHD driver to communicate with the radio hardware. 
The example below uses an X300/X310-class USRP with a 30.72 MS/s sampling rate.

```yml
ru_sdr:
  device_driver: uhd
  device_args: type=x300
  clock: default           # Supported: [default, internal, external, gpsdo].
  sync: default            # Supported: [default, internal, external, gpsdo].
  srate: 30.72
  tx_gain: 25
  rx_gain: 25
```
The `device_args` field should match the connected USRP type. For example, X300/X310 radios commonly use `type=x300`, while other USRP platforms may require different UHD device arguments. 
The `srate` value must be compatible with the selected channel bandwidth and numerology.

The `clock` and `sync` options control the reference and timing sources used by the USRP. For a single-radio setup, the default or internal clock is usually sufficient. 
For multi-radio experiments, external synchronization through a 10 MHz reference and PPS source, such as an OctoClock or GPSDO, is recommended to maintain timing and frequency alignment across devices.

The `tx_gain` and `rx_gain` values may need tuning depending on the antenna, RF front-end, cable loss, and target coverage area. Very high transmit gain can cause distortion or saturation, while very low gain may result in poor UE attachment or weak received signal strength.


### Cell configuration
The transmission band can be changed under the cell_cfg block. Refer to the NR band table at [**sqimway**](https://www.sqimway.com/nr_band.php) to verify that the selected band, ARFCN, bandwidth, and subcarrier spacing are valid for the intended deployment.
```yml
cell_cfg:
  dl_arfcn: 636666            # Required UINT, sets the Downlink ARFCN.
  band: 78                    # Optional TEXT - auto
  channel_bandwidth_MHz: 30
  common_scs: 30
  plmn: "00101"
  tac: 7
  pci: 1
```
The `dl_arfcn` determines the downlink carrier frequency, while `band` selects the corresponding NR operating band. The `channel_bandwidth_MHz` and `common_scs` fields define the bandwidth and numerology used by the cell. These values must be consistent with the selected NR band and supported by the SDR sampling rate.

## O-RAN E2 Connection
The `e2` block enables the O-RAN E2 interface between the OCUDU gNB and the near-RT RIC. This allows the gNB to expose RAN information and control interfaces to xApps running on the RIC.
```yml
e2:
  enable_du_e2: true               # Enable DU E2 agent (one for each DU instance)
  enable_cu_cp_e2: true            # Enables the CU E2 agent for CU-CP
  enable_cu_up_e2: true            # Enables the CU E2 agent for CU-UP
  e2sm_kpm_enabled: true           # Enable KPM service module
  e2sm_rc_enabled: true            # Enable RC service module
  e2sm_ccc_enabled: true           # Enable CCC service module
  addr: 192.168.50.103             # RIC IP address 
  bind_addr: 192.168.50.38         # A local IP that the E2 agent binds to for traffic from the RIC. ONLY required if running the RIC on a separate machine. 
  port: 32222                      # RIC port
```
The DU, CU-CP, and CU-UP E2 agents can be enabled depending on which parts of the gNB should communicate with the RIC. The DU E2 agent is commonly used for lower-layer RAN measurements and control, while the CU-CP and CU-UP agents expose control-plane and user-plane related information.

The service model options define which E2 service models are advertised to the RIC. KPM is used for key performance measurements, RC supports RAN control procedures, and CCC enables additional control-related capabilities when supported by the deployment.

The `addr` field should point to the near-RT RIC E2 termination IP address. The `bind_addr` should be set to the local interface IP of the machine running OCUDU, especially when the RIC and gNB are deployed on different hosts. The port must match the E2 termination service port exposed by the RIC. On the same host the `addr` and `port` field will be the corresponding cluster ip addresses. 