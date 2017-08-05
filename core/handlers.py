#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 30/07/2017

from gpiozero import (
    Button,
    LED
)
from signal import pause


if __name__ == '__main__':

    led = LED(17)
    button = Button(2)
    button.when_activated = led.on
    button.when_deactivated = led.off
    pause()




