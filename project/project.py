import pyttsx3
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

book=[word for line in open('sowpods.txt', 'r') for word in line.split()]


lettersi=str(input("What are the letters you have on your rack?"))
engine = pyttsx3.init();
engine.say("What are the letters you have on your rack?");
engine.runAndWait() ;

lettersir=[]
lettersir1=[]
letterct={}
for z in lettersi:
    lettersir.append(z)
for i in lettersir:
    ltrkeys=letterct.keys()
    if i in ltrkeys:
        letterct[str(i)]=letterct[str(i)]+1
    else:
        letterct[str(i)]=1
print( letterct)
def findwords(letters,book1):
    wordslist=[]
    for x in book1:
        letterctdct={}
        checker=True
        lettersir1=[]
        for ltr in x:
            lettersir1.append(ltr)
        for ltr1 in lettersir1:
            ltrkeys1=letterctdct.keys()
            if ltr1.lower() in ltrkeys1:
                    letterctdct[str(ltr1).lower()]+=1
            else:
                    letterctdct[str(ltr1).lower()]=1 
        ltrkeys1=letterctdct.keys()
        ltrkeys=letters.keys()
        
            
        for j in ltrkeys1:
                
                if j in ltrkeys:
                    if letterctdct[j]>letters[j]:
                         checker=False
                         
                else:
                   checker=False
                  
            
               
        if checker is True:
                
                wordslist.append(x)
   
    return(wordslist)  
     
def findscore(word):
    word1=word.lower()
    totalscore=0
    for q in word1:
        totalscore+=scores[q]
    return totalscore
wrdlist=findwords(letterct,book)
finaldict={}
for d in wrdlist:
    finaldict[d]=findscore(d)
str(finaldict)


print(finaldict)
