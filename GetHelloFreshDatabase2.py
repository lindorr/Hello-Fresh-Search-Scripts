import requests 
from getHelloFreshRecipesOOP import * 
import pickle 
import sys 

sys.setrecursionlimit(100000)

requestURL="https://gw.hellofresh.com/api/recipes/search?offset=0&limit=250&locale=en-CA&country=ca"
requestHeaders={

"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NzA4NDE4MTIsImp0aSI6ImMxMDQwZjkzLTg2ZWQtNDgwZS1iYjZmLTQzOGQ4MjMwYTMxMyIsImlhdCI6MTU2ODIxMjA2OSwiaXNzIjoic2VuZiJ9.okUQDudxB8VD4vxWO7IzisK_2w2DZxZHiaxurNiI7Qs"

}

r=requests.get(requestURL, headers=requestHeaders)
data=r.json()
recipes=[]

x=1 #see how many have gone thourgh

for JSONitem in data["items"]: 
	url=JSONitem["websiteUrl"]
	try:
		print (x, url)
		recipeObject = HelloFreshRecipe(url) #instantiating a recipe object by passing the URL to the constructor
		recipes.append( recipeObject ) #append the recipe object 
		x=x+1
	except AttributeError: 
		print ("FAILED: ",url)

#need to save the recipes array even after its been done bu dumping values inside the variable to another file

with open("recipeDump.pickle","wb") as file: #open a blank file and dump recipes array inside as a "write binary" (wb) format
	pickle.dump (recipes, file) #saves the variable content even after its closed 



