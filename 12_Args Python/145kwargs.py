
# kwarge..... mtlb (keyword arguments)
#**kwarge (double star operator)

# kwargs as a parameter 
# kwargs me dictionary ki trh kaam  krta hain

def func(**kwarge):
    print(kwarge)

func(first_name = 'Niranjan', last_name = 'Kumar')


# aap dictionary ki trh loop bhi chla skte hain

def func(**kwarge):
    for k, v in kwarge.items():
         print( f"{k} : {v}")

func(first_name = 'Niranjan', last_name = 'Kumar')


## importent aap key word aargument pass krange to  kwarge as a dictionary input krayga


