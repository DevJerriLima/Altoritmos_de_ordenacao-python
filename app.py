import random

 
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






vetor = list(range(0,50))

random.shuffle(vetor)

print(vetor)

bubble_sort(vetor)
