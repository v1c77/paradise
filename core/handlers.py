#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 30/07/2017

from time import sleep
from gpiozero import Button, LED


if __name__ == '__main__':

    # led = LED(17)
    button = Button(2)
    # led.blink(n=2, background=False)
    print("wait for butten pressed")
    button.wait_for_active()
    print("pressed")
    # led.blink(on_time=0.2, off_time=2, n=3, background=False)



