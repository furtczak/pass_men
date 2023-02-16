import os

dir_path = os.path.dirname(os.path.abspath(__file__))

pass_file = os.path.join(dir_path, "pass.txt")

m_pwd=input("Main passwrd: ")

def view():
    with open('pass.txt',"r") as f:
        for line in f.readlines():
            data=(line.rstrip())
            user,pas=data.split("|")
            print(user, pas)
def add():
    name=input('Name: ')
    pas=input('Password: ')
     
    with open('pass.txt','a')as f:
        f.write(name+"|"+pas+"\n")

def remove(l_num):
    newpath=pass_file+".new"
    with open(pass_file,'r') as file, open(newpath, 'w') as new_file:
        for Line_num, line in enumerate(file):
            if Line_num != l_num:
                new_file.write(line)

    os.replace(newpath,pass_file)

while True:
    mode =input("What would you want to do, add new pass or view existing ones (v=view,a=add,q=quit,r=remove): ")
    if mode=="q":
        break
    if mode=="a":
        add()
    elif mode =="v":
        view()
    elif mode=="r":
        num=input("pleas specify a line: ")
        if num!=-1:
            num=int(num)- 1
            remove(int(num))
    else:
        print("invalid choice")