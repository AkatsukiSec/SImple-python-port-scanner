import socket
import argparse

#args
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip", help="IP")
parser.add_argument("-p", "--port", help="Port - comma separated values ex. 22,80,443", required=False)
parser.add_argument("-r", "--range", help="Specify a port range ex 1 1000", required=False, nargs=2)
args = parser.parse_args()

targetIp = args.ip

targetPort = args.port

if targetPort != None:
    targetPort = targetPort.split(",")
 
targetRange = 0
targetRange = args.range

def scanner(targetPort):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
		
    if s.connect_ex((targetIp,int(targetPort))):
        pass
    else:
        try:
            banner = s.recv(1024)
            print(f"Port {targetPort} is open {banner}")
        except: 
            print(f"Port {targetPort} is open")
    s.close()

if targetRange == None:
    x = 0 
    for line in targetPort:
        scanner(targetPort[x])
        x += 1
else:
    for i in range(int(targetRange[0]), int(targetRange[1]) + 1):
        targetPort = i
        scanner(targetPort)
