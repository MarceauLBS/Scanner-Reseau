import socket
import os
import re
import subprocess
import datetime

tmps = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def menu():
  print('[+] Choix')
  print('1 - Scan Réseau')
  print('2 - Scan IP')
  print('3 - Exit')
  choix = input()
  choixmenu = choix
  f = open('sauvegarde.txt','a')
  if choixmenu == "1":
    f.write(str(tmps) + '\n')
    f.write(str(choixmenu) + '\n')
    print('[+] Entrer une adresse IP')
    ip = str(input())
    f.write(ip + '\n')
    print(" ")
    ip = ip.split('.')
    ip = ip[0] + '.' + ip[1] + '.' + ip[2] + '.'
    print("Quel interval d'ip voulez-vous scanner ?")
    interval = int(input())
    print(" ")
    f.write("interval : " + str(interval) + '\n')
    if interval > 255:
      print("Erreur, interval trop grand")
      exit(1)
    for i in range(1, interval):
      ip2 = ip + str(i)
      if portscan(80, ip2):
        hosts.append(ip2)
        print('[+] IP Connectée : ' + ip2)
    print(" ")
    print('[+] IP Connectées : ' + str(hosts))
    print(" ")
    print("--------------------")
    print(" ")
    f.write(str(hosts) + "\n")
    menu()
  elif choixmenu == "2":
    f.write(str(tmps) + '\n')
    f.write(str(choixmenu) + '\n')
    print('[+] Entrer une adresse IP')
    ip = str(input())
    f.write(ip + '\n')
    print('Quel port voulez-vous scanner ?')
    port = int(input())
    f.write(str(port) + '\n')
    print(" ")
    print("--------------------")
    print(" ")
    if portscan(port, ip):
      print('Le port', port, "est ouvert sur l'ip", ip)
    else:
      print('Le port', port, "est fermé sur l'ip", ip, " ou l'ip n'est pas connectée")
    f.write(str(portscan(port, ip)) + '\n')
    print(" ")
    print("--------------------")
    print(" ")
    menu()
  elif choixmenu == "3":
    print(" ")
    print("Au Revoir !")
    f.write(" " + '\n')
    f.write("--------------------" + '\n')
    f.write(" " + '\n')
    exit(1)
  else:
    menu()


hosts = []

def portscan(port, ip):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(3)
  if sock.connect_ex((ip, port)) :
    return False
    exit(1)
  else :
      return True


menu()
