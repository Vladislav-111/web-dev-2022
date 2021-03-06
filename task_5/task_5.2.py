"""
Задание 5.2
Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
Затем вывести информацию о сети и маске в таком формате:
Network:
10        1         1         0
00001010  00000001  00000001  00000000
Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях сеть/маска.
Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)
Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_temp = '''
    Network:
    {0:<8} {1:<8} {2:<8} {3:<8}
    {0:08b} {1:08b} {2:08b} {3:08b}
'''

mask_temp = '''
    Mask:
    {}
'''

ip = input('Введите ip-адрес в формате 10.1.1.0/24: ')
ip = ip.split('/')
mask = ip[1]
ip = ip[0]
ip = ip.split('.')
print(ip_temp.format(int(ip[0]), int(ip[1]),int(ip[2]), int(ip[3])))
print(mask_temp.format('1'* int(mask) + '0' * (32-int(mask)) ))