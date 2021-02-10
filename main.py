import skinny 
import time 
import os
import binascii

key='0x5ba8c7572ac2df5e1b474a91441abbc3'
with open ("testfile.txt", "r") as original_file:
    data = str.encode(original_file.read())

print(data)

hex_data = binascii.hexlify(data)
print(hex_data)
##data = original_file.read 
p = skinny.SkinnyCipher(int(key,16)) 

start = time.time()


for i in range(0,100):
  d = p.encrypt(int(hex_data,16))
    w = p.decrypt(d)

print(w)
end = time.time() 
##encrypted = p.encrypted(data)

wdcode = str(w, 'ascii')
print(wdcode)
decrypted = binascii.unhexlify(wdcode)
with open ("enc_file.enc, wb") as encrypted_file:

