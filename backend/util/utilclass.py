
class util_class():
    #func_var="class level"
    
    def func1():
        func_var="in func1"
    def func2():
        #nonlocal func_var
        func_var="in func2"
    def func3():
       # global func_var
        func_var="in func3"
        
        