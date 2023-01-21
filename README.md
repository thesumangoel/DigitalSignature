# Digital Signature
> Simple terminal app developed for a practicial work in Systems Security class at UFPI
## 🔖 Features
  - Easily create and verify digital signatures.
  - Automatically generate a RSA keypair if you don't have one
  - Available hash algorithms:
    - SHA224
    - SHA256
    - SHA384
    - SHA512

# 🛠️ How to setup
## 🧩 Required modules
  - [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html)
  ```
    pip install pycryptodome
  ```

## ⏬ Downloading project
After installing the requirements, clone the repository using the command below:
```
  git clone https://github.com/CassianoJunior/DigitalSignature ./DigitalSignature
```

# 📱 How to use
Still in terminal, enter the folder created DigitalSignature, where are all project codes.
The file you want to sign must be inside it. 

In the terminal, run command below to start app:
  ```
    python main.py
  ```

With each signature, 3 files are created to follow the job specifications:
  - publicKey.base64 - Public key pair used to sign the file.
  - signature.base64 - Digital Signature
  - USED_SHA.txt - Text file with the SHA version used to hash the message in the signature.

To verify a signed file in this app, choose one of folders into signatures folder to place on program in 'Signature folder name' step.

## 🖼️ Preview images

<div align="center">
  <img align="left" src="https://gist.githubusercontent.com/CassianoJunior/6d6630ae3b81c9912f79b70c93bc776c/raw/17015854b5487ff0cef20acb1cdcec691b8dd143/signing-digitalSignatureApp.png" height="290" width="398" />

  <img align="" src="https://gist.githubusercontent.com/CassianoJunior/6d6630ae3b81c9912f79b70c93bc776c/raw/17015854b5487ff0cef20acb1cdcec691b8dd143/verifySignature-digitalSignatureApp.png" height="308" width="533" />

</div>