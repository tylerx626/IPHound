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

def dnsTrail():
    headers = {'Accept': 'application/json', 'APIKEY': 'pYIVSi6qspPzwXL6FJM9QQNCfxPCXboEE'}
    url = 'https://api.securitytrails.com/v1/domain/' + ip
    r= requests.get(url, headers=headers)
    print(r.json())

def main():
    print('Checking GreyNoise.io...')
    greynoise()
    print('Checking ipinfo.io...')
    ipinfo()
    print('Checking with SecurityTrails DNS records...')
    dnsTrail()

if __name__ == "__main__":
    main()
    
    ##to-do, AWS integration
    ##
    ##[default]
    ##aws_access_key_id = AKIAYVP4CIPPK6H73IUM
    ##aws_secret_access_key = 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
    ##output = json
    ##region = us-east-2
