#!/usr/bin/python3

import os,requests,ipinfo,pprint

ip = input("Enter the IP address: ")


def greynoise():
    headers = {'content-type': 'application/json', 'key': 'null'}
    url = 'https://api.greynoise.io/v3/community/' + ip
    r= requests.get(url)
    print(r.json())


def ipinfo():
    headers = {'content-type': 'application/json'}
    url = 'https://ipinfo.io/' + ip
    r= requests.get(url)
    print(r.json())


def main():
    print('Checking GreyNoise.io...')
    greynoise()
    print('Checking ipinfo.io...')
    ipinfo()

if __name__ == "__main__":
    main()