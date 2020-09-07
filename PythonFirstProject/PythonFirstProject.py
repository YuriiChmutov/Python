import random;

def logicForWhile (rv, amount):
	user_value = int(input("Input your number -> "))
	if user_value == rv:
		print("Yes, it is!")
		amount -= 1
		return
	elif user_value < random_value:
		print("Your number is less then our value:(")
		amount -= 1
	else:
		print("Your number is begger then our value:(")
		amount -= 1



random_value = random.randint(1,50)
user_value = int(input("Input your number -> "))
amount_of_tryes = 6

if user_value != random_value and user_value < random_value:
	amount_of_tryes -= 1
	print("No, your number less then our value")
	while user_value != random_value and amount_of_tryes > 0:
		logicForWhile(random_value, amount_of_tryes)
	else: 
		print("Game over!")
if user_value != random_value and user_value > random_value:
	amount_of_tryes -= 1
	print("No, your number bigger then our value")
	while user_value != random_value and amount_of_tryes > 0:
		logicForWhile(random_value, amount_of_tryes)
	else: 
		print("Game over!")
else:
	print("Yes, it is!")
	amount_of_tryes = 0
	





	


