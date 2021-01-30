'''1'''
# import json#importenq are json 
# def result(file_name,peoples,raiting):#funkcyanq stexce vore entunuma 3 argument

# 	classes={}#miat taza datark dictionarienq bace
# 	for i,j in zip(peoples,raiting):#ciklenq sarkum vor vekali miat arjek peoplic miat raitingic 
# 		classes[i]=j

# 	students={'students':classes}

# 	try:
# 		f=open(file_name)#bacumenk faile 
# 		return json.load(f)#veradarcnumek u karta(load) mer faile
# 	except FileNotFoundError:
# 		f=open(file_name,'w')#baci mer faile u gri meche
# 		json.dump(students,f,sort_keys=True,indent=4)#avelasni mer faili mech dictionary sort_key =est aibubeni keyere sortavoruma , indent =4 ostupa tali 4 tab u gruma irar tak
# 		return 'File created and updated successfully'
# 	finally:
# 		f.close()#pagi mer faile

# file_name='User.json'
# peoples=['John','Snow','Elizabet']
# raiting=[10,7,5]
# res=result(file_name,peoples,raiting)
# print(res)



'''2'''
# import json

# def music(artist,word):
	
# 	songs={}
# 	for i,j in zip(artist,word):
# 		songs[i]=j

# 	database_artist={'singer':songs}

# 	try:
# 		f=open(file_name)
# 		return json.load(f)
# 	except FileNotFoundError:
# 		f=open(file_name,'w')
# 		json.dump(database_artist,f,indent=4)
# 		return 'File created and updated successfully'
# 	finally:
# 		f.close()

# file_name='music_information'
# artist=['Britney Spears','Acon','Jastin Timberlayd','Elman']
# word=['Criminal','Africa','Say Something','My ocean']

# res=music(artist,word)
# print(res)


'''3'''
# import json
# def myfunction(file_name,number):
# 	sume=0
# 	for x in range(1,number+1):
# 		if x%3==0 or x%5==0 :
# 			sume+=x
# 	return sume

# 	try:
# 		f=open(file_name)
# 		return json.load(f)
# 	except FileNotFoundError:
# 		f=open(file_name,'w')
# 		json.dump(sume,f)
# 		return 'File created and updated successfully'
# 	finally:
# 		f.close()
# file_name='modules.json'
# number=int(input('write your number : '))
# print(myfunction(file_name,number))