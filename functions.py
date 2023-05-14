# In python its possible to multiply a string like 'abc' * 10 but add is not permitted.
# str.replace(".","_",1)
# list.sor(revers=True)
#  immutable list => tuple
# enumurate(list) produce some tuples that can be show using list
def read_file(filename): # default returl is none and len none you will get error
    with open(filename, 'r') as local_file_todo:
        todo_file = local_file_todo.readlines()
    return todo_file


def write_file(filename, data): # default return is none and len none you will get error
    with open(filename, 'w') as local_file_todo:
        local_file_todo.writelines(data)


if __name__ == "__main__":
    print("You run functions module directly")