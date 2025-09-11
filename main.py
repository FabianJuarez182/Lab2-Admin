from estadistica import media, mediana, moda, variance, ds

def main():
    datos = [1, 2, 2, 3, 4, 5, 5, 5, 6]

    print("Datos:", datos)
    print("Media:", media(datos))
    print("Mediana:", mediana(datos))
    print("Moda:", moda(datos))
    print("Varianza:", round(variance(datos), 2))
    print("Desviación estándar:", round(ds(datos), 2))

if __name__ == "__main__":
    main()
