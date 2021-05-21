user_pass = {"Vuyani": "Vuya@2021", "Amanda": "@manda20", "Nathan": 'blue101', "Ikraam": "carsthemovie", "Atheelah": "maroon17" }

user = input("enter username")
password = input("enter password")


def user_pass_search(username, _password, _dict):
    if username in _dict:
        if _password == _dict[username]:
            return 1
        else:
            return 0
    else:
        return -1


x = int(user_pass_search(user, password, user_pass))
print('')
if x == 1:
    print("your details are correct")
elif x ==0:
    print("incorrect password")
elif x ==-1:
    print("user doesn't exist")

