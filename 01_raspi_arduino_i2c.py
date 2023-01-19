#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smbus
import time

if __name__ == '__main__':
	bus = smbus.SMBus(1)
	address = 0x04

	try:
		while True:

			bus.write_byte(address,ord('R'))
			msg = chr(bus.read_byte(address))
			print(msg)
			time.sleep(1)

	except KeyboardInterrupt:
		print("\nCtl+C")
	except Exception as e:
		print(str(e))
	finally:
		print("\nexit program")

