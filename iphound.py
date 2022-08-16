#!/usr/bin/python3

import os,requests

ip = input("Enter the IP address: ")


def greynoise():
    headers = {'content-type': 'application/json', 'key': 'null'}
    url = 'https://api.greynoise.io/v3/community/' + ip
    r= requests.get(url)
    print(r.json())


#def ipinfo():


def main():
    greynoise

if __name__ == "__main__":
    main()