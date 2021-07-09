from colorama import *
import os

os.system("clear")

while True:
    print(Fore.CYAN + "//////")
    print("/" + Fore.RESET + "NMAP" + Fore.CYAN + "/")
    print("//////\n" + Fore.RESET)

    class Nmap():
        nmap1 = "1: Escaneo de puertos\n\n"
        nmap2 = "2: Escaneo de Sistema Operativo\n\n"
        nmap3 = "3: Escaneo de servicios\n\n"
        nmap4 = "4: Escaneo de Paginas Web\n\n"
        nmap5 = "5: Escaneo de puertos silencioso\n"

    print(Nmap.nmap1 +  Nmap.nmap2 + Nmap.nmap3 + Nmap.nmap4 + Nmap.nmap5)
    print("6: Salir\n")

    opcion = int(input("Opcion> "))
    while opcion < 1 or opcion > 7 or opcion == "":
        print("Numero Incorrecto,por favor vuelva a intentarlo.")
        opcion = int(input("Opcion> "))

    if opcion == 1:
        ip_o_enlace = input("Direccion ip o enlace: ")

        os.system("sudo nmap " + ip_o_enlace + "/24")

    if opcion == 2:
        ip_o_enlace_os = input("Direccion ip o enlace: ")

        os.system("sudo nmap -O " + ip_o_enlace_os)

    if opcion == 3:
        ip_o_enlace_ser = input("Direccion ip o enlace: ")

        os.system("sudo nmap -v " + ip_o_enlace_ser)

    if opcion == 4:
        enlace_de_la_pagina = input("Enlace de la pagina: ")

        os.system("sudo nmap -sV " + enlace_de_la_pagina)

    if opcion == 5:
        ip_o_enlace_si = input("Direccion ip o enlace: ")

        os.system("sudo nmap -p 1-1000 " + ip_o_enlace_si)

    if opcion == 6:
        os.system("clear")
        break