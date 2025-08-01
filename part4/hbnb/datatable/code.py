import bcrypt

hashed = bcrypt.hashpw(b"mary1234", bcrypt.gensalt())
print(hashed.decode())
