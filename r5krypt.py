import base64

from sys import platform
from os import system
from pathlib import Path
from colorama import Fore, init, Back
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pyfiglet import Figlet

init(autoreset=True)

custom_fig = Figlet(font='big')
print(Fore.CYAN + custom_fig.renderText('SHA-256'))
print(Fore.BLUE + "By ru55o.")
input("press ENTER to continue...")

def clear():
    if platform.startswith('win') or platform.startswith('cygwin'):
        system('cls')
    else:
        system('clear')


clear()
password_introduced = input(Fore.CYAN + "PASSWORD: ")
password = password_introduced.encode()
salt: bytes = b'5\\;\x85\xf0%\xc6wW\x0b\x91Xo~j\xa3'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    backend=default_backend(),
    iterations=100000)
key = base64.urlsafe_b64encode(kdf.derive(password))
print(Fore.LIGHTGREEN_EX + "Key generated successfully: " + Fore.LIGHTBLUE_EX)
print(Fore.BLACK + Back.RED + str(key.decode()))


def encrypt():
    message = input(Fore.CYAN + "TEXT TO ENCRYPT: ")
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message).decode()
    print(Fore.RED + "ENCRYPTED TEXT: " + Fore.LIGHTWHITE_EX + str(encrypted_message))


def decrypt():
    encrypted = input(Fore.CYAN + "TEXT TO DECRYPT: ").encode()
    f = Fernet(key)
    decrypted: bytes = f.decrypt(encrypted)
    decrypted_message = decrypted.decode()
    print(Fore.RED + "DECRYPTED TEXT: " + Fore.LIGHTWHITE_EX + str(decrypted_message))


def file_encrypt():
    file_path = Path(input(Fore.CYAN + "FILE PATH: "))
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        original_file = file.read()
    encrypted = f.encrypt(original_file)
    print(Fore.LIGHTGREEN_EX + "File encrypted successfully!")
    destination_path = input(Fore.CYAN + "DESTINATION PATH: ")
    with open(destination_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def file_decrypt():
    file_path = Path(input(Fore.CYAN + "FILE PATH: "))
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        original_file = file.read()
    decrypted = f.decrypt(original_file)
    print(Fore.LIGHTGREEN_EX + "File decrypted successfully!")
    destination_path = input(Fore.CYAN + "DESTINATION PATH: ")
    with open(destination_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)


while True:
    input(Fore.RESET + "press " + Fore.RED + "ENTER " + Fore.RESET + "to continue")
    clear()
    print(Fore.CYAN + '''
    [0]: Exit program
    [1]: Encrypt string
    [2]: Decrypt string
    [3]: Encrypt file
    [4]: Decrypt file
    ''')
    choice = input(Fore.GREEN + "r5krypt:~$ " + Fore.RESET)
    if choice == "1":
        encrypt()
    elif choice == "2":
        decrypt()
    elif choice == "3":
        file_encrypt()
    elif choice == "4":
        file_decrypt()
    elif choice == "clear":
        clear()
    elif choice == "quit" or choice == "0":
        quit()
    else:
        print("That's not a valid option")
