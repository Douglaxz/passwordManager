#!/usr/bin/python

import bcrypt

passwd = b'12345'

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(passwd, salt)

if bcrypt.checkpw(passwd, hashed):
    print("match")
else:
    print("does not match")

print(hashed)
print("-----------------------------------------------------")
if bcrypt.checkpw(passwd, hashed):


#$2b$12$jn9cY.4NQ7e97HCQc4STee9BbIbxA3jlPfkO9gGvCmCXchV76Lo1O