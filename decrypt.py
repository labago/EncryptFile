import sys
import string

print 'Decrypting file...'

try:
	the_file = sys.argv[1]
except NameError:
	print "You must specify a file to encrypt"
	error = true

parts = the_file.split(".")

# find the type of file extension
extension = parts[len(parts)-1]

bytes = []

# try opening the file, if you can, put all the bytes into a large array
try:
	with open(the_file, 'rb') as f:
		while 1:
			byte_s = f.read(1)
			if not byte_s:
				break
			byte = byte_s[0]
			bytes.append(byte)
except NameError:
	print "File with that name was not found"

# output file with whatever file extension we are dealing with.
f = open('decrypt_output.'+extension,'wb')

# decrypt
for x in bytes:
	value = ord(x)
	if value == 0:
		f.write(chr(255))
	else:
		f.write(chr(value-1))
f.close()
print 'File Decryption Complete'