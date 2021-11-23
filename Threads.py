from Encrypt import *
from Decrypt import *
from IVsKeys import *
import threading

def HybridCrypt():
	iv1,iv2=generateIV()
	key1,key2=generateKey()
	HybridCryptKeys()
	t1 = threading.Thread(target=AES, args=(key1,iv1,))
	t2 = threading.Thread(target=EFernet, args=(key2,))

    #Starting the Encription Process	
	t1.start() 
	t2.start()
    #Thread Sync.
	t1.join() 
	t2.join()


 
def HybridDeCrypt():
	HybridDeCryptKeys()
	iv=FetchIV()
	key1,key2=FetchKey()
	t1 = threading.Thread(target=DAES, args=(key1,iv[0],))
	t2 = threading.Thread(target=DFernet, args=(key2,))

    #Starting the Encription Process
	t1.start() 
	t2.start()

    #Thread Sync.
	t1.join() 
	t2.join()
	
