import time

name = input("Hola, como te llamas? ")

print ("Hola, " + name, "Vamos a jugar al ahorcado!")

time.sleep(1)

print ("Adivina la palabra...")
time.sleep(0.5)
 
palabra = ("ballena")

adivinanza = ''

turnos = 10

while turnos > 0:         

    failed = 0             
    
    for char in palabra:      

        if char in adivinanza:    
    
            print (char,end=""),    

        else:
    
            print ("_",end=""),     
       
            failed += 1    


    if failed == 0:        
        print (" Ganaste!")
        break            
    adivina = input(" adivina una letra:") 

    adivinanza += adivina                    

    if adivina not in palabra:  
 
        turnos -= 1        
 
        print (" Incorrecto")  
 
        print (" tenes", + turnos, 'volve a adivinar' )
 
        if turnos == 0:           
    
            print (" Perdiste!"  )

      