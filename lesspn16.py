#Dictionary
# thisdict={'name':'Ashot','year':1994,'hobbi':'box'}
# print(thisdict)

# thisdict={'name':'Ashot','year':1994,'hobbi':'box'}
# x=thisdict.popitem()#verchic hobbin hanuma
# print(thisdict)


# thisdict={'name':'Ashot','year':1994,'hobbi':'box'}
# thisdict['year']=2016#yeare popoxumenq 1994 poxumenq 2016 luboi kei karanq poxenq senc
# print(thisdict)


# thisdict={'name':'Ashot','year':1994,'hobbi':'box'}
# print(len(thisdict))#asuma konkret item unem ira mech aysiqn name u ashot irar grec (kei u value)


# thisdict={'name':'Ashot','year':1994,'hobbi':'box'}
# thisdict['age']=26#taza keya vercnum u grum thisdisti mech
# print(thisdict)

# thisdict=dict(brand='Ford',model='Mustang',year=1964)
# print(thisdict)


# web={
# 	'name':'Ashot',
# 	'age':24,
# 	'year':1996,
# 	'email':'ashot.s96@lis.ru'
# }
# for i in web:#kame grenq web.keys() tarberucun che ka 
# 	print(i,end=' ')#gri sax mi toxi vra ende eta nshanakum

# for i,j in web.items():#i-key j-value
# 	print(i,j)


# thisdict={
# 	'name1':'Ashot',
# 	'name2':'Arnak',
# 	'name3':'Ani',
# 	'name4':'Raz'
# }
# name=input('please write name wich wanted:')
# if name in thisdict.values():
# 	print('yes we have a student')
# else:
# 	print('sorry ,but we dont have a student')

# name=input('please write name wich wanted:')
# thisdict={
# 	'name1':'Ashot',
# 	'name2':'Arnak',
# 	'name3':'Ani',
# 	'name4':'Raz'
# }
# for i in thisdict:
# 	if name == thisdict[i]:
# 		print('yes we have a student')


# thisdict={
# 	'name1':'Ashot',
# 	'name2':'Arnak',
# 	'name3':'Ani',
# 	'name4':'Raz'
# }
# thisdict['name3']='Nick'
# print(thisdict)


# thisdict={
# 	'name':'Ashot',
# 	'age':24,
# 	'year':1996
# }

# if 'age' in thisdict:
# 	del thisdict['age']
# 	print('lets go')
# else:
# 	print('sorry but dont have a key age')

# count=0
# thisdict={
# 	'a':12,
# 	'b':20
# }
# for i in thisdict.values():
# 	count+=i
# print(count)

# list1=[]
# thisdict={
# 	'a':12,
# 	'b':20
# }
# for i in thisdict.values():
# 	list1.append(i)
# print(max(list1))
# 	


# list1=[]
# thisdict={
# 	'a':12,
# 	'b':20
# }
# for i in thisdict.values():
# 	list1.append(i)
# print(max(list1))
	
# count=0#gumare
# list1=[10,12,65,2.85,-5]
# for i in list1:
# 	count+=i
# print(count)

# count=1#ankame
# list1=[10,12,65,2.85,-5]
# for i in list1:
# 	count*=i
# print(count)

# list1=[10,12,65,2.85,-5]#max
# c=list1[0]
# for i in list1:
# 	if i>c:
# 		c=i
# print(c)

# list1=[10,12,65,2.85,-5]#min
# c=list1[0]
# for i in list1:
# 	if i<c:
# 		c=i
# print(c)

# list1=[]
# thisdict={
# 	'number1':1,
# 	'number2':2,
# 	'number3':5,
# 	'number4':7,
# 	'number5':10,
# 	'number6':0,
# 	'number7':2.85
# }
# numbers=float(input('write your number: '))
# for i,j in thisdict.items():
# 	if j==numbers:
# 		print(i)
# 		break
# else:
# 	print('error')


# list1=[]
# thisdict={
# 	'number1':1,
# 	'number2':2,
# 	'number3':5,
# 	'number4':7,
# 	'number5':10,
# 	'number6':0,
# 	'number7':2.85
# }
# print(sorted(thisdict.values())[-2])

# list1=[]
# thisdict={
# 	'number1':1,
# 	'number2':2,
# 	'number3':5,
# 	'number4':7,
# 	'number5':10,
# 	'number6':0,
# 	'number7':2.85
# }
# print(sorted(thisdict.values())[0])#kani vor poqric mecen sortavorum 0 grum arachi sortavore beri amena poqre