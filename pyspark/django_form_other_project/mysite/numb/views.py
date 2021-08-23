from django.shortcuts import render
from django.http import HttpResponse
import time
from django.core.files import File
# Create your views here.


import lets_convert
from django.shortcuts import render
import mysql_test


def traider(req):
    
    f = open("to_be_frontend_check_make_traid.html", "r")
    output= f.read()
    f.close()
    return HttpResponse( output )

def add_traid(req):
    f = open("add_user.html", "r")
    output= f.read()
    f.close()
    return HttpResponse( output )

def compleat_traid(req):
    f = open("to_be_frontend_check_fin_traid.html", "r")
    output= f.read()
    f.close()
    return HttpResponse( output )

def print_convertion(req):
    f = open("to_be_frontend_check_transaction.html.html", "r")
    output= f.read()
    f.close()
    return HttpResponse( output )

def print_user(req):
    f = open("to_be_frontend_check_user.html", "r")
    output= f.read()
    f.close()
    return HttpResponse( output )


def pyspark(req):
    return HttpResponse( "output6" )

def reset(req):
    return HttpResponse( "output6" )


def doit(req):
    print("in here")
    #return HttpResponse( "mysting" )

    action_type=""
    try:
        action_type=req.GET["action_type"]
    except:
        action_type=""

    user=""
    try:
        user=req.GET["user"]
    except:
        user=""

    email=""
    try:
        email=req.GET["email"]
    except:
        email=""

    phone=""
    try:
        phone=req.GET["phone"]
    except:
        phone=""

    password=""
    try:
        password=req.GET["password"]
    except:
        pass


    traid_id=""
    try:
        traid_id=req.GET["traid_id"]
    except:
        pass

    request_amound=""
    try:
        request_amound=float(req.GET["request_amound"])
    except:
        pass


    request_type=""
    try:
        request_type=req.GET["request_type"]
    except:
        pass


    send_type=""
    try:
        send_type=req.GET["send_type"]
    except:
        pass
    send_amount=""
    try:
        send_amount=float(req.GET["send_amount"])
    except:
        pass
    #127.0.0.1:8000/doit?action_type=adduser&user=v1&email=a&password=1&phone=1
    #127.0.0.1:8000/doit?action_type=adduser&user=v3&email=a&password=1&phone=1


    if action_type=="adduser":
        if password!="":
            pass
        else:

            return HttpResponse( "blank1" )
        if user!="":
            pass
        else:
            return HttpResponse( "blank2" )
        if email!="":
            pass
        else:
            return HttpResponse( "blank3" )
        if phone!="":
            pass
        else:
            return HttpResponse( "blank4" )
        out=mysql_test.makeuseremail(user,email,password)
        return HttpResponse( out )

    #127.0.0.1:8000/doit?action_type=maketraid&user=v1&password=1&request_type=money1&send_type=money2&request_amound=1&send_amount=1


    #SELECT * from `traidtable` WHERE `traid_id` LIKE 'mvqtpftuhlmhcyfneazdyysmouaajaobhaoxesqycbrrryjbbnwjnvhkopzzhaya';
    if action_type=="maketraid":
        if password!="":
            pass
        else:
            return HttpResponse( "blank1" )
        if user!="":
            pass
        else:
            return HttpResponse( "blank2" )

        if request_type not in ["money1","money2"]:

            return HttpResponse( "blank4",request_type," done " )

        if send_type not in ["money1","money2"]:
            return HttpResponse( "blank5" )

        if send_type==request_type:
            return HttpResponse( "blank6" )

        if request_amound=="":
            return HttpResponse( "blank7" )
        if send_amount=="":
            return HttpResponse( "blank8" )
        out=mysql_test.funtion_make_traid(user,password,request_type,request_amound,send_type,send_amount)
        return HttpResponse( out )

    #127.0.0.1:8000/doit?action_type=fintraid&user=v2&password=1&traid_id=vyyyihrlgoefyiznjngvnpgwaeduqqgpottlkgjrawvfeooinulyxwhgcezyhuej

    if action_type=="fintraid":
        if password!="":
            pass
        else:
            return HttpResponse( "blank1" )
        if user!="":
            pass
        else:
            return HttpResponse( "blank2" )

        if traid_id =="":
            return HttpResponse( "blank4" )


        out=mysql_test.compleat_traid(user,password,traid_id)
        mysql_test.log_traid(out)

        return HttpResponse( out )

    #127.0.0.1:8000/doit?action_type=print_convertion
 

    if action_type=="print_convertion":
        return HttpResponse( mysql_test.print_convertions("</br>") )
    #127.0.0.1:8000/doit?action_type=reset_convertion


    if action_type=="reset_convertion":
        mysql_test.reset_convertion()
        return HttpResponse( "done" )

    #127.0.0.1:8000/doit?action_type=Uprint&user=v2


    if action_type=="Uprint":
        return HttpResponse(mysql_test.user_acount(user,"</br>"))

    


    mysting=action_type+","+user+","+password+","+traid_id+","+request_amound+","+request_type+","+send_type+","+send_amount

    return HttpResponse( mysting )


def get_from_cash(req):

    return render_to_response('./test.html')



    



