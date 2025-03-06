---
title: Component Selection
---
## Voltage Regulator
|Solution | Pros | Cons |
|------|------|------|
|![image](LM2575-3.3WU-TR.jpg) <br> LM2575-3.3WU-TR <br> $1.75/ea <br> [digikey](https://www.digikey.com/en/products/detail/microchip-technology/LM2575-3-3WU-TR/1027646)| \* Equivalent to regulator used in class, so more familiar and easier to use than other options <br> \* Inexpensive | \* Less experience gained |
|![image](ADP2370ACPZ-3.3-R7.JPG) <br> ADP2370ACPZ-3.3-R7 <br> $6.14/ea <br> [digikey](https://www.digikey.com/en/products/detail/analog-devices-inc/ADP2370ACPZ-3-3-R7/3232861)| \* Exposed pads would be a new and enriching soldering challenge | \* Expensive <br> \* Least current|
|![image](TPS5403DR.jpg) <br> TPS5403DR <br> $1.68/ea <br> [digikey](https://www.digikey.com/en/products/detail/texas-instruments/TPS5403DR/3671586)| \* Least expensive option <br> \* Most current | \* Unfamiliar|

### Selection
I chose the LM2575 because it's familiar from the Switching Power Supply lab. It's only a few cents more expensive than the TPS5403DR, and provides up to 1 Amp of current, which is far more than enough. 

## Microchip
### Requirements 
I will use an ESP32 microcontroller for this project because my subsystem requires the use of a wifi module. 
### ESP32
|Info  | Answer |
|-----|-----|
|Model |ESP32-S3-WROOM-1-N4|
|Datasheet|[link](documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf)|
|Vendor Link|[Link](https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-WROOM-1-N4/16162639)|
|Unit Cost|$5.06|
|Maximum Current|500 mA|
|Supply Voltage |3.0-3.6V|

### Pinout
![image](ESP32pinout.png)
### Pin Allocation
|Pin number | Name | Use|
|-----|-----|-----|
|1| GND |Ground|
|2| 3v3 |Power In|
|3| EN |reset button & RC circuit to stabilize input power|
|4| IO4 |Debugging LED|
|5|IO5 |Debugging LED|
|6|IO6 |Debugging Pushbutton|
|7|IO7 |Debugging Header|
|8|IO15 |Debugging Header|
|9|IO16 |Debugging Header|
|10|IO17 |Debugging Header|
|11|IO18 |Debugging Header|
|12|IO8 |Debugging Header|
|13|IO19 |USB_D-|
|14|IO20 |USB_D+|
|15|IO3 |Debugging Header|
|16|IO46 |Debugging Header|
|17|IO9 |Debugging Header|
|18|IO10 |Debugging Header|
|19|IO11 |Debugging Header|
|20|IO12 |Debugging Header|
|21|IO13 |Debugging Header|
|22|IO14 |Debugging Header|
|23|IO21 |Debugging Header|
|24|IO47 |Debugging Header|
|25|IO48 |Debugging Header|
|26|IO45 |Debugging Header|
|27|IO0 |Debugging Header|
|28|IO35 |Debugging Header|
|29|IO36 |Debugging Header|
|30|IO37 |Debugging Header|
|31|IO38 |Debugging Header|
|32|IO39 |Debugging Header|
|33|IO40 |Debugging Header|
|34|IO41 |Debugging Header|
|35|IO42 |Debugging Header|
|36|RXD0 |Receiving Data from Upstream|
|37|TXD0 |Transmitting Data Downstream|
|38|IO2 |Debugging Header|
|39|IO1 |Debugging Header|
|40|GND |Ground|

## Power Budget
![Power Budget](powerBudget.png)

This page is up-to-date as of February 28, 2025 and will continue to be updated throughout the semester. 