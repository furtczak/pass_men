m_pwd=input("Main passwrd: ")

def view():
    with open('pass.txt',"r") as f:
        for line in f.readlines():
            print(line.rstrip())
            
def add():
    name=input('Name: ')
    pas=input('Password: ')
     
    with open('pass.txt','a')as f:
        f.write(name+"|"+pas+"\n")

while True:
    mode =input("What would you want to do, add new pass or view existing ones (v=view,a=add,q=quit): ")
    if mode=="q":
        break
    if mode=="a":
        add()
    elif mode =="v":
        view()
    else:
        print("invalid choice")