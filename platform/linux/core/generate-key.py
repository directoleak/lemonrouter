import os, shutil

#start in sudo
def generateKey():
	try:
		with open("/etc/tor/torrc") as torrc:
			if "LemonServiceInstalled" in torrc.read():
				print("Config already intalled in torrc file")
				removeKey()
			else:
				filetorrc = open("/etc/tor/torrc", "a")
				filetorrc.write("\n################ This section is for Lemon Service #####################")
				filetorrc.write("""\n\n## Once you have configured a lemon service, you can look at the
## contents of the file "var/lib/tor/lemon-service" for the address
## to tell people.
##
## HiddenServicePort 80 says to redirect requests on port 1009 to the
## address myadress.onion""")
				filetorrc.write("\n\nHiddenServiceDir /var/lib/tor/lemon-service/")
				filetorrc.write("\nHiddenServicePort 80 127.0.0.1:1009")
				filetorrc.write("\n\n#LemonServiceInstalled do not delete this line")
				filetorrc.close()
				removeKey()
	except:
		print("file torrc not found")

def removeKey():
	shutil.rmtree('/var/lib/tor/lemon-service/')
	os.system('sudo service tor stop')
	os.system('sudo service tor start')
	print("new key generated")

generateKey()