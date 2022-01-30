def fun(name,**data):
    print(name)
    # print(data)

    for i,j in data.items():
        print(i,j)

fun('ashok',age=31, city='chennai', mobile=9790346171)