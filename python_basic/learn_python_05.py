# 字典

#字典是无序的
alien_0 = {'color': 'red', 'points': 5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])
alien_0['sex'] = 'male'
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
del alien_0['color']
print(alien_0)

for key, value in alien_0.items():
    print('\nKye: ' + key)
    print('\nValue: ' + str(value))

for key in alien_0.keys():
    print("\n" + key.title())

#字典与列表的嵌套 就是灵活应用 不写例子了