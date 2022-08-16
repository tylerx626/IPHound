#!/usr/bin/python3

import os

greynoiseKey = input("Enter your GreyNoise API key: ")

os.system("greynoise setup --api-key " + greynoiseKey )
