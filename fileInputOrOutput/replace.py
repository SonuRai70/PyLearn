with open("sonu.txt","r") as f:
    data=f.read()
    new_data=data.replace("Hello","Hi")
    print(new_data)
    
    
with open("sonu.txt","w") as f:
    f.write(new_data)
print(new_data)
