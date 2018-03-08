#!python3
def eggs(spam):
	x = "'"+spam[0]+", "
	for i in range(1,len(spam)):
		if i == (len(spam)-2):
			x = x + spam[i] + ", and "
		elif i == (len(spam)-1):
			x = x + spam[i]+ "'"
		else:
			x = x + spam[i] + ", "
	print(x)

list1 = ['apples','bananas','tofu','cats']
list2 = ['1','bananas','cats','ddddw']
eggs(list2)	 