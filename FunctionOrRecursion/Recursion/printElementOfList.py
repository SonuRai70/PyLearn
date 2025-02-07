names = ['sonu','amit','nikhil','ranjan']
def ele(list,idx=0):
    if(idx==len(names)):
        return
    print(list[idx])
    ele(list, idx +1)

ele(names)