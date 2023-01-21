import os

from Crypto import Random
from Crypto.PublicKey import RSA


def generateKeys():
  randomGenerator = Random.new().read
  key = RSA.generate(1024, randomGenerator)
  private, public = key, key.publickey()

  if not os.path.exists('keys'): os.mkdir('keys')

  with open('keys/private.pem', 'w') as f:
    f.write(repr(private.export_key('PEM')))
    f.close()

  with open('keys/public.pem', 'w') as f:
    f.write(repr(public.export_key('PEM')))
    f.close()
  
  return importKeys()

def importKeys():
  with open('keys/private.pem', 'r') as f:
    private = RSA.import_key(eval(f.read()))
    f.close()
  
  return private