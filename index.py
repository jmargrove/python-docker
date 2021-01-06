"""
This is the modules document string that discribes the way things are here.
"""
print("Hello World")

my_file = open("container-data/newdata.txt", 'w+')
my_file.write("Additional data")
my_file.close()


def func_key(variable_a, variable_b):
    """
    Function for muliplication
    """
    result = variable_a * variable_b
    print(result)
