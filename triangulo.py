def basealtura():
    return(base* altura /2)

if __name__ == "__main__":
    base = int(input("Digite o valor da base:"))
    altura = int(input("Digite o valor da altura:"))

    print(basealtura())