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

      fileName = input('Plaintext file name > ')
      try:
        with open(fileName, 'r') as file:
          message = file.read().encode('UTF-8')
          file.close()
      except FileNotFoundError:
        print('File not found.')
        continue

      while True:
        hasKey = input('Do you have a key? (y/n) > ')
        if hasKey == 'y':
          try:
            private = importKeys()
          except FileNotFoundError:
            print('Key not found. Generating a new one.')
            private = generateKeys()
          break
        elif hasKey == 'n':
          private = generateKeys()
          break
        else:
          print('Invalid option.')
          continue 

      digitalSignature, publicKey = assign(message, private, hashAlgorithm)
      print('\nFile signed. Verify created files in signatures folder.\n')
    elif option == 2:
      fileName = input('Plain text file name > ')

      try:
        with open(fileName, 'r') as file:
          message = file.read().encode('UTF-8')
          file.close()
      except FileNotFoundError:
        print('Plain text file not found.')
        continue

      folderName = input('Signature folder name > ')
      try:
        with open(f'signatures/{folderName}/signature.base64', 'rb') as file:
          digitalSignature = file.read()
          file.close()
        with open(f'signatures/{folderName}/publicKey.base64', 'rb') as file:
          publicKey = file.read()
          file.close()
      except FileNotFoundError:
        print('Folder not found.')
        continue

      hashAlgorithm = getHashUsed(folderName)

      if verify(message, digitalSignature, publicKey, hashAlgorithm):
        print(f'{GREEN}\nThe message is authentic.{RESET}\n')
      else:
        print(f'{RED}\nThe message is not authentic.{RESET}\n')
    else:
      print('Invalid option.')



  

  
    



