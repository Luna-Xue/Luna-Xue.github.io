## Physical SIM/ISIM setup
![cots-ue](/assets/img/docs/oran/cots-ue.jpg)

For COTS UE testing, a programmable SIM/USIM is required so that the UE credentials match the subscriber profile configured in the 5G core. The SIM can be programmed using a compatible smart-card reader, a programmable USIM card, and the SIM programming tool.

The subscriber information is stored in a CSV file using the following format:

```csv
Name,IMSI,Key,OP_Type,OP/OPc,AMF,QCI,IP_alloc
```
For a basic testbed setup, each UE should have a unique Name, IMSI, and IP_alloc. The remaining authentication values can be kept the same across entries. The current csv currently consists of two rows for the UEs we have tested with a Commericial Android Phone and a SixFab 5G Development Kit.

```csv
Name,IMSI,K,OP_Type,OPc,AMF,SQN,UE_IP
S23U,001010123456780,00112233445566778899AABBCCDDEEFF,opc,63BFA50EE6523365FF14C1F45F88737D,8000,9,10.45.1.2
A22,001010123456781,00112233445566778899AABBCCDDEEFF,opc,63BFA50EE6523365FF14C1F45F88737D,8000,9,10.45.1.3
```

For the sim card we used a `sysmoISIM-SJA5-9FV SIM` and a `HID OMNIKEY 3121` sim reader/programming tool. 

### Reading/Writing to SIM
sysmocom SIM cards support programming sim values through their python library. Install the pySim library
```sh
git clone https://github.com/osmocom/pysim
cd pysim
sudo apt-get install --no-install-recommends \
    pcscd libpcsclite-dev \
    python3 \
    python3-setuptools \
    python3-pyscard \
    python3-pip
pip3 install -r requirements.txt
```
Check the current ISIM configuration:

```sh
./pySim-read.py -p0 # may need to be ran with sudo on some devices
```
Writing the values according to your csv row.
```sh
./pySim-prog.py -p0 -s <ICCID> --mcc=<MCC> --mnc=<MNC> -a <ADM-KEY> --imsi=<IMSI> -k <KI> --opc=<OPC>
```

e.g.
```sh
./pySim-prog.py -p0 -s <ICCID> --mcc=001 --mnc=01 -a <ADM-KEY> \
  --imsi=001010123456781 \
  -k 00112233445566778899AABBCCDDEEFF \
  --opc=63BFA50EE6523365FF14C1F45F88737D
```
The following values will be provided by your individual sim card.
- `<ICCID>`   = SIM card ICCID
- `<ADM-KEY>` = programmable SIM admin key

<!-- ## eSIM TBC--> 