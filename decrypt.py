import sys
import string

def unrotate(times, amount, value, limit):
	temp = value
	the_amount = amount
	while times > 0:
		while the_amount > 0:	
			if temp == 0:
				temp = limit
				the_amount -= 1
			else:
				temp -= 1
				the_amount -= 1
		times -= 1
		the_amount = amount
	return temp

print 'Decrypting file...'

try:
	the_file = sys.argv[1]
except (RuntimeError, TypeError, NameError, ValueError):
	print "You must specify a file to encrypt"
	error = true

parts = the_file.split(".")

# find the type of file extension
extension = parts[len(parts)-1]

file_found = True

# try opening the file, if you can, put all the bytes into a large array
try:
	f = open(the_file, 'rb')
except Exception:
	file_found = False
	print "File with that name was not found"

bytes = []

if file_found:
	while 1:
		byte_s = f.read(1)
		if not byte_s:
			break
		byte = byte_s[0]
		bytes.append(byte)
	f.close()

# output file with whatever file extension we are dealing with.
f = open('decrypt_output.'+extension,'wb')

# decrypt
for x in bytes:
	value = unrotate(1, 2, ord(x), 255)
	f.write(chr(value))
f.close()
print 'File Decryption Complete'