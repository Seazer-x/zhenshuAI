import hashlib


def password_hash(password):
    hash_md5 = hashlib.md5()
    hash_md5.update(str(password).encode('utf-8'))
    return hash_md5.hexdigest()


print(password_hash("password"))
