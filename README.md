## Encryptor
Some files have personal and very valuable information for people. For example, a file can store bank card or account numbers, passwords or any other personal information. This program offers a very simple interface to encrypt the file. To do this, just remember the key to the file and keep it in mind.
### User interface



##### Encryption interface uses `encrypt`, `filename` and `key(password)` arguments.
```bash
python3 crypt.py encrypt file.txt 12345
```
###### After the encryption, a file will be created in .encrypt format so that you can distinguish it.
##### The decryptor works in a similar way.
```bash
python3 crypt.py decrypt file.txt.encrypt 12345
```
