import random

#bubble sort
def bubble_sort(v):
    fim = len(v)
    
    while fim > 0:
        i = 0
        #percorrendo o vetor de 0 até fim
        while i < fim -1: 
            #se vetor atual for maior que o próximo vetor 
            if v[i] > v[i+1]:
                #se realiza a troca do vetor atual para uma variavel temp
                temp = v[i]
                #troca o valor do vetor atual pelo do proximo vetor
                v[i] = v[i+1]
                #troca o valor do proximo vetor pelo do vetor atual que esta armazenado na variavel temp
                v[i+1] = temp
                print(v)
            i += 1
        fim -= 1        


#Selection sort
def selection_sort(v):
    n = len(v)
    for j in range(n-1):
        menor_valor_index = j
        for i in range(j, n):
            if v[i] < v[menor_valor_index]:
                menor_valor_index = i
        if v[j] > v[menor_valor_index]:
            temp = v[j]
            v[j]= v[menor_valor_index]
            v[menor_valor_index] = temp
        
    
    
    
    
     



vetor = random.sample(range(1,100),10)

print(vetor)


selection_sort(vetor)

print(vetor)
