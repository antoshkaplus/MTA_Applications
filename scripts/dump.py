import ConfigParser as CP
import requests

p = CP.ConfigParser()
p.read("./../config/config.ini")
key = p.get("MTA", "bus_key")

params = {'key': key}
print params
r = requests.get('http://bustime.mta.info/api/siri/vehicle-monitoring.json', params=params)

s = r.text;
out = open("./../output/out.txt", "w")
out.write(s)