# 📍 Программа для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in ['❌', '✔️ ']:
    for y in ['❌', '✔️ ']:
        for z in ['❌', '✔️ ']:
            if not (x or y or z) == (not x and not y and not z):
                print(f'X: {x} ; Y: {y} ; X: {z} ')