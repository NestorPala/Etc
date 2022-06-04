""" github.com/NestorPala """


# La media es el valor promedio de un conjunto de datos numéricos, 
# calculada como la suma del conjunto de valores dividida 
# entre el número total de valores.
def media(nums):
    if not nums: return None
    total = 0
    for n in nums: total += n
    return total/len(nums)


# En el ámbito de la estadística, la mediana representa el valor de 
# la variable de posición central en un conjunto de datos ordenados.
# Si la serie tiene un número par de puntuaciones, 
# la mediana es la media entre las dos puntuaciones centrales.
def mediana(nums):
    if not nums: 
        return None

    n = len(nums)
    medio = int((n - 1)/2)
    nums = sorted(nums)

    return nums[medio + 1] if (n % 2 != 0) else (nums[medio] + nums[medio + 1]) / 2


# En la estadística, la moda es el valor que aparece con mayor frecuencia 
# en un conjunto de datos. Esto va en forma de una columna cuando 
# encontremos dos modas, es decir, dos datos que tengan la misma 
# frecuencia absoluta máxima. Una distribución trimodal de los datos 
# es en la que encontramos tres modas.
def moda(nums):
    if not nums: 
        return None
    
    apariciones = dict()
    maximo = 0
    modas = set()
    
    for n in nums:
        if n not in apariciones:
            apariciones[n] = 1
        else:
            apariciones[n] += 1
            
        if apariciones[n] >= maximo:
            maximo = apariciones[n]
    
    for a in apariciones:
        if apariciones[a] == maximo:
            modas.add(a)
    
    return list(modas)[::-1]


def main():
    nums = [5, 5, 8, 7, 8, 7.5]

    print("Media:", round(media(nums), 2))
    print("Mediana:", mediana(nums))
    print("Moda:", moda(nums))


main()
