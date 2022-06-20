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