from django.shortcuts import render
from django.http import HttpResponse
import time
from django.core.files import File
# Create your views here.
import number_to_english as conv

import lets_convert
from django.shortcuts import render

def home(req):
    
    f = open("to_be_frontend.html", "r")
    output= f.read()
    f.close()
    return HttpResponse( output )

def add_traid(req):
    f = open("to_be_frontend.html", "r")
    output= f.read()
    f.close()
    return HttpResponse( output )

def compleat_traid(req):
    f = open("to_be_frontend.html", "r")
    output= f.read()
    f.close()
    return HttpResponse( output )

def print_convertion(req):
    f = open("to_be_frontend.html", "r")
    output= f.read()
    f.close()
    return HttpResponse( output )

def print_user(req):
    f = open("to_be_frontend.html", "r")
    output= f.read()
    f.close()
    return HttpResponse( output )


def doit():
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
        request_amound=req.GET["request_amound"]
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
        send_amount=req.GET["send_amount"]
    except:
        pass






def post(req):
    from selenium import webdriver
    value="now value"
    url = "https://odysee.com/$/embed/testing/dc8d2599724f8593a7c92dde815527dcf33c1b78?r=CnRc5Ve1u4xmW4mLp6hz2mxZg5QPQwiC"
    driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(20)  # seconds

    embed = driver.find_elements_by_class_name("markdown-preview")

    value=embed[0].find_element_by_tag_name("p").text
    print(value)
    time.sleep(10)
    f = open('/Users/ahauss/Desktop/lbry/files/mysight/mysite/cash.txt', 'w')
    testfile = File(f)
    testfile.write(str(value)+"done")
    testfile.close()
    f.close()
    time.sleep(1)



    return HttpResponse("cashed" )

def get_from_cash(req):

    return render_to_response('./test.html')


    
    



