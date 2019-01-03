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



class Rmi():
	#pola
	src_file = None
	dest_name = None

	#funkcje
	def zmienne(self):
		self.src_file = input("Wprowadz nazwe pliku zrodlowego: ")
		self.dest_name = input("Wprowadz nazwe pliku docelowego: ")

	def wysylanie(self):
		self.zmienne()
		filesource = open(self.src_file, 'rb').read()
		#wylacznie zaladowanie kodu na serwer
		flame.sendfile(dest_name, filesource)

	def moduly(self):
		self.zmienne()
		modulesource = open(self.src_file).read() 
		#wyslanie kodu JAKO MODUL (import):
		flame.sendmodule(self.dest_name, modulesource)
		#uruchomienie wyslanego kodu z podanymi argumentami
		result = flame.module(self.dest_name).doSomething("hello", 42)
		print("\nresult from uploaded module:", result)

	def poprawnosc(self):
		self.zmienne()
		modulesource = open(self.src_file).read() 
		root = flame.evaluate(modulesource)
		print("result=", root)
		#tutaj jest miejsce na napisanie testu, czy kod z pliku faktycznie oblicza oczekiwana wartosc, ta funkcja sprawdza kod bez definicji czyli macie napisac cos w kodzie i tyle

file = Rmi()
# Informacje na serwerze gdy polaczy sie z klientem
flame.builtin("print")("Serwer polaczyl sie z klientem")


def main():
	wybor = 0;
	print ("Witaj programie klienta")
	while wybor != 1 and wybor !=2 and wybor !=3 and wybor != 5:
		print ("Aby uruchomic funkcje klienta wybierz jedna z wybranych opcji: ")
		
		print ("1 - Wysylanie pliku do serwera")
		print ("2 - Sprawdzenie poprawnosci kodu i kompilacja  ")
		print ("3 - Wykonanie programu")
		wybor = int(input("Podaj numer: "))

	#wyslanie pliku na serwer
	if wybor == 1:
		file.wysylanie()

	# wysylanie kodu jako modul na serwer	
	if wybor == 2:
		file.moduly()

	#sprawdzenie poprawnosci 
	if wybor == 3:	
		file.poprawnosc()
while True:
	main()
	

