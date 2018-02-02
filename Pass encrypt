import time
from six.moves import input
import hashlib
import base64
print("Simple pass encrypt. Twitter: @ibootdev")
time.sleep(1)
while True:
	option = int(eval(input('''Choose
	your option:
		--------------------
		|Simple text crypt |
		|Made By @ibootdev |
		| V 0.5            |
		| 1 : md5          |
		| -SHA ENCODERS-   |
		| 2: Sha256        |
		| 3: Sha512        |
		| 4: Sha1          |
		| 5: Sha224        |
		| 6: Sha384        |
		| -BASE ENCODERS-  |
		| 7: base16        |
		| 8: base32        |
		| 9: base64        |
		| 10: base85       |
		| -BASE DECODERS-  |
		| 11: base16       |
		| 12: base32       |
		| 13: base64       |
		| 14: base85       |
		| Hit CTR+C to stop|
		--------------------
		
		''')))
	string = input('String to crypt/decrypt: ').encode('utf-8')
	if option == 1:
		text = hashlib.md5(string).hexdigest()
	elif option == 2:
		text = hashlib.sha256(string).hexdigest()
	elif option == 3:
		text = hashlib.sha512(string).hexdigest()
	elif option == 4:
		text = hashlib.sha1(string).hexdigest()
	elif option == 5:
		text = hashlib.sha224(string).hexdigest()
	elif option == 6:
		text = hashlib.sha384(string).hexdigest()
	elif option == 7:
		text = base64.b16encode(string)
	elif option == 8:
		text = base64.b32encode(string)
	elif option == 9:
		text = base64.b64encode(string)
	elif option == 10:
		text = base64.b85encode(string)
	elif option == 11:
		text = base64.b16decode(string)
	elif option == 12:
		text = base64.b32decode(string)
	elif option == 13:
		text = base64.b64decode(string)
	elif option == 14:
		text = base64.b85decode(string)
	print("The text is: ", text)
