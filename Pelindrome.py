def is_pelindrome(word):
	word=word.lower()
	word1=word
	new_str=''
	while len(word1)>0:
		new_str=new_str+ word1[-1]
		word1=word1[:-1]

	print(new_str)
	if (new_str== word):
		return True
	else:
		return False
		
if is_pelindrome(input("Enter String >>>")):
	print("yes,this is pelindrome")
else:
	print("Sorry,this is not pelindrome")