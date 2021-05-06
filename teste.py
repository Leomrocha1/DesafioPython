x = float(input("Digite x: "))
y = float(input("Digite y: "))

# suponha que (x,y) esta dentro
dentro = True

if x < 0 or x > 5 or y < 0 or y > 5:
    # aqui sabemos que (x,y) esta fora da face
    dentro = False


if dentro:
    print("dentro")
else:
    print("fora")
