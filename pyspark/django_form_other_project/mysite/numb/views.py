from django.shortcuts import render
from django.http import HttpResponse
import time
from django.core.files import File
# Create your views here.
import number_to_english as conv


from django.shortcuts import render

def home(req):
    import lets_convert
    f = open("/Users/ahauss/Desktop/lbry/files/mysight/mysite/cash.txt", "r")
    output= f.read()
    print(output)
    return HttpResponse( lets_convert.convert_back(output) )
    #return render(req, 'numb/test.html')


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


    
    



