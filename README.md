This is a file encryption program (both encrypt and decrypt files included). All you need to do is give it a filename as an argument and it will output an encrytped version of that file. 

This is intended to be used with Python 2.7 (Any other version is not gauranteed to work)

Example

"python encrypt.py test.txt"

will output a file called "encrypt_output.txt". In order to decrypt this file do this:

"python decrypt.py encrypt_output.txt"

And this will output a file called "decrypt_output.txt" with the original file contents intact, just change the file name back to what it was