students={
	'John':8,
	'Nick':9,
	'Elizabet':10,
	'Snoy':5,
	'Maik':7,
	'Anabel':6.5,
	'Arnak':10,
	'Ani':7,
	'Ashot':7,
	'Aleksandr':8
}
'''1)Task1'''
# count=0
# for i in students.values():
# 	count+=i
# result=count/len(students)
# print(result)


'''2)Task2'''
# max_reding=sorted(students.values())[-1]
# for i in students:
# 	if students[i] == max_reding:
# 		print(i,max_reding)



'''3)Task3'''	
# min_reding=sorted(students.values())[0]
# for i in students:
# 	if students[i]==min_reding:
# 		print(i,min_reding)



'''4)Task4'''
# for i in students:
# 	if students[i]>=5:
# 		print(i)



'''5)Task5'''
# for i in students:
# 	if students[i]<7:
# 		print(i)



'''6)Task6'''
# name=input('Please write your name:')
# if name in students:
# 	print(name,students[name])


'''7)Task7'''
# s='a,2,b,5,c,8,a,4,e,11'.split(',')
# c={}
# for i in range(0,len(s),2):
# 	if s[i] in c:
# 		c[s[i]]=int(s[i+1])+int(c[s[i]])
# 	else:	
# 		c[s[i]]=s[i+1]
# print(c)



'''8)Task8'''
# word='exercises'
# c={}
# for i in word:
# 	if i in c:
# 		c[i]=c[i]+1
# 	else:
# 		c[i]=1
# print(c)



