def ejercicio5():
    repetir1=True
    repetir2=True
    print "dime un dia"
    while(repetir1==True):
        a=input("a= ")
        repetir1=a<1 or a>31
        if(repetir1==True):
            print "ERROR. este dia no existe"
    print "dime un mes"
    while(repetir2==True):
        b=input("b= ")
        repetir2=b<1 or b>12
        if(repetir2==True):
            print "ERROR. este mes no existe" 
    if (b==1):
        b="enero"
    if (b==2):
        b="febrero"
    if (b==3):
        b="marzo"
    if (b==4):
        b="abril"
    if (b==5):
        b="mayo"
    if (b==6):
        b="junio"
    if (b==7):
        b="julio"
    if (b==8):
        b="agosto"
    if (b==9):
        b="septiembre"
    if (b==10):
        b="octubre"
    if (b==11):
        b="noviembre"
    if (b==12):
        b="diciembre"
    print "dime un a�o"
    c=input("c= ")
    print a, "de", b, "de", c

ejercicio5()
        
    
