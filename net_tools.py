#Imports

from colorama import *
from getpass import getpass
import os
os.system("clear")

def borrar():
	os.system("clear")

while True:
	print(Fore.CYAN + "/////////////")
	print("/" + Fore.RESET + "NET-TOOLKIT" + Fore.CYAN + "/")
	print("/////////////" + Fore.RESET)

	print(Fore.CYAN + "\nGitHub: " + Fore.RESET + "martinval9")
	print(Fore.YELLOW + "[?] " + Fore.RESET + "CTRL + Z para Salir\n")
	
	print("1: Conectarse a una red wifi\n")
	print("2: Levantar Interfaz de red\n")
	print("3: Desconectar Wifi\n")
	print("4: Escanear Wifi\n")
	print("5: Ver Redes Wifi disponibles\n")
	print("6: Registrar agente\n")
	print("7: IP\n")
	print("8: Grafico de red\n")
	print("9: Wireshark\n")
	print("10: Nmap\n")
	print("11: Nombre de la Tarjeta de red\n")
	print("12: Escanear tarjeta de red\n")
	print("13: Ejecutar comandos propios\n")
	print("14: Matar NetworkManager(peligroso)\n")
	print("15: Ping\n")
	print("16: Monitorear red\n")
	print("17: Ver información detallada del dispositivo\n")
	print("18: Test de Velocidad\n")

	while True:
		try:
			opcion = int(input("Opcion> "))
			while opcion < 1 or opcion > 18:
				opcion = int(input("Opcion> "))
			break

		except ValueError:
			pass
	
	if opcion == 1:
		while True:
			try:
				id_net = input("SSID de red: ")
				contraseña = getpass("Contraseña: ")
				os.system("sudo nmcli d wifi connect " + id_net + " password " + contraseña)
				break

			except ValueError:
				pass

	if opcion == 2:
		os.system("sudo ifconfig wlan0 up")

	if opcion == 3:
		os.system("sudo ifconfig wlan0 down")

	if opcion == 4:
		borrar()
		print("Espere...")
		os.system("connmanctl scan wifi")

	if opcion == 5:
		borrar()
		os.system("connmanctl services")

	if opcion == 6:
		borrar()
		os.system("connmanctl agent on")

	if opcion == 7:
		borrar()	
		os.system("ifconfig")

	if opcion == 8:
		borrar()
		os.system("sudo etherape")

	if opcion == 9:
		borrar()
		os.system("sudo wireshark")

	if opcion == 10:
		borrar()
		os.system("python3 .config/qtile/nmap.py")

	if opcion == 11:
		borrar()
		os.system("iwconfig")

	if opcion == 12:
		borrar()
		os.system("iwlist wlan0 scanning")

	if opcion == 13:
		borrar()
		print(Fore.YELLOW + "Puedes salir usando el comando exit" + Fore.RESET)
		os.system("sudo su")

	if opcion == 14:
		borrar()
		print("Espero que seas consiente de lo que estas haciendo")

		while True:
			try:
				seguro = input("Estas seguro[si/no]")
				break

			except ValueError:
				pass

		if seguro == "si":
			os.system("pkill nm-applet")
			os.system("pkill NetworkManager")
		else:
			exit

	if opcion == 15:
		while True:
			try:
				ping = input("Enlace de la pagina: ")
				os.system("ping " + ping)
				break
				
			except ValueError:
				pass

	if opcion == 16:
		os.system("network-top")

	if opcion == 17:
		os.system("clear")
		os.system("sudo server-info --show --system")

	if opcion == 18:
		os.system(".config/qtile/./fast")