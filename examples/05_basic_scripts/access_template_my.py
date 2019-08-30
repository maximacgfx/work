import sys
from sys import argv

#for i in argv :
#	print (i,type(i))

if len(argv) == 1:

	plan_text='''
........................................................................

Функция запушена без аргумета	
Пример использования
	 
access_template  Fa0/1  10

........................................................................
	 
	 '''
	print(plan_text)	
	sys.exit()
interface = input('Enter interface type and number : ')
vlan = input('Enter VLAN number: ')

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

print('\n' + '-' * 30)
print('interface {}'.format(interface))
print('\n'.join(access_template).format(vlan))
