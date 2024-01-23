
# functions with all parameters
# very important to understand 

# PADK

# parameters
# *args
# default parameters
# **kwargs

 ## parameters, *args, default parameters, **kwargs kaise use krne ya do method ek sath use 
# krne hai to kaise line by line use krenge 
# kis oder me parameters ko likhenge ye janna impotent hain


def fun(name,*args, last_name = 'unknown', **kwarge):
    print(name)
    print(args)
    print(last_name)
    print(kwarge)

fun('Niranjan', 1,2,3, a = 1, b = 2)  
    

    


