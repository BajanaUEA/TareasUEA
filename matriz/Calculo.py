def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el monto del descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Programa principal
if __name__ == "__main__":
    # Primera llamada a la función (sin porcentaje de descuento, usa el valor por defecto)
    monto1 = 150.00  # Monto total de la compra
    descuento1 = calcular_descuento(monto1)  # Llamada a la función
    monto_final1 = monto1 - descuento1  # Calcular el monto final
    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}\n")

    # Segunda llamada a la función (con porcentaje de descuento personalizado)
    monto2 = 200.00  # Monto total de la compra
    porcentaje2 = 15  # Porcentaje de descuento
    descuento2 = calcular_descuento(monto2, porcentaje2)  # Llamada a la función
    monto_final2 = monto2 - descuento2  # Calcular el monto final
    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento: ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")
