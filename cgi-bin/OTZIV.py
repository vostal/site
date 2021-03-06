# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import cgi
form=cgi.FieldStorage()
text=""
flag=0
with open("otzivi.txt","r") as f:
	for line in f:
		if(line[-1]=="\n"):line=line[:-1]
		text+="""<div class="container">
            <div class="row align-items-center">
                <div class="col-xl-5 col-lg-5 offset-lg-1 col-md-6">
                    <h3>"""*(flag==0)+line+"</h3><h3>"*(flag==1)+(flag==0)*"""</h3>
                    <h3>"""+(flag==2)*"""</h3>
                </div>
                <p><textarea rows="10" cols="90" name="text" readonly>"""+(flag==3)*"""</textarea></p>
            </div>
        </div>"""
		flag+=1
		if(flag==4):flag=0
print(u"Content-type: text/html\n")
print(u'''<!DOCTYPE html>
<html class="no-js" lang="zxx">
<head>
    <meta charset="cp1251">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Туристы</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" type="../image/x-icon" href="../img/favicon.png">
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
    <h3>Отзывы</h3>
</div>
<div class="about_area">
        '''+text+'''
    </div>
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
    <script src="../js/popper.min.js"></script>
    <script src="../js/bootstrap.min.js"></script>
    <script src="../js/owl.carousel.min.js"></script>
    <script src="../js/isotope.pkgd.min.js"></script>
    <script src="../js/ajax-form.js"></script>
    <script src="../js/waypoints.min.js"></script>
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
    <script src="../js/mail-script.js"></script>
    <script src="../js/main.js"></script>
</body>
</html>''')
