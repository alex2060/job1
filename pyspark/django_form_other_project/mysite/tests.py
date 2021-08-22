import requests
r = requests.get('http://127.0.0.1:8080/number?number=1')
#print(r.status_code)
#print(r.text)
if "One" in r.text:
    print("Passed Test")
else:
    print("Failed Test")

if "Ok" in r.text:
    print("Passed Test")
else:
    print("Failed Test")


r = requests.get('http://127.0.0.1:8080/number?number=8')
#print(r.status_code)
#print(r.text)
if "Eight" in r.text:
    print("Passed Test")
else:
    print("Failed Test")



r = requests.get('http://127.0.0.1:8080/number?number=5A')
#print(r.status_code)
#print(r.text)
if "Five" in r.text:
    print("Failed Test")
else:
    print("Passed Test")

if "NAN" in r.text:
    print("Passed Test")
else:
    print("Failed Test")


r = requests.get('http://127.0.0.1:8080/number?number=')
#print(r.status_code)
#print(r.text)
if "NAN" in r.text:
    print("Passed Test")
else:
    print("Failed Test")


r = requests.get('http://127.0.0.1:8080/number?number=1000000000000000000000000000')
#print(r.status_code)
#print(r.text)
if "NTL" in r.text:
    print("Passed Test")
else:
    print("Failed Test")

r = requests.get('http://127.0.0.1:8080/number')
print(r.status_code)
print(r.text)
if "NAN" in r.text:
    print("Passed Test")
else:
    print("Failed Test")

r = requests.get('http://127.0.0.1:8080/number',data = {'number': '1'})

print(r.status_code)
print(r.text)
if "NAN" in r.text:
    print("Passed Test")
else:
    print("Failed Test")
