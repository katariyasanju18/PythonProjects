db = []

# Add to Database
def insert(id,name,username,password):
    try:
        db.append({"id":id,"name":name,"username":username,"password":password})
    except:
        print("data is incorrect")
#Show database record

def show():
    for i in db:
        print(i)

def updatePassword(id,password):
    for i in db:
        for items in i.items():
            if items['id']==id:
                items["password"] = password
                print("password updated")
            else:
                print("record not found")

def delete(id):
    for i in db:
        for items in db.items():
            if items['id']==id:
                del i
                print("record deleted")
            else:
                print("record not found")