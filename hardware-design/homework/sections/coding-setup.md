---
---

# Coding Setup

## Install VSCode

foo

bar





## Pi Connection Debugging



### Pi Network Management Failure

Windows only?

```
nmcli -o
```

If stuck connecting (orange) 



### IPv4 Forwarding Disabled

```powershell
Get-NetIPInterface -InterfaceAlias "Wi-Fi" | Select-Object Forwarding
Get-NetIPInterface -InterfaceAlias "Ethernet" | Select-Object Forwarding
```


```powershell
Set-NetIPInterface -InterfaceAlias "Wi-Fi" -Forwarding Enabled
Set-NetIPInterface -InterfaceAlias "Ethernet" -Forwarding Enabled
```

Set this setting to persist so we don't have to do it repeatedly

1. Win + R, type regedit.
2. Go to: HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\SharedAccess
3. Right-click > New > DWORD (32-bit) Value.
4. Name it EnableRebootPersistConnection and set the value to 1



