# -*- coding: cp1251 -*-
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
MESSAGE=form.getfirst("message","")
NAME=form.getfirst("name","")
EMAIL=form.getfirst("email","")
SUBJECT=form.getfirst("subject","")
flag=False
Flag=False
if(MESSAGE and NAME and EMAIL and SUBJECT):
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.settimeout(.1)
	sock.connect(("127.0.0.1",31222))
	data=RECV(sock,timedelay)
	for line in list(map(str,data.split("|"))):
		if((not flag) and (line==EMAIL)):Flag=True;break
		flag=not flag
text="Îøèáêà ïðè äîáàâëåíèè îòçûâà: äëÿ ïóáëèêàöèè îòçûâà âû äîëæíû áûòü çàðåãèñòðèðîâàíû è çàïîëíåíû âñå ïîëÿ!"
if(Flag):
	with open("otzivi.txt","a") as f:f.write(SUBJECT+"\n"+NAME+"\n"+EMAIL+"\n"+MESSAGE+"\n")
	text="Óäà÷íîå äîáàâëåíèå îòçûâà."
print(u"Content-type: text/html\n")
print(u'''<!DOCTYPE html>
<html class="no-js" lang="zxx">
<head>
    <meta charset="cp1251">
    <meta http-equiv="refresh" content="5; url=OTZIV.py">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Возвращаем к туристы...</title>
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