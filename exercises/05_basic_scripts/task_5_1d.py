# -*- coding: utf-8 -*-
import re
'''
Задание 5.1d

Переделать скрипт из задания 5.1c таким образом, чтобы, при запросе параметра,
пользователь мог вводить название параметра в любом регистре.

Пример выполнения скрипта:
$ python task_5_2d.py
Введите имя устройства: r1
Введите имя параметра (ios, model, vendor, location, ip): IOS
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

device_list =london_co.keys()

mess = 'введите имя устройства('+ re.sub('[\[\]\']','',str(list(device_list)))+')\n:>'
print('>'+'-'*39)
count = 0;

while count <= 10:
    device = input(mess)
    if device not in device_list:
        print(count,' Нет такого устройсва в списке. Повторите ввод')        
        count +=1
        continue
    else:break
param_list = london_co[device].keys()
mess = 'введите параметр ('+ re.sub('[\[\]\']','',str(list(param_list)))+')\n:>'
param = input(mess)

#debug
#print('param in param_list', param in param_list)
#print('param.UP =', param.upper() ,' in param_list', param.upper() in param_list)
#print('param.lower =', param.lower() ,' in param_list', param.lower() in param_list)

if( (param in param_list) or (param.lower() in param_list)) :
    print('\n param ',param,' = ', london_co[device][param.lower()] )
    print('-'*39+'<')
else:
    print(' нет такого параметра в списке')




