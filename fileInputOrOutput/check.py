with open("sonu.txt","r") as f:
    data=f.read()
    if(data.find("jehanabad")):
        print("jehanabad is in the file")
    else:
        print("jehanabad is not in the file")