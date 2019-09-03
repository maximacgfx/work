# -*- coding: utf-8 -*-
import re
'''
Задание 5.1b

Переделать скрипт из задания 5.1a таким образом, чтобы, при запросе параметра,
отображался список возможных параметров.

Вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
$ python task_5_2b.py
Введите имя устройства: r1
Введите имя параметра (ios, model, vendor, location, ip): ip
10.255.0.1

Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if.
'''

london_co = {
    'r1': {
		'device':'router',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
		'device':'router',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
		'device':'switch',
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

device_list = list(london_co.keys())
rw =0; #для подсчета устройств в списке London_co
sw =0;

for i in device_list:
	if london_co[i]['device'] == 'switch':
		sw+=1
	if london_co[i]['device'] == 'router':
		rw+=1
print ('\n В списке ',len(device_list), ' устройств(а|o)\n' )
print (' Роутеров ',rw , ', Свичей ',sw,'\n' )

mess = 'Введите имя устройства('+ re.sub( r'[\[\]\']', '', str(device_list))+')\n:>' 
device = input(mess)
if device in device_list:
	#print(' Устройство ',device, ' это ' ,london_co[device]['device'])
	print('-'*40+'\n', london_co[device]['device'].upper(), '   ', device.upper(),'\n'+'-'*40+'\n')
	param_list = list(london_co[device].keys())
	#print (param_list)
	for param in param_list:
		print(' %-10s: %-15s' % (param , london_co[device][param]))
