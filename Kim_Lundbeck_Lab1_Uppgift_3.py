#Kubsummering
#2016-08-30

#Följande program kommer att fråga efter, och läsa in, två heltal; a och b
#Programmet kommer sedan summera deras kuber och skriva ut svaret.
#Detta kommer att återupprepas så länge användaren önskar.
print("""Detta program räknar ut kubsumman av två heltal, a och b.
    avsluta programmet genom med Ctrl+c eller Ctrl+z""")

while True:
    print("")
    a=int(input("Skriv in a: "))
    b=int(input("Skriv in b: "))

    sum=a**3+b**3
    print("Kubsumman av (",a,"^3)+(",b,"^3)=",sum,sep='')

        
