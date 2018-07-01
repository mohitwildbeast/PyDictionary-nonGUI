#Import necessary libraries
import json #Library for handling JSON files
from difflib import get_close_matches #Library for implementing 'Did You Mean?' feature

#Load the contents of dictionary.json in data(Dicitonary data type)
data = json.load(open("dictionary.json","r"))

#Function for returning meaning of the input word
def meaning(word):

	#Convert the word to lower case
	word = word.lower()

	if word in data:
		return data[word]

	elif len(get_close_matches(word, data.keys(), cutoff = 0.8)) > 0: #If any close matches are found, its length will be greater than 0
		closest = get_close_matches(word, data.keys(), cutoff = 0.8)[0] #Closest word or first item in list
		print("Did you mean: ",closest)
		choice = input("Press [y] to confirm or [n] to reject: ")
		if choice == 'y' or choice == 'Y':
			return data[closest]
		elif choice == 'n' or choice == 'N':
			return word +" doesn't exist in the dictionary.Please check again!"
		else:
			return "Sorry, we didn't understand your query!"

	else:
		return word +" doesn't exist in the dictionary.Please check again!"

word = input("Enter word: ")

word_meaning = meaning(word)

if type(word_meaning) == list: #It is list only when meaning is found, else a string is returned
	#Print each meaning in seperate line
	for item,i in zip(word_meaning,range(len(word_meaning))):
		print('\t',i+1,'. ',item)
else:
	print(word_meaning)