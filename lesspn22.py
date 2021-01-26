'''1)1 kilometr in miles'''

# def myfunction(kilometer):
# 	miles=kilometer*1.6
# 	return miles

# kilometer=int(input('Your miles:'))
# print(myfunction(kilometer))

'''2)one day in second'''

# def myfunction(days):
# 	second=days*86400
# 	return second
# days=int(input('Days = '))
# print(myfunction(days))

'''3)strong pasword'''
# import random

# def valid_password():
# 	password=''
# 	letters='ashjrwiuqponqgvzcp'
# 	numbers='123978513640'
# 	chars='*!#$&@()?!@%'

# 	letters_count=6
# 	numbers_count=chars_count=2
# 	for i in range(letters_count):
# 		l=random.choice(letters)
# 		password+=l

# 	for i in range(numbers_count):
# 		n=random.choice(numbers)
# 		c=random.choice(chars)
# 		password+=n
# 		password+=c

# 	password=list(password)#stringe darcnumek list vor oktagorcenq shuffle
# 	random.#shuffle xarnuma texerov
# 	return"".join(password)
# print(valid_password())


'''4)factorial'''
# def myfunction(factorial):
# 	res= 1
# 	for i in range(2,factorial+1):
# 		res *=i
# 	return res	

# number=int(input('write your number:'))	
# print(myfunction(number))


'''5)max number funkcion'''
# def myfunction(mylist):

# 	res=list1[0]
# 	for i in list1:
# 		if i>res:
# 			res=i
# 	return (res)
# list1=[1,5,6,8,9,3]	
# print(myfunction(list1))


'''6)Blot'''
import random as r

def star():
	global name#funkcyaic durs oktagorcem 
	print('you play blot ')
	name=input('what is your name ')
star()#mer funkcyaneq kanchum


def card():
	all_cards=[]
	cards_type=['clob','diamond','heart','spade']
	cards=[9,10,'J','Q','K','T']
	
	for i in cards_type:
		for j in cards:
			result = i + str(j)
			all_cards.append(result)

	r.shuffle(all_cards)

	player=[]
	comp=[]

	for i in range(1,6):
		players_card=all_cards.pop()
		player.append(players_card)
		comp_cards=all_cards.pop()
		comp.append(comp_cards)

	trump_card = all_cards.pop()

	player.sort()
	comp.sort()
	print(' ')
	print('Trump card - ',trump_card)
	print(' ')
	print(name,player)
	print(' ')
	print('comp',comp)
	print(' ')
	print('      ',name)

	while True:
		players_choice=input(' you want to take trump card yes(y),(no): ')=='y'

		if player_choice:
			pass