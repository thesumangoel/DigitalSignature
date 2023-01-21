from Crypto.Hash import SHA224, SHA256, SHA384, SHA512


def choosenHashAlgorithm():
  while True:
    print('Choose a hash algorithm:')
    print('1. SHA-224')
    print('2. SHA-256')
    print('3. SHA-384')
    print('4. SHA-512')
    print('0. Exit')
    option = int(input('Option > '))
    if option == 0: exit()
    
    if option == 1:
      return SHA224, 'SHA-224'
    elif option == 2:
      return SHA256, 'SHA-256'
    elif option == 3:
      return SHA384, 'SHA-384'
    elif option == 4:
      return SHA512, 'SHA-512'
    else:
      print('Invalid option.')

def getHashUsed(filename):
  with open(f'signatures/{filename}/USED_SHA.txt', 'r') as file:
    hashUsed = file.read()
    file.close()
  
  if hashUsed == 'SHA-256':
    return SHA256
  elif hashUsed == 'SHA-512':
    return SHA512
  elif hashUsed == 'SHA-384':
    return SHA384
  elif hashUsed == 'SHA-224':
    return SHA224
  else:
    print('Invalid hash algorithm!')
    exit()