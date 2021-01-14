import random
count = 0

while True:
	
	if count==20:
		user  = int(input('number betwen (1) '))
		if user == 1:	
			print('win pc')
			break
		else:
			print('please write 1')	
			
	elif count == 19:
		user  = int(input('number betwen (1-2) '))
		if user == 2:
			print('win pc')
			break
		elif user == 1:
			print(count,'+',user,"=",count+user)
			count += user	
			print(count,"+ 1 = 21")
			print('win user')
			break

	else:
		user  = int(input('number betwen (1-3) '))		
			
	if 0<user<4 and count<19:
		print(count,'+',user,"=",count+user)
		count += user
		
		if count>20:
			print("win pc")
			break

		if count==20:
			print(count,"+ 1 = 21")
			print('win user')
			break

		elif count>16 and count<20:
			pc = 20-count	
			print(count,'+',pc,"=",20)
			count = 20
		elif count>12 and count<16:
			pc = 16-count	
			print(count,'+',pc,"=",count+pc)
			count+=pc	
		elif count>8 and count<12:
			pc = 12-count	
			print(count,'+',pc,"=",count+pc)
			count+=pc
		elif count>4 and count<8:
			pc = 8-count	
			print(count,'+',pc,"=",count+pc)
			count+=pc
		elif count>0 and count<4:
			pc = 4-count	
			print(count,'+',pc,"=",count+pc)
			count+=pc	
		else:	
			pc = random.randint(1,3)
			print(count,'+',pc,"=",count+pc)
			count+=pc
	elif 0 > user >3:
		print('please input 1-3')