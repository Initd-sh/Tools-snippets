#Aim: To find all the email ids present in a website
#Author: Shrutirupa Banerjiee(@freak_crypt)
#Date: 13.2.2019

#-------------------------------------------------------------------------------------------------------------------------#

#Modules to be imported

import urllib2
import csv
from bs4 import BeautifulSoup
import re
import urlparse
import requests
import urllib
import os
import spf
import subprocess

#-------------------------------------------------------------------------------------------------------------------------#

#Variables defined globally

email_list = []


#-------------------------------------------------------------------------------------------------------------------------#

def validUrl():
	"This function specifies the format of the url the user should follow"
	print("Please enter a proper and a working url in the below format \n")
	print("http[s]://www.example.com \n")
	print("DO not add / at the end \n")
	
#-------------------------------------------------------------------------------------------------------------------------#

def find_record(url):
	"This function finds the entire record of the url including the SPF record given by the user"
# The step is kind of baby one but I wanted to take a simple step	
	url = url.replace("http://www.","")
	url = url.replace("https://www.","")
	url = url.replace("https://","")
	url = url.replace("http://","")
	print "Here is the entire record of the domain provided by the user \n"
	data = os.system('nslookup -type=txt' + ' ' +  url)
	end()

#-------------------------------------------------------------------------------------------------------------------------#

def end():
	"This function just describes the end of the code"

	print "YOu are free to contribute to this code \n"
	print "More functionalities will be added to it \n"
	print "---------------------------------------------------------------------------------------------------------"

#-------------------------------------------------------------------------------------------------------------------------#

def findEmails(s):
	"This function will bring out all the emails provided by the website"
	pattern = re.compile('[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}', re.MULTILINE)
	captured = pattern.findall(s)

	for i in captured:
		if i not in email_list:
			email_list.append(i)
	print "Here is the list of email ids found from the url provided by the user"
	print email_list

	print "##############################################################################################################"

	return s
	pass



#-------------------------------------------------------------------------------------------------------------------------#

def parseUrl(url):
	"This function checks if a proper url is given"
	try:
		url_parse = urllib2.urlopen(url)
		s = url_parse.read()

		findEmails(s)
		find_record(url)

	except urllib2.URLError as err:
		validUrl()


	pass

#-------------------------------------------------------------------------------------------------------------------------#

def main():
	"And the main function starts"
	urlToCheck = raw_input("Enter the url: \n")
	res1 = urlToCheck.startswith('http://')
	res2 = urlToCheck.startswith('https://')
	if res1 == True or res2 == True:
		parseUrl(urlToCheck)
	else:
		validUrl()

#-------------------------------------------------------------------------------------------------------------------------#

if __name__=="__main__":
	main()
	pass


#-------------------------------------------------------------------------------------------------------------------------#






