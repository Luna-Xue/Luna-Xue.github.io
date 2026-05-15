---
toc: true
---
## Smartphone Setup
Insert the sim card in your test smartphone and navigate to the the sim cards Access Point Name settings and add a new APN as shown in image:

![APN-Setting](/assets/img/docs/oran/APN.jpg)

## SixFab 5G development kit

The SixFab 5G Development Kit provides a Raspberry Pi-based modem UE platform with a 5G HAT, Quectel M.2 modem, SIM interface, antennas, USB connectivity, and external power support for private 5G/O-RAN testbed experiments.

### Modem Manager
Many Linux distributions have ModemManager preinstalled. They must uninstall it before starting the tutorial. They can be easily uninstalled through the package manager.

```sh
sudo apt purge modemmanager -y
```
Install the required serial communication program such as minicom.

```sh
sudo apt install minicom -y
```
Open the serial communication for /dev/ttyUSB2 device port with 115200 baudrate using minicom

### APN Setup
```sh
sudo minicom -D /dev/ttyUSB2 -b 115200  
```
Configure the modem for ECM mode. The response should be `OK`.

```sh
AT+QCFG="usbnet",1
```

Add our `srsapn` to connect and restart.

```sh
AT+CGDCONT=1,"IP","srsapn"
AT+CFUN=1,1
```

Check the allocated IP address it should match our entry in `subscriber_db.csv`

```sh
AT+CGPADDR=1
```

![apn-setup](/assets/img/docs/oran/cots-ue-apn.png)

Close the `minicom` interface by pressing `ctrl+A` and `Z`. This completes the APN setup.

### Internet Connectivity
We can now check internet connectivity through a speedtest-cli. Install the speedtest-cli
```sh
sudo apt install speedtest-cli
```

Check the `IPv4` address assigned to the modem interface. For the SixFab 5G Development Kit, the interface is typically named `usb0`. Run the speedtest.

```sh
speedtest-cli --source <usb0 IPV4>
# e.g. speedtest-cli --source 192.168.225.24
```

![speedtest-cli](/assets/img/docs/oran/speedtest.png)
