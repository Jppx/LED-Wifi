# LED-Wifi
Controlling Wifi Enabled LED Strip from Python

<img src='https://github.com/Jppx/LED-Wifi/blob/main/LED_WIFI_CONTROLLER2.jpg'/>

After buying at RGB LED Strip controller like the one shown, I discovered that it has a WIFI interface broadcasting an access point ('LEDnet003324007'), I connected and used nmap to discover an open port - 5577. Since there wasnt any software included, a Google search turn up a number of experimental interfaces for this. But all of these were a little vague. So I wrote a  simple python script for controlling the LED Strip via the interface.
When connected to the LEDnet003324007 access point, my machine was given an IP address of 10.10.123.4. Scanning this network using nmap discovered the gateway address of of the controller:  10.10.123.3. 

Script use examples:
  python lednet.py 10.10.123.3 5577 FF0000  - RED
  python lednet.py 10.10.123.3 5577 00FF00  - GREEN
  python lednet.py 10.10.123.3 5577 0000FF  - BLUE
  python lednet.py 10.10.123.3 5577 000000  - ALL LEDS OFF
  
