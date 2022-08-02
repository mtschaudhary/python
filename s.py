#print(eval(b))
#print(type(eval(b)))

from cgi import print_arguments


def A(i):
    i+=10

    return i

a = map(A, [1,2,3])
b = map(lambda x:x+10, [5,9,6])

 print(list(b))

