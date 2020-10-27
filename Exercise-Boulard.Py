# Ecrire un programme en langage Python qui demande à l’utilisateur de saisir son nom et de lui afficher son nom avec un message de bienvenue !
#name= input("votre name:")
#print("welcome:",name)

def exercice_2():
    a= input(" number please:")
    b= input(" number please:")
    a= int(a)
    b= int(b)
    c= a+b
    return c
#print(exercice_2())

def exercice_3():
    a= input(" number please:")
    b= input(" number please:")
    a= int(a)
    b= int(b)
    if (a>b):
        return(a)
    else:
        return(b)
#print(exercice_3())

def exercice_4():
    for i in range(0,101): 
       return(i)  
#print(exercice_4())

def exercice_5():
    a= input(" number please:")
    a= int(a)
    if( a%2 == 0):
        return("number is pair")
    else:
        return("number is impair")
#print(exercice_5())   

def exercice_6():
    a= input(" Your age please:")
    a= int(a)
    if( a >= 18):
        return("you are Major")
    else:
        return("you are a child ")
#print(exercice_6())   

def exercice_7():
    a= input(" number please:")
    b= input(" number please:")
    c= input(" number please:")
    a= int(a)
    b= int(b)
    c= int(c)
    if (a>b) and (a>c):
        return(a)
    elif(b>c):
        return(b)
    else:
        return(c)            
#print(exercice_7())

def exercice_8():
    g=int(input("a monbre please"))
    y=0
    for i in range (1,(g+1)):
        y= y+i
    return (y)
#print(exercice_8())

def exercice_9():
    Z=int(input("a monbre please"))
    y=1
    for i in range (1,(Z+1)):
        y= y*i
    return (y)
#print(exercice_9())

def exercice_10():
    from math import pi
    r=int(input("a monbre please"))
    #Périmetre 
    P= 2*pi*r
    #Surface du cercle
    S=(pi*(r**2))
    return S,P
#print(exercice_10())


def exercice_11():
    n=int(input("a monbre please"))
    for i in range (1,n+1):
        if(n%i==0):
                print(i)
#(exercice_11())

def exercice_12():
    # 1)
    e=int(input("a monbre please"))
    print("la table de multiplication de :",e)
    for i in range (1,10):
        print(i,"x",e,"=",i*e)
    # 2)
    f=int(input("a monbre please"))
    print("la table de multiplication de :",f)
    for i in range (1,10):
        print(i,"x",f,"=",i*f)  
    g=int(input("a monbre please"))
    print("la table de multiplication de :",g)
    for i in range (1,10):
        print(i,"x",g,"=",i*g) 
    h=int(input("a monbre please"))
    print("la table de multiplication de :",h)
    for i in range (1,10):
        print(i,"x",h,"=",i*h)               
#(exercice_12())

def exercice_13():
 a=int(input("a monbre please:"))
 b=int(input("a monbre please:"))
 c=(a//b)
 d=(a%b) 
 print(c,d)
#(exercice_13())

def exercice_14():
    from math import sqrt 
    z=int(input("a monbre please:"))
    if (sqrt(z) - int(sqrt(z))) == 0:
       print("carrée parfait")
    else:
        print("non")
#(exercice_14())


def exercice_15():
    e=int(input("a monbre please:"))
    j=0
    for i in range (1,e+1):
        if(e%i == 0):
            j = j + 1
    if( j == 2):
        print("nombre premier")
    else:
        print("n'est pas un nombre premier ")
#(exercice_15())

#CHAINE DE CARRACTAIRE 

def exercice_16():
     r=("python")
     print(r[0])
     print(r[1])
     print(r[2])
     print(r[3])
     print(r[4])
     print(r[5])     
#(exercice_16())

def exercice_17():
    r=("je suis en master inductrie numerique")
    nombre =set({})
    for x in r:
        if x not in nombre:
            nombre.add(x)
            print("there is", x, " in r :", r.count(x))
#(exercice_17())

def exercice_18():
    z=str(input("a chain of character:"))
    for i in z:
        if (i=='o'):
            print('the letter o is in position ',i, )
        else:
            print("your letter is not in",i,)           
#(exercice_18())

def exercice_19():
    a=['laptop','iphone','tablet','rouge']
    e=a[0]
    i=a[1]
    s=a[2]
    f=a[3]
    print(f,len(f),e,len(e),i,len(i),s,len(s))
#(exercice_19())

def exercice_20():
    a="caractere-dune-chaine-en-python"
    b=len(a)
    first=a[0]
    last= a[b-1]
    l1= a[1:b-1]
    l2= last + l1 + first  
    print(l2)
#(exercice_20())

def exercice_21():
    voyelle = ['a','e','y','u','i','o']
    z=str(input("a chain of character:"))
    voy =0
    for i in z:
        if (z[i] in voyelle):
            voy =  voy + 1
            print("there is" ,voy, 'in ',i, )
        else:
           print("there is no vowel in",i,)   
#(exercice_21())

def exercice_22():
    s=str(input("a chain of character:"))
    l=len(s)
    first=" "
    i=0
    while (s[i] != " "):
        first = first + s[i]
        i = i + 1
    print('the first is ', s[:i], 'la longeur et',l)   
#(exercice_22())

def exercice_23():
    file= input("a name of a file:")
    r = list(file.split("."))
    extentionfile = "."+ r [-1]
    print(extentionfile)
#(exercice_23())

def exercice_24():
    palindrome= str(input("a chain of character:"))
    l=len(palindrome)
    verif = False
    for i in range (0,l):
        if palindrome[i] !=palindrome[l-i-1]:
            verif=True
    if verif== True:
        print("Not a palindrome",l)
    else:
        print("palindrome",l)
#(exercice_24())
    
def exercice_25():
    mot=str(input("a chain of character:"))
    l=len(mot)
    for i in range (0,l):
        print(mot[l-i-1])
#(exercice_25())

def exercice_26():
   texte=str(input("a chain of character:"))
   recherche = list(texte.split(" "))
   for i in recherche:
        if (i[0]=='a'):
            print(i)            
#(exercice_26())

def exercice_27():
    liste1=list(input("a chain of character:"))
    somme= 0
    for i in liste1:
        somme= somme+i
    return somme
print(exercice_27())


