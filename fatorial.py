def fatorial(num):
    num = int(input('Digite um número para se calcular o fatorial dele: '))
    if num < 0:         
        print("Fatorial negativo não existe.")    
    elif num == 0:         
        return 1            
    else:         
        fact = 1        
    while(num > 1):             
        fact *= num             
        num -= 1        
        return fact 