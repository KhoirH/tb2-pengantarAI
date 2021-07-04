from flask_bcrypt import Bcrypt

print(Bcrypt().generate_password_hash('hilmi').decode('utf-8'))