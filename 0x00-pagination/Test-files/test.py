
server = __import__("1-simple_pagination").Server


def add_numbers(a, b):
    assert a == int(a), "A is not an interger"
    assert b == int(b), "B is not an interger"
    #assert int(a), "Not an integer"
    #assert int(b), "The sum of a and b is not Integer"
    return a + b

#print(add_numbers(13, 4))
#print(add_numbers(2, 'lov'))


Server = server()

# print(Server.dataset())
print(Server.get_page())
