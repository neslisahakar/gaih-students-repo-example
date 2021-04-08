#HW2

#Question :-Get Username and Password values from the user. 
#check the values in an if statement and tell the user if they are sccessful.
#extra? try building same user login application but this time, usa a dictionary.


kullanıcı_bilgileri = {"ali@gmail.com":"knsfflak",
                       "veli@gmail.com": "293128367",
                       "ayse@hotmail.com":"AYsödöan22"}

mail = str(input("Lütfen mail adresinizi giriniz :"))

sifre =  str(input("Lütfen şifrenizi giriniz :"))

if (mail not in kullanıcı_bilgileri.keys() and sifre in kullanıcı_bilgileri.values()):
    print("Mail adresiniz hatalı")
elif (mail in kullanıcı_bilgileri.keys() and sifre not in kullanıcı_bilgileri.values()):
    print("Parolanız hatalı")
elif (mail not in kullanıcı_bilgileri.keys() and sifre not in kullanıcı_bilgileri.values()):
    print("Mail adresiniz ve parolanız hatalıdır.")
else:
    print("Tebrikler, Başarıyla giriş yaptınız")
