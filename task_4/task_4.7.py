# Задание 4.7
# Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
# '101010101010101010111011101110111100110011001100'
# Полученную новую строку вывести на стандартный поток вывода (stdout) с помощью print.

mac = "AAAA:BBBB:CCCC"
mac = mac.replace(':','')
mac = bin(int(mac, 16))
print(mac[2:])