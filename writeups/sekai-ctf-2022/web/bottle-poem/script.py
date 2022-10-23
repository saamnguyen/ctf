from bottle import response

response.set_cookie('name', {'name': 'admin'}, secret="Se3333KKKKKKAAAAIIIIILLLLovVVVVV3333YYYYoooouuu")
print(f'Cookie: {response.headerlist[1][1]}')