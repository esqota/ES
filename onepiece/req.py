import requests
PreRegisterId = "MTU2NjI0NzQ0NTQ5NDY4MzMzMQ=="
PhoneNumber = "7156913180"
PushToken = "GCM:dJ8w_8NBQ_Ksi8yET6hxXm:APA91bEw894q39qP4wDfX9sUdOsnTGHYKXvI91LQ4PjQ16pXTez3S9y1frHZE-zO20VzZ4mfl5aXHkllMb1F7PApAYeZY9XPViomAPXU4oqe84zJj9lVVfu4jgU-4H9vQVru62Dhiy5_"
CountryIDDCode = "1"
UDID = "74983d250dfbbc5bf230a021b1ec529689496129"
DeviceType = "A33w"
DeviceManuf = "oppo"
SystemVersion = "5.1"
System = "Android"
Language = "en"
ViberVersion = "15.2.0.14"
CC = "eg"
IMSI = "602022202435114"
xml = """XMLDOC=%3CRegisterUserRequest%3E%0A%20%20%20%3CPreRegisterId%3E{0}%3C%2FPreRegisterId%3E%0A%20%20%20%3CPhoneInputMethod%3E1%3C%2FPhoneInputMethod%3E%0A%20%20%20%3CPhoneNumber%3E{1}%3C%2FPhoneNumber%3E%0A%20%20%20%3CPushToken%3E{2}%3C%2FPushToken%3E%0A%20%20%20%3CCountryIDDCode%3E{3}%3C%2FCountryIDDCode%3E%0A%20%20%20%3CUDID%3E{4}%3C%2FUDID%3E%0A%20%20%20%3CDeviceType%3E{5}%3C%2FDeviceType%3E%0A%20%20%20%3CDevice%3Ephone%3C%2FDevice%3E%0A%20%20%20%3CDeviceManuf%3E{6}%3C%2FDeviceManuf%3E%0A%20%20%20%3CSystemVersion%3E{7}%3C%2FSystemVersion%3E%0A%20%20%20%3CSystem%3E{8}%3C%2FSystem%3E%0A%20%20%20%3CLanguage%3E{9}%3C%2FLanguage%3E%0A%20%20%20%3CViberVersion%3E{10}%3C%2FViberVersion%3E%0A%20%20%20%3CCC%3E{11}%3C%2FCC%3E%0A%20%20%20%3CMCC%3E602%3C%2FMCC%3E%0A%20%20%20%3CMNC%3E02%3C%2FMNC%3E%0A%20%20%20%3CVoIP%3E1%3C%2FVoIP%3E%0A%20%20%20%3CMCCSim%3E602%3C%2FMCCSim%3E%0A%20%20%20%3CMNCSim%3E03%3C%2FMNCSim%3E%0A%20%20%20%3CMCCNetwork%3E602%3C%2FMCCNetwork%3E%0A%20%20%20%3CMNCNetwork%3E02%3C%2FMNCNetwork%3E%0A%20%20%20%3CIMSI%3E{12}%3C%2FIMSI%3E%0A%20%20%20%3CNoHangup%3E0%3C%2FNoHangup%3E%0A%20%20%20%3CReRegisterState%3E0%3C%2FReRegisterState%3E%0A%3C%2FRegisterUserRequest%3E""".format(PreRegisterId,PhoneNumber,PushToken,CountryIDDCode,UDID,DeviceType,DeviceManuf,SystemVersion,System,Language,ViberVersion,CC,IMSI)
content_length = len(xml)
accept_encoding = "gzip, deflate"
headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'User-Agent':'Android',
           'Content-Length':'{0}'.format(content_length),
           'Host':'secure.viber.com',
           'Connection':'close',
           'Accept-Encoding':'{0}'.format(accept_encoding)
           }
           

print("sending the request...")   

print(requests.post('http://secure.viber.com/viber/viber.php?function=RegisterUser', data=xml, headers=headers).text)

i = 0
#while i < 10: 
##  print(requests.post('http://secure.viber.com/viber/viber.php?function=RegisterUser', data=xml, headers=headers).text)    
# i = i + 1

print("finished")   
