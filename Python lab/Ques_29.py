# wap to encrpyt a message  by adding a key value  to every character

msg = input("Enter message: ")
key = int(input("Enter key: "))
enc = ""

for ch in msg:
    enc = enc + chr(ord(ch) + key)

print("Encrypted message:", enc)