import requests
from bs4 import BeautifulSoup

'''respond = requests.get("http://www.google.com")
print(respond.text)'''


'''url = "https://jsonplaceholder.typicode.com/posts"
data =  {
    "title":"tejas",
    "Body":"Bhai",
    "Userid":"12"
}
headers =  {
    'Content-type': 'application/json; charset=UTF-8',
 }
response = requests.post(url,headers=headers,json = data)
print(response.text)'''

url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
for heading in soup.find_all("h2"):
  print(heading.text)