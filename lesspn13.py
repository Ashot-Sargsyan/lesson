# a=()
# print(type(a))

# b=tuple()#miat vedro vorte karas pahes ham string ham int 
# print(type(b))


# tupl=('physics','chemistry',1997,2000)
# print(tupl.__sizeof__())#sizeof cuica tali ira chape ichkana tex gravum biterov


# thistuple = ('apple','banana','cherry',12,2000)#cuica tali erkarucune
# print(len(thistuple))


# thistuple=('apple','banana','cherry',12,2000)#kanakna cuic tali
# print(thistuple.count('banana'))


# thistuple = ('apple','banana','cherry')#cuica tali cucaki mech ka apple
# if 'apple' in thistuple:
# 	print("yes 'apple' is in the fruits tuple")

# thistuple = ('apple','banana','cherry')
# for x in thistuple:
# 	print(x)

# thistuple = ('apple','banana','cherry','kiwi')
# print(thistuple[1])

# thistuple = ('apple','banana','cherry','kiwi')
# print(thistuple[1:2])


# x=(5,10,15,20)
# y=reversed(x)#hakaraka veradarcnum
# print(tuple(y))

# thistuple=('apple','banana','cherry','orange','kiwi','melon','mango')
# print(thistuple[-4:-1])


# tuple1=('a','b','c')
# tuple2=(1,2,3)
# tuple3=tuple1+tuple2
# print(tuple3)


# num=[10,20,30,10,(20,),40]
# c=0
# for n in num:
# 	if isinstance(n,tuple):
# 		break
# 	c+=1
# print(c)

# tup=('e','x','e','r','c','i','s','e','s')
# mystr=''.join(tup)#sax irara kpcnum darcnuma bar
# print(mystr)


# tup=('e','x','e','r','c','i','s','e','s')
# mystr=''
# for i in tup:
# 	mystr+=i
# print(mystr)



# tup=('apple', 'samsung', 'dell', 'toshiba')
# notebook=input('what notebook you wanted?')
# if notebook in tup:
# 	print('yes')
# 	print(tup.count(notebook))
# else:
# 	print('no')



# n=''
# res=(1,2,3,4,5,6,7,8,9,0)
# for i in res:
# 	if i%2==0:
# 		n+=str(i) 	
# print(n)


# for i in range(1,6):
# 	print(i*'*')
# for i in range(6,0,-1):
# 	print(i*'*')


word=input('A')