import skinny
import time
import os
import binascii

key = '0x5ba8c7572ac2df5e1b474a91441abbc3'
with open("1024kb.txt", "r") as original_file:
    data = str.encode(original_file.read())

##print(data)

hex_data = binascii.hexlify(data)
##print(hex_data)
##data = original_file.read
p = skinny.SkinnyCipher(int(key, 16))

start = time.time()


for i in range(0, 100):
  d = p.encrypt(int(hex_data, 16))
  w = p.decrypt(d)

print(d)
print(format(w, '#018x'))
end = time.time()


wdcode = format(w, '#018x')[2:]
print(wdcode)
##print(Success)
decrypted = binascii.unhexlify(wdcode).decode('ascii')

#print(decrypted)

with open("enc_file.enc", "w") as encrypted_file:
    encrypted_file.write(decrypted)
