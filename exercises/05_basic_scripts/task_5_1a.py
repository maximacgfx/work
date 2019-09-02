# -*- coding: utf-8 -*-
import re
'''
Задание 5.1a

Переделать скрипт из задания 5.1 таким образом, чтобы,
кроме имени устройства, запрашивался также параметр устройства, который нужно отобразить.

Вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
$ python task_5_2a.py
Введите имя устройства: r1
Введите имя параметра: ios
15.4

Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if.
'''

london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
#	for param in param_list:
#		print(param)


device_list = london_co.keys()
print('\n device_list = london_co.keys()  это',type(device_list))
print('#'*40)
print('\n Список устройств', re.sub( r'[\[\]\']','', str(list(device_list ))))
name  = input (' Введите имя устройства >: ')

if name  in device_list:
	
	#print(type(london_co[name]))	тип данных 
	param_list = london_co[name].keys()
	#Ввод данных, подготовка форматированной строки ввода
	mess = ' Введите параметр устройства\n ('+ re.sub(r'[\[\]\']','',str(list(param_list)))+')\n >:'# 1 вариант
	param = input(mess)# 1 вариант
	#param  = input (' Введите параметр устройства\n('+ re.sub(r'[\[\]\']','',str(list(param_list)))+'): ')
	#можно встроить все в одну сторку но так более запутанно
	print('-'*40)
	if param in param_list:
		print(' {:10}: {:15}'.format(param.capitalize(),london_co[name][param]))
		# Функция ''.format() не выводит значени False True None
	print('-'*40)
	for param in param_list:
		#  тогда старым методом все прекрасно выводиться
		print(' %-10s: %-15s ' % (param.capitalize(),london_co[name][param]))	
	print('-'*40)
'''
 ПРИМЕР ФОРМАТИРОВАННОГО ВВОДА 
 
 Список устройств r1, r2, sw1
 Введите имя устройства: sw1
 Введите параметр устройства
 (location, vendor, model, ios, ip, vlans, routing)
 >:

'''
