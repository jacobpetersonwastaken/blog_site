from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
hash = bcrypt.generate_password_hash('password').decode('utf-8')
print(hash)
is_valid = bcrypt.check_password_hash(hash, 'p')
print(is_valid)