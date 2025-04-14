import os
import random
import time
from googletrans import Translator
from termcolor import colored
import pyfiglet

names = ["ZAIN", "RAHEEL", "FAROOQ", "PHULPOTO", "JINSAR", "MYSTIC", "DRAGON", "GHOST"]
emojis = ["😂", "🔥", "😈", "👑", "💀", "💥", "😎", "❤️", "🚀", "🤖"]
quotes = [
    "Power belongs to PHULPOTO.",
    "Coding is the new magic.",
    "Zain Bhai in the zone!",
    "Jarvis is online."
]

voice_enabled = True

def speak(text):
    if voice_enabled:
        os.system(f'espeak-ng "{text}" 2>/dev/null')

def print_title():
    os.system("clear")
    banner = pyfiglet.figlet_format("JARVIS PH")
    print(colored(banner, 'cyan'))

def slow_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def hold():
    print(colored("\n[!] Press Enter to continue...", "yellow"))
    input()

def text_spam():
    print_title()
    text = input("Kya likhna hai? ")
    style = input("Styled text chahiye? (y/n): ").lower()
    repeat = int(input("Kitni baar likhna hai? "))
    final = ""
    for _ in range(repeat):
        final += f"{text.upper() if style == 'y' else text}  "
    print("\n" + "-" * 60)
    print(colored("[OUTPUT]:", "green"))
    print(final)
    print("-" * 60)
    hold()

def emoji_spam():
    print_title()
    count = int(input("Kitni alag emojis chahiye? "))
    repeat = int(input("Har emoji kitni baar aaye? "))
    selected = random.sample(emojis, min(count, len(emojis)))
    result = ""
    for e in selected:
        result += (e + " ") * repeat + "\n"
    print("\n" + "-" * 60)
    print(colored("[OUTPUT]:", "green"))
    print(result)
    print("-" * 60)
    hold()

def text_emoji_combo():
    print_title()
    text = input("Kya likhna hai? ")
    emoji_custom = input("Custom emoji chahte ho? (Leave blank for random): ")
    emoji_use = emoji_custom if emoji_custom else random.choice(emojis)
    repeat = int(input("Kitni baar repeat karein? "))
    result = ""
    for _ in range(repeat):
        result += f"{text}{emoji_use}  "
    print("\n" + "-" * 60)
    print(colored("[OUTPUT]:", "green"))
    print(result)
    print("-" * 60)
    hold()

def random_name_emoji():
    print_title()
    repeat = int(input("Kitni baar repeat karein? "))
    result = ""
    for _ in range(repeat):
        result += f"{random.choice(names)}{random.choice(emojis)}  "
    print("\n" + "-" * 60)
    print(colored("[OUTPUT]:", "green"))
    print(result)
    print("-" * 60)
    hold()

def text_styler():
    print_title()
    text = input("Kya text style karna hai? ")
    styled = pyfiglet.figlet_format(text)
    print(colored(styled, "green"))
    hold()

def voice_speak():
    print_title()
    text = input("Kya bolna hai? ")
    speak(text)
    hold()

def language_change():
    print_title()
    text = input("Enter text: ")
    lang = input("Target language code (e.g. en, ur, hi, ar): ")
    translator = Translator()
    translated = translator.translate(text, dest=lang)
    print("Translated:", translated.text)
    hold()

def secret_mode():
    print_title()
    print(colored("** SHADOW BROTHERHOOD MODE ACTIVATED **", "magenta"))
    slow_print("Zain Bhai rules the cyber world!", 0.03)
    speak("Shadow Mode Activated")
    hold()

def main():
    if voice_enabled:
        speak(random.choice(quotes))

    while True:
        print_title()
        print(colored("--- JARVIS_PH TOOL MENU ---", "yellow"))
        print(colored("""
1. Text Spam (normal/styled)
2. Emoji Spam
3. Text + Emoji Combo
4. Random Names + Emojis
5. Text Styler
6. Voice with espeak-ng
7. Language Changer
8. Secret Brotherhood Mode
9. Exit
        """, "cyan"))

        choice = input("Select Option (1-9): ")

        if choice == '1':
            text_spam()
        elif choice == '2':
            emoji_spam()
        elif choice == '3':
            text_emoji_combo()
        elif choice == '4':
            random_name_emoji()
        elif choice == '5':
            text_styler()
        elif choice == '6':
            voice_speak()
        elif choice == '7':
            language_change()
        elif choice == '8':
            secret_mode()
        elif choice == '9':
            speak("Goodbye Zain Bhai.")
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    main()
