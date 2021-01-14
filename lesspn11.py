'''1)'''
# n=int(input(''))
# for i in range(2,n):
# 	if n%i==0:
# 		print('not',n)
# 		break
# else:
# 	print('simple',n)



# n=int(input(''))
# res=n//2
# for i in range(2,res):
# 	if n%i:
# 		print('not',res)
# 		break
# else:
# 	print('simple',res)




# n=int(input(''))
# res=int(n**0.5)
# for i in range(2,res):
# 	if n%i:
# 		print('not',n)
# 		break
# else:
# 	print('simple',n)



'''2)'''
# n=int(input(''))
# even = 0
# odd = 0
# for i in range(1,n+1):
# 	if i %2==0:		
# 		even+=1
# 	else:	
# 		odd+=1
# print(even,odd)		


# n=int(input(''))
# if n %2==0:
# 	res = n / 2
# 	print('even',res,'odd',res)
# else:
# 	res = n//2 
# 	print('even',res,'odd',res+1)


'''3)'''
# n=int(input(''))
# fibonacci=0
# if n==(n+(n-1)):
# 	print('fibonacci:',n)
		
# else:
# 	print('error')


# x,y=0,1#fibonachi
# print(0)
# while y<40:
# 	print(y)
# 	x,y=y,x+y


# x,y=0,1#fibonachi
# print(0)
# while y<40:
# 	print(y)
# 	res=x+y
# 	x=y
# 	y=res



'''4)'''

# tarer= 0
# tver = 0
# probel = 0
# word=input('---  ')
# for i in word:
# 	if i.isalpha():
# 		tarer += 1
# 	elif i.isdigit():
# 		tver += 1
# 	elif i == " ":
# 		probel+=1
# print(tarer,tver,probel)


'''5)'''
# res = '0123456789'
# word=input('')
# for i in word:
# 	if 	i in res:
# 		print('no')#ete mer graci mech tiv ka u inke stuguma res ete ka uremn tpuma no hakarak depkum yes 
# 		break

# else:
# 	print('ok')				



'''6)'''
count = 0#counte patasxana havasara 0
number=int(input(''))
for i in str(number):#str integere darcnuma string vor fra meche
	count += int(i)#gumarumem i aysiqn stringi mechi gracnere gumarumem irar
print(count)



count = 0
number=int(input(''))
for i in str(number):
	
