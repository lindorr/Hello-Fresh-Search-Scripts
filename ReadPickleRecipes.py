import pickle 
from getHelloFreshRecipesOOP import *

with open("recipeDump.pickle","rb") as file:  #reading the recipeDump.pickle binary file (rb)
	recipes=pickle.load(file) #loads the pickle file


def refine (keyword, exclude=""):
	out=[]
	for item in recipes:
		if (item.isIngredientPresent(keyword)==True and exclude==""): 
			out.append(item)
			print ("[%s]: %s" % (item.title, item.url))
		elif (item.isAllergenPresent(exclude) ==False and item.isIngredientPresent(keyword)==True):
			out.append(item)
			print ("[%s]: %s" % (item.title, item.url))


UserInputIngredient=input("List ingredients: ")
UserInputAllergens = input ("List any allergies, press enter for none: ")


refine(UserInputIngredient, UserInputAllergens)