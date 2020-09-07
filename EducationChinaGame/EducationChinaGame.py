players = {"Yura" : 10, "Vita" : 10}

flag = True

while flag == True:
	print(players)
	print()
	yuraValue = 0
	mishaValue = 0

	while yuraValue < 1 or yuraValue > 3: 
		print("You can take only 1-3")
		print('{} -> '.format(list(players)[0]).upper(), end='')
		yuraValue = int(input())
		print()

	players["Yura"] = list(players.values())[0] - yuraValue

	if list(players.values())[0] <= 0:
		print(f'{list(players)[0]} won and {list(players)[1]} lost')
		break

	while mishaValue < 1 or mishaValue > 3:
		print("You can take only 1-3")
		print('{} -> '.format(list(players)[1]).upper(), end = '')
		mishaValue = int(input())
		print()

	players["Vita"] = list(players.values())[1] - mishaValue

	if list(players.values())[1] <= 0:
		print(f'{list(players)[1]} won and {list(players)[0]} lost')
		break





