immutable_var = (1, 2, True, 'string', [3, 4])
print(immutable_var) #(1, 2, True, 'string', [3,4])
#immutable_var[0] = 2
#print(immutable_var) #TypeError
#Нельзя изменить элементы кортежа, потому что тип данных tuple, предназначенный для хранения информации в исходном виде.
mutable_list = [1, 2, True, 'string',[3, 4]]
mutable_list[0] = 'apple'
print(mutable_list) #['apple', 2, True, 'string', [3, 4]]
