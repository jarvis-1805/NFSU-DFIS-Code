import requests

r = requests.get('https://www.amazon.in')
print(r.text)
print(dir(r))
print(help(r))
print(r.text)
print(r.status_code)
print(r.ok)
print(r.headers)

