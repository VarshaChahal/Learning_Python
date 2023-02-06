#from backend.businesslogic import business_logic
#from . import anotherutil
import sys
import utilclass

def utility_function():
    print("hey there! you are in the utility function")

#business_logic()
#anotherutil.another_util()
#print(sys.path)
#sys.modules

print(utilclass.util_class.name_attr)
del utilclass.util_class.name_attr
print(utilclass.util_class.name_attr)
