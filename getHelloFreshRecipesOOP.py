from bs4 import BeautifulSoup
import requests
import re

class Recipe:
	

	def isKeywordPresent (self, keyword,array):
		for item in array:
			if(keyword.lower() in item.lower()):
				return True
		return False

	
	def isIngredientPresent(self, ingredientKeyword):
		return self.isKeywordPresent(ingredientKeyword,self.ingredients)

	def isAllergenPresent (self, allergenKeyword):
		return self.isKeywordPresent(allergenKeyword, self.allergens) or self.isKeywordPresent(allergenKeyword, self.ingredients)

	def __init__(self, url):
		self.url=url
		self.title=""
		self.allergens=[]
		self.ingredients=[]


		page=requests.get(url)
		self.soup = BeautifulSoup(page.text, 'html.parser')		
		# Parse webpage content into something Python can better read


class HelloFreshRecipe(Recipe):
	def __init__(self, url):
		super().__init__(url)
		self.scrapeInfo()

	def scrapeInfo(self):

		listOfAllergy=self.soup.find("span",{"data-translation-id":"recipe-detail.allergens"}).parent.parent # use this one because its more specific since it has id
		# var_name=self.soup.find("tag --invovles< >", {attribute -- stuff inside <...> BEFORE the = : value --the value associated with the attribute})
		listOfIngredients=self.soup.find("div",{"data-test-id":"recipeDetailFragment.ingredients"})
		#print (listOfAllergy.prettify()) 
		title=self.soup.find("h1",{"data-test-id":"recipeDetailFragment.recipe-name"})
		self.title=title.text


	
		for row in listOfAllergy.contents[1].contents[0].contents:
			item = row.getText() # grabs only the text info, otherwise going to get the <span> crap
			item = item.strip("•") # strips/cleans it up
			#item.find("/") # returns the index of where the / appears
			#item = item[:item.find("/")]
			self.allergens.append(item)
			#print(row.text[:row.text.find("/")].strip("•")) #all done at once


		for ingredientrow in listOfIngredients.contents[3].contents[0].contents:
			text = ingredientrow.getText(separator=u' ') # Get all the text from this element, combine them and use a space ' ' as the combiner (u is for unicode format)
			pattern = r'[0-9½⅓⅔¼¾⅕⅖⅗⅘⅙⅚⅐⅛⅜⅝⅞⅑⅒]+ (g|kg|cup|tbsp|tsp|unit|can|box)' # Pattern is the conditions on what to find, writte in the r'....' format
			match = re.match(pattern, text) # Look for the pattern in the string (in this case the ingredient, here we want find the quatity and unit of the ingredient)
			
			if(match): # Only do this if the pattern is found
				matchIndex = match.span()[1] # Get the end of the match, this return the index in where it ends in the string
				text = text[:matchIndex] + " of" + text[matchIndex:] # Add ' of' inbetween the quanityt/unit and the actual ingredient
				self.ingredients.append(text)


	



a=HelloFreshRecipe('https://www.hellofresh.ca/recipes/beef-stroganoff-5877cb289f236a02eb5879c2')
b=HelloFreshRecipe('https://www.hellofresh.ca/recipes/italian-spaghetti-and-meatballs-598c7f54c9fd087e7a37c502?locale=en-CA')
c=HelloFreshRecipe("https://www.hellofresh.ca/recipes/cajun-spiced-chicken-burger-5a0472fbae702a7b3368eaa2?locale=en-CA")

