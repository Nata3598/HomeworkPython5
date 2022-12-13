# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
in_str = input("Введите строку: ")

print('=== filter() ===')
res = in_str.split(' ')
res = filter( lambda s: not 'абв' in s, res )
print ( ' '.join(list(res)) )

print('=== python comrehension ===')
res = in_str.split(' ')
res = [ s for s in res if s.find('абв') == -1 ]
print ( ' '.join(list(res)) )