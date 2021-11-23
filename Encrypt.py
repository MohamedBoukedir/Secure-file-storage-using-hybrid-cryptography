from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import rsa
from Cryptodome.Cipher import PKCS1_OAEP
import binascii
import os
import pickle
from stegano import lsb
def AES(key,iv):
    f=open(os.path.join(os.getcwd()+"/Segments","0.txt"),"r")
    content=f.read()
    f.close()
    content=content.encode()
    b=len(content)
    if(b%16!=0):
        while(b%16!=0):
            content+=" ".encode()
            b=len(content)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    cont = encryptor.update(content) + encryptor.finalize()
    open(os.path.join(os.getcwd()+"/Segments","0.txt"),"wb").close()
    f=open(os.path.join(os.getcwd()+"/Segments","0.txt"),"wb")
    f.write(cont)
    f.close();

def EFernet(key):
    f=open(os.path.join(os.getcwd()+"/Segments","1.txt"),"r")
    content=f.read()
    f.close()
    content=content.encode()
    fer = Fernet(key)
    content=fer.encrypt(content)
    open(os.path.join(os.getcwd()+"/Segments","1.txt"),'w').close()
    f=open(os.path.join(os.getcwd()+"/Segments","1.txt"),"wb")
    f.write(content)
    f.close()

def HybridCryptKeys():
    publicKey, privateKey = rsa.newkeys(512) 
    print(privateKey)   
    # Step 2
    with open('Original.txt', 'wb') as config_dictionary_file:
        # Step 3
        pickle.dump(privateKey, config_dictionary_file)
    
    secret = lsb.hide("./img.png", "Hello World")
    secret.save("./Lenna-secret.png")

    clear_message = lsb.reveal("./Lenna-secret.png")

    listDir=os.listdir(os.getcwd()+"/Infos")
    for i in listDir:
        KI=open(os.getcwd()+'/Infos//'+i,'rb')
        content=KI.read()
        KI.close()
        content=rsa.encrypt(content,publicKey)
        open(os.path.join(os.getcwd()+"/Infos",i),'wb').close()
        f=open(os.path.join(os.getcwd()+"/Infos",i),"wb")
        f.write(content)
        f.close()


