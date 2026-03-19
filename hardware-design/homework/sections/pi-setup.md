---
---

# Raspberry Pi Setup



## Flash SD Card

### Download Pi Imager

### Dongle Assembly

### Configure Settings

### Write Image


## Laptop Setup

### Install VSCode

foo

bar

### Install Remote SSH Extension





## Raspberry Pi Assembly

### Confirm Kit Contents

### Heat Sinks

### Nonslip Nubs

### Insert Into Case

### Plug It In!

### Connect Ethernet Cord


## Verify/Debug Connection


### Lost WiFi on Laptop

Update priority order for network connections

### Connection Stays Red

Are you plugged in?

Are you sure there is an image on this SD card?


### SSH: Unknown Name

Go to network settings. Find the IP address. Use that instead of `raspberrypi.local`

### SSH: Denied

Double check your username and password. Default is `kiwi`/`blueberry` (we will change this shortly)

Sometimes the "Enable SSH" setting doesn't stick.

If you have access to a keyboard and monitor, run this on your Pi:
```
sudo raspi-config
```

Otherwise, you can create an empty file named `ssh` in the root of the bootfs

Otherwise, you may need to flash a clean image

### Network Devices

Mac only?

Make sure VSCode has permission to find devices on the network


### Internet Sharing

SSH keeps disconnecting.

Make sure you have network sharing enabled on your laptop. You need to share your WiFi connection.

You may also need to switch your WiFi network to `St Olaf Guest`. The `eduroam` network sometimes blocks Pi connections

### Internet Sharing Blocked

Try
```
ping -c 4 yahoo.com
```

If it fails, you are not sharing the internet with your Pi

### Pi Network Management Failure

Windows only?

```
nmcli -o
```

If stuck connecting (orange) 

```bash
sudo mv /etc/netplan/90-NM-*.yaml /tmp/netplan-backup.yaml
```

```bash
touch /etc/netplan/01-netcfg.yaml 
```


```bash
network:
	version: 2
	renderer: NetworkManager
```

```bash
sudo netplan apply
```

then reboot



### IPv4 Forwarding Disabled

**Windows:** make sure internet sharing is enabled for both IPv4 and IPv6


```powershell
Get-NetIPInterface -InterfaceAlias "Wi-Fi" | Select-Object Forwarding
Get-NetIPInterface -InterfaceAlias "Ethernet" | Select-Object Forwarding
```

If anything is disabled, enable it:

```powershell
Set-NetIPInterface -InterfaceAlias "Wi-Fi" -Forwarding Enabled
Set-NetIPInterface -InterfaceAlias "Ethernet" -Forwarding Enabled
```

Make this setting persist so we don't have to do it repeatedly

1. Win + R, type regedit.
2. Go to: `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\SharedAccess`
3. Right-click > New > DWORD (32-bit) Value.
4. Name it EnableRebootPersistConnection and set the value to 1


## Configure Pi

### Change Admin Password


### Create Personal Account


### Add Host to VSCode

Also add the folder! This is necessary to get the file navigator, drag and drop files