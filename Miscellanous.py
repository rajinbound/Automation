import requests

#'visit-month'
cookie = {'visit-month':'December'}
response = requests.get('http://google.com',allow_redirects=False,cookies=cookie,timeout=1)
#301,200
#print(response.history)
print(response.status_code)


se = requests.session()
se.cookies.update({'visit-month':'January'})

res = se.get("https://httpbin.org/cookies",cookies={'visit-year':'2022'})
print(res.text)

#Attachments
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('C:\\Users\\Owner\\Documents\\ra.png', 'rb')}
r= requests.post(url,files=files)
print(r.status_code)
print(r.text)








