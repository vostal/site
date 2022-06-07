# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import cgi
from datetime import datetime
import socket
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
EMAIL,PASSWORD=form.getfirst("email",""),form.getfirst("password","")
flag=False
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.settimeout(.1)
sock.connect(("127.0.0.1",31222))
data=RECV(sock,timedelay)
FLAGUSERREG=0
text="Error: bad server connection"
if(data):
    text=""
    for line in list(map(str,data.split("|"))):
        if(not line):continue
        if(not flag):
            if((line==EMAIL) and (EMAIL=="liveflovers@gmail.com") and (FLAGUSERREG==0)):FLAGUSERREG=1
            elif(FLAGUSERREG!=2):FLAGUSERREG=0
        elif((line==PASSWORD) and (FLAGUSERREG==1)):FLAGUSERREG=2
        text+="""		<div class="container">
            <h3>"""*(not flag)+line+(not flag)*" | "+flag*"""</h3>
        </div>"""
        flag=not flag
if(FLAGUSERREG!=2):
	print(u"Content-type: text/html\n")
	print(u'''<!DOCTYPE html>
<html class="no-js" lang="zxx">
<head>
    <meta charset="cp1251">
    <meta http-equiv="refresh" content="1; url=../ADMINPANEL.html">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Возвращаемся в туристы...</title>
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
  <div class="bradcam_area breadcam_bg_1 overlay">
    <h3>BAD DATA</h3>
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
else:
	print(u"Content-type: text/html\n")
	print(u'''<!DOCTYPE html>
<html class="no-js" lang="zxx">
<head>
    <meta charset="cp1251">
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
</head>
<body>
    <header>
            <div class="header-area ">
                <div id="sticky-header" class="main-header-area">
                    <div class="container-fluid p-0">
                        <div class="row align-items-center no-gutters">
                            <div class="col-xl-5 col-lg-5">
                                <div class="main-menu  d-none d-lg-block">
                                    <nav>
                                        <ul id="navigation">
                                            <li><a href="../index.html">Главная</a></li>
                                            <li><a href="MENU.py">Туры</a></li>
                                            <li><a href="ABOUT.py">О компании</a></li>
                                            <li><a href="../contact.html">Отзывы</a></li>
                                        </ul>
                                    </nav>
                                </div>
                            </div>
                            <div class="col-xl-2 col-lg-2">
                                <div class="logo-img">
                                    <a href="../index.html">
                                        <img src="../img/logo.png" alt="">
                                    </a>
                                </div>
                            </div>
                            <div class="col-xl-5 col-lg-5 d-none d-lg-block">
                                <div class="book_room">
                                    <div class="socail_links">
                                        <ul>
                                            <li>
                                                <a href="https://t.me/LiveFIowers">
                                                    <i class="fa fa-telegram"> </i>
                                                </a>
                                            </li>
                                            <li>
                                                <a href="https://vk.com/club212661644">
                                                    <i class="fa fa-vk"></i>
                                                </a>
                                            </li>
                                            <li>
                                                <a href="https://ok.ru/group/68919525769263">
                                                    <i class="fa fa-odnoklassniki"></i>
                                                </a>
                                            </li>
                                        </ul>
                                    </div>
                                    <div class="book_btn d-none d-xl-block">
                                        <a class="#" href="../reg.html">Регистрация</a>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12">
                                <div class="mobile_menu d-block d-lg-none"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>
	<div class="bradcam_area breadcam_bg_1 overlay">
		<h3>Аккаунты</h3>
	</div>
    <form action="ADDDELFLOWER.py">
        <input type="hidden" name="email" value="'''+EMAIL.encode("utf-8").decode("cp1251")+'''" />
        <input type="hidden" name="password" value="'''+PASSWORD.encode("utf-8").decode("cp1251")+'''" />
        <div class="form-group mt-3">
            <button type="submit" class="button button-contactForm boxed-btn">Настроить ассортимент</button>
        </div>
	</form>
    <div class="about_area">'''+text+'''</div>
</div>
<footer class="footer">
    <div class="footer_top">
        <div class="container">
            <div class="row">
                <div class="col-xl-4 col-md-6 col-lg-4">
                    <div class="footer_widget text-center ">
                        <h3 class="footer_title pos_margin">
                              Санкт-Петербург
                        </h3>
                        <p>Дворцовая пл., 2, <br> 
                                <a href="../contact.html">tyrissting@gmai.com</a></p>
                        <a class="number" href="../contact.html">+7 900 000 00 00</a>

                    </div>
                </div>
                <div class="col-xl-4 col-md-6 col-lg-4">
                    <div class="footer_widget text-center ">
                        <h3 class="footer_title pos_margin">
                            Саратов
                        </h3>
                        <p>Парковая ул., 42 <br> 
                                <a href="../contact.html">tyrissting@gmai.com</a></p>
                        <a class="number" href="../contact.html">+7 900 000 00 00</a>
                    </div>
                </div>
                <div class="col-xl-4 col-md-6 col-lg-4">
                    <div class="footer_widget text-center ">
                        <h3 class="footer_title pos_margin">
                            Нерюнгри
                        </h3>
                        <p> 678960, ул. Карла Маркса, д 4, корп 1 <br> 
                                <a href="../contact.html">tyrissting@gmai.com</a></p>
                        <a class="number" href="../contact.html">+7 900 000 00 00</a>
                    </div>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-lg-2">
                    <div class="socail_links text-center">
                        <ul>
                            <li>
                                <a href="https://t.me/LiveFIowers">
                                    <i class="fa fa-telegram"> </i>
                                </a>
                            </li>
                            <li>
                                <a href="https://vk.com/club212661644">
                                    <i class="fa fa-vk"></i>
                                </a>
                            </li>
                            <li>
                                <a href="https://ok.ru/group/68919525769263">
                                    <i class="fa fa-odnoklassniki"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
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
</html>''')
