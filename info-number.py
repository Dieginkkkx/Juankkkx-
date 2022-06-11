import phonenumbers
import os
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier



BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

os.system ("clear")

print(RED+"██╗███╗░░██║███████╗░█████╗░░░░░░░░███╗░░██║██║░░██╗████╗░░████║")
print("██║████╗░██║██╔════╝██╔══██╗░░░░░░░████╗░██║██║░░██║██╔██░██░██║")   
print("██║██╔██╗██║█████╗░░██║░░██║█████╗░██╔██╗██║██╚░░██║██║░███░░██║")
print("██║██║╚████║██╔══╝░░██║░░██║╚════╝░██║╚████║██╚══██║██║░░░░░░██║")
print("██║██║░╚███║██║░░░░░╚█████╔╝░░░░░░░██║░╚███║███████║██╝░░░░░░██║")
print("╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░░░░░░░░╚═╝░░╚══╝╚══════╝╚══════════╝\n ") 


 
print("--------------------------------------")
print("Autor : Juankkkx")
print("-------------------------------------- \n ")

print(RED+"Digite el numero de teléfono junto al prefijo ejemplo, +92xxxxxxxxxx \n ")
phone = input  ("Digite el numero de telefono: "+MAGENTA)
print("    ")

phone_number = phonenumbers.parse(phone)
zone = timezone.time_zones_for_number(phone_number)
geo = geocoder.description_for_number(phone_number, 'es')
carrier = carrier.name_for_number(phone_number, 'es')

print("[!] Country Code ")
print(phone_number)
print(" ")
print("[!] Country ")
print(zone)
print(" ")
print("[!] Time zone ")
print(geo)
print(" ")
print("[!] Carrier  ")
print(carrier)
print(" ")




