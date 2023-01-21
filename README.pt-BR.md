# Digital Signature
> Aplicativo de terminal simples desenvolvido para um trabalho prático para a disciplina de Segurança em Sistemas da UFPI
## 🔖 Funcionalidades
  - Crie e verifique facilmente assinaturas digitais.
  - Gere automaticamente um par de chaves RSA se você não tiver um
  - Algoritmos de hash disponíveis:
    - SHA224
    - SHA256
    - SHA384
    - SHA512

# 🛠️ Como configurar
## 🧩 Módulos necessários
  - [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html)
  ```
    pip install pycryptodome
  ```

## ⏬ Baixando o projeto
Após instalar os requisitos, clone o repositório usando o comando abaixo:
```
  git clone https://github.com/CassianoJunior/DigitalSignature ./DigitalSignature
```

# 📱 Como usar
Ainda no terminal, entre na pasta criada DigitalSignature, onde estão todos os códigos do projeto.
O arquivo que você deseja assinar deve estar dentro dele.

No terminal, execute o comando abaixo para iniciar o aplicativo:
  ```
    python main.py
  ```

A cada assinatura, são criados 3 arquivos para seguir as especificações do trabalho:
  - publicKey.base64 - Par público da chave usado na assinatura do arquivo.
  - signature.base64 - Assinatura digital
  - USED_SHA.txt - Arquivo de texto com a versão SHA usada para fazer o hash da mensagem na assinatura.

Para verificar um arquivo assinado neste aplicativo, escolha uma das pastas na pasta 'signatures' para colocar no programa na etapa 'Signature file name'

## 🖼️ Imagens

<div align="center">
  <img align="left" src="https://gist.githubusercontent.com/CassianoJunior/6d6630ae3b81c9912f79b70c93bc776c/raw/17015854b5487ff0cef20acb1cdcec691b8dd143/signing-digitalSignatureApp.png" height="290" width="398" />

  <img align="" src="https://gist.githubusercontent.com/CassianoJunior/6d6630ae3b81c9912f79b70c93bc776c/raw/17015854b5487ff0cef20acb1cdcec691b8dd143/verifySignature-digitalSignatureApp.png" height="308" width="533" />

</div>