This is a file encryption program (both encrypt and decrypt files included). All you need to do is give it a filename as an argument and it will output an encrytped version of that file. 

This is intended to be used with Python 2.7 (Any other version is not gauranteed to work)

Example

<code>python encrypt.py test.txt</code>

will output a file called "encrypt_output.txt". In order to decrypt this file do this:

<code>python decrypt.py encrypt_output.txt</code>

And this will output a file called "decrypt_output.txt" with the original file contents intact, just change the file name back to what it was

UPDATE:

The above still works, but there is now an executable file in the "dist" folder. Run that and the rest is self explanatory. 