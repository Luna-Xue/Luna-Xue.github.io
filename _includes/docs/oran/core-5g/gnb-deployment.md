## Configuration setup

Several of our OTA tested configs are present in the [**configs**](https://github.com/WINGS-UHM/O-RAN/tree/main/configs) folder. OCUDU supports all 3GPP Release 17 bands, the following parameters need to be changed to braodcast at a specific band.

### Cell configuration


```yml
cell_cfg:
  dl_arfcn: 636666
  band: 78
  channel_bandwidth_MHz: 30
  common_scs: 30
  plmn: "00101"
  tac: 7
  pci: 1
```