def obtener_monto():
    monto = float(input("Ingrese el monto en Dólares (USD): "))
    return monto

def convertir_moneda(monto, tasa=3.75):
    return monto * tasa

def main():
    print("--- Conversor de Monedas Express ---")
    monto = obtener_monto()
    resultado = convertir_moneda(monto)
    print(f"Monto equivalente: {resultado:.2f} PEN")

if __name__ == "__main__":
    main()