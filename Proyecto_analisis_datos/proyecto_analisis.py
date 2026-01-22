import pandas as pd
import matplotlib.pyplot as plt

# importamos nuestros datos del archivo CSV
df = pd.read_csv('sales.csv')

# Vista de los datos
print("Vista de datos CSV: ")
print(df.head())

# Limpieza de datos
df.dropna(inplace = True)

# Analizar tipos de datos
df['total_price'] = df['total_price'].astype(float)
df['tax'] = df['tax'].astype(float)

# Análisis estadístico
print("\nAnalisis estadistico descriptivo: ")
print(df.describe())

# Resumen estadistico de ventas
total_ventas = df['total_price'].sum()
promedio_ventas = df['total_price'].mean()
max_ventas = df['total_price'].max()
min_ventas = df['total_price'].min()
cantidad_ventas = df.shape[0]

# KPIs de ventas
print(f"\nKPIs :")
print(f"Total de ventas: {total_ventas}")
print(f"Promedio de ventas: {promedio_ventas}")
print(f"Máximo de ventas: {max_ventas}")
print(f"Mínimo de ventas: {min_ventas}")
print(f"Cantidad de ventas: {cantidad_ventas}")

# Analisis por categoria
ventas_categoria = (
    df.groupby('product_category')['total_price'].sum().sort_values(ascending=False)
)

print("\nVentas por categoria de producto: ")
print(ventas_categoria)

# Analisis por categoria de producto, más cantidad vendida y total de ventas
ventas_categoria_cantidad_total = (
    df.groupby('product_category')[['quantity', 'total_price']].sum().sort_values(by = 'quantity', ascending=False)
)

print("\nVentas por categoria de producto (cantidad y total): ")
print(ventas_categoria_cantidad_total)

# Nombre de los productos más vendidos
productos_mas_vendidos = (
    df.groupby('product_name')['quantity'].sum().sort_values(ascending = False)
)

print("\nProductos más vendidos (por cantidad): ")
print(productos_mas_vendidos)

# Nombre de los productos mas vendidos por la cantidad y total de ventas
productos_cantidad_ventas = (
    df.groupby('product_name')[['quantity', 'total_price']].sum().sort_values(by = 'quantity', ascending=False)
)

print("\nProductos más vendidos (cantidad y total): ")
print(productos_cantidad_ventas)

# Ventas por ciudad
ventas_ciudad = (
    df.groupby('city')['total_price'].sum().sort_values(ascending=False)
)
print("\nVentas por ciudad: ")
print(ventas_ciudad)

# Ventas por ciudad, cantidad y total de ventas
ventas_ciudad_cantidad_total = (
    df.groupby('city')[['quantity', 'total_price']].sum().sort_values(by = 'quantity', ascending=False)
)

print("\nVentas por ciudad (cantidad y total): ")
print(ventas_ciudad_cantidad_total)

# Sucursal con mas ventas 
ventas_sucursal = (
    df.groupby('branch')['total_price'].sum().sort_values(ascending=False)
)

print("\nVentas por sucursal: ")
print(ventas_sucursal)

# Sucursal con mas ventas, cantidad y total de ventas
ventas_sucursal_cantidad_total = (
    df.groupby('branch')[['quantity', 'total_price']].sum().sort_values(by = 'quantity', ascending=False)
)

print("\nVentas por sucursal (cantidad y total): ")
print(ventas_sucursal_cantidad_total)

# Precio promedio por categoria de producto
precio_promedio_categoria = (
    df.groupby('product_category')['total_price'].mean().sort_values(ascending=False)
)

print("\nPrecio promedio por categoria de producto: ")
print(precio_promedio_categoria)

# Ingreso promedio por categoria de producto
ingreso_promedio_categoria = (
    df.groupby('product_category')['total_price'].mean().sort_values(ascending=False)
)

print("\nIngreso promedio por categoria de producto: ")
print(ingreso_promedio_categoria)

# Precio promedio por categoria
precio_promedio_producto = (
    df.groupby('product_name')['unit_price'].mean().sort_values(ascending=False)
)

# Tipos de clientes que compran más
ventas_tipo_cliente = (
    df.groupby('customer_type')['total_price'].sum().sort_values(ascending=False)
)

print("\nVentas por tipo de cliente: ")
print(ventas_tipo_cliente)

# Tipos de cliente que compran más, cantidad y total de ventas
ventas_tipo_cliente_cantidad_total = (
    df.groupby('customer_type')[['quantity', 'total_price']].sum().sort_values(by = 'quantity', ascending=False)
)

print("\nVentas por tipo de cliente (cantidad y total): ")
print(ventas_tipo_cliente_cantidad_total)

# Ventas por genero
ventas_genero = (
    df.groupby('gender')['total_price'].sum().sort_values(ascending=False)
)

print("\nVentas por genero: ")
print(ventas_genero)

# Promedio de ventas por genero
promedio_ventas_genero = (
    df.groupby('gender')['total_price'].mean().sort_values(ascending=False)
)

print("\nPromedio de ventas por genero: ")
print(promedio_ventas_genero)

# Impuesto total recaudado
impuesto_total = df['tax'].sum()
print(f"\nImpuesto total recaudado: {impuesto_total}")

# Impuesto promedio por venta
impuesto_promedio = df['tax'].mean()
print(f"\nImpuesto promedio por venta: {impuesto_promedio}")

# Impuesto por ciudad
impuesto_ciudad = (
    df.groupby('city')['tax'].sum().sort_values(ascending=False)
)

print("\nImpuesto recaudado por ciudad: ")
print(impuesto_ciudad)

# Promedio de impuesto por ciudad
impuesto_promedio_ciudad = (
    df.groupby('city')['tax'].mean().sort_values(ascending=False)
)

print("\nPromedio de impuesto por ciudad: ")
print(impuesto_promedio_ciudad)

# Puntos de fidelidad totales otorgados por tipo de cliente
puntos_fidelidad_totales = (
    df.groupby('customer_type')['reward_points'].sum().sort_values(ascending=False)
)

print("\nPuntos de fidelidad totales otorgados por tipo de cliente: ")
print(puntos_fidelidad_totales)

# Promedio de puntos de fidelidad por tipo de cliente
puntos_fidelidad_promedio = (
    df.groupby('customer_type')['reward_points'].mean().sort_values(ascending=False)
)

print("\nPromedio de puntos de fidelidad por tipo de cliente: ")
print(puntos_fidelidad_promedio)

# Graficamos los datos, todos los datos

plt.figure()
ventas_categoria.plot(kind = 'bar', color = 'green')
plt.title('Ventas por Categoria de Producto')
plt.xlabel('Categoria de Producto')
plt.ylabel('Total de Ventas')
plt.xticks(rotation = 0)
plt.show()

plt.figure(figsize = (10, 5))
ventas_categoria_cantidad_total.plot(kind='bar')
plt.title('Ventas por categoría de producto (Cantidad y Total)')
plt.xlabel('Categoria de Producto')
plt.ylabel('Cantidad / Total de Ventas')
plt.xticks(rotation = 0)
plt.tight_layout()
plt.show()

plt.figure()
productos_mas_vendidos.plot(kind = 'bar', color = 'orange')
plt.title('Productos Más Vendidos (por Cantidad)')
plt.xlabel('Nombre del Producto')
plt.ylabel('Cantidad Vendida')
plt.xticks(rotation = 0)
plt.tight_layout()
plt.show()

plt.figure(figsize = (10, 5))
productos_cantidad_ventas.plot(kind='bar')
plt.title('Productos Más Vendidos (Cantidad y Total)')
plt.xlabel('Nombre del Producto')
plt.ylabel('Cantidad / Total de Ventas')
plt.xticks(rotation = 0)
plt.show()

plt.figure()
ventas_ciudad.plot(kind = 'bar', color = 'purple')
plt.title('Ventas por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Total de Ventas')
plt.xticks(rotation = 0)
plt.show()

plt.figure(figsize = (10, 5))
ventas_ciudad_cantidad_total.plot(kind='bar')
plt.title('Ventas por Ciudad (Cantidad y Total)')
plt.xlabel('Ciudad')
plt.ylabel('Cantidad / Total de Ventas')
plt.xticks(rotation = 0)
plt.tight_layout()
plt.show()

plt.figure()
ventas_sucursal.plot(kind = 'bar', color = 'red')
plt.title('Ventas por Sucursal')
plt.xlabel('Sucursal')
plt.ylabel('Total de Ventas')
plt.xticks(rotation = 0)
plt.show()

plt.figure(figsize = (10, 5))
ventas_sucursal_cantidad_total.plot(kind='bar')
plt.title('Ventas por Sucursal (Cantidad y Total)')
plt.xlabel('Sucursal')
plt.ylabel('Cantidad / Total de Ventas')
plt.xticks(rotation = 0)
plt.tight_layout()
plt.show()

plt.figure()
ventas_tipo_cliente.plot(kind = 'bar', color = 'brown')
plt.title('Ventas por Tipo de Cliente')
plt.xlabel('Tipo de Cliente')
plt.ylabel('Total de Ventas')
plt.xticks(rotation = 0)
plt.show()

plt.figure(figsize=(10, 5))
ventas_tipo_cliente_cantidad_total.plot(kind='bar')
plt.title('Ventas por Tipo de Cliente (Cantidad y Total)')
plt.xlabel('Tipo de Cliente')
plt.ylabel('Cantidad / Total de Ventas')
plt.xticks(rotation = 0)
plt.tight_layout()
plt.show()

plt.figure()
ventas_genero.plot(kind = 'bar', color = 'cyan')
plt.title('Ventas por Género')
plt.xlabel('Género')
plt.ylabel('Total de Ventas')
plt.xticks(rotation = 0)
plt.show()

plt.figure()
promedio_ventas_genero.plot(kind = 'bar', color = 'magenta')
plt.title('Promedio de Ventas por Género')
plt.xlabel('Género')
plt.ylabel('Promedio de Ventas')
plt.xticks(rotation = 0)
plt.show()

plt.figure()
impuesto_ciudad.plot(kind = 'bar', color = 'gray')
plt.title('Impuesto Recaudado por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Total de Impuesto')
plt.xticks(rotation = 0)
plt.show()

plt.figure()
impuesto_promedio_ciudad.plot(kind = 'bar', color = 'olive')
plt.title('Promedio de Impuesto por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Promedio de Impuesto')
plt.xticks(rotation = 0)
plt.show()

plt.figure()
puntos_fidelidad_totales.plot(kind = 'bar', color = 'navy')
plt.title('Puntos de Fidelidad Totales por Tipo de Cliente')
plt.xlabel('Tipo de Cliente')
plt.ylabel('Total de Puntos de Fidelidad')
plt.xticks(rotation = 0)
plt.show()

plt.figure()
puntos_fidelidad_promedio.plot(kind = 'bar', color = 'teal')
plt.title('Promedio de Puntos de Fidelidad por Tipo de Cliente')
plt.xlabel('Tipo de Cliente')
plt.ylabel('Promedio de Puntos de Fidelidad')
plt.xticks(rotation = 0)
plt.show()

plt.figure()
precio_promedio_categoria.plot(kind = 'bar', color = 'darkgreen')
plt.title('Precio Promedio por Categoria de Producto')
plt.xlabel('Categoria de Producto')
plt.ylabel('Precio Promedio')
plt.xticks(rotation = 0)
plt.show()

plt.figure()
precio_promedio_producto.plot(kind = 'bar', color = 'darkblue')
plt.title('Precio Promedio por Producto')
plt.xlabel('Nombre del Producto')
plt.ylabel('Precio Promedio')
plt.xticks(rotation = 0)
plt.show()