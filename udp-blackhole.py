#! /usr/bin/env python3

# Robby Stahl - beefnog@gmail.com
# 
# Sometimes you just need a datagram endpoint for testing...
#
# I assert no license; use this code as you see fit.

import argparse
import socket
from datetime import datetime as dt

parser = argparse.ArgumentParser(description = 'This script will listen for UDP datagrams, and dump them to stdout.')
parser.add_argument('--addr', required = True, help = 'IPv4 address to bind. Note: 0.0.0.0 = IPv4 any')
parser.add_argument('--port', required = True, help = 'UDP port to listen on.')
a = parser.parse_args()

# runtime arguments
h, p = a.addr, int(a.port)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((h, p))

count = 0
while True:
	dgram, source = s.recvfrom(1024)
	print(count, dt.now().time(), source, dgram)
	count += 1

