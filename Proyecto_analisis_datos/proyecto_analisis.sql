// Consultas de la tabla para ver todos los valores
SELECT * FROM Sales;

// Consulta de conteo de ventas totales
SELECT COUNT(*) AS Numero_ventas
FROM Sales;

// Consulta del total del ingreso generado
SELECT SUM(total_price) AS Total_ventas
FROM Sales;

// Consulta del promedio de ingreso generado
SELECT AVG(total_price) AS Ticket_promedio
FROM Sales;

// Consulta del valor maximo y minimo del ingreso generado
SELECT 
    MAX(total_price) AS Venta_mas_alta,
    MIN(total_price) AS Venta_mas_baja
FROM Sales;

// Numero de ventas por tipo de cliente
SELECT customer_type, COUNT(*) AS Numero_ventas
FROM Sales
GROUP BY customer_type;

// Productos mas vendidos por cantidad, ordenados de mayor a menor
SELECT product_name, SUM(quantity) AS Unidades_vendidas
FROM Sales
GROUP BY product_name
ORDER BY Unidades_vendidas DESC;

// Productos que generaron mayor ingreso, ordenados de mayor a menor
SELECT product_name, SUM(total_price) AS Ingreso_total
FROM Sales
GROUP BY product_name
ORDER BY Ingreso_total DESC;

// Productos por categoria mas vendidos por cantidad, ordenados de mayor a menor
SELECT product_category, SUM(quantity) AS Unidades_vendidas
FROM Sales
GROUP BY product_category
ORDER BY Unidades_vendidas DESC;

// Categoria de producto que genera mayor ventas 
SELECT product_category, SUM(quantity) AS Unidades_vendidas
FROM Sales
GROUP BY product_category
ORDER BY Unidades_vendidas DESC
LIMIT 1;

// Producto con precio unitario promedio mas alto
SELECT product_name, AVG(unit_price) AS Precio_promedio
FROM Sales
GROUP BY product_name
ORDER BY Precio_promedio DESC
LIMIT 1;

// Productos que vendieron menos que el promedio de unidades vendidas
SELECT product_name,
       SUM(quantity) AS Unidades_vendidas,
       SUM(total_price) AS Ingreso_total
FROM Sales
GROUP BY product_name
HAVING SUM(quantity) < (
    SELECT AVG(quantity)
    FROM Sales
)
ORDER BY Ingreso_total DESC;

// Ciudad con mayor ingreso total
SELECT city, SUM(total_price) AS Ingreso_total
FROM Sales
GROUP BY city
ORDER BY Ingreso_total DESC
LIMIT 1;

// Ciudad con mayor unidades vendidas
SELECT city, SUM(quantity) AS Unidades_vendidas
FROM Sales
GROUP BY city
ORDER BY Unidades_vendidas ASC
LIMIT 1;

// Sucursal con mayor ingreso total, ordenados de mayor a menor
SELECT branch, SUM(total_price) AS Ingreso_sucursal
FROM Sales
GROUP BY branch
ORDER BY Ingreso_sucursal DESC;

// Sucursal  con mayor promedio de ingreso
SELECT branch, AVG(total_price) AS Ticket_promedio
FROM Sales
GROUP BY branch
ORDER BY Ticket_promedio DESC
LIMIT 1;

// Ciudades que vendieron menos que el promedio de unidades vendidas
SELECT city,
       SUM(quantity) AS Unidades_vendidas,
       SUM(total_price) AS Ingreso_total
FROM Sales
GROUP BY city
HAVING SUM(quantity) < (
    SELECT AVG(cantidad_ciudad)
    FROM (
        SELECT SUM(quantity) AS cantidad_ciudad
        FROM Sales
        GROUP BY city
    ) sub
)
ORDER BY Ingreso_total DESC;

// Tipo de cliente que compro mas unidades
SELECT customer_type, SUM(quantity) AS Unidades_compradas
FROM Sales
GROUP BY customer_type
ORDER BY Unidades_compradas DESC
LIMIT 1;

// Tipo de cliente que genero mayor ingreso
SELECT customer_type, SUM(total_price) AS Ingreso_total
FROM Sales
GROUP BY customer_type
ORDER BY Ingreso_total DESC
LIMIT 1;

// Tipo de cliente que compro mas unidades
SELECT customer_type, SUM(quantity) AS Unidades
FROM Sales
GROUP BY customer_type
ORDER BY Unidades DESC
LIMIT 1;

// Tipo de cliente con mayor ticket promedio
SELECT customer_type, AVG(total_price) AS Ticket_promedio
FROM Sales
GROUP BY customer_type;

// Tipo de cliente con mas puntos de fidelidad acumulados
SELECT customer_type, SUM(reward_points) AS Puntos_fidelidad
FROM Sales
GROUP BY customer_type
ORDER BY Puntos_fidelidad DESC
LIMIT 1;

// Genero que compro mas unidades
SELECT gender, SUM(quantity) AS Cantidad
FROM Sales
GROUP BY gender
ORDER BY Cantidad DESC
LIMIT 1;

// Genero que genero mayor ingreso
SELECT gender, SUM(total_price) AS Ingreso
FROM Sales
GROUP BY gender
ORDER BY Ingreso DESC
LIMIT 1;

// Genero con mayor ingreso promedio
SELECT gender, AVG(total_price) AS Promedio_ticket
FROM Sales
GROUP BY gender;

// Suma total de impuestos generados
SELECT SUM(tax) AS Total_impuesto
FROM Sales;

// Ciudad con mayor impuestos generados
SELECT city, SUM(tax) AS Impuesto_ciudad
FROM Sales
GROUP BY city
ORDER BY Impuesto_ciudad
LIMIT 1;

// Promedio de impuestos por venta
SELECT AVG(tax) AS Impuesto_promedio_venta
FROM Sales;

// Promedio de impuestos por ciudad
SELECT city, AVG(tax) AS Impuestos
FROM Sales
GROUP BY city
ORDER BY Impuestos;

// Ingreso promedio por venta
SELECT AVG(total_price) AS Ingreso_promedio_venta
FROM Sales;

// Ingreso promedio por categoria de producto
SELECT product_category, AVG(total_price) AS Promedio_categoria
FROM Sales
GROUP BY product_category
ORDER BY Promedio_categoria DESC;

// Producto con cantidad vendida mayor al promedio general pero con total de ventas menor al promedio general
SELECT product_name, SUM(quantity) AS Cantidad, SUM(total_price) AS Total_venta
FROM Sales
GROUP BY product_name
HAVING 
SUM(quantity) > (
  SELECT AVG(quantity) FROM Sales
)
AND
SUM(total_price) < (
  SELECT AVG(total_price) FROM Sales
)
ORDER BY Cantidad DESC;

// Categoria de producto con cantidad vendida y total de ventas menor al promedio general
SELECT product_category, SUM(quantity) AS Cantidad, SUM(total_price)
FROM Sales
GROUP BY product_category
HAVING 
SUM(quantity) < (
  SELECT AVG(quantity) FROM Sales
)
AND
SUM(total_price) < (
  SELECT AVG(total_price) FROM Sales
)
ORDER BY Cantidad DESC;

// Tipo de cliente con total de ventas y promedio de venta
SELECT customer_type, SUM(total_price) AS Total_ventas, AVG(total_price) AS Promedio_venta
FROM Sales
GROUP BY customer_type 
ORDER BY Total_ventas;

// Ciudad y producto con mayor ganancia
SELECT city, product_name, SUM(total_price) AS Total_ganancia
FROM Sales
GROUP BY city, product_name
ORDER BY Total_ganancia DESC
LIMIT 1;

// Sucursal y producto con mayor ganancia
SELECT branch, product_name, SUM(total_price) AS Ganancia
FROM Sales
GROUP BY branch, product_name
ORDER BY Ganancia DESC;

// Ciudad y tipo de cliente con total de ganancia y promedio de ganancia
SELECT city, customer_type, SUM(total_price) AS Ganancia, AVG(total_price) AS Promedio_ganancia
FROM Sales
GROUP BY city, customer_type
ORDER BY city, Ganancia DESC;

// Ciudad y producto con total de ventas y promedio de venta
SELECT city, product_name, COUNT(*) AS Total, AVG(total_price) AS Promedio
FROM Sales
GROUP BY city, product_name
HAVING 
COUNT(*) > (
  SELECT AVG(quantity) FROM Sales
)
AND 
AVG(total_price) < (
  SELECT AVG(total_price) FROM Sales
)
ORDER BY Total DESC;

// Producto con numero de ventas y promedio de ingreso mayor al promedio general pero con numero de ventas menor al promedio general
SELECT product_name,
       COUNT(*) AS Numero_ventas,
       AVG(total_price) AS Ingreso_promedio
FROM Sales
GROUP BY product_name
HAVING AVG(total_price) > (
    SELECT AVG(total_price) FROM Sales
)
AND COUNT(*) < (
    SELECT AVG(quantity) FROM Sales
)
ORDER BY Ingreso_promedio DESC;

// Producto con cantidad vendida y total de ventas menor al promedio general
SELECT product_name, SUM(quantity) AS Cantidad, SUM(total_price) AS Total
FROM Sales
GROUP BY product_name
HAVING
SUM(quantity) < (
  SELECT AVG(quantity) FROM Sales
)
AND
SUM(total_price) < (
  SELECT AVG(total_price) FROM Sales
)
ORDER BY Total DESC;