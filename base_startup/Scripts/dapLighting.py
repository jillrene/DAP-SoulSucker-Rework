from dmxpy import DmxPy as DMX
import time
import socket
import sys
from argparse import ArgumentParser

localIP = "10.12.23.17"
localPort = 4200
bufferSize = 1024
comPort = 'COM4'


def My_python_method(kwargs):
 
    disp_str = 'key: {} | value: {} | type: {}'
    for each_key, each_value in kwargs.items():
        formatted_str = disp_str.format(each_key, each_value, type(each_value))
        if each_key == 'in2':
            comPort = each_value
            print('updated comPort ' + comPort)
        if each_key == 'in':
            localIP = each_value
            print('updated ip ' + localIP)
        print(formatted_str)
 
    # keep the shell open so we can debug
    #time.sleep(int(kwargs.get('delay')))
 
# execution order matters -this puppy has to be at the bottom as our functions are defined above
if __name__ == '__main__':
    parser = ArgumentParser(description='A simple argument input example')
    parser.add_argument("-i", "--input", dest="in", help="an input string", required=True)
    parser.add_argument("-i2", "--input2", dest="in2", help="an input string", required=True)
    parser.add_argument("-d", "--delay", dest="delay", help="how long our terminal stays up", required=False, default=10)
     
    args = parser.parse_args()
    My_python_method(vars(args))
    pass

dmx = DMX.DmxPy(comPort)
#message to send back to the client
msgFromServer = "Hello UDP Client\n"

bytesToSend = str.encode(msgFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")


#blackout
def run0():
    dmx.blackout()
    dmx.render()
    print('0')
    return

#outside light on, inside lights off
'''
def run1():
    dmx.set_channel(1, 50)    #outside
    dmx.set_channel(2, 0)  #master
    dmx.set_channel(3, 0)    #red
    dmx.set_channel(4, 0)    #green
    dmx.set_channel(5, 0)    #blue
    dmx.set_channel(6, 0)    #amber
    dmx.set_channel(7, 0)    #white
    dmx.set_channel(8, 0)  #UV
    dmx.render()
    print('1')
    return
    '''

def run1():
    dmx.set_channel(1, 36)  #outside red
    dmx.set_channel(2, 17)   #outside green
    dmx.set_channel(3, 5)   #outside blue
    dmx.set_channel(4, 17)   #outside white
    dmx.set_channel(5, 0)   #inside master
    dmx.set_channel(6, 0)   #inside red
    dmx.set_channel(7, 0)   #inside green
    dmx.set_channel(8, 0)   #inside blue
    dmx.set_channel(9, 0)   #inside amber
    dmx.set_channel(10, 0)  #inside cool white
    dmx.set_channel(11, 0)  #inside lime
    dmx.set_channel(12, 0)  #inside UV
    dmx.render()
    print('1')
    return


#outside light off, inside light soft white
'''
def run2():
    dmx.set_channel(1, 0)    #outside
    dmx.set_channel(2, 100)  #master
    dmx.set_channel(3, 0)    #red
    dmx.set_channel(4, 0)    #green
    dmx.set_channel(5, 0)    #blue
    dmx.set_channel(6, 255)    #amber
    dmx.set_channel(7, 255)    #white
    dmx.set_channel(8, 0)  #UV
    dmx.render()
    print('2')
    return '''

def run2():
    dmx.set_channel(1, 0)  #outside red
    dmx.set_channel(2, 0)   #outside green
    dmx.set_channel(3, 0)   #outside blue
    dmx.set_channel(4, 0)   #outside white
    dmx.set_channel(5, 100)   #inside master
    dmx.set_channel(6, 0)   #inside red
    dmx.set_channel(7, 0)   #inside green
    dmx.set_channel(8, 0)   #inside blue
    dmx.set_channel(9, 255)   #inside amber
    dmx.set_channel(10, 255)  #inside cool white
    dmx.set_channel(11, 0)  #inside lime
    dmx.set_channel(12, 0)  #inside UV
    print('2')
    return


#outside light off, inside light UV full
'''
def run3():
    dmx.set_channel(1, 0)    #outside
    dmx.set_channel(2, 255)  #master
    dmx.set_channel(3, 0)    #red
    dmx.set_channel(4, 0)    #green
    dmx.set_channel(5, 0)    #blue
    dmx.set_channel(6, 0)    #amber
    dmx.set_channel(7, 0)    #white
    dmx.set_channel(8, 255)  #UV
    dmx.render()
    print('3')
    return '''

def run3():
    dmx.set_channel(1, 0)  #outside red
    dmx.set_channel(2, 0)   #outside green
    dmx.set_channel(3, 0)   #outside blue
    dmx.set_channel(4, 0)   #outside white
    dmx.set_channel(5, 255)   #inside master
    dmx.set_channel(6, 0)   #inside red
    dmx.set_channel(7, 0)   #inside green
    dmx.set_channel(8, 0)   #inside blue
    dmx.set_channel(9, 0)   #inside amber
    dmx.set_channel(10, 0)  #inside cool white
    dmx.set_channel(11, 0)  #inside lime
    dmx.set_channel(12, 255)  #inside UV
    dmx.render()
    print('3')
    return

'''
def run4():
    dmx.set_channel(1, 0)    #outside
    dmx.set_channel(2, 255)  #master
    dmx.set_channel(3, 0)    #red
    dmx.set_channel(4, 100)    #green
    dmx.set_channel(5, 255)    #blue
    dmx.set_channel(6, 0)    #amber
    dmx.set_channel(7, 0)    #white
    dmx.set_channel(8, 255)  #UV
    dmx.render()
    print('4')
    return
    '''

def run4():
    dmx.set_channel(1, 0)  #outside red
    dmx.set_channel(2, 0)   #outside green
    dmx.set_channel(3, 0)   #outside blue
    dmx.set_channel(4, 0)   #outside white
    dmx.set_channel(5, 255)   #inside master
    dmx.set_channel(6, 0)   #inside red
    dmx.set_channel(7, 100)   #inside green
    dmx.set_channel(8, 255)   #inside blue
    dmx.set_channel(9, 0)   #inside amber
    dmx.set_channel(10, 0)  #inside cool white
    dmx.set_channel(11, 0)  #inside lime
    dmx.set_channel(12, 255)  #inside UV
    dmx.render()
    print('4')
    return

'''
def run5():
    dmx.set_channel(1, 0)    #outside
    dmx.set_channel(2, 255)  #master
    dmx.set_channel(3, 255)    #red
    dmx.set_channel(4, 0)    #green
    dmx.set_channel(5, 255)    #blue
    dmx.set_channel(6, 0)    #amber
    dmx.set_channel(7, 0)    #white
    dmx.set_channel(8, 0)  #UV
    dmx.render()
    print('5')
    return '''

def run5():
    dmx.set_channel(1, 0)  #outside red
    dmx.set_channel(2, 0)   #outside green
    dmx.set_channel(3, 0)   #outside blue
    dmx.set_channel(4, 0)   #outside white
    dmx.set_channel(5, 255)   #inside master
    dmx.set_channel(6, 255)   #inside red
    dmx.set_channel(7, 0)   #inside green
    dmx.set_channel(8, 255)   #inside blue
    dmx.set_channel(9, 0)   #inside amber
    dmx.set_channel(10, 0)  #inside cool white
    dmx.set_channel(11, 0)  #inside lime
    dmx.set_channel(12, 0)  #inside UV
    dmx.render()
    print('5')
    return

#listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize) #receive address and message
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    lightVal = int(format(message.decode()))
    #print(type(lightVal))

    if lightVal == 0:
        run0()
        print('0')
    elif lightVal == 1:
        run1()
        print('1')
    elif lightVal == 2:
        run2()
        print('2')
    elif lightVal == 3:
        run3()
        print('3')
    elif lightVal == 4:
        run4()
        print('4')
    elif lightVal == 5:
        run5()
        print('5')

    #print(type(lightVal))
    bytesToSend = message
    #sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)

#input('Press ENTER to exit')
