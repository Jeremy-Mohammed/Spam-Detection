import re

def validatePhone(value):
	phoneNumberType1 = re.compile('[0-9]{3}-[0-9]{3}-[0-9]{4}')
	phoneNumberType2 = re.compile('[0-9]{3}-[0-9]{4}')
	phoneNumberType3 = re.compile('\([0-9]{3}\)[0-9]{3}-[0-9]{4}')

	match1 = phoneNumberType1.match(value)
	match2 = phoneNumberType2.match(value)
	match3 = phoneNumberType3.match(value)
	
	if match1:
		return True
		
	if match2:
		return True
		
	if match3:
		return True
		
	else:
		return False
		
		
value = '(905)999-9497'
if (validatePhone(value) == True):
	print ("This is a valid phone number.")
else:
	print ("This is not a valid phone number")
	
	
def validateDomain(value):
	emailType1 = re.compile('[a-zA-Z0-9]+\.?[A-Za-z0-9]+?[.com]')
	emailType2 = re.compile('[a-zA-Z0-9]+\.?[A-Za-z0-9]+?[.ca]')
	emailType3 = re.compile('[a-zA-Z0-9]+\.?[A-Za-z0-9]+?[.org]')
	
	match1 = emailType1.match(value)
	match2 = emailType2.match(value)
	match3 = emailType3.match(value)
	
	if match1:
		return True
		
	if match2:
		return True
		
	if match3:
		return True
		
	else:
		return False


value = "zachary.windover.com"
if (validateDomain(value) == True):
	print ("It is a real email address")
else:
	print ("This is not a real email address")


def validateLang(value):
	langType = re.compile('^(?:a{2})*([b]*)(?:c{3})*$')
	doesMatch = langType.match(value)
	
	if doesMatch:
		return True
	else:
		return False
	
value = "aaaabbbbbbbbccccccccc"
if (validateLang(value) == True):
	print ("This is a language")
else:
	print ("This isn't a language")

def trimSpaces(value):
	change1 = re.sub(r"\s+", " ", value)
	change2 = change1.strip()
	
	return change2
	
value = "      Computer      Science is    Good."
print ("Original:", value)
print ("With trimming:", trimSpaces(value))



	
