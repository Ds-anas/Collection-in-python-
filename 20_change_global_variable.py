# Change a global variable inside a function
global_var = 10

def change_value():
    global global_var
    global_var = 20

print("Before function:", global_var)
change_value()
print("After function:", global_var)
