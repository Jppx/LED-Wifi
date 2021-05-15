import socket
import time
import sys

def doLEDSend():
    if (len(sys.argv) < 4):
        print ('Usage:  python lednet.py ipaddress port RRGGBB [HEX]')
        print ('(eg: python lednet.py 10.14.123.7 5577 ''FF00FF'')')
        print ('')   
        exit
    else:
        try:
            olist = [0x31,0x00,0x00,0x00,0x00,0x00,0x00,0x00] #message template
            params = sys.argv[1:] #extract the params (address, port, colorHex)
            address = str(params[0])
            port = int(params[1]) #port must be an integer
            hexcolor = str(params[2]) #extract hex color value (RRGGBB)
            red = '0x' + hexcolor[0:2]
            green = '0x' + hexcolor[2:4]
            blue = '0x' + hexcolor[4:6]
            olist[1] = int(red,16)
            olist[2] = int(blue,16)
            olist[3] = int(green,16)  
            print ('connecting to: ' + str(address) + ':' + str(port) + '  RED:' + str(red) + ' GREEN:' +  str(green) + ' BLUE:' + str(blue))
        except Exception as e:
            print ('Error processing arguments - ' + e.message)
            print ('')
            
        else:
            client_socket = socket.socket()  # instantiate the tcp socket
            try:            
                client_socket.connect((address, port))  # connect to the LED server 
                client_socket.send(bytearray(olist))  # send olist byte array
            except Exception as e:
                 print ('Error sending message - ' + e.message)
                 print ('')
            finally:
                client_socket.close()  # close the connection
                
                
    
if __name__ == "__main__":
    doLEDSend()
     


