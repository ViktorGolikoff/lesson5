immutable_var = 1,3,4,"a","fc"
print(immutable_var)
#immutable_var[0:4]=15,17,1,1
#Кортеж относится к неизменяемым типам данным и если мы хотим изменить
#его элементы, то столкнемся с ошибкой.Но несмотря на неизменямость мы можем создать внутри кортежа список,
#который
print(immutable_var)
mutable_list = ([1,3,4,"Hi"],"Nice")
print(mutable_list)
mutable_list [0][0]= "I am Victor"
print(mutable_list)