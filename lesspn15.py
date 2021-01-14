'''1)'''
# list1=[1,2,3,4,5,6,5.6,"ani",True,('book',5)]

'''2)'''
# name=['Apple', 'ph', 'toshiba', 'samsung', 'assus']
# notebook=input('what do you want?')
# if notebook in name:
# 	x = name.count(notebook)
# 	print('very well',x)
# else:
# 	print('eror')



'''3)'''
# letter=0
# number=0
# character=0
# characters=('!','@','#','$','%','&','*')

# while True:
# 	password=input('Your password is:')
# 	if len(password)>8:
# 		for i in password:
# 			if i.isdigit():
# 				number+=1
# 			# elif i.isalpha():
# 			# 	letter+=1
# 			elif i in characters:
# 				character+=1
# 		if number>1 and  character>1 and password[0].isupper():#letter>0 and 
# 			print('Strong')
# 			break
# 		else:
# 			print('Your password is not right')
# 	else:
# 		print('Your password lenght is less then 8')



'''4)'''
# link='https://www.youtube.com/watch?v=asdkjajhsdijahdja'
# print(link[link.index('=')+1:])


'''4.1)'''
# link='https://www.youtube.com/watch?v=asdkjajhsdijahdja'
# if '?v' in link:
# 	counts=0
# 	for i in link:
# 		counts+=1
# 		if i=='=':
# 			break
# 	print(link[counts:])
# else:
# 	print('you dont write correct link')


'''5)bari hakarake polidrom'''
# word=input('')
# if word == word[::-1]:#[::-1] bare frcnuma
# 	print('yes')
# else:
# 	print('error')


'''6)'''
# number=input('pleace input number: ').split()#lista taza sarkum 
# res=[i for i in number if int(i)%2==0]
# print(res)

# number=input('pleace input number: ').split()
# even=[]
# for i in number:
# 	if int(i)%2==0:
# 		even.append(i)
# print(even)



'''9)2 listi mech pahuma ken u zuig tvere'''

# list1=[12, 21, 56, 40, 8, 7, 9]
# even=[]
# odd=[]
# for i in list1:
# 	if i%2==0:
# 		even.append(i)
# 	else:
# 		odd.append(i)
# print('','even',even,'\n','odd',odd)



# list1=[12, 21, 56, 40, 8, 7, 9]
# even=[i for i in list1 if i%2==0]
# odd=[i for i in list1 if i%2==1 ]
# print('','even',even,'\n','odd',odd)