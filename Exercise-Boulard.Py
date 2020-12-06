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
    a="caractere-d'une-chaine-en-python"
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
    a=""
    for i in range (0,l):
        a=a+mot[l-i-1]
    print(a)
#(exercice_25())

def exercice_26():
   texte=str(input("a chain of character:"))
   recherche = list(texte.split(" "))
   for i in recherche:
        if (i[0]=='a'):
            print(i)            
#(exercice_26())

def exercice_27():
    liste1=input("a chain of character:")
    liste =list(liste1.split(" "))
    somme= 0
    for i in liste:
        somme= somme + int(i)
    return somme
#print(exercice_27())

def exercice_27bis():
    liste1=input("a chain of character:")
    liste =list(liste1.split(" "))
    somme= 1
    for i in liste:
        somme= somme * int(i)
    return somme
#print(exercice_27bis())

def exercice_28():
    liste1=input("a chain of character:")
    liste =liste1.split(" ")
    if liste==['']:
        return('liste vide')
    else:
        return ('liste pleine',liste)
#print(exercice_28())

def exercice_29():
    list1=input("a chain of character:")
    list2=input("a chain of character:")
    list12 =list1.split(" ")
    list13 =list2.split(" ")
    list3=[]
    for i in (list12 + list13): 
        if i not in list3: 
            list3.append(i) 
    return(list3 )
#print(exercice_29())

def exercice_30():
    list1=input("a chain of character:")
    list2=input("a chain of character:")
    list12 =list1.split(" ")
    list13 =list2.split(" ")
    list3= 0
    for i in list12 : 
        if i in list13: 
            list3= list3 +1
    if list3 !=0:       
        return('il y a',list3,'Caractere en commun' )
    else:
        return ()
#print(exercice_30())

def exercice_31():
    list1=input("a chain of character:")
    list12 =list1.split(" ")
    list3=[]
    list4=[]
    for i in list12: 
        if(int(i)%2 == 0): 
            list3.append(i) 
        else:
            list4.append(i) 
    return('liste des nombre impair',list4,'liste des nombre pair',list3)
#print(exercice_31())

def exercise_32():
    from itertools import permutations
    list1=input("a chain of character:")
    list12 =list1.split(" ")
    list12=list(permutations(list12))
    return list12
#print (exercise_32())

def exercise_33():
    s=input("a chain of character:")
    return(s[0::2])
#print (exercise_33())

def exercice_34():
    notes = [12 , 4 , 14 , 11 ,  18 , 13 ,  7, 10 , 5 , 9 , 15 , 8 , 14 , 16] 
    list3=[]
    list4=[]
    for i in notes: 
        if i>= 10: 
            list3.append(i)
        else:
            list4.append(i) 
    return(list4,list3)
#print(exercice_34())

def exercice_35():
    import webbrowser 
    url =input("a chain of character:")
    webbrowser.open(url)
    return(url)
#print(exercice_35())

def exercice_36():
    sentence =input("a chain of character:")
    t=" ".join(sentence.split()) 
    return(t)
#print(exercice_36())
 
def exercice_37():
    s1=(input("a chain of character:"))
    s2=(input("a chain of character:"))
    s4 =s1.split(" ")
    s5 =s2.split(" ")
    s3=[]
    for i in s4 : 
        if i in s5:
            s3.append(i)
    return(s3)
#print(exercice_37())

def exercice_38():
    phrase=(input("a chain of character:"))
    phrase1=phrase.split(" ")
    phrase2=[]
    for i in phrase1:
        if len(i)> len(phrase2):
            phrase2=i
    return(phrase2)        
#print(exercice_38())

def exercice_39():
    texte=(input("a chain of character:"))
    texte1=texte.split(" ")
    return len(texte1)       
#print(exercice_39())

def exercice_40():
    texte=(input("a chain of character:"))
    texte1=texte.split(" ")
    texte_inverse= ""
    save=texte1[0]
    texte1[0]=texte1[len(texte1)-1]
    texte1[len(texte1)-1]=save
    for i in texte1:
        texte_inverse = texte_inverse + i + ' '
    return(texte_inverse)    
#print(exercice_40())

def exercice_41():
    s=(input("liste of nomber please:"))
    s1=s.split(" ")
    n=int(input("nomber please:")) 
    s3=[]
    for i in s1:
        if int(i)%n==0:
            s3.append(i)
    return(s3)
#print(exercice_41())

def exercice_42():
    l=(input("liste of nomber please:"))
    l1=l.split(" ")
    print(l1)
    x=(input("nomber please:")) 
    l3=0
    for i in l1:
        if (i==x):
            l3=l3+1
    return(l3)
#print(exercice_42())

def exercice_43():
    l=(input("Word please:"))
    l1=l[0]
    for i in l[1:]:
        l1=l1+"*"+i
    return(l1)
#print(exercice_43())

def exercice_45():
    s=(input("Words please:"))
    s2=0
    s3=0
    for i in s:
        if i==i.upper():
            s2=s2+1
        else:
            s3=s3+1
    return('nombre de majuscules',s2,'nombre de minuscules',s3,)
#print(exercice_45())

def exercice_46():
    user_number = int(input("Enter a number : "))
    list_number = []
    while user_number > 0:
        number = user_number % 10
        list_number.append(number)
        user_number = user_number // 10
    return (list_number[::-1])
#print(exercice_46())

def exercice_47():
    s1=(input("a chain of character:"))
    s2=(input("a chain of character:"))
    s4 =s1.split(" ")
    s5 =s2.split(" ")
    s3=[]
    for i in s4 : 
        if i in s5:
            s3.append(i)
    return(s3)
#print(exercice_47())



