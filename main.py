from hashOperations import choosenHashAlgorithm, getHashUsed
from keyOperations import generateKeys, importKeys
from signatureOperations import assign, verify

GREEN = "\033[0;32m"
RED = "\033[0;31m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"

if __name__ == '__main__':
  while True:
    print('Choose an option:')
    print('1. Sign')
    print('2. Verify')
    print('0. Exit')
    option = int(input('Option > '))
    if option == 0: exit()
    
    if option == 1:
      hashAlgorithm = choosenHashAlgorithm()

      filename = input('Plaintext filename > ')

      generateKeys()
      private = importKeys()

      with open(filename, 'r') as file:
        message = file.read().encode('UTF-8')
        file.close()  

      digitalSignature, publicKey = assign(message, private, hashAlgorithm)
      print('File signed. Verify created files in signatures folder.')
    elif option == 2:
      filename = input('Plaintext filename > ')

      with open(filename, 'r') as file:
        message = file.read().encode('UTF-8')
        file.close()

      foldername = input('Signature folder name > ')

      hashAlgorithm = getHashUsed(foldername)

      with open(f'signatures/{foldername}/signature.base64', 'rb') as file:
        digitalSignature = file.read()
        file.close()
      
      with open(f'signatures/{foldername}/publicKey.base64', 'rb') as file:
        publicKey = file.read()
        file.close()

      if verify(message, digitalSignature, publicKey, hashAlgorithm):
        print(f'{BOLD + GREEN}The message is authentic.{RESET}')
      else:
        print(f'{BOLD + RED}The message is not authentic.{RESET}')
    else:
      print('Invalid option.')



  

  
    



