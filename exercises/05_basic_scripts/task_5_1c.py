# -*- coding: utf-8 -*-
import re
'''
Задание 5.1c

Переделать скрипт из задания 5.1b таким образом, чтобы, при запросе параметра,
которого нет в словаре устройства, отображалось сообщение 'Такого параметра нет'.

> Попробуйте набрать неправильное имя параметра или несуществующий параметр,
чтобы увидеть какой будет результат. А затем выполняйте задание.

Если выбран существующий параметр,
вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
$ python task_4_5c.py
Введите имя устройства: r1
Введите имя параметра (ios, model, vendor, location, ip): ips
Такого параметра нет

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

device_list = list(london_co.keys())

print('\n>'+'-'*39+'\n')
mess = 'Введите имя устройства('+re.sub('[\[\]\']','',str(list(device_list)))+')\n:>'
device = input(mess)
if device not in device_list:
    print(' нет такого устройства в списке')
else:
    param_list = london_co[device].keys()
    mess = 'Введите праметр('+re.sub('[\[\]\']','',str(list(param_list)))+')\n:>'
    while True:
        param = input(mess)
        if param not in param_list:
            print(' нет такого параметра в списке')
            continue
        else: break
    print('\n param ',param,' = ', london_co[device][param] )
    print('-'*39+'<')    
        
        
        
'''
 В списке  3  устройств(а|o)

 Роутеров  2 , Свичей  1 

Введите имя устройства(r1, r2, sw1)
:>sw1
>---------------------------------------
 SWITCH     SW1 
----------------------------------------

 device    : switch         
 location  : 21 New Globe Walk
 vendor    : Cisco          
 model     : 3850           
 ios       : 3.6.XE         
 ip        : 10.255.0.101   
 vlans     : 10,20,30       
 routing   : True           

---------------------------------------<



------------------
(program exited with code: 0)
Press return to continue

'''
