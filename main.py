def obtener_monto():
    while True:
        try:
            monto = float(input("Ingrese el monto en Dólares (USD): "))
            if monto <= 0:
                print("El monto debe ser mayor a cero. Intente de nuevo.")
                continue
            return monto
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def convertir_moneda(monto, tasa=3.75):
    return monto * tasa

def main():
    print("--- Conversor de Monedas Express ---")
    monto = obtener_monto()
    resultado = convertir_moneda(monto)
    print(f"\n[Éxito] {monto:.2f} USD equivalen a {resultado:.2f} PEN")

if __name__ == "__main__":
    main()