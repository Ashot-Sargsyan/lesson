import random 

print('       Hi you play Tic Tac Toe ')
print('')

all_steps=[1,2,3,4,5,6,7,8,9]

def print_tablo ():
	print('')
	print('')
	print('     ',all_steps[0],'|',all_steps[1],'|',all_steps[2],' ')
	print('     --- --- --- ')
	print('     ',all_steps[3],'|',all_steps[4],'|',all_steps[5],'')
	print('     --- --- --- ')
	print('     ',all_steps[6],'|',all_steps[7],'|',all_steps[8],' ')
	print('')
	print('')
print_tablo ()
c=[]
point=0
while True:
	while True:
		user=int(input('where do you want to put the cross? '))
		if user in all_steps:
			print('user:',user)
			all_steps[user-1]='x'
			print_tablo()
			c.append(user)
			break
		else:
			print('et toxe zbaxvaca')
			continue
	if all_steps[0]==all_steps[1]==all_steps[2]=='x' or all_steps[3]==all_steps[4]==all_steps[5]=='x' or all_steps[6]==all_steps[7]==all_steps[8]=='x' or all_steps[0]==all_steps[4]==all_steps[8]=='x' or all_steps[2]==all_steps[4]==all_steps[6]=='x' or all_steps[0]==all_steps[3]==all_steps[6]=='x' or all_steps[1]==all_steps[4]==all_steps[7]=='x' or all_steps[2]==all_steps[5]==all_steps[8]=='x':
		point+=1
		print('the win user',point)
		break
	if len(c)==9:
		break			
	while True:	
		pc=random.randint(1,10)
		if pc in all_steps:
			print('pc:',pc)
			all_steps[pc-1]='o'
			print_tablo()
			c.append(user)
			break
		else:
			print('et toxe zbaxvaca')
			continue

	if all_steps[0]==all_steps[1]==all_steps[2]=='o' or all_steps[3]==all_steps[4]==all_steps[5]=='o' or all_steps[6]==all_steps[7]==all_steps[8]=='o' or all_steps[0]==all_steps[4]==all_steps[8]=='o' or all_steps[2]==all_steps[4]==all_steps[6]=='o' or all_steps[0]==all_steps[3]==all_steps[6]=='o' or all_steps[1]==all_steps[4]==all_steps[7]=='o' or all_steps[2]==all_steps[5]==all_steps[8]=='o':
		point+=1
		print('the win pc',point)
		break

	