def toplama():
    sayi1=int(input("sayi1:"))
    sayi2=int(input("sayi2:"))
    sonuc=sayi1+sayi2
    print(f"sonuc:{sonuc}")

def cikarma():
    sayi1=int(input("sayi1:"))
    sayi2=int(input("sayi2:"))
    sonuc=sayi1-sayi2
    print(f"sonuc:{sonuc}")

def carpma():
    sayi1=int(input("sayi1:"))
    sayi2=int(input("sayi2:"))
    sonuc=sayi1*sayi2
    print(f"sonuc:{sonuc}")

def bolme():
    sayi1=int(input("sayi1:"))
    sayi2=int(input("sayi2:"))
    if sayi2==0:
        print("tanimsizlik var.")
        sayi2=int(input("yeni sayi2:"))

    sec=int(input("tam bolme(1) kesirli bolme(2):"))
    if sec==1:
        sonuc=sayi1//sayi2
        print(f"sonuc:{sonuc}")

    elif sec==2:
        sonuc=sayi1/sayi2
        print(f"sonuc:{sonuc}")
    
def mutlakdeger():
    sayi=int(input("sayi:"))

    if sayi>=0:
        print(f"sonuc:{sayi}")
    else:
        sayi=sayi*(-1)
        print(f"sonuc:{sayi}")

def faktoriyel():
    sayi=int(input("sayi:"))
    sonuc=1

    if sayi==0 or sayi==1:
        sonuc=1
    else:
        for i in range(0,sayi,1):
            sonuc=sonuc*(i+1)

    print(f"sonuc:{sonuc}")

def karekok():
    sayi=int(input("sayi:"))
    sonuc=sayi**0.5
    print(f"sonuc:{sayi}")

def denklemkoku():
    a=int(input("a:"))
    b=int(input("b:"))
    c=int(input("c:"))
    delta=(b**2)-(4*a*c)
    x1=(b-(delta**0.5))/2*a
    x2=(-b-(delta**0.5))/2*a
    print(f"x1:{x1} x2:{x2}")

def us():
    taban=int(input("taban:"))
    us=int(input("us:"))
    sonuc=1
    for i in range(0,us,1):
        sonuc*=taban
    print(f"sonuc:{sonuc}")

while True:
    print("toplama:1 cikarma:2 carpma:3 bolme:4 mutlakdeger:5 faktoriyel:6 karekok:7 denklem:8 us:9")
    secim=int(input("secim:"))

    if secim==0:
        break
    elif secim==1:
        toplama()
    elif secim==2:
        cikarma()
    elif secim==3:
        carpma()
    elif secim==4:
        bolme()
    elif secim==5:
        mutlakdeger()
    elif secim==6:
        faktoriyel()
    elif secim==7:
        karekok()
    elif secim==8:
        denklemkoku()
    else:
        us()
    