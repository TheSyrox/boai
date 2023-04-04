from boai import *

password_gen = PasswordGenerator(8)  # 8 karakterli bir şifre oluştur
password = password_gen.generate_password()
print("Oluşturulan şifre:", password)
