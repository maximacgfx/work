# -*- coding: utf-8 -*-

'''
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ip = '192.168.3.192'

a,b,c,d = ip.split('.')


print ('{:9}{:9}{:9}{:9}'.format(a,b,c,d))
print ('{:08b} {:08b} {:08b} {:08b} '.format(int(a),int(b),int(c),int(d)))





#Сравни для метода
#		print('%-9s%-9s%-9s%-9s' % tuple(ip.split(sep='.')))
# ~ 	for y in tuple([int(i) for i in ip.split(sep='.')]):
# ~ 	print('%08d' % int(bin(y)[2:]), end=' ')







#  опыт - сын ошибок трудных
#print('%08d%08d%08d%08d' % tuple([int(i) for i in ip.split(sep='.')]))

#[180]: '%08d' % int(bin('1')[2:])

#tuple([int(i) for i in ip.split(sep='.')])




'''
In [1]: ip = '192.168.3.1'

In [2]: ip.split()
Out[2]: ['192.168.3.1']

In [3]: ip.split?
Signature: ip.split(sep=None, maxsplit=-1)
Docstring:
Return a list of the words in the string, using sep as the delimiter string.

sep
  The delimiter according which to split the string.
  None (the default value) means split according to any whitespace,
  and discard empty strings from the result.
maxsplit
  Maximum number of splits to do.
  -1 (the default value) means no limit.
Type:      builtin_function_or_method

In [4]: ip.split(sep=',')
Out[4]: ['192.168.3.1']

In [5]: ip.split(sep='.')
Out[5]: ['192', '168', '3', '1']

In [6]: '{:<10}{:<10}{:<10}{:<10} '.format(ip.split(sep='.'))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-ad2d1c904960> in <module>
----> 1 '{:<10}{:<10}{:<10}{:<10} '.format(ip.split(sep='.'))

TypeError: unsupported format string passed to list.__format__

In [7]: format?
Signature: format(value, format_spec='', /)
Docstring:
Return value.__format__(format_spec)

format_spec defaults to the empty string.
See the Format Specification Mini-Language section of help('FORMATTING') for
details.
Type:      builtin_function_or_method

In [8]: '{:<10}{:<10}{:<10}{:<10} '.format(for i in range(ip.split(sep='.')))
  File "<ipython-input-8-c79bc24656ff>", line 1
    '{:<10}{:<10}{:<10}{:<10} '.format(for i in range(ip.split(sep='.')))
                                         ^
SyntaxError: invalid syntax


In [9]: '{:<10}{:<10}{:<10}{:<10} '.format(for i in range(ip.split(sep='.')):)
  File "<ipython-input-9-4c4ddecf92bb>", line 1
    '{:<10}{:<10}{:<10}{:<10} '.format(for i in range(ip.split(sep='.')):)
                                         ^
SyntaxError: invalid syntax


In [10]: (ip.split(sep='.'))
Out[10]: ['192', '168', '3', '1']

In [11]: data = (ip.split(sep='.'))

In [12]: data
Out[12]: ['192', '168', '3', '1']

In [13]: for d in data
  File "<ipython-input-13-ac46c581760c>", line 1
    for d in data
                 ^
SyntaxError: invalid syntax


In [14]: for d in data:
    ...:     printd
    ...:
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-14-e25cccc6609f> in <module>
      1 for d in data:
----> 2     printd
      3

NameError: name 'printd' is not defined

In [15]: for d in data:
    ...:     print(d)
    ...:
    ...:
192
168
3
1

In [16]: '{:<10}{:<10}{:<10}{:<10} '.format(for i in data)
  File "<ipython-input-16-0ebd6c3b21c5>", line 1
    '{:<10}{:<10}{:<10}{:<10} '.format(for i in data)
                                         ^
SyntaxError: invalid syntax


In [17]: '{:<10}{:<10}{:<10}{:<10} '.format(for i in data:)
  File "<ipython-input-17-739038695e22>", line 1
    '{:<10}{:<10}{:<10}{:<10} '.format(for i in data:)
                                         ^
SyntaxError: invalid syntax


In [18]: '{:<10}{:<10}{:<10}{:<10} '.format(str(for i in data))
  File "<ipython-input-18-c11961f66058>", line 1
    '{:<10}{:<10}{:<10}{:<10} '.format(str(for i in data))
                                             ^
SyntaxError: invalid syntax


In [19]: '{:<10}'.format(ip.split(serp='.'))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-19-3f06d884f28d> in <module>
----> 1 '{:<10}'.format(ip.split(serp='.'))

TypeError: 'serp' is an invalid keyword argument for split()

In [20]: '{:<10}'.format(ip.split(sep='.'))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-20-272eeee0ff9d> in <module>
----> 1 '{:<10}'.format(ip.split(sep='.'))

TypeError: unsupported format string passed to list.__format__

In [21]: '{:<10}'.format(ip.split(sep='.'))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-21-272eeee0ff9d> in <module>
----> 1 '{:<10}'.format(ip.split(sep='.'))

TypeError: unsupported format string passed to list.__format__

In [22]: data
Out[22]: ['192', '168', '3', '1']

In [23]: data.keys()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-23-43ebc71570da> in <module>
----> 1 data.keys()

AttributeError: 'list' object has no attribute 'keys'

In [24]: int(data)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-24-c07095f4a360> in <module>
----> 1 int(data)

TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'

In [25]: int(data[])
  File "<ipython-input-25-06a26e6fb069>", line 1
    int(data[])
             ^
SyntaxError: invalid syntax


In [26]: data[0]
Out[26]: '192'

In [27]: %history
ip = '192.168.3.1'
ip.split()
ip.split?
ip.split(sep=',')
ip.split(sep='.')
'{:<10}{:<10}{:<10}{:<10} '.format(ip.split(sep='.'))
format?
'{:<10}{:<10}{:<10}{:<10} '.format(for i in range(ip.split(sep='.')))
'{:<10}{:<10}{:<10}{:<10} '.format(for i in range(ip.split(sep='.')):)
(ip.split(sep='.'))
data = (ip.split(sep='.'))
data
for d in data
for d in data:
    printd
for d in data:
    print(d)
'{:<10}{:<10}{:<10}{:<10} '.format(for i in data)
'{:<10}{:<10}{:<10}{:<10} '.format(for i in data:)
'{:<10}{:<10}{:<10}{:<10} '.format(str(for i in data))
'{:<10}'.format(ip.split(serp='.'))
'{:<10}'.format(ip.split(sep='.'))
'{:<10}'.format(ip.split(sep='.'))
data
data.keys()
int(data)
int(data[])
data[0]
%history

In [28]: data = (ip.split(sep='.'))

In [29]: data
Out[29]: ['192', '168', '3', '1']

In [30]: type(data)
Out[30]: list

In [31]: '{} {} {} {}'.format(data)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-31-6117856747bf> in <module>
----> 1 '{} {} {} {}'.format(data)

IndexError: tuple index out of range

In [32]: '{} {} {} {}{}'.format(data)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-32-e1b6f438e1b3> in <module>
----> 1 '{} {} {} {}{}'.format(data)

IndexError: tuple index out of range

In [33]: data
Out[33]: ['192', '168', '3', '1']

In [34]: data = (ip.split(sep='.'))

In [35]: result = [int(item) for item i a]
  File "<ipython-input-35-7f47b862d6e0>", line 1
    result = [int(item) for item i a]
                                 ^
SyntaxError: invalid syntax


In [36]: result = [int(item) for item i data]
  File "<ipython-input-36-880e2fb9c619>", line 1
    result = [int(item) for item i data]
                                 ^
SyntaxError: invalid syntax


In [37]: result = [int(item) for item in data]

In [38]: result
Out[38]: [192, 168, 3, 1]

In [39]: '{} {} {} {}{}'.format(result)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-39-0dbe504ffc7b> in <module>
----> 1 '{} {} {} {}{}'.format(result)

IndexError: tuple index out of range

In [40]: '{} {} {} {}'.format(result)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-40-10207bb35704> in <module>
----> 1 '{} {} {} {}'.format(result)

IndexError: tuple index out of range

In [41]: '{} {} {} {}'.format([1,2,3,4])
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-41-8b20d6ee5c0a> in <module>
----> 1 '{} {} {} {}'.format([1,2,3,4])

IndexError: tuple index out of range

In [42]:

In [42]: '{:08b} {:08b} {:08b} {:08b}'.format(192, 100, 1, 1)
Out[42]: '11000000 01100100 00000001 00000001'

In [43]: '{:08b} {:08b}{:08b}{:08b}'.format(192, 100, 1, 1)
Out[43]: '11000000 011001000000000100000001'

In [44]: data
Out[44]: ['192', '168', '3', '1']

In [45]: result
Out[45]: [192, 168, 3, 1]

In [46]: '{:08b} {:08b}{:08b}{:08b}'.format(result)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-46-4d6479204fe4> in <module>
----> 1 '{:08b} {:08b}{:08b}{:08b}'.format(result)

TypeError: unsupported format string passed to list.__format__

In [47]: ip = '192.168.3.1'

In [48]:

In [48]: data = ip.split(sep='.')

In [49]: ip_template =
    ...:     10.1.10.1
    ...: {0:<8} {1:<8} {2:<8} {3:<8}
    ...: {0:08b} {1:08b} {2:08b} {3:08b}
    ...: 

In [50]: p1 = data[0]

In [51]: p2 = data[1]

In [52]: p3 = data[2]

In [53]: p4 = data[3]

In [54]: print (ip_template.format(p1,p2,p3,p4))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-54-135454c40d79> in <module>
----> 1 print (ip_template.format(p1,p2,p3,p4))

ValueError: Unknown format code 'b' for object of type 'str'

In [55]: print (ip_template.format(int(p1),int(p2),int(p3),int(p4)))

    10.1.10.1
192      168      3        1
11000000 10101000 00000011 00000001


In [56]: data = ip.split(sep='.')

In [57]: data
Out[57]: ['192', '168', '3', '1']

In [58]: data = int(ip.split(sep='.'))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-58-08594caa1515> in <module>
----> 1 data = int(ip.split(sep='.'))

TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'

In [59]: data = ip.split(sep='.')

In [60]: data
Out[60]: ['192', '168', '3', '1']

In [61]: int(data)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-61-c07095f4a360> in <module>
----> 1 int(data)

TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'



Exception list index out of range
Press ENTER to continue...
In [62]: tuple(data)
Out[62]: ('192', '168', '3', '1')

In [63]: print (ip_template.format(tuple(data)))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-63-e8b037e1bc1d> in <module>
----> 1 print (ip_template.format(tuple(data)))

TypeError: unsupported format string passed to tuple.__format__

In [64]: data2 = tuple(data)

In [65]: print (ip_template.format(data2))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-65-d64f9097d7b1> in <module>
----> 1 print (ip_template.format(data2))

TypeError: unsupported format string passed to tuple.__format__

In [66]: dada2
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-66-856b9d84ff45> in <module>
----> 1 dada2

NameError: name 'dada2' is not defined

In [67]: data2
Out[67]: ('192', '168', '3', '1')

In [68]: '{} {} {} {}'.format(data2)
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-68-e7ed9a77c2fc> in <module>
----> 1 '{} {} {} {}'.format(data2)

IndexError: tuple index out of range

In [69]: data = int(ip.split(sep='.'))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-69-08594caa1515> in <module>
----> 1 data = int(ip.split(sep='.'))

TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'

In [70]: data =ip.split(sep='.')

In [71]: data
Out[71]: ['192', '168', '3', '1']

In [72]: '%s %s %s %s' % data
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-72-aaa2035fb0f6> in <module>
----> 1 '%s %s %s %s' % data

TypeError: not enough arguments for format string

In [73]: '%s %s %s %s' % (data)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-73-48839c61cb2f> in <module>
----> 1 '%s %s %s %s' % (data)

TypeError: not enough arguments for format string

In [74]: data
Out[74]: ['192', '168', '3', '1']

In [75]: tuple(data)
Out[75]: ('192', '168', '3', '1')

In [76]: '%s %s %s %s' % (tuple(data))
Out[76]: '192 168 3 1'

In [77]: ip = '234.23.34.2'

In [78]: tuple(ip.split(sep='.'))
Out[78]: ('234', '23', '34', '2')

In [79]: print('%+8d%+8d%+8d%+8d' %    tuple(ip.split(sep='.')))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-79-4c3ddc9e1453> in <module>
----> 1 print('%+8d%+8d%+8d%+8d' %    tuple(ip.split(sep='.')))

TypeError: %d format: a number is required, not str

In [80]: print('%+8d%+8d%+8d%+8d' %    tuple(ip.split(sep='.')))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-80-4c3ddc9e1453> in <module>
----> 1 print('%+8d%+8d%+8d%+8d' %    tuple(ip.split(sep='.')))

TypeError: %d format: a number is required, not str

In [81]: tuple(ip.split(sep='.'))
Out[81]: ('234', '23', '34', '2')

In [82]: '%s %s %s %s ' %tuple(ip.split(sep='.'))
Out[82]: '234 23 34 2 '

In [83]: '%s %s %s %s' %tuple(ip.split(sep='.'))
Out[83]: '234 23 34 2'

In [84]: print('%s %s %s %s' %tuple(ip.split(sep='.')))
234 23 34 2

In [85]: print('%+8s %s %s %s' %tuple(ip.split(sep='.')))
     234 23 34 2

In [86]: print('%-8s %s %s %s' %tuple(ip.split(sep='.')))
234      23 34 2

In [87]: print('%-8s %-8s %s %s' %tuple(ip.split(sep='.')))
234      23       34 2

In [88]: print('%-8s %-8s %-8s %-8s' %tuple(ip.split(sep='.')))
234      23       34       2

In [89]: ip='1.12.3.9'

In [90]: print('%-8s %-8s %-8s %-8s' %tuple(ip.split(sep='.')))
1        12       3        9

In [91]: tuple(ip.split(sep='.'))
Out[91]: ('1', '12', '3', '9')

In [92]: print('%-8b %-8b %-8b %-8b' %tuple(ip.split(sep='.')))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-92-5e4d3a2e89c2> in <module>
----> 1 print('%-8b %-8b %-8b %-8b' %tuple(ip.split(sep='.')))

ValueError: unsupported format character 'b' (0x62) at index 3

In [93]: print('%-8x %-8x %-8x %-8x' %tuple(ip.split(sep='.')))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-93-450f6f006d98> in <module>
----> 1 print('%-8x %-8x %-8x %-8x' %tuple(ip.split(sep='.')))

TypeError: %x format: an integer is required, not str

In [94]: print('%-8x %-8x %-8x %-8x' %tuple(ip.split(sep='.')))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-94-450f6f006d98> in <module>
----> 1 print('%-8x %-8x %-8x %-8x' %tuple(ip.split(sep='.')))

TypeError: %x format: an integer is required, not str

In [95]: ip2 =(12,12,12,12)

In [96]: print('%-8s %-8s %-8s %-8s' %tuple(ip2.split(sep='.')))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-96-7d34df8e9a3b> in <module>
----> 1 print('%-8s %-8s %-8s %-8s' %tuple(ip2.split(sep='.')))

AttributeError: 'tuple' object has no attribute 'split'

In [97]: print('%-8d %-8d %-8d %-8d' %tuple(ip2.split(sep='.')))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-97-429d40044f43> in <module>
----> 1 print('%-8d %-8d %-8d %-8d' %tuple(ip2.split(sep='.')))

AttributeError: 'tuple' object has no attribute 'split'

In [98]: print('%-8d %-8d %-8d %-8d' % ip2)
12       12       12       12

In [99]: print('%-8d %-8d %-8d %-8s' % ip2)
12       12       12       12

In [100]: print('%-8d %-8d %-8d %-8d' % ip2)
12       12       12       12

In [101]: type(ip2)
Out[101]: tuple

In [102]: ip2.count?
Signature: ip2.count(value, /)
Docstring: Return number of occurrences of value.
Type:      builtin_function_or_method

In [103]: op2
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-103-b2224c83b41c> in <module>
----> 1 op2

NameError: name 'op2' is not defined

In [104]: ip2
Out[104]: (12, 12, 12, 12)

In [105]: ip2[1]
Out[105]: 12

In [106]: ip[1]
Out[106]: '.'

In [107]: ip
Out[107]: '1.12.3.9'

In [108]: idata
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-108-ed808df6ca02> in <module>
----> 1 idata

NameError: name 'idata' is not defined

In [109]: data
Out[109]: ['192', '168', '3', '1']

In [110]: data[1]
Out[110]: '168'

In [111]: bin(data[1])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-111-47d91149336f> in <module>
----> 1 bin(data[1])

TypeError: 'str' object cannot be interpreted as an integer

In [112]: bin(int(data[1]))
Out[112]: '0b10101000'

In [113]: int(data[1])
Out[113]: 168

In [114]: or i in data:
     ...:     print(data)
  File "<ipython-input-114-20a0d2101f54>", line 1
    or i in data:
     ^
SyntaxError: invalid syntax


In [115]: or i in data:
     ...:     print(i)
  File "<ipython-input-115-5e5486d05434>", line 1
    or i in data:
     ^
SyntaxError: invalid syntax


In [116]: for i in data:
     ...:     print(i)
     ...:
192
168
3
1

In [117]: for i in data:
     ...:     print(bin(int(i)))
     ...:
0b11000000
0b10101000
0b11
0b1

In [118]: for i in data:
     ...:     data3.appdend(bin(int(i)))
     ...:
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-118-04ac2d1a8518> in <module>
      1 for i in data:
----> 2     data3.appdend(bin(int(i)))
      3

NameError: name 'data3' is not defined

In [119]: for i in data:
     ...:     data3.appdend(bin(int(i)))
     ...:
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-119-04ac2d1a8518> in <module>
      1 for i in data:
----> 2     data3.appdend(bin(int(i)))
      3

NameError: name 'data3' is not defined

In [120]: data2=()

In [121]: for i in data:
     ...:     data2.appdend(bin(int(i)))
     ...:
     ...:
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-121-0cf50d3fba65> in <module>
      1 for i in data:
----> 2     data2.appdend(bin(int(i)))
      3
      4

AttributeError: 'tuple' object has no attribute 'appdend'

In [122]: data2=[]

In [123]: for i in data:
     ...:     data2.appdend(bin(int(i)))
     ...:
     ...:
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-123-0cf50d3fba65> in <module>
      1 for i in data:
----> 2     data2.appdend(bin(int(i)))
      3
      4

AttributeError: 'list' object has no attribute 'appdend'

In [124]: type(data2)
Out[124]: list

In [125]: for i in data:
     ...:     data2.apend(bin(int(i)))
     ...:
     ...:
     ...:
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-125-db2acb2216c1> in <module>
      1 for i in data:
----> 2     data2.apend(bin(int(i)))
      3
      4
      5

AttributeError: 'list' object has no attribute 'apend'

In [126]: for i in data:
     ...:     data2.append(bin(int(i)))
     ...:
     ...:
     ...:

In [127]: data
Out[127]: ['192', '168', '3', '1']

In [128]: data2
Out[128]: ['0b11000000', '0b10101000', '0b11', '0b1']

In [129]: bin?
Signature: bin(number, /)
Docstring:
Return the binary representation of an integer.

>>> bin(2796202)
'0b1010101010101010101010'
Type:      builtin_function_or_method

In [130]: bin()?
  File "<ipython-input-130-253a7bd4d6a5>", line 1
    bin()?
         ^
SyntaxError: invalid syntax


In [131]: bin(1)
Out[131]: '0b1'

In [132]: '%-8'% bin(1)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-132-0abfa5c409e5> in <module>
----> 1 '%-8'% bin(1)

ValueError: incomplete format

In [133]: '%-8s'% bin(1)
Out[133]: '0b1     '

In [134]: '%08s'% bin(1)
Out[134]: '     0b1'

In [135]: '%80s'% bin(1)
Out[135]: '                                                                             0b1'

In [136]: '%0s'% bin(1)
Out[136]: '0b1'

In [137]: '%-0s'% bin(1)
Out[137]: '0b1'

In [138]: '%+10s' % 25
Out[138]: '        25'

In [139]: '%+10f' % 25
Out[139]: '+25.000000'

In [140]: '%+10d' % 25
Out[140]: '       +25'

In [141]: '%+0d' % 25
Out[141]: '+25'

In [142]: '%0d' % 25
Out[142]: '25'

In [143]: '%0-d' % 25
Out[143]: '25'

In [144]: '%0+d' % 25
Out[144]: '+25'

In [145]: '%0 d' % 25
Out[145]: ' 25'

In [146]: '%0  d' % 25
Out[146]: ' 25'

In [147]: '%0    d' % 25
Out[147]: ' 25'

In [148]: '%0    10d' % 25
Out[148]: ' 000000025'

In [149]: '%08d' % 25
Out[149]: '00000025'

In [150]: '%08d' % bin(12)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-150-f49593deee97> in <module>
----> 1 '%08d' % bin(12)

TypeError: %d format: a number is required, not str

In [151]: '%08d' % str(bin(12))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-151-5e6dd67ca84f> in <module>
----> 1 '%08d' % str(bin(12))

TypeError: %d format: a number is required, not str

In [152]: '%08s' % str(bin(12))
Out[152]: '  0b1100'

In [153]: '%010s' % str(bin(12))
Out[153]: '    0b1100'

In [154]: '%0-10s' % str(bin(12))
Out[154]: '0b1100    '

In [155]: '%0+10s' % str(bin(12))
Out[155]: '    0b1100'

In [156]: '%0+10s' % 12
Out[156]: '        12'

In [157]: '%010s' % 12
Out[157]: '        12'

In [158]: '%-010s' % 12
Out[158]: '12        '

In [159]: '%-010d' % 12
Out[159]: '12        '

In [160]: '%010d' % 12
Out[160]: '0000000012'

In [161]: '%010d' % bin(12)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-161-579cbc1bf0b0> in <module>
----> 1 '%010d' % bin(12)

TypeError: %d format: a number is required, not str

In [162]: '%010d' % bin(12)[;2]
  File "<ipython-input-162-81de9f52a166>", line 1
    '%010d' % bin(12)[;2]
                      ^
SyntaxError: invalid syntax


In [163]: '%010d' % bin(12)[:2]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-163-4962058a8eb1> in <module>
----> 1 '%010d' % bin(12)[:2]

TypeError: %d format: a number is required, not str

In [164]: '%010d' % int(bin(12)[:2])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-164-0aa6f5864baf> in <module>
----> 1 '%010d' % int(bin(12)[:2])

ValueError: invalid literal for int() with base 10: '0b'

In [165]:  int(bin(12)[:2])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-165-77647ee085dc> in <module>
----> 1 int(bin(12)[:2])

ValueError: invalid literal for int() with base 10: '0b'

In [166]: bin(12)[:2]
Out[166]: '0b'

In [167]: bin(12)[2:]
Out[167]: '1100'

In [168]:  int(bin(12)[:2])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-168-77647ee085dc> in <module>
----> 1 int(bin(12)[:2])

ValueError: invalid literal for int() with base 10: '0b'

In [169]:  int(bin(12)[2:])
Out[169]: 1100

In [170]:  int(bin(12)[2:])
Out[170]: 1100

In [171]: '%08d' % int(bin(12)[2:])
Out[171]: '00001100'

In [172]: data
Out[172]: ['192', '168', '3', '1']

In [173]: data2
Out[173]: ['0b11000000', '0b10101000', '0b11', '0b1']

In [174]: '%08d' % int(bin(12)[2:])
Out[174]: '00001100'

In [175]: '%08d' % int(bin(2)[2:])
Out[175]: '00000010'

In [176]: '%08d' % int(bin(23)[2:])
Out[176]: '00010111'

In [177]: tuple(ip.split(sep='.'))
Out[177]: ('1', '12', '3', '9')

In [178]: for i in tuple(ip.split(sep='.'))
  File "<ipython-input-178-c56cfa2d02ab>", line 1
    for i in tuple(ip.split(sep='.'))
                                     ^
SyntaxError: invalid syntax


In [179]: '%08d' % int(bin(2)[2:])
Out[179]: '00000010'

In [180]: '%08d' % int(bin('1')[2:])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-180-8afeb330a5fa> in <module>
----> 1 '%08d' % int(bin('1')[2:])

TypeError: 'str' object cannot be interpreted as an integer

In [181]: '%08d' % int(bin()[2:])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-181-1566912697ef> in <module>
----> 1 '%08d' % int(bin()[2:])

TypeError: bin() takes exactly one argument (0 given)

In [182]: tuple(ip.split(sep='.'))
Out[182]: ('1', '12', '3', '9')

In [183]: ip.split(sep='.')
Out[183]: ['1', '12', '3', '9']

In [184]: int(ip.split(sep='.'))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-184-256f94e9ef0e> in <module>
----> 1 int(ip.split(sep='.'))

TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'

In [185]: ip.split(sep='.')
Out[185]: ['1', '12', '3', '9']

In [186]: list2 =[int(i) for i in ip.split(sep='.')]

In [187]: list2
Out[187]: [1, 12, 3, 9]

In [188]: list2 =[bint(int(i)) for i in ip.split(sep='.')]
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-188-0d8d3d1dd31d> in <module>
----> 1 list2 =[bint(int(i)) for i in ip.split(sep='.')]

<ipython-input-188-0d8d3d1dd31d> in <listcomp>(.0)
----> 1 list2 =[bint(int(i)) for i in ip.split(sep='.')]

NameError: name 'bint' is not defined

In [189]: list2 =[bin(int(i)) for i in ip.split(sep='.')]

In [190]: list2
Out[190]: ['0b1', '0b1100', '0b11', '0b1001']

In [191]: list2 =[int(i) for i in ip.split(sep='.')]

In [192]: list2
Out[192]: [1, 12, 3, 9]

In [193]: tuple([int(i) for i in ip.split(sep='.')])
Out[193]: (1, 12, 3, 9)

In [194]: tuple([int(i) for i in ip.split(sep='.')])
Out[194]: (1, 12, 3, 9)

In [195]: tuple(bin( [int(i) for i in ip.split(sep='.')]) )
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-195-92fa75b0961b> in <module>
----> 1 tuple(bin( [int(i) for i in ip.split(sep='.')]) )

TypeError: 'list' object cannot be interpreted as an integer

In [196]: tuple(bin( [int(i) for i in ip.split(sep='.')])[2:] )
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-196-46ad8ec167c0> in <module>
----> 1 tuple(bin( [int(i) for i in ip.split(sep='.')])[2:] )

TypeError: 'list' object cannot be interpreted as an integer

In [197]: bin( [int(i) for i in ip.split(sep='.')])[2:]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-197-13c9ba24fc9e> in <module>
----> 1 bin( [int(i) for i in ip.split(sep='.')])[2:]

TypeError: 'list' object cannot be interpreted as an integer

In [198]: [int(i) for i in ip.split(sep='.')]
Out[198]: [1, 12, 3, 9]

In [199]: tuple([int(i) for i in ip.split(sep='.')])
Out[199]: (1, 12, 3, 9)

In [200]: '%08s ' % tuple([int(i) for i in ip.split(sep='.')])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-200-6efb60774321> in <module>
----> 1 '%08s ' % tuple([int(i) for i in ip.split(sep='.')])

TypeError: not all arguments converted during string formatting

In [201]: '%08s%08d%08d%08d ' % tuple([int(i) for i in ip.split(sep='.')])
Out[201]: '       1000000120000000300000009 '

In [202]: tuple([int(i) for i in ip.split(sep='.')])
Out[202]: (1, 12, 3, 9)

In [203]: for y in tuple([int(i) for i in ip.split(sep='.')])
  File "<ipython-input-203-d7d3dc91f423>", line 1
    for y in tuple([int(i) for i in ip.split(sep='.')])
                                                       ^
SyntaxError: invalid syntax


In [204]: for y in tuple([int(i) for i in ip.split(sep='.')]):
     ...:     print(y)
     ...:
1
12
3
9

In [205]: for y in tuple([int(i) for i in ip.split(sep='.')]):
     ...:     print(bin(y))
     ...:
     ...:
0b1
0b1100
0b11
0b1001

In [206]: for y in tuple([int(i) for i in ip.split(sep='.')]):
     ...:     print(bin(y)[2:])
     ...:
1
1100
11
1001

In [207]: for y in tuple([int(i) for i in ip.split(sep='.')]):
     ...:     print(bin(y)[2:], sep=' ')
     ...:
     ...:
1
1100
11
1001

In [208]: for y in tuple([int(i) for i in ip.split(sep='.')]):
     ...:     print(bin(y)[2:], sep='\t')
     ...:
1
1100
11
1001

In [209]: print()?
  File "<ipython-input-209-b8b45a21b8fd>", line 1
    print()?
           ^
SyntaxError: invalid syntax


In [210]: print?
Docstring:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
Type:      builtin_function_or_method

In [211]: for y in tuple([int(i) for i in ip.split(sep='.')]):
     ...:     print('%08s' % bin(y)[2:], end=' ')
     ...:
       1     1100       11     1001
In [212]:

In [212]: for y in tuple([int(i) for i in ip.split(sep='.')]):
     ...:     print('%08d' % int(bin(y)[2:]), end=' ')
     ...:
     ...:
00000001 00001100 00000011 00001001
In [213]: %history
ip = '192.168.3.1'
ip.split()
ip.split?
ip.split(sep=',')
ip.split(sep='.')
'{:<10}{:<10}{:<10}{:<10} '.format(ip.split(sep='.'))
format?
'{:<10}{:<10}{:<10}{:<10} '.format(for i in range(ip.split(sep='.')))
'{:<10}{:<10}{:<10}{:<10} '.format(for i in range(ip.split(sep='.')):)
(ip.split(sep='.'))
data = (ip.split(sep='.'))
data
for d in data
for d in data:
    printd
for d in data:
    print(d)
'{:<10}{:<10}{:<10}{:<10} '.format(for i in data)
'{:<10}{:<10}{:<10}{:<10} '.format(for i in data:)
'{:<10}{:<10}{:<10}{:<10} '.format(str(for i in data))
'{:<10}'.format(ip.split(serp='.'))
'{:<10}'.format(ip.split(sep='.'))
'{:<10}'.format(ip.split(sep='.'))
data
data.keys()
int(data)
int(data[])
data[0]
%history
data = (ip.split(sep='.'))
data
type(data)
'{} {} {} {}'.format(data)
'{} {} {} {}{}'.format(data)
data
data = (ip.split(sep='.'))
result = [int(item) for item i a]
result = [int(item) for item i data]
result = [int(item) for item in data]
result
'{} {} {} {}{}'.format(result)
'{} {} {} {}'.format(result)
'{} {} {} {}'.format([1,2,3,4])
'{:08b} {:08b} {:08b} {:08b}'.format(192, 100, 1, 1)
'{:08b} {:08b}{:08b}{:08b}'.format(192, 100, 1, 1)
data
result
'{:08b} {:08b}{:08b}{:08b}'.format(result)
ip = '192.168.3.1'
data = ip.split(sep='.')

ip_template =\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    10.1.10.1
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
p1 = data[0]
p2 = data[1]
p3 = data[2]
p4 = data[3]
print (ip_template.format(p1,p2,p3,p4))
print (ip_template.format(int(p1),int(p2),int(p3),int(p4)))
data = ip.split(sep='.')
data
data = int(ip.split(sep='.'))
data = ip.split(sep='.')
data
int(data)
tuple(data)
print (ip_template.format(tuple(data)))
data2 = tuple(data)
print (ip_template.format(data2))
dada2
data2
'{} {} {} {}'.format(data2)
data = int(ip.split(sep='.'))
data =ip.split(sep='.')
data
'%s %s %s %s' % data
'%s %s %s %s' % (data)
data
tuple(data)
'%s %s %s %s' % (tuple(data))
ip = '234.23.34.2'
tuple(ip.split(sep='.'))
print('%+8d%+8d%+8d%+8d' %    tuple(ip.split(sep='.')))
print('%+8d%+8d%+8d%+8d' %    tuple(ip.split(sep='.')))
tuple(ip.split(sep='.'))
'%s %s %s %s ' %tuple(ip.split(sep='.'))
'%s %s %s %s' %tuple(ip.split(sep='.'))
print('%s %s %s %s' %tuple(ip.split(sep='.')))
print('%+8s %s %s %s' %tuple(ip.split(sep='.')))
print('%-8s %s %s %s' %tuple(ip.split(sep='.')))
print('%-8s %-8s %s %s' %tuple(ip.split(sep='.')))
print('%-8s %-8s %-8s %-8s' %tuple(ip.split(sep='.')))
ip='1.12.3.9'
print('%-8s %-8s %-8s %-8s' %tuple(ip.split(sep='.')))
tuple(ip.split(sep='.'))
print('%-8b %-8b %-8b %-8b' %tuple(ip.split(sep='.')))
print('%-8x %-8x %-8x %-8x' %tuple(ip.split(sep='.')))
print('%-8x %-8x %-8x %-8x' %tuple(ip.split(sep='.')))
ip2 =(12,12,12,12)
print('%-8s %-8s %-8s %-8s' %tuple(ip2.split(sep='.')))
print('%-8d %-8d %-8d %-8d' %tuple(ip2.split(sep='.')))
print('%-8d %-8d %-8d %-8d' % ip2)
print('%-8d %-8d %-8d %-8s' % ip2)
print('%-8d %-8d %-8d %-8d' % ip2)
type(ip2)
ip2.count?
op2
ip2
ip2[1]
ip[1]
ip
idata
data
data[1]
bin(data[1])
bin(int(data[1]))
int(data[1])
or i in data:
    print(data)
or i in data:
    print(i)
for i in data:
    print(i)
for i in data:
    print(bin(int(i)))
for i in data:
    data3.appdend(bin(int(i)))
for i in data:
    data3.appdend(bin(int(i)))
data2=()
for i in data:
    data2.appdend(bin(int(i)))
data2=[]
for i in data:
    data2.appdend(bin(int(i)))
type(data2)
for i in data:
    data2.apend(bin(int(i)))
for i in data:
    data2.append(bin(int(i)))
data
data2
bin?
bin()?
bin(1)
'%-8'% bin(1)
'%-8s'% bin(1)
'%08s'% bin(1)
'%80s'% bin(1)
'%0s'% bin(1)
'%-0s'% bin(1)
'%+10s' % 25
'%+10f' % 25
'%+10d' % 25
'%+0d' % 25
'%0d' % 25
'%0-d' % 25
'%0+d' % 25
'%0 d' % 25
'%0  d' % 25
'%0    d' % 25
'%0    10d' % 25
'%08d' % 25
'%08d' % bin(12)
'%08d' % str(bin(12))
'%08s' % str(bin(12))
'%010s' % str(bin(12))
'%0-10s' % str(bin(12))
'%0+10s' % str(bin(12))
'%0+10s' % 12
'%010s' % 12
'%-010s' % 12
'%-010d' % 12
'%010d' % 12
'%010d' % bin(12)
'%010d' % bin(12)[;2]
'%010d' % bin(12)[:2]
'%010d' % int(bin(12)[:2])
 int(bin(12)[:2])
bin(12)[:2]
bin(12)[2:]
 int(bin(12)[:2])
 int(bin(12)[2:])
 int(bin(12)[2:])
'%08d' % int(bin(12)[2:])
data
data2
'%08d' % int(bin(12)[2:])
'%08d' % int(bin(2)[2:])
'%08d' % int(bin(23)[2:])
tuple(ip.split(sep='.'))
for i in tuple(ip.split(sep='.'))
'%08d' % int(bin(2)[2:])
'%08d' % int(bin('1')[2:])
'%08d' % int(bin()[2:])
tuple(ip.split(sep='.'))
ip.split(sep='.')
int(ip.split(sep='.'))
ip.split(sep='.')
list2 =[int(i) for i in ip.split(sep='.')]
list2
list2 =[bint(int(i)) for i in ip.split(sep='.')]
list2 =[bin(int(i)) for i in ip.split(sep='.')]
list2
list2 =[int(i) for i in ip.split(sep='.')]
list2
tuple([int(i) for i in ip.split(sep='.')])
tuple([int(i) for i in ip.split(sep='.')])
tuple(bin( [int(i) for i in ip.split(sep='.')]) )
tuple(bin( [int(i) for i in ip.split(sep='.')])[2:] )
bin( [int(i) for i in ip.split(sep='.')])[2:]
[int(i) for i in ip.split(sep='.')]
tuple([int(i) for i in ip.split(sep='.')])
'%08s ' % tuple([int(i) for i in ip.split(sep='.')])
'%08s%08d%08d%08d ' % tuple([int(i) for i in ip.split(sep='.')])
tuple([int(i) for i in ip.split(sep='.')])
for y in tuple([int(i) for i in ip.split(sep='.')])
for y in tuple([int(i) for i in ip.split(sep='.')]):
    print(y)
for y in tuple([int(i) for i in ip.split(sep='.')]):
    print(bin(y))
for y in tuple([int(i) for i in ip.split(sep='.')]):
    print(bin(y)[2:])
for y in tuple([int(i) for i in ip.split(sep='.')]):
    print(bin(y)[2:], sep=' ')
for y in tuple([int(i) for i in ip.split(sep='.')]):
    print(bin(y)[2:], sep='\t')
print()?
print?
for y in tuple([int(i) for i in ip.split(sep='.')]):
    print('%08s' % bin(y)[2:], end=' ')
for y in tuple([int(i) for i in ip.split(sep='.')]):
    print('%08d' % int(bin(y)[2:]), end=' ')
%history

In [214]:
'''
