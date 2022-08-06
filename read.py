import shutil
import os
db = ""
def ReadDataPost(DataBase,DataPost):
    try:
        f2 = open("Data/DataBase/" + DataBase + "/" + DataPost + "/list")
        print("DataBase:" + DataPost)
        for file2 in f2.readlines():
            file2 = file2.replace("\n","")
            file2 = file2.replace("\r","")
            f3 = open("Data/DataBase/" + DataBase + "/" + DataPost + "/" + file2 + "/post",mode='r')
            print("---" + file2 + "---")
            for file3 in f3.readlines():
                file3=file3.replace("\n","")
                print(file3)
            f3.close()
        f2.close()
    except:
        print("Have a error,Program not run your command.")


while True:
    a = input("CoolDB>")
    b = a.split(' ')
    if(b[0] == "link"):
        try:
            db = b[1]
        except:
            print("Have a error,Program not run your command.")
        else:
            print("Link to Database:" + b[1])
    elif(b[0] == "view"):
        try:
            ReadDataPost(db,b[1])
        except:
            print("Have a error,Program not run your command.")
    elif(b[0] == "quit"):
        exit()
    elif(b[0] == "help"):
        print("Command list")
        fhelp = open("Data/help.txt")
        for fht in fhelp.readlines():
            fht = fht.replace("\n","")
            print(fht)
        fhelp.close()
    elif(b[0] == "delreport"):
        try:
            a = input("Deleted?[Y/N]:")
            if(a == "Y"):
                shutil.rmtree('./Data/DataBase/' + db + "/" + b[1])
                print("Deleted")
            else:
                print("Not Deleted")
        except:
            print("Have a error,Program not run your command.")
    elif(b[0] == "newreport"):
        try:
            os.makedirs("Data/DataBase/" + db + "/" + b[1])
        except:
            print("Have a error,Program not run your command.")
        else:
            print("Create Report:" + b[1])
    else:
        print("Bad command:" + b[0])
        print("input 'help' get command help.")
    continue