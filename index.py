# # authentication part
import re
the_public_list=[]
the_public_dic={}

def home_paage():
    print("for login enter 1 and for register enter 2")

def firstname (counter):
    count = counter
    first_name= input ("please enter your first name :")
    mfirtname= first_name.split()
    if (len(mfirtname)==1):
        the_public_dic["f_name"]= first_name
    elif (len(mfirtname ) >1 or len(mfirtname)==0):
        count += 1
        print("eroooor -> please enter only one name without spaces")
        firstname(count)
    elif (count == 2) :
        home_paage()
    else :
        pass    



def secondname (counter):
    count = counter
    second_name= input ("please enter your second name :")
    msecondname= second_name.split()
    if (len(msecondname)==1):
        the_public_dic["s_name"]= second_name
    
    elif (count == 2) :
        home_paage()
    elif (len(msecondname ) >1 or len(msecondname)==0):
        count += 1
        print("eroooor -> please enter only one name without spaces")
        secondname(count)
    else :
        pass    



# #enter email
def enterMail():
    mail=input("Please Enter your e-mail : ")
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex,mail)):
        the_public_dic["email"]= mail
    else:
        print("Mail is wrong !")
        enterMail()


def confirm_pass(password):
    confirm = input("please confirm password ")
    if (confirm==password):
       the_public_dic["password"]= password
    else:
       confirm_pass(password)


def enterpass ():
    password = input ("please enter ur password : ")
    regex = '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{4,16}$'
    if (re.search(regex,password)):
        confirm_pass(password)

    else:
        print ("Password must be at least 4 characters, no more than 16 characters, and must include at least one upper case letter, one lower case letter, and one numeric digit.")
        enterpass()

def enter_mobile():
    phone = input("please enter ur phone no : ")
    mylist = list (phone)
    if( ( mylist [0]== "0") and ( mylist [1]== "1") and (len (mylist)==11) ):
        the_public_dic["phone_no"]= phone
    else :
        enter_mobile()
    


def register ():
    counter1 =0
    firstname (counter1)
    secondname (counter1)
    enterMail()
    enterpass()
    enter_mobile()
    print (the_public_dic)
    the_public_list.append(the_public_dic)
    print (the_public_list)

register()