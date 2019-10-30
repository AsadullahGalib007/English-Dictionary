#!/usr/bin/env python

#auther @galib

#requirements:
#install packages such as pip, pyaudio,speech recognition module
#pip install SpeechRecognition
#sudo apt install python-pip
#sudo apt install python-pyaudio python3-pyaudio
#and
#sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip install pyaudio
import sys
import json
import pyaudio
import speech_recognition as sr
from difflib import get_close_matches
collection = json.load(open("collection.json"))

def lookup(word):
    word = word.lower()

    if word in collection:
    	return collection[word]

    elif len(get_close_matches(word, collection.keys())) > 0:
    	yn = raw_input("Are you looking for the word %s ? Enter Y for Yes or N for No: " % get_close_matches(word, collection.keys())[0])

	if yn == "Y" or yn == "y" :
		return collection[get_close_matches(word, collection.keys())[0]]
	elif yn == "N" or yn == "n" :
		return "Word not found. Please try again."
	else:
		return "Please enter either Y or N"
    else:
    	return "No word entered"


def search_word():
	word = raw_input("Enter a word: ")
	output = lookup(word)
	if type(output) == list:
		for item in output:
			print(item)
	else:
		print(output)

def search_word2(val):
	word = val
	output = lookup(word)
	if type(output) == list:
		for item in output:
			print(item)
	else:
		print(output)


def voice_search():
	r = sr.Recognizer()
	r.energy_threshold=4000
	mic = sr.Microphone(sample_rate = 48000, chunk_size = 2048)

	with mic as source:
		r.adjust_for_ambient_noise(source)
		print('Say Something...')
		audio = r.listen(source)

		try:
			val = r.recognize_google(audio)
			print('You said: '+ val)
			search_word2(val)

		except sr.UnknownValueError:
			print("Sorry...Could not catch that")
			print('Try Again...')
			voice_search()

		except sr.RequestError as e:
			print("Could not request results from Google Speech Recognition service; {0}".format(e))
			print('Maybe the internet connection is down.')


def choose_action(i):
	if i == 0:
		exit()
	elif i == 1:
		search_word()
	elif i == 2:
		voice_search()
	else:
		print('Wrong Input!!!\nTry Again...')

print('\n***** WELCOME TO THE ENGLISH DICTIONARY *****\n\n\n\n')
while True:
	try:
		print('\n\n\nEnter 0 to exit...\n')
		print('Enter 1 to type the word...\n')
		print('Enter 2 for voice search...\n')
		try:
			choice = input("\nNow Enter your choice: ")
			choose_action(choice)
		except (NameError, SyntaxError):
			print('Invalid Input\nTry Again...')
			choice = input("\nEnter your choice: ")
			choose_action(choice)
	except KeyboardInterrupt:
		print('\nKeyboardInterrupt raised. Do you really want to exit?')
		inturrupt = raw_input('Type Y for yes or N for no: ')
		if inturrupt == "Y" or inturrupt == "y":
			exit()
		else:
			continue
