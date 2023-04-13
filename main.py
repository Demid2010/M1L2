import ranom
password = "+-*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ21234567890"

long = int(input("Какую длину пароля вы хотите?:"))
save_password = "".join(random.saple(password,long))
print(save_password)
