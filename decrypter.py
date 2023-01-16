import os
import pyaes
import sys

if len(sys.argv) <= 2:
    print("Modo de uso python decrypter.py FILENAME NEWFILENAME")
else:
    ## open file
    file_name = (sys.argv[1])
    file = open(file_name, 'rb')
    file_data = file.read()
    file.close()

    ## key
    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    ## remove file
    os.remove(file_name)

    ## create new file
    new_file = (sys.argv[2])
    new_file = open(f'{new_file}', 'wb')
    new_file.write(decrypt_data)
    new_file.close()
