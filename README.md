# IPHound
Gather OSINT information on an IP address

Clone
git clone https://github.com/tylerx626/iphound

Install Requirements
pip install -r requirements

Make executable
chmod +x iphound.py

Usage
./iphound.py

"Enter the IP address: 1.1.1.1"
{'ip': '1.1.1.1', 'noise': False, 'riot': True, 'classification': 'benign', 'name': 'Cloudflare Public DNS', 'link': 'https://viz.greynoise.io/riot/1.1.1.1', 'last_seen': '2022-08-15', 'message': 'Success'}
