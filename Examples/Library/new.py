from lib.mBot import *
from time import sleep
if __name__ == '__main__':
	bot = mBot()
	bot.startWithSerial("COM3")
	while(1):
             bot.doRGBLedOnBoard(1,0,100,0)
	