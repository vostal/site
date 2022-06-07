# -*- coding: cp1251 -*-
#!/usr/bin/env python3
import cgi
import socket
from datetime import datetime
def SEND(sock,s,timetodie):
  #Complite
  timeSTOP=datetime.now()
  IsNormal=False
  while(not IsNormal):
    ToClose=False
    Time=datetime.now()-timeSTOP
    if((Time.seconds+Time.microseconds/10**6)>timetodie):IsNormal=False;break
    try:
      if(type(s)!=bytes):t=b"0";s=s.encode("utf-8")
      else:t=b"1"
      timeSTO=datetime.now()
      while(True):
        Time=datetime.now()-timeSTO
        try:sock.send(t);break
        except:
          if((Time.seconds+Time.microseconds/10**6)>timdelayI):IsNormal=False;ToClose=True;break
      if(ToClose):continue
      output=bytearray()
      while(s):
        if(len(s)>=255):
          output.append(255)
          output+=bytearray(s[:255])
          s=s[255:]
          if(not s):output.append(0)
          sock.send(bytes(output))
          output=[]
        else:
          output.append(len(s))
          output+=bytearray(s)
          s=bytes()
          sock.send(bytes(output))
      IsNormal=True
      break
    except Exception as e:
      #if(("[WinError 10053]" in str(e)) or ("[WinError 10054]" in str(e))):assert "Disconnected"
      IsNormal=False
  return IsNormal
form=cgi.FieldStorage()
EMAIL=form.getfirst("email","")
PASSWORD=form.getfirst("password","")
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.settimeout(.1)
timdelay=2
timdelayI=.4
text="������� ���������� ������� ����� �����������. ��� ��������� ��������� ����������� �������� �����."
try:
	sock.connect(("127.0.0.1",23333))
	SEND(sock,EMAIL+" "+PASSWORD,timdelay)
except:text="������ �������� ��������.(������ � ������ ������ ����������)."
try:sock.close()
except:pass

print(u"Content-type: text/html\n")
print(u'''<!DOCTYPE html>
<html class="no-js" lang="zxx">
<head>
    <meta charset="cp1251">
    <meta http-equiv="refresh" content="5; url=../index.html">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Возвращение на Туристы...</title>
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
    <h3>'''+text+'''</h3>
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
</html>
<head>''')