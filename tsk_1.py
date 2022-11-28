def register():      #return True Success, False Failure
    s=input()
    #print(s)
    flag=0   #success
    try:
        f=s[0]
    except IndexError:
        print("please enter a valid user name, name cannot be Null")
        flag=1     #fail --user name is null
        return False
    if s in d:
        print("user name already present please try with different user name")
        flag=1    #username already present
        return False
    if not((f>="a" and f<="z") or (f>="A"and f<="Z")):
        flag=1   #fail --check first character not special character or numbers
        print("please enter valid username first char must be a alphabet not special char or numbers")
        return False
    if s.count("@")!=1 or s.count(".")!=1 or s.index("@")<3:
        flag=1   #fail --check @ . occurance once, 3 char before @ 
        print("please enter valid username occurance of @ and . must be once, 3 char must be before @")
        return False
    dif=s.index(".")-s.index("@")
    if (dif<=1):
        flag=1  #fail any one char between @ and .
        print("please enter valid username atleast one char must be present between @ and .")
        return False
    if (dif<4):
        flag=1  #atleast 3 character between @ and .   additional check added
        for i in range(s.index("@")+1,s.index(".")):
            if s[i] not in ((f>="a" and f<="z") or (f>="A"and f<="Z")):
                flag=1 #fail ---not an alphabet between @ and . additional check added
                print("please enter valid username char between @ and .  must be alphabet additional check")
                return False
        for i in range(s.index(".")+1,len(s)):
            if s[i] not in ((f>="a" and f<="z") or (f>="A"and f<="Z")):
                flag=1 #fail ---not an alphabet after . additional check added
                print("please enter valid username char after .  must be alphabet additional check")
                return False
    #print(dif)
    #print(s.index("@"))
    #print(flag)
    #print(s.index("."))
    print("user name is fine enter password")
    while flag==0:
        pas=input("Enter password len must be >5 and <16 with atleast one digit, one special char,one caps and one small")
        #print("pass",pas)
        if len(pas)>5 and len(pas)<16 and re.findall("[\d]",pas) and re.findall("[A-Z]",pas) and re.findall("[a-z]",pas) and re.findall("[^a-zA-Z0-9]",pas):
            d.update({s:pas})
            return True
        else:
            print("please enter valid password")
def login():
    print("Enter the user name")
    user=input()
    if user in d:
        print("Enter login password")
        pas1=input()
        if d[user]==pas1:
            print("Login successful")
        else:
            print("Enter valid password")
            print("please Try again from login page or try with forget password")
    else:
        print("User name is not found Please register for login")
def forget_pas():
    print("Enter the valid user name")
    user=input()
    if user in d:
        while 1:
            print("please enter 1 to view old password or 2 to update new password")
            number=int(input())
            if number==1:
                print("old password is ",d[user])
                print("please go to login and try with this old password")
                break
            elif number==2:
                while 1:
                    new_pas=input("Enter new password len must be >5 and <16 with atleast one digit, one special char,one caps and one small")
                    if len(new_pas)>5 and len(new_pas)<16 and re.findall("[\d]",new_pas) and re.findall("[A-Z]",new_pas) and re.findall("[a-z]",new_pas) and re.findall("[^a-zA-Z0-9]",new_pas):
                        d[user]=new_pas
                        print("password updated successsfully")
                        break
                    else:
                        print("please enter valid new password")
                break
            else:
                print("please enter valid number 1 or 2")
    else:
        print("Please enter valid username or register for login")

print("please enter 1 for registration, 2 for login, 3 for forgetpassword")
import pickle
import re
d={}
num=int(input())
if num==1:
    print("Registration page please enter user name")
    try:
        f=open("Register.pickle","rb")
        d=pickle.load(f)
        print("loaded here",d)
        f.close()
    except EOFError:   #if no data in file create empty dict and proceed
        d={}
        print("No data in file",d)
    except FileNotFoundError:      #if no file is there create file first time
        d={}
        f=open("Register.pickle","wb")   #file creation first time
        f.close()
        print("create first time empty file",d)
    o=register()
    if o:
        print("Registration successful")
        print(d)
        f=open("register.pickle","wb")         
        pickle.dump(d,f)                    #dumping new data to the existing file
        f.close()
    else:
        print("Registration unsuccessful")
elif num==2:
    f=open("Register.pickle","rb")
    d=pickle.load(f)                           #loading data from file to check in dict 
    print("login page please enter user name")
    login()
    f.close()
else:
    f=open("Register.pickle","rb")
    d=pickle.load(f)                        #loading data from file to check in dict for old password or update new password 
    f.close
    print("Forget password  to view old password or to update with new password")
    forget_pas()
    f=open("Register.pickle","wb")         #dumping with new password data
    pickle.dump(d,f)
    f.close()