# krkrypter
## Introduction
This is a string and file encrypter and decrypter. Works with **SHA-256** algorithm by creating a **ultra-secure key**.
## Quick guide              
As easy as it gets, make sure the string or file is decrypted with the same program that it was encrypted.    
## Requirements
**Python version:** 3.6 or greater                                   
**Libraries:** base64, pathlib, colorama, cryptography, and pyfiglet.             
## More information:
If you want the maximum security, change the salt at line 21.            
We recommend generating one yourself using os.           
Type this in python3 console:
```python
>>> import os
>>> os.urandom(16)
b"\xe0\x0fO\xc0;mf\x03\xb5<6'\xe0\xa6+6"
```
Replace salt in the script with the output of **os.urandom(16)**.           
In this case it will be:  ```salt: bytes = b"\xe0\x0fO\xc0;mf\x03\xb5<6'\xe0\xa6+6"```                      
Remember to change the salt in your _mate's file also_. In case you are decrypting in another computer
## Problems
You can report problems [here](https://github.com/Kik449/schat/issues)!                      
Don't be afraid of asking questions, if it is posible, we will be answering them.
## Authors 
**ru55o**: added 32 characters key generation and SHA-256 encryption string encryption and decryption, later file encryption and decryption.
