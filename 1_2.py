#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#Нужно написать таблицу истинности.

print()
print('Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.')
predic = [True,False]
for x in predic:
    for y in predic:
        for z in predic:
            res = not (x or y or z) == (not x) and (not y) and (not z)
            print('X=', x,'Y=', y,'Z=', z, ':' '¬(X v Y v Z) = ¬X ⋀ ¬Y ⋀ ¬Z' '=', res)