# using decorators, we can add extra features in the existing function
# OR
# we can access the features of 1st function into the other one without touching the 1st function

def div(a,b):
    print(a/b)


def smart_div(func):                                     # decorator

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)

    return inner 

div1 = smart_div(div)
div1(2,4)

