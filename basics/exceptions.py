import sys

def convert_to_int(s):
    try:
        x = int(s)
    except ValueError:
        x = -1
    except TypeError:
        x = -2
    return x

valid_string_int = "12"
invalid_string_int = "abc"
invalid_arr_int = [1, 2, 3]

valid_result = convert_to_int(valid_string_int)
invalid_result = convert_to_int(invalid_string_int)
invalid_arr_result = convert_to_int(invalid_arr_int)

print(valid_string_int + " converts to int with result " + str(valid_result))
print(invalid_string_int + " raises exception which returns " + str(invalid_result))
print(str(invalid_arr_int) + " raises exception which returns " + str(invalid_arr_result))

print("--- io errors ---------------------")
def open_file(file_name):
    try:
        f = open(file_name)
        s = f.readline()
        i = int(s.strip())
    except IOError as e:
        errno, sterror = e.args
        print("I/O error({0})".format(errno, sterror))
        print("----------")
        print(e)
        print("end of e")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

open_file("non-existing")
open_file("variables.py")
