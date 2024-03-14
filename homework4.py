immutable_var = 1, 2, 3, "The sun is shining ", "in spring"
print(immutable_var)
# immutable_var[2] = 50 - кортеж не поддерживает обращение по элементам

mutable_list = [1, 2, 3, "Winter", "go away"]
print(mutable_list)
mutable_list[3] = "Frost"
print(mutable_list)





# food = ["apple", "coconut", "banana"]
# food.append(True)
# print(food)
# food.extend(["string", 2])
# print(food)
# food.remove("apple")
# print(food)
# print("coconut" not in food)
# print(food[0:2:2])

# tuple_ = 1, 2, 3, True, "String"
# tuple2_ = (1, 2, 3, 4)
# tuple3_ = tuple([1, 2, 3, 4])
# print(tuple_)
# print(tuple2_)
# print(tuple3_)
# print(tuple_[0])
# tuple_[0] = 200 #кортеж не поддерживает обращение по элементам (это делается для того чтобы какой-либо список не менял значений, чтобы они были постоянны, от греха подальше лучше сделать список кортежем. Точно так же можно эти элименты доставать и как-то с ними работать, но при этом мы будем уверенны, что само содержимое (кортежа), оно не изменится и  котежи занимают меньше памяти чем списки

# tuple_ = 1, 2, 3, True, "String"
# list_ = [1, 2, 3, True, "String"]
# print(tuple_.__sizeof__())
# print(list_.__sizeof__())

# print(tuple_)
# tuple_[0][0] = 2
# print(tuple_)
# tuple_  = (1, 2) * 3
# print(tuple_)
