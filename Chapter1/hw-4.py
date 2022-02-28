# 4.1
# Используя подготовленную строку nat, получить новую строку, 
# в которой в имени интерфейса вместо FastEthernet написано GigabitEthernet.
# Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
nat = nat.replace('Fast', 'Gigabit') 
print(nat)

# 4.2
# Преобразовать строку в переменной mac из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX
# Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

mac = "AAAA:BBBB:CCCC"
mac = mac.replace(":",".")
print(mac)

# 4.3
# Получить из строки config такой список VLANов:
# ['1', '3', '10', '20', '30', '100']
# Записать итоговый список в переменную result.
# Полученный список result вывести на стандартный поток вывода (stdout) с помощью print.
# Тут очень важный момент, что надо получить именно список (тип данных),
# а не, например, строку, которая похожа на показанный список.

config = "switchport trunk allowed vlan 1,3,10,20,30,100"
config = config.split()
result = config[-1].split(',')
print(result)

# 4.4
# Из списка vlans нужно получить новый список уникальных номеров VLANов, 
# отсортированный по возрастанию номеров.
# Для получения итогового списка нельзя удалять конкретные vlanы вручную.
# Записать итоговый список уникальных номеров VLANов в переменную result.

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
result = sorted(set(vlans))
print(result)

# 4.5
# Из строк command1 и command2 получить список VLANов,
# которые есть и в команде command1 и в команде command2 (пересечение).
# В данном случае, результатом должен быть такой список: ['1', '3', '8']
# Записать итоговый список в переменную result.

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

command1 = command1.split()
command1 = command1[-1].split(',')
command2 = command2.split()
command2 = command2[-1].split(',')

result = sorted(set(command1).intersection(command2))
print(result)

# 4.6 (не работает)
# Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
# Prefix                10.0.24.0/24
# AD/Metric             110/41
# Next-Hop              10.0.13.3
# Last update           3d18h
# Outbound Interface    FastEthernet0/0

# ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
# ospf_route = ospf_route.strip().split()
# ospf_route.pop(2)
# result = ''
# print(result)

# 4.7 (не работает)
# Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
# 101010101010101010111011101110111100110011001100
# Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

# mac = "AAAA:BBBB:CCCC"
# mac = mac.replace(':','')
# mac = '{:b}'.format(mac)
# print(mac)

# 4.8 (не работает)
# Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный поток 
# вывода вывод столбцами, таким образом:
# первой строкой должны идти десятичные значения байтов
# второй строкой двоичные значения
# Вывод должен быть упорядочен также, как в примере:
# столбцами
# ширина столбца 10 символов (в двоичном формате надо добавить 
# два пробела между столбцами для разделения октетов между собой)
# Пример вывода для адреса 10.1.1.1:
# 10        1         1         1
# 00001010  00000001  00000001  00000001

# ip = "192.168.3.1"
# ip = ip.split('.')
# ip = '{:<8} {:<8} {:<8} {:<8}'.format(int(ip[::]))
# ip = ip.format(ip[::])
# print(ip)
