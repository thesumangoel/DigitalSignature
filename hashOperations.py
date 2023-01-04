from Crypto.Hash import SHA224, SHA256, SHA384, SHA512


def choosenHashAlgorithm():
  while True:
    print('Choose a hash algorithm:')
    print('1. SHA256')
    print('2. SHA512')
    print('3. SHA384')
    print('4. SHA224')
    print('0. Exit')
    option = int(input('Option > '))
    if option == 0: exit()
    
    if option == 1:
      return SHA256, 'SHA256'
    elif option == 2:
      return SHA512, 'SHA512'
    elif option == 3:
      return SHA384, 'SHA384'
    elif option == 4:
      return SHA224, 'SHA224'
    else:
      print('Invalid option.')

def getHashUsed(filename):
  with open(f'signatures/{filename}/USED_SHA.txt', 'r') as file:
    hashUsed = file.read()
    file.close()
  
  if hashUsed == 'SHA256':
    return SHA256
  elif hashUsed == 'SHA512':
    return SHA512
  elif hashUsed == 'SHA384':
    return SHA384
  elif hashUsed == 'SHA224':
    return SHA224
  else:
    print('Invalid hash algorithm!')
    exit()