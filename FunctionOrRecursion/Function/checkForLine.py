word=str(input('enter the word to check it exist in the file : '))

def check():
    data=True
    line=1
    with open("sonu.txt","r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line)
                return 
            line+=1
    return (print("no word found"))

check()