from hashlib import sha256
user_password = "fbfdd827b403abd8146ca46ccf07eae5370477f90f6b5be72dcd5e67d1ae6a54"
def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()
user_comments_list = []
while len(user_comments_list)>=0:
    list_number = 1
    user_input = input("Please enter your comment or leave the program by typing 'leave':")
    if (user_input == "leave"):
        break
    password2 = input("Please type your password to save your comment: ")
    password_hash = create_hash(password2)
    if user_password == password_hash:
        print("Your password is confirmed.")
        user_comments_list.append(user_input)
        print("Your comments are: ")
        for one_comment in user_comments_list:
            print(str(list_number) + ") " + one_comment)
            list_number += 1
    else:
        print("Password that you have typed is wrong, please try again. ")

