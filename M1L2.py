import random
password = "+-*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ21234567890"

long = int(input("Какую длину пароля вы хотите?:"))
save_password = "".join(random.sample(password,long))
print(save_password)
