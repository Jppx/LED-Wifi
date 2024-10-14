# LED-Wifi control using Python
Controlling Wifi Enabled LED Strip from Python

<img src='https://github.com/Jppx/LED-Wifi/blob/main/LED_WIFI_CONTROLLER2.jpg'/>

After buying a RGB LED Strip controller like the one shown, I discovered that it has a WIFI interface broadcasting an access point ('LEDnet003324007'), I connected and used nmap to discover an open port - <b>5577</b>. Since there wasnt any software included, a Google search turn up a number of experimental interfaces for this. But all of these were a little vague. So I wrote a  simple python script for controlling the LED Strip via the interface.
<br>When connected to the LEDnet003324007 access point, my machine was given an IP address of 10.10.123.4. Scanning this network using nmap I discovered the gateway address of the controller:  <b>10.10.123.3</b>, and its open port on 5577.<br>
The colour is set by the third parameter and is a 3 byte hex value (eg. RRGGBB) which each byte being the intensity of that colour.

Script use examples:<br>
  <b>python lednet.py 10.10.123.3 5577 FF0000</b>  - switch ON RED only<br>
  <b>python lednet.py 10.10.123.3 5577 00FF00</b>  - GREEN only<br>
  <b>python lednet.py 10.10.123.3 5577 0000FF</b>  - BLUE only<br>
  <b>python lednet.py 10.10.123.3 5577 FF00FF</b>  - PURPLE (Red plus Blue)<br>
  <b>python lednet.py 10.10.123.3 5577 000000</b>  - ALL LEDS OFF
  
