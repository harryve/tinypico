from machine import SoftSPI, Pin
import tinypico as TinyPICO
from dotstar import DotStar
import time, random, micropython, gc

spi = SoftSPI(sck=Pin(TinyPICO.DOTSTAR_CLK), mosi=Pin(TinyPICO.DOTSTAR_DATA), miso=Pin(TinyPICO.SPI_MISO))
dotstar = DotStar(spi, 1, brightness=0.1) # Just one DotStar, 10% brightness
TinyPICO.set_dotstar_power(True)

print("\nHello from TinyPICO!")
print("--------------------\n")

# Show some info on boot 
print("Battery Voltage is {}V".format(TinyPICO.get_battery_voltage()))
print("Battery Charge State is {}\n".format(TinyPICO.get_battery_charging()))

while True:
    dotstar[0] = (50, 0, 0, 1)
    time.sleep_ms(50)

    dotstar[0] = (0, 0, 0, 10)
    time.sleep_ms(250)

    dotstar[0] = (0, 50, 0, 1)
    time.sleep_ms(50)

    dotstar[0] = (0, 0, 0, 10)
    time.sleep_ms(250)

    dotstar[0] = (0, 0, 50, 1)
    time.sleep_ms(50)

    dotstar[0] = (0, 0, 0, 10)
    time.sleep_ms(250)
