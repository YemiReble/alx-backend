
# server = __import__("1-simple_pagination").Server
server = __import__("3-hypermedia_del_pagination").Server


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
# print(Server.indexed_dataset())

less = {
    'prom': 24,
    'hello': 'mom',
    'bye': 2,
    'wel': 'you are'
}


def get(data, idx: str):
    for idx2 in data:
        return idx2[idx]


print(less.get("bye"))
