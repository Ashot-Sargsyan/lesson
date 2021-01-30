'''JSON'''
'''1)'''
# import json

# file_json='about_users.json'

# player1 = {
# 	'name':'John',
# 	'age':18,
# 	'height':180,
# 	'awards':['master',3,2,1]
# }

# player2 ={
# 	'name':'Elizabet',
# 	'age':14,
# 	'height':178,
# 	'awards':[3,2,1]
# }

# myplayers = [player1,player2]
# with open(file_json,'w') as file:
# 	json.dump(myplayers,file) 

# file=open(file_json)
# json_data=json.load(file)
# for data in json_data:
# 	print(data)

# for data in json_data:
# 	print('\n Player name is ',data['name'])
# 	print('Player age is ',data['age'])
# 	print('Player height is ',data['height'])
# 	print('Player awards is ', data['awards'])

# 	if data['name']== 'John':
# 		data['name']= 'Snow'
# 		data['awards'].append('general')
# 		print('\n Player name is ',data['name'])
# 		print('Player awards is ', data['awards'])
# 		'''break'''#ete greink break elizabeti tvyalnere chi gri
# 		


# import json
# f='character_data.txt'
# try:
# 	with open(f) as file:
# 		user=json.load(file)
# 		print('hello',user)

# except FileNotFoundError:
# 	username=input('what is your name?')
# 	with open (f,'w') as file:
# 		user=json.dump(username,file)
# 		print('hello',username)

