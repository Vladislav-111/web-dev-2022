#!/usr/bin/env python

# 6.1
# Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX. Однако, в оборудовании
# cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.
# Написать код, который преобразует MAC-адреса в формат cisco и добавляет их в новый
# список result. Полученный список result вывести на стандартный поток вывода (stdout) с
# помощью print.

mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []
for address in mac:
    result.append(address.replace(':','.'))
print(result)

# 6.2
# Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
# В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
#     «unicast» - если первый байт в диапазоне 1-223
#     «multicast» - если первый байт в диапазоне 224-239
#     «local broadcast» - если IP-адрес равен 255.255.255.255
#     «unassigned» - если IP-адрес равен 0.0.0.0
#     «unused» - во всех остальных случаях

address = input('Введите адрес в формате - 10.0.1.1: ')
bite = address.split('.')
if int(bite[0]) in range(1,224):
    print('Формат адреса unicast')
elif int(bite[0]) in range(224,240):
    print('Формат адреса multicast')
elif address == '255.255.255.255':
    print('Формат адреса local broadcast')
elif address == '0.0.0.0':
    print('Формат адреса unassigned')
else:
    print('unused')

# 6.2a (не работает)
# Сделать копию скрипта задания 6.2.
# Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
#     состоит из 4 чисел (а не букв или других символов)
#     числа разделенны точкой
#     каждое число в диапазоне от 0 до 255

# address = input('Введите адрес в формате - 10.0.1.1: ')
# bite = address.split('.')

# while True:
#     point = address.count('.')
#     for bit in bite:
#         if type(int(bit)) != int:
#             print('Не верный тип числа')
#         elif int(bit) not in range(0,256):
#             print('Числа не в диапазоне от 0 до 255')
#         elif point != 3:
#                 print('Числа не разделены точками или неправильный формат ввода адреса')
#         else:
#             print('Пароль установлен')
#             break
    
    
# if int(bite[0]) in range(1,224):
#     print('Формат адреса unicast')
# elif int(bite[0]) in range(224,240):
#     print('Формат адреса multicast')
# elif address == '255.255.255.255':
#     print('Формат адреса local broadcast')
# elif address == '0.0.0.0':
#     print('Формат адреса unassigned')
# else:
#     print('unused')

# 6.2b (не работает)
# Сделать копию скрипта задания 6.2a.
# Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

# address = input('Введите адрес в формате - 10.0.1.1: ')
# bite = address.split('.')

# while True:
#     point = address.count('.')
#     for bit in bite:
#         if type(int(bit)) != int:
#             print('Не верный тип числа')
#         elif int(bit) not in range(0,256):
#             print('Числа не в диапазоне от 0 до 255')
#         elif point != 3:
#                 print('Числа не разделены точками или неправильный формат ввода адреса')
#         else:
#             print('Пароль установлен')
#             break
#     address = input('Введите пароль еще раз: ')

# if int(bite[0]) in range(1,224):
#     print('Формат адреса unicast')
# elif int(bite[0]) in range(224,240):
#     print('Формат адреса multicast')
# elif address == '255.255.255.255':
#     print('Формат адреса local broadcast')
# elif address == '0.0.0.0':
#     print('Формат адреса unassigned')
# else:
#     print('unused')