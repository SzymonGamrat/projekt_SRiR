from __future__ import print_function
import sys

import Pyro4.utils.flame


if sys.version_info < (3, 0):
    input = raw_input

Pyro4.config.SERIALIZER = "pickle"  # flame requires pickle serializer

print("Start a Pyro Flame server somewhere.")
location = input("what is the location of the flame server, hostname:portnumber? ")
print()

# connect!
flame = Pyro4.utils.flame.connect(location)

# basic stuff
socketmodule = flame.module("socket")
osmodule = flame.module("os")
print("remote host name=", socketmodule.gethostname())
print("remote server current directory=", osmodule.getcwd())



# Informacje na serwerze gdy polaczy sie z klientem
flame.builtin("print")("Serwer polaczyl sie z klientem")
def main():
	wybor = 0;
	print ("Witaj programie klienta")
	while wybor != 1 and wybor !=2 and wybor !=3:
		print ("Aby uruchomic funkcje klienta wybierz jedna z wybranych opcji: ")
		print ("1 - Wysylanie pliku do serwera")
		print ("2 - Sprawdzenie poprawnosci kodu i kompilacja  ")
		print ("3 - Wykonanie programu")
		wybor = int(input("Podaj numer: "))
	#wyslanie pliku na serwer
	if wybor == 1:

		src_file = input("Wprowadz nazwe pliku zrodlowego: ")
		dest_name = input("Wprowadz nazwe pliku docelowego: ")
		filesource = open(src_file, 'rb').read()
		flame.sendfile(dest_name, filesource)

	#sprawdzenie poprawnosci 
	if wybor == 2:
		root = flame.evaluate(modulesource)
		print("calculated square root=", root)	

	# upload a module source and call a function, on the server, in this new module
	if wybor == 3:
		
		modulesource = open(src_file).read() 
		flame.sendmodule(dest_name, modulesource)
		result = flame.module(dest_name).doSomething("hello", 42)
		print("\nresult from uploaded module:", result)
while True:
	main()
	print("wracamy? y/n")
	if input() == "y":
		main()






