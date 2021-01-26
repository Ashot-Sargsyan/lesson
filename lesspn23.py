'''Exception Handling'''
'''1)brnumek errore'''
# while True:
# 	try:
# 		age=int(input('age: '))
# 		break

# 	except NameError:
# 		print('something went wrong')
	
# 	except TypeError:
# 		print('tiv ev bar chi kareli gumarel')

# 	except ValueError:
# 		print('xndrumem grel tiv ayl voch te bar')



'''2)print aneq x vor error che ta'''
# try:
# 	print(x)
# except NameError:
# 	print('Xndrumenq mutk areq x chisht')


'''3)print areq 5/0 vor error che ta'''
# try:
# 	number1=5
# 	number2=0
# 	res=number1/number2
# 	print(res) 
# except ZeroDivisionError:
# 	print('Duq chek karox 0 bajanel')


'''4)else epa ashxatum 1 drvakum chi ashxatum kani vor print('hello') chishta grac u dra hamar vochmi xntir error chuneq 2 drvakum uneq error '''
# try:
# 	print('Hello')
# except:
# 	print('Something went wrong')
# else:
# 	print('Nothing went wrong')


# try:
# 	print(Hello)
# except:
# 	print('Something went wrong')
# else:
# 	print('Nothing went wrong')



'''5)erp chenk uzum cragire sharnaki ira gorcoxucune inch aneq '''
# try:
# 	print(x)

# except:
# 	print('Something went wrong')

# finally:
# 	print("The 'try except' is finished")


# try:
# 	a=int(input('write  something number: '))

# except KeyboardInterrupt:
# 	print('\nDuq kainacrik cragire CTRL+C gorcoxucunov')


'''6)'''
# x=-1
# if x<0:
# 	raise Exception("Sorry,no numbers below zero")

# try:
# 	x='hello'

# 	if not type(x) is int:
# 		raise TypeError('Only integers are allowed')

# except TypeError:
# 	print('you can only enter number')


'''7)'''
# list1=[12,56,80,9]
# try:
# 	print(list1[1])
# except IndexError:
# 	print('nman arjeq chunenq')
# finally:
# 	print('ok')


'''8)dictionary'''
# my_dictionary={'name':'ASH',}
# try:
# 	print(my_dictionary['nnn'])
# except KeyError:
# 	print('senc anunov chuneq key')



'''9)import modul chuneq tenc '''
# try:
# 	import sazdhghsa
# except ModuleNotFoundError:
# 	print('senc modul chuneq')



'''10)'''
# def my_function(assad):
	
# 	print(assad)
# try:
# 	my_function()
# except TypeError:
# 	print('Xndrumenq grek argument funkcyanere')

