
#PRECEDENCIA

# 1. (n + n) 
# 2. **
# 3. * / // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5 
print(conta_1)  #conta está errada por conta da precedencia 

conta_2 = (1 + 1) ** (5 + 5) 
print(conta_2)  #conta está correta por conta da precedencia 


conta_3 = (1 + int(0.5 + 0.5)) ** (5 + 5) #Exemplo do prof.
print(conta_3)