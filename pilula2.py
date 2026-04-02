def simularCrecimento(pop, taxa, limite):
    anos = 0
    while pop <= limite:
        pop = pop * (1+taxa/100)
        anos += 1
    return anos

#main
p = float(input('População: '))
t = float(input('Taxa (%): '))
l = float(input('Limite: '))
print(f'Anos = {simularCrecimento(p,t,l)}')