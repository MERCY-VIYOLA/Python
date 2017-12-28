'''Get IP and TCP info on https://www.ietf.org/rfc/rfc768.txt'''
import struct
import socket
import binascii #makes strings more readable 
import os

def main():
    os.system('cls')
    rawSocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    #rawSocket.bind(('10.0.0.3',0)) <<-- since its a raw socket, its not bound to any specific port

    receivedPacket = rawSocket.recv(2048)
    
#IP Header... 
    ipHeader=receivedPacket[0:20]
    ipHdr=struct.unpack("!12s4s4s",ipHeader)
    sourceIP = socket.inet_ntoa(ipHdr[0])#ntoa -->> Network to Ascii
    destinationIP=socket.inet_ntoa(ipHdr[2])
#Padding only happens when options happens and padding does not always happen
    print "Source IP: " +sourceIP
    print "Destination IP: "+destinationIP


#TCP Header...
    tcpHeader=receivedPacket[34:54]
    tcpHdr=struct.unpack("!2s2s16s",tcpHeader)
    sourcePort=socket.inet_ntoa(tcpHdr[0])
    destinationPort=socket.inet_ntoa(tcpHdr[1])
    print "Source Port: " + sourcePort
    print "Destination Port: " + destinationPort

main()
