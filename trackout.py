#!/usr/bin/python3

# Name          : Trackout
# Writer(s)     : Abay | abaykan.com
# Contribution  : Arap Bett
# Description   : TrackOut is a simple IP Tracker using Python.

import os
import requests
import json
import colorama
from geopy.distance import geodesic

colorama.init(autoreset=True)

def clear_screen():
    os.system("clear")

def print_banner():
    print(colorama.Fore.CYAN + """
      _____                _      ___       _   
     /__   \\_ __ __ _  ___| | __ /___\\_   _| |_ 
       / /\\/ '__/ _` |/ __| |/ ///  // | | | __|
      / /  | | | (_| | (__|   </ \\_//| |_| | |_ 
      \\/   |_|  \\__,_|\\___|_|\\_\\___/  \\__,_|\\__|                                           
      Python IP Tracker - Abay | abaykan.com
    """)

def get_ip_data(ip):
    url = f"https://api.ipdata.co/{ip}?api-key=test"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(colorama.Fore.RED + f"Error: {e}")
        return None

def print_ip_data(values):
    if values:
        print("------------------------------------")
        print("\r")
        print(f" IP           :  {values['ip']}")
        print(f" City         :  {values['city']}")
        print(f" Region       :  {values['region']}")
        print(f" Country      :  {values['country_name']}")
        print(f" Continent    :  {values['continent_name']}")
        print(f" Time Zone    :  {values['time_zone']}")
        print(f" Currency     :  {values['currency']}")
        print(f" Calling Code :  +{values['calling_code']}")
        print(f" Organisation :  {values['organisation']}")
        print(f" ASN          :  {values['asn']}")
        print("\r")

def calculate_distance(ip1, ip2):
    data1 = get_ip_data(ip1)
    data2 = get_ip_data(ip2)
    if data1 and data2:
        coords_1 = (data1['latitude'], data1['longitude'])
        coords_2 = (data2['latitude'], data2['longitude'])
        distance = geodesic(coords_1, coords_2).kilometers
        print(f"Distance between {ip1} and {ip2}: {distance:.2f} km")

def main():
    clear_screen()
    print_banner()
    while True:
        ip = input("What is your target IP: ")
        ip_data = get_ip_data(ip)
        print_ip_data(ip_data)
        another_ip = input("Enter another IP to calculate distance (or press Enter to skip): ")
        if another_ip:
            calculate_distance(ip, another_ip)
        break

if __name__ == "__main__":
    main()
	    
