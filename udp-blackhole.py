#! /usr/bin/env python3

# Robby Stahl - beefnog@gmail.com
# 
# Sometimes you just need a datagram endpoint for testing...
#
# I assert no license; use this code as you see fit.

import socket
from datetime import datetime as dt

# tunables
bind_host = "0.0.0.0" # 0.0.0.0 -> ANY IPv4
bind_port = 54321

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((bind_host, bind_port))

count = 0
while True:
	dgram, source = s.recvfrom(1024)
	print(count, dt.now().time(), source, dgram)
	count += 1

