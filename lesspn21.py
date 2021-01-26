'''python Function'''

# def my_function():
# 	print('Hello I am a John ')
# my_function()#function call(kanchuma funkcyan)

# def my_function(fname,lname):
# 	print(fname , ' ' , lname)
# my_function('John','Sargsyan')
# my_function('Aleks', 'Gabtin')

# def my_function(fname,lname):
# 	print(fname , ' ' , lname)
# a='Aleks'
# c='Sargsyan'
# my_function(a,c)


'''keyowrd Arguments'''
# def my_function(child2,child1):
# 	print('','The youngest child is : ',child2,'\n','The oldest child is : ',child1)
# my_function(child1='Emil',child2='Jon')


'''Default parameter Value'''
# def my_function(country = 'USA'):
# 	print('I am from ',country)
# my_function('Sweden')
# my_function('India')
# my_function()


# def my_function(food):
# 	for x in food:
# 		print(x)
# fruits=['apple','banana','cherry']
# my_function(fruits)


# def my_function(list1):
# 	print('','max number: ',max(list1),'\n','min namber: ',min(list1))
# list1=[12,15,1,8,9,0]
# my_function(list1)


# def my_function(list1):
# 	c=sum(list1)/len(list1)
# 	print(c)
# list1=[12,5,9,10]	
# my_function(list1)


# def my_function(x):
# 	return 5*x
# print(my_function(3))


# def my_function():
# 	global x
# 	x='fantastic'
# my_function()
# print('python is ',x)


# def my_function(*args):
# 	print(args)
# my_function(5,6,7,8,6,7)


# def my_function(**kwargs):
# 	print(kwargs)
# my_function(name='Aram',age=27)


# add=lambda x,y: x+y
# print(add(2,5))


'''calculate'''

# def add (x,y):
# 	return(x+y)
# def minus(x,y):
# 	return(x-y)
# def multiplication(x,y):
# 	return(x*y)
# def division(x,y):
# 	return(x/y)

# def result(choice,x,y):
	
# 	if choice =='+':
# 		print(add(x,y))
	
# 	elif choice == '-':
# 		print(minus(x,y))
	
# 	elif choice == '*':
# 		print(multiplication(x,y))
	
# 	elif choice == '/':
# 		print(division(x,y))

# choice=input('choice: ')
# while True:
# 	x=int(input('x = '))
# 	y=int(input('y = '))
# 	if choice == '/' and y!=0 :
# 		break
# 	else:
# 		print('Please dont write zero1`')
# result(choice,x,y)


''' one day how many second'''

# def my_function(day):
# 	return(day*86400)
# day=int(input('write day : '))
# print(my_function(day))					