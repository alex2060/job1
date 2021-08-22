
import requests


f=open("/home/pi/Desktop/yooo6.txt","r")
value=f.read().split(" ")[0]
print(value)
value = value.split("/dat2")[0]
requests.get("http://alexhaussmann.com/adhaussmann/update2.php?loc=mykey&key="+value)






