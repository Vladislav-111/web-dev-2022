# 4.6 (не работает)
# Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
# Prefix                10.0.24.0/24
# AD/Metric             110/41
# Next-Hop              10.0.13.3
# Last update           3d18h
# Outbound Interface    FastEthernet0/0

temp = '''
    Prefix                 {}
    AD/Metric              {}
    Next-Hop               {}
    Last update            {}
    Outbound Interface     {}
'''

ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf_route = ospf_route.strip().split()
result = temp.format(ospf_route[0], ospf_route[1].strip('[]'), ospf_route[3].rstrip(','), ospf_route[4].rstrip(','), ospf_route[5])
print(result)