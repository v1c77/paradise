#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 30/07/2017

from gpiozero import (
    Button,
    LED
)


if __name__ == '__main__':

    button = Button(27)
    button.wait_for_active()
    print("wait for you.")




