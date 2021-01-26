# print('Hi everyone, thank you for coming today ^_^')

# day=input('You all know what day it is or not?') == 'yes'
# print('Very well...and so whats next...',day)

# name=input('Please write yourname :')
# print(name,'','oooo you Arnak?','\n','Today is an important day for you')

# year = 1994
# print(year,type(year))
# print('Your age.. ',2020-int(year),'..am I right?')
# print(type((int(year))))

# import calendar
# year=int(input('My year is :'))
# month=int(input('My month is:'))
# print(calendar.month(year,month))

name=input('Please enter the word you need:')
for i in name:
	i=i.upper()
	if(i=='*'):
		print("    #    #         ####       ######    ######   #    #  \n    #    #        #    #      #    #    #    #    #  #   \n    ######        ######      ######    ######     ##    \n    #    #        #    #      #         #          ##    \n    #    #        #    #      #         #          ##    \n\n")
	elif(i=='+'):
		print('    #####       ######       #####    ######      #    #        #####         ####       #    #  \n    #    #        ##        #    #      ##        #    #        #    #       #    #       #  #   \n    #####         ##        # ##        ##        ######        #    #       ######        ##    \n    #    #        ##        #   #       ##        #    #        #    #       #    #        ##    \n    #####       ######      #    #      ##        #    #        #####        #    #        ##    \n\n')
	