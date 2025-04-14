import os
import time
import requests
from colorama import Fore, init

init(autoreset=True)

# ===== VIRUS CREATOR (PRANK) =====
def virus_creator():
    print(f"\n{Fore.RED}🦠 Select Virus Type:")
    print(f"{Fore.YELLOW}1. Fake Delete All Files")
    print(f"{Fore.YELLOW}2. Endless Popup (Android)")
    print(f"{Fore.YELLOW}3. Keyboard Blocker (Prank)")
    choice = input(">> ")
    
    if choice == "1":
        with open("virus_prank.bat", "w") as f:
            f.write("@echo off\necho Your PC is hacked! Just kidding :P\npause")
        print(f"{Fore.GREEN}Fake virus created (virus_prank.bat)!")
    elif choice == "2":
        os.system("termux-toast 'Prank! You Got Hacked!'")
    else:
        print(f"{Fore.RED}Use 'pip install keyboard' + 'keyboard.block_key()'")

# ===== WHATSAPP BOMBER =====
def whatsapp_bomber():
    print(f"\n{Fore.RED}📵 Use Only With Consent!")
    phone = input("Enter Target WhatsApp (e.g., +92123456789): ")
    msg = input("Message to Spam: ")
    count = int(input("Number of Messages: "))
    
    print(f"{Fore.GREEN}Spamming WhatsApp...")
    for _ in range(count):
        requests.get(f"https://example-api.com/send_wa?phone={phone}&text={msg}")  # Replace with real API
        time.sleep(1)

# ===== SMS BOMBER 2.0 =====
def sms_bomber():
    print(f"\n{Fore.RED}⚠️ Legal Warning: Use Responsibly!")
    phone = input("Enter Target Phone: ")
    api = input("Enter SMS API Key (or 'demo' for test): ")
    
    if api == "demo":
        for _ in range(10):
            print(f"{Fore.YELLOW}SMS Sent to {phone} (Simulated)")
            time.sleep(0.5)

# ===== KEYLOGGER =====
def keylogger():
    print(f"\n{Fore.RED}🔑 Educational Use Only!")
    print("Run: 'pkg install python -y && pip install pynput'")

# ===== WI-FI EXTRACTOR =====
def wifi_extractor():
    print(f"\n{Fore.RED}📶 Requires Root!")
    os.system("cp /data/misc/wifi/wpa_supplicant.conf ./wifi_passwords.txt")

# ===== MAIN MENU =====
def main():
    print(f"\n{Fore.MAGENTA}=== TERMUX ULTIMATE HACKING TOOL v5.0 ===")
    print(f"{Fore.RED}1. Virus Creator")
    print(f"{Fore.RED}2. WhatsApp Bomber")
    print(f"{Fore.RED}3. SMS Bomber 2.0")
    print(f"{Fore.RED}4. Keylogger")
    print(f"{Fore.RED}5. Wi-Fi Extractor")
    print(f"{Fore.YELLOW}6. Exit")

    choice = input("\n>> Select Option (1-6): ")

    if choice == "1":
        virus_creator()
    elif choice == "2":
        whatsapp_bomber()
    elif choice == "3":
        sms_bomber()
    elif choice == "4":
        keylogger()
    elif choice == "5":
        wifi_extractor()
    elif choice == "6":
        exit()
    else:
        print(f"{Fore.RED}Invalid choice!")

if __name__ == "__main__":
    main()
