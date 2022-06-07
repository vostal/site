# -*- coding: cp1251 -*-
#!/usr/bin/env python3
import cgi
from datetime import datetime
import socket
from os import remove
timedelay=2
timdelayI=.4
def RECV(sock,timetodie):
  #Complited
  timeSTOP=datetime.now()
  IsNormal=False
  while(not IsNormal):
    ToClose=False
    Time=datetime.now()-timeSTOP
    if((Time.seconds+Time.microseconds/10**6)>timetodie):IsNormal=False;break
    try:
      timeSTO=datetime.now()
      while(True):
        Time=datetime.now()-timeSTO
        try:t=sock.recv(1);break
        except:
          if((Time.seconds+Time.microseconds/10**6)>timdelayI):IsNormal=False;ToClose=True;break
      if(ToClose):continue
      s=bytes()
      while(True):
        data=bytes()
        size=int(sock.recv(1)[0])
        if(not size):break
        timeSTO=datetime.now()
        while(len(data)<size):
          data+=sock.recv(size-len(data))
          Time=datetime.now()-timeSTO
          if((len(data)!=size) and ((Time.seconds+Time.microseconds/10**6)>timdelayI)):IsNormal=False;ToClose=True;break
        if(ToClose):break
        s+=data
        if(size!=255):break
      if(ToClose):continue
      if(t==b"0"):s=s.decode("utf-8")
      IsNormal=True
    except Exception as e:
      #if(("[WinError 10053]" in str(e)) or ("[WinError 10054]" in str(e))):assert "Disconnected"
      IsNormal=False
  if(IsNormal):return s
  else:return False
form=cgi.FieldStorage()
EMAIL,PASSWORD,NAME,INFO,MONEY=form.getfirst("email",""),form.getfirst("password",""),form.getfirst("name",""),form.getfirst("info",""),form.getfirst("money","")
try:PICTURE=form["picture"].file.read()#form.getfirst("picture","")
except:pass
flag=False
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.settimeout(.1)
sock.connect(("127.0.0.1",31222))
data=RECV(sock,timedelay)
FLAGUSERREG=0
if(data):
  for line in list(map(str,data.split("|"))):
    if(not line):continue
    if(not flag):
      if((line==EMAIL) and (EMAIL=="liveflovers@gmail.com") and (FLAGUSERREG==0)):FLAGUSERREG=1
      elif(FLAGUSERREG!=2):FLAGUSERREG=0
    elif((line==PASSWORD) and (FLAGUSERREG==1)):FLAGUSERREG=2
    flag=not flag
if(EMAIL and PASSWORD and FLAGUSERREG==2):
    flag=0
    kol=0
    FLAGUSERREG=False
    with open("FLOWERS.txt","r",encoding="utf-8") as f:
        for line in f:
            if(not line):continue
            if(line[-1]=="\n"):line=line[:-1]
            if((flag==0) and (NAME==line)):FLAGUSERREG=True;break#str(kol)
            flag+=1
            if(flag==3):
                flag=0
                kol+=1
    #NAME,INFO,MONEY,PICTURE
    if(NAME):
        if(FLAGUSERREG):#DELETE
            INFO=kol
            kol=0
            flag=0
            try:remove("img/flowers/"+str(INFO)+".png")
            except:pass
            with open("FLOWERS.txt","r",encoding="utf-8") as f:NAME=f.read()
            with open("FLOWERS.txt","w",encoding="utf-8") as f:
              for line in list(map(str,NAME.split("\n"))):
                if(not line):break
                if(line[-1]=="\n"):line=line[:-1]
                if(kol!=INFO):f.write(line+"\n")
                flag+=1
                if(flag==3):
                  flag=0
                  kol+=1
        elif(INFO and MONEY and PICTURE):#ADD
          with open("img/flowers/"+str(kol)+".png","wb") as f:f.write(PICTURE)
          with open("FLOWERS.txt","a",encoding="utf-8") as f:f.write(NAME+"\n"+INFO+"\n"+MONEY+"\n")
    print(u"Content-type: text/html\n")
    print(u'''<!DOCTYPE html>
<html class="no-js" lang="zxx">
<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Туристы</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" type="image/x-icon" href="../img/favicon.png">
    <link rel="stylesheet" href="../css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/owl.carousel.min.css">
    <link rel="stylesheet" href="../css/font-awesome.min.css">
    <link rel="stylesheet" href="../css/themify-icons.css">
    <link rel="stylesheet" href="../css/animate.css">
    <link rel="stylesheet" href="../css/slicknav.css">
    <link rel="stylesheet" href="../css/style.css">
    <style type="text/css">
      *{box-sizing:border-box}
@import 'https://fonts.googleapis.com/css?family=Open+Sans:400,400i&subset=cyrillic';
body {
  margin: 0;
  background: #F7F7F7;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-family: 'Open Sans', sans-serif;
}
.form-wrap {
  width: 550px;
  background: #ffd500;
  border-radius: 20px;
}
.form-wrap *{transition: .1s linear}
.profile {
  width: 240px;
  float: left;
  text-align: center;
  padding: 30px;
}
form {
  background: white;
  float: left;
  width: calc(100% - 240px);
  padding: 30px;
  border-radius: 0 20px 20px 0;
  color: #7b7b7b; 
}
.form-wrap:after, form div:after {
  content: "";
  display: table;
  clear: both;
}
form div {
  margin-bottom: 15px;
  position: relative;
}
h1 {
  font-size: 24px;
  font-weight: 400;
  position: relative;
  margin-top: 50px;
}
h1:after {
  content: "\f138";
  font-size: 40px;
  font-family: FontAwesome;
  position: absolute;
  top: 50px;
  left: 50%;
  transform: translateX(-50%);
}
label, span {
  display: block;
  font-size: 14px;
  margin-bottom: 8px;
}
input[type="text"], input[type="file"] {
  width: 100%;
  padding: 10px 15px;
  border-width: 0;
  background: #e6e6e6;
  outline: none;
  margin: 0;
}
input[type="text"]:focus, input[type="file"]:focus {
  box-shadow: inset 0 0 0 2px rgba(0,0,0,.2);
}
.radio label {
  position: relative;
  padding-left: 50px;
  cursor: pointer;
  width: 50%;
  float: left;
  line-height: 40px;
}
.radio input {
  position: absolute;
  opacity: 0;
}
.radio-control {
  position: absolute;
  top: 0;
  left: 0;
  height: 40px;
  width: 40px;
  background: #e6e6e6;
  border-radius: 50%;
  text-align: center;
}
.male:before {
  content: "\f222";
  font-family: FontAwesome;
  font-weight: bold;
}
.female:before {
  content: "\f221";
  font-family: FontAwesome;
  font-weight: bold;
}
.radio label:hover input ~ .radio-control,
.radiol input:focus ~ .radio-control {
  box-shadow: inset 0 0 0 2px rgba(0,0,0,.2);
}
.radio input:checked ~ .radio-control {
  color: red;
}
select {
  width: 100%;
  cursor: pointer;
  padding: 10px 15px;
  outline: 0;
  border: 0;
  background: #e6e6e6;
  color: #7b7b7b;
  -webkit-appearance: none;
  -moz-appearance: none;
}
select::-ms-expand {
  display: none;
}
.select-arrow {
  position: absolute;
  top: 38px;
  right: 15px;
  width: 0;
  height: 0;
  pointer-events: none;
  border-style: solid;
  border-width: 8px 5px 0 5px;
  border-color: #7b7b7b transparent transparent transparent;
}
button {
  padding: 10px 0;
  border-width: 0;
  display: block;
  width: 170px;
  margin: 25px auto 0;
  background: #60e6c5;
  color: white;
  font-size: 14px;
  outline: none;
  text-transform: uppercase;
}
@media (max-width: 600px) {
  body {display: block}
  .form-wrap {margin: 20px auto; max-width: 550px; width:100%}
  .profile, form {float: none; width: 100%}
  h1 {margin-top: auto; padding-bottom: 50px;}
  form {border-radius: 0 0 20px 20px}
}
    </style>
</head>

<div class="form-wrap">
    <div class="profile"><img src="../img/flowers/pngegg (4).png">
      <h1>Цветочек</h1>
    </div>
    <form action="ADDDELFLOWER.py" enctype="multipart/form-data" method="post">
      <input type="hidden" name="email" value="'''+EMAIL.encode("utf-8").decode("cp1251")+'''" />
      <input type="hidden" name="password" value="'''+PASSWORD.encode("utf-8").decode("cp1251")+'''" />
      <div>
        <label for="name">Название цветочка</label>
        <input type="text" name="name" maxlength="254" required>
      </div>
      <div class="radio"></div>
      <div>
        <label for="info">Описание цветочка</label>
        <input type="text" name="info" maxlength="254">
      </div>
      <div>
        <label for="money">Цена цветочека</label>
        <input type="text" name="money" maxlength="7">
      </div>
      <div class="radio"></div>
      <input type="hidden" name="MAX_FILE_SIZE" value="102400" />
      <input type="file" name="picture" multiple accept="image/png">
      <button type="submit">Добавть/Убрать цветочек</button>
    </form>
  </div>
    <script src="../js/vendor/modernizr-3.5.0.min.js"></script>
    <script src="../js/vendor/jquery-1.12.4.min.js"></script>
    <script src="../js/bootstrap.min.js"></script>
    <script src="../js/owl.carousel.min.js"></script>
    <script src="../js/isotope.pkgd.min.js"></script>
    <script src="../js/ajax-form.js"></script>
    <script src="../js/jquery.counterup.min.js"></script>
    <script src="../js/imagesloaded.pkgd.min.js"></script>
    <script src="../js/scrollIt.js"></script>
    <script src="../js/jquery.scrollUp.min.js"></script>
    <script src="../js/wow.min.js"></script>
    <script src="../js/jquery.slicknav.min.js"></script>
    <script src="../js/plugins.js"></script>
    <script src="../js/jquery.ajaxchimp.min.js"></script>
    <script src="../js/jquery.form.js"></script>
    <script src="../js/jquery.validate.min.js"></script>
    <script src="../js/main.js"></script>
</body>
</html>''')
else:
    print(u"Content-type: text/html\n")
    print(u'''<!DOCTYPE html>
<html class="no-js" lang="zxx">
<head>
    <link rel="stylesheet" href="../css/magnific-popup.css">
    <link rel="stylesheet" href="../css/nice-select.css">
    <link rel="stylesheet" href="../css/flaticon.css">

    <meta charset="utf-8">
    <meta http-equiv="refresh" content="5; url=../index.html">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Back to liveflovers...</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" type="image/x-icon" href="../img/favicon.png">
    <link rel="stylesheet" href="../css/animate.css">
    <link rel="stylesheet" href="../css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/owl.carousel.min.css">
    <link rel="stylesheet" href="../css/themify-icons.css">
    <link rel="stylesheet" href="../css/slicknav.css">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/font-awesome.min.css">
    <div class="bradcam_area breadcam_bg_1 overlay">
        <h3>Ви попали ни туды,валите из моего огорода, а то закопаю!!!!</h3>
    </div>
</footer>
    <script src="../js/vendor/modernizr-3.5.0.min.js"></script>
    <script src="../js/vendor/jquery-1.12.4.min.js"></script>
    <script src="../js/bootstrap.min.js"></script>
    <script src="../js/owl.carousel.min.js"></script>
    <script src="../js/isotope.pkgd.min.js"></script>
    <script src="../js/ajax-form.js"></script>
    <script src="../js/jquery.counterup.min.js"></script>
    <script src="../js/imagesloaded.pkgd.min.js"></script>
    <script src="../js/scrollIt.js"></script>
    <script src="../js/jquery.scrollUp.min.js"></script>
    <script src="../js/wow.min.js"></script>
    <script src="../js/jquery.slicknav.min.js"></script>
    <script src="../js/plugins.js"></script>
    <script src="../js/jquery.ajaxchimp.min.js"></script>
    <script src="../js/jquery.form.js"></script>
    <script src="../js/jquery.validate.min.js"></script>
    <script src="../js/main.js"></script>
</body>
</html>
<head>''')