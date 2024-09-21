def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcular el descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    # Retornar el monto del descuento calculado
    return descuento

# Programa principal

# Llamada 1: Proporcionando solo el monto total (descuento por defecto del 10%)
monto_total_1 = 5000.0  # Monto total de la compra
descuento_1 = calcular_descuento(monto_total_1)
print(f"Descuento con 10% predeterminado para una compra de ${monto_total_1}: ${descuento_1:.2f}")

# Llamada 2: Proporcionando el monto total y un porcentaje de descuento personalizado (15%)
monto_total_2 = 2000.0  # Monto total de la compra
descuento_2 = calcular_descuento(monto_total_2, 15)  # 15% de descuento
print(f"Descuento con 15% para una compra de ${monto_total_2}: ${descuento_2:.2f}")
