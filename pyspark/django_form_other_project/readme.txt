Start django 

source .venv/bin/activate

python3 manage.py runserver 8080




important files for django files

number_to_english.py
Converts numbers to english

tests.txt 
Basic tests on Django server

link.py
Links cloud server to PI server


Important dejango files

numb/url 
points the numb app to the view page

numb/views
the place where the functions run

mysite/urls
Points to the numb app



Important External Files

Frontend_numb.php
The front end user javascript package

Dj.php
layer between the php on the PI and the Django

Decode_from_PI.php
Layer between Server and PI






Server layout
Frontend JS calls frondend_server/Decode_from_PI returns Number or error string

Frondend_server/Decode_from_PI calls PI/Dj.php returns Json

PI/Dj.php calls DJango service return Json

DJango file imports and calls number_to_english.py whos function returns Json




Tests

test.py
tests primary functionality of the server does not test post due to cross origin problems I believe 
please use /post_reqest to test post








