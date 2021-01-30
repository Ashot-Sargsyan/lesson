'''File Handing'''
# f=open('Armenia.txt')#mer txt dokumente bacec f
# print(f)#cuica tali txt dokumente inch tesaka vonca grvac


# f=open('Armenia.txt')
# print(f.read())#karduma mer txt dokumenti mech inch ka 


# try:
# 	f=open('Arm.txt')#faila txt anune Arm
# except FileNotFoundError:
# 	print('You dont have faile name Arm')#chuneq tenc fail dra hamar errora talis



# f=open('Armenia.txt')
# print(f.read(8))#gruma 8 indexsi tvyalnere voore grvaca txt faili mech aysqin hello _ i _


# f=open('Armenia.txt')
# for i in f.read():
# 	print(i, end='')#kartuma bolor toxere miankamic


# f=open('Armenia.txt')
# print(f.readline())
# print(f.readline())#kartuma 1 u 2 toxere


# f=open('Armenia.txt')
# print(f.read())
# f.close()#paguma faile dra hamar errora tali
# print(f.read())



# f=open('Armenia.txt','a')
# f.write('\nNow the file has more content!')
# f.close()

# f=open('Armenia2.txt','w')
# f.write('\nI have deleted the content!')
# f.close()



# def new_file(file,mode,text):
# 	try:
# 		f=open(file,mode)
# 		print(f.read())
# 	except FileNotFoundError:
# 		f=open(file,'w')
# 		f.write(text)
# file='Ashot.txt'
# mode='r'
# text='\tTell me somethign boy \n are you happy in this modern world '

# new_file(file,mode,text)


# file='Ashot.txt'
# mode='r'

# f=open(file,mode)

# c=f.read().split(' ')

# if 'boy\n' in c:
# 	print(c.index('boy\n'))




# import os
# os.remove('Armenia2.txt')#jnjuma konkret faile



with open('password.txt','w') as f:
	login = input('write your login: ')
	password = input('write your password: ')
	a='login'+login+' '+'password'+password
	f.write(a)

with open('password.txt') as f:
	print(f.read())