import os, sys, string, random


def encrypt(file_name, key):
    ask = input(
        "Are you sure you want to encrypt the file? As a result, the original version will be overwritten.\n Press Y/y to continue... ")

    while ask.lower() != "y":
        ask = input("Press Y/y to continue... ")

    file = open(file_name, 'rb')
    bytes_file = file.read()
    file.close()

    hex_file = bytes_file.hex()
    int_file = int(hex_file, 16)

    hex_key = key.encode('utf-8').hex()
    int_key = int(hex_key, 16)

    int_encrypt = int_file * int_key
    hex_encrypt = hex(int_encrypt)
    
    encrypt_file = open(file_name + '.encrypt', 'w')
    encrypt_file.write(hex_encrypt)
    encrypt_file.close()

    os.remove(file_name)


def decrypt(encrypt_file_name, key):
    encrypt_file = open(encrypt_file_name, 'r')
    encrypt_text = encrypt_file.read()

    int_encrypt = int(encrypt_text, 16)

    hex_key = key.encode('utf-8').hex()
    int_key = int(hex_key, 16)

    int_out = int_encrypt // int_key
    hex_out = hex(int_out)[2:] if hex(int_out).find('0x') == 0 else hex(int_out)

    bytes_out = bytes.fromhex(hex_out)

    file = open(encrypt_file_name.replace('.encrypt', '') if encrypt_file_name.rfind('.encrypt') == len(
        encrypt_file_name) - len('.encrypt') else encrypt_file_name, 'wb')
    file.write(bytes_out)
    file.close()


def help_description():
    print("""""")


def main():
    if len(sys.argv) < 2:
        print("The startup must contain more arguments.")
        exit()

    command = sys.argv[1]

    if command == "encrypt" or command == "decrypt":
        if len(sys.argv) < 3:
            print("For encrypting or decrypting file, program must contain more arguments.")
            exit()
        if command == "encrypt" and len(sys.argv) < 4:
            print("Yet program must also contain a key(password) for encryption.")
            exit()
        if command == "decrypt" and len(sys.argv) < 4:
            print("Yet program must also contain a key(password) for decryption.")
            exit()

    if command == "encrypt": encrypt(sys.argv[2], sys.argv[3])
    if command == "decrypt": decrypt(sys.argv[2], sys.argv[3])
    if command == "help": help_description()


if __name__ == "__main__":
    main()