# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac1 = '0BAA:CEB0:CCCC'
mac2 = 'AAAA:BBBB:CCCC'

print (mac1)
print (mac2)

# ~ print(bin(int(mac1.replace(':',''),16))[2:])
# ~ print(bin(int(mac2.replace(':',''),16))[2:])


#len('{:0>48}'.format(bin(int(mac1.replace(':',''),16))[2:]))

print('{:0>48}'.format(bin(int(mac1.replace(':',''),16))[2:]))
print('{:0>48}'.format(bin(int(mac2.replace(':',''),16))[2:]))

