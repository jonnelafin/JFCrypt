


print("JFCrypt by elias eskelinen aka 'Jonnelafin'")

import numpy as np

def encrypt(inp = [], password = 0):
	key1 = 141650939 #Prime
	key2 = int(key1) * int(password) #Generate a key from the password
	out = []
	iterator = 0
	print("------Encrypt------")
	for x in inp:
		for i in x:
			plc = ord(i)+(iterator)
			final = np.multiply(plc, key2)
			out.append(final)
			iterator = iterator + 1
	return(out)
def decrypt(lisd = [], password = 0):
	key1 = 141650939
	key2 = int(key1) * int(password)
	out = []
	iterator = 0
	print("------Decrypt------")
	comment = False
	for i in lisd:
		if i[0] == "#":
			print("Comment: " + i)
		else:
			num = (int(i) / (key2))-(iterator)
			try:
				out.append(chr(int(num)))
			except:
				print("Problem with " + str(num))
				out.append("[Incorrect encryption: " + str(num)+"]")
			iterator = iterator + 1
	return(out)
choice = input("(E)ncrypt or (D)ecrypt? ")
if(choice == "E"):
	inp = input("Input, leave empty for reading a file: ")
	if inp == "":
		try:
			with open("input.txt", 'r') as f2:
				inp = []
				for x in f2:
					try:
						inp.append(x)
					except:
						print("Problem with "+str(x))
		except Exception as e:
			print("Failed: ")
			print(e)
	pswd = input("Password (Must be a number): ")
	lis = encrypt(inp, pswd)
	with open('encrypted.txt', 'w+') as f:
		f.truncate(0)
		f.write("#Encrypted using JFCrypt\n")
		for line in lis:
			f.write(str(line)+"\n")
	print("Done")
elif(choice == "D"):
	inputt = " "
	lis = []
	while inputt != "":
		inputt = input("Don't type anything and press enter to finish: ")
		try:
			lis.append(int(inputt))
		except:
			print("Not an integer")
	if(len(lis) == 0):
		print("List empty, trying to read from file...")
		try:
			with open("encrypted.txt", 'r') as f:
    				lis = f.readlines()
		except:
			print("Failed")
	pswd = input("Password (Must be a number): ")
	out = decrypt(lis, pswd)
	with open('decrypted.txt', 'w+') as f:
		f.truncate(0)
		for s in out:
			f.write(s)
	print("Done")
print("Exit")
















