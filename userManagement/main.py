# make user management system
import database as db

def main(answer = "yes"):
    while answer in ["Yes","YES","Y","y","yes"]:
        print("enter choice")
        print("1. Add record")
        print("2. show record")
        print("3. update record")
        print("4.  delete record")
        print("5. go to main")
        print("6. exit")
        choice = int(input("enter your choice"))
        match choice:
            case 1:
                id = input("enter user id : ")
                name = input("enter name : ")
                username = input("enter username : ")
                passwrd = input("enter password : ")
                if(id.isnumeric() and name.isalpha() and username.isalnum() and passwrd.isalnum()):
                    db.insert(id,name,username,passwrd)
                else:
                    print("incorrect input")
            case 2:
                db.show()
            case 3:
                id = input("enter user id")
                passwrd = input("enter password")
                if(id.isnumeric() and passwrd.isalnum()):
                    db.updatePassword(id,passwrd)
                else:
                    print("incorrect input : ")
            case 4:
                id = input("enter user id : " )
                if id.isnumeric():
                    db.delete(id)
                else:
                    print("incorrect input ")
            case 5:
                main()
            case 6:
                answer = "no"
            case _ :
                print("wrong choice")

if __name__ == "__main__":
    main()
