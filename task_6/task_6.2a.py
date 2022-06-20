"""
Задание 6.2a
Сделать копию скрипта задания 6.2.
Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255
Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


address = input('Введите IP-адрес в формате 10.0.1.1: ')
bite = address.split('.')
ip_address_correct = True

if len(bite) == 4:
    for bit in bite:
      if not (bit.isdigit() and int(bit) in range(0,256)):
         ip_address_correct = False
else:
   ip_address_correct = False

if ip_address_correct:
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
else:
    print('Неправильный IP-адрес')