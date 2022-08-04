# so now our username will be generated through a function

def register():
    db = open("database.txt", "r")
    username=input("Create Username: ")
    password=input("Create password: ")
    password_1=input("Confirm password: ")                             # this is for verification of the first inserted password

    if password != password_1:    # if the first password does not match the verification password.
        print("Does not match!,  restart: ")
        register()

    
    elif username != db:   # checks if username already exists in the text file
        print("Username already exists!")
        register()

    else:
        if len(password) <6:   # if your password is less than 6 words/digits
            print("Too short!, restart: ")
            register()
        elif len(username) <6:
            print("Too short!, restart: ")

        else:
            db= open("database.txt", "a")  # we will then append the new information to the text
            db.write(username+", "+password+"\n")
            print("Done.")

register()

