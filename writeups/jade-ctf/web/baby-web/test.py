import requests


def test(page):
    params = {
        'page': page,
    }
    r = requests.get('http://34.76.206.46:10008/', params=params)
    output = f"page: {page} has {r.text}"
    return output

i = 1
while i <= 100:
    req1 = test(i)
    print('Test1')
    print(req1)

    req2 = test(i)
    print('Test2')
    print(req2)
    if(req1 == req2):
        print('KQ:')
        print(req1)
    i += 1        