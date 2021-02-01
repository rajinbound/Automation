import requests

from payLoad import *
from utilities.configurations import *
from utilities.resources import *

url = getConfig()['API']['endpoint'] + ApiResources.addBook
#print(url)
headers = {"Content-Type": "application/json"}
addBook_response = requests.post(url,json=addBookPayload("terimaa"),headers=headers, )
#query = 'select * from Books'
#addBook_response = requests.post(url,json=buildPayLoadFromDB(query),headers=headers, )
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
print(bookId)
# Delete Book -

url = getConfig()['API']['endpoint'] + ApiResources.deleteBook
headers =headers={"Content-Type": "application/json"}

response_deleteBook = requests.post(url, json=deletebook_id(bookId), headers=headers, )

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"

#Authentication

se = requests.session()
se.auth = auth=('rajinbound',getPassword())

url = "https://api.github.com/user"
github_response = requests.get(url,verify=True,auth=('rajinbound',getPassword()))

print(github_response)
print(github_response.status_code)

url2 = "https://api.github.com/user/repos"
response= se.get(url2)
print("this is second session", response.status_code)







