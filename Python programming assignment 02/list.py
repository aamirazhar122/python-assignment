list_1= [1,2,3]
list_2 = [4,5,6]

list_1.extend(list_2) 
print(f"Updated_list_1 : {list_1}")

#output
#Updated_list_1 : [1, 2, 3, 4, 5, 6]

#pop method

list = [10,20,30,40]
list.pop()
print(list)

#output
#[10,20,30]

#index method

colors = ['red', 'blue', 'green', 'yellow']

green_index = colors.index("green")

print(green_index)

#output
#2