# pip install flask-bcrypt
from flask_bcrypt import Bcrypt
bcrpyt = Bcrypt()
hash_pw = bcrpyt.generate_password_hash('test').decode('utf-8')

print(bcrpyt.check_password_hash(hash_pw, 'test'))
print(bcrpyt.check_password_hash(hash_pw, 'tst'))