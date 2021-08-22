
#https://www.vocabulary.cl/Basic/Numbers.html


###
"""

	This is basic program for converting a string value of number into upto 999,999,999 into english
	The program works baised on the number english convertion in the websight https://www.vocabulary.cl/Basic/Numbers.html
	it is not object based as in my opinion simple operations should be single call functions not classes in order to make outside code
	cleaner. 

"""

#For adding a 100 to a three digent numbers 
def one_hundreds(number):
	if number=="0":
		return ""
	return ""+one(number)+" hundred"

#Converting a 1 diget string number to english
def one(number):
	value=number
	if value=="0":
		return "zero"
	if value=="1":
		return "one"
	if value=="2":
		return "two"
	if value=="3":
		return "three"
	if value=="4":
		return "four"
	if value=="5":
		return "five"
	if value=="6":
		return "six"
	if value=="7":
		return "seven"
	if value=="8":
		return "eight"
	if value=="9":
		return "nine"

#Converting a 2 diget string number to english in the case where the first diget is a 1
def teens(number):
	value=number
	if value=="0":
		return "ten"
	if value=="1":
		return "eleven"
	if value=="2":
		return "twelve"
	if value=="3":
		return "thirteen"
	if value=="4":
		return "fifteen"
	if value=="5":
		return "fifteen"
	if value=="6":
		return "sixteen"
	if value=="7":
		return "seventeen"
	if value=="8":
		return "eighteen"
	if value=="9":
		return "nineteen"


#For adding dashes in between the 10s place and the 1s place for three diget number stings a helper function for the funtion tens
def ones(number):
	if number=="0":
		return ""
	return "-"+one(number)


#Converting a 2 diget string number to english 
def tens(number):
	value=number[0]
	number=number[1]

	if value=="0":
		return one(number)
	if value=="1":
		return teens(number)

	if value=="2":
		return "twenty"+ones(number)

	if value=="3":
		return "thirty"+ones(number)

	if value=="4":
		return "forty"+ones(number)

	if value=="5":
		return "fifty"+ones(number)

	if value=="6":
		return "sixty"+ones(number)

	if value=="7":
		return "seventy"+ones(number)

	if value=="8":
		return "eighty"+ones(number)

	if value=="9":
		return "ninety"+ones(number)


#Converting a 3 diget string number to english for values greater then one thousand
def hundreds_extion(number,ening_value):
	adder=tens( number[1]+number[2] )
	if number[0]!="0":
		if adder!="zero":
			adder=" and "+adder
		else:
			adder=""
	out=one_hundreds( number[0] )+adder
	if out=="zero":
		out=""
	else:
		out=out+ening_value
	return out


#Converting a 3 diget string number to english for values less then one thousand
def hundreds(number):
	adder=tens( number[1]+number[2] )
	if number[0]!="0":
		if adder!="zero":
			adder=" and "+adder
		else:
			adder=""
	return one_hundreds( number[0] )+adder


#Converting a 9 diget number to english.
def Numb_to_english(number):

	#Pad the number if it to short 
	number_holder=len(number)
	for x in range(number_holder,9):
		number="0"+number

	#Check if the number is to lonmg
	if len(number)!=9:
		return "NTL"

	#Check if its not a number 
	for x in range(len(number)):
		if number[x].isnumeric() !=True:
			return "NAN"


	millons_coma=""
	thosands_coma=""
	#get the ending string
	ending=hundreds(str(number[6]+number[7]+number[8]))

	#get the thousand place string
	thousand_place=hundreds_extion(number[3]+number[4]+number[5]," thousand ")
	#get the millons place string
	millons_place=hundreds_extion(number[0]+number[1]+number[2]," million ")



	#check and see if  the value is zero
	if thousand_place!="" or millons_place!="":
		if ending=="zero":
			ending=""


	#check and see if there needs to be after millons
	if millons_place!="":
		if ending!="" or thousand_place!="":
			millons_coma=",  "
			if number[3]=="0":
				millons_coma=",  and "
	
	#check and see if there needs to be after the thousand place
	if thousand_place!="":
		if ending!="":
			thosands_coma=",  "
			# adding and for case where there is no hudreds
			if number[6]=="0":
				thosands_coma=",  and "
				



	#Capitalize First letter
	theoutput=millons_place+millons_coma+thousand_place+thosands_coma+ending

	fist_char=theoutput[0].upper()
	final_output=""
	for x in range(1, len(theoutput) ):
		final_output+=theoutput[x]



	return fist_char+final_output+"."











