## 🪟 Windows Startup Folder Privilege Escalation (Short Note – বাংলা)

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
