import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
elongacion = np.array([0, 0.00044, 0.00076, 0.00144, 0.00216, 0.0029, 0.0033, 0.00346, 0.0037, 0.00424, 
                       0.01, 0.016, 0.026, 0.062, 0.28, 0.484])
fuerza = np.array([0, 1000, 2000, 4000, 6000, 8000, 9000, 9400, 9800, 10100, 10600, 11000, 12000, 
                   13000, 14200, 11750])

# Datos geométricos
L0 = 2.0  # Longitud inicial (in)
A0 = np.pi * (0.5 / 2)**2  # Área inicial (in²)

# Cálculo de la deformación unitaria
deformacion_unitaria = elongacion / L0

# Cálculo del esfuerzo
esfuerzo = fuerza / A0

# Paso 1: Ampliar la zona elástica para encontrar el 0.2%
plt.figure(figsize=(10, 6))
plt.plot(deformacion_unitaria, esfuerzo, label='Esfuerzo vs Deformación Unitaria', marker='o', color='b')

# Definir el 0.2% de deformación unitaria
deformacion_02 = 0.002  # en términos de deformación unitaria (no en %)

# Trazar la línea paralela a la recta elástica inicial
pendiente_elastica = (esfuerzo[1] - esfuerzo[0]) / (deformacion_unitaria[1] - deformacion_unitaria[0])
interseccion_y = pendiente_elastica * (deformacion_unitaria - deformacion_02) + esfuerzo[1] - pendiente_elastica * deformacion_unitaria[1]

# Graficar la línea paralela
plt.plot(deformacion_unitaria, interseccion_y, label='Línea Paralela al 0.2%', linestyle='--', color='r')

# Calcular la intersección de la línea paralela con la curva
interseccion_x = None
interseccion_y_real = None

for i in range(len(deformacion_unitaria) - 1):
    if (interseccion_y[i] <= esfuerzo[i] and interseccion_y[i + 1] >= esfuerzo[i + 1]) or \
       (interseccion_y[i] >= esfuerzo[i] and interseccion_y[i + 1] <= esfuerzo[i + 1]):
        # Interpolación lineal para encontrar el punto de intersección
        m1 = (interseccion_y[i + 1] - interseccion_y[i]) / (deformacion_unitaria[i + 1] - deformacion_unitaria[i])
        m2 = (esfuerzo[i + 1] - esfuerzo[i]) / (deformacion_unitaria[i + 1] - deformacion_unitaria[i])
        
        # Ecuación de la línea: y = mx + b
        interseccion_x = (esfuerzo[i] - interseccion_y[i] + m1 * deformacion_unitaria[i] - m2 * deformacion_unitaria[i]) / (m1 - m2)
        interseccion_y_real = m1 * interseccion_x + interseccion_y[i] - m1 * deformacion_unitaria[i]
        break

# Mostrar la intersección en la gráfica
if interseccion_x is not None and interseccion_y_real is not None:
    plt.scatter(interseccion_x, interseccion_y_real, color='green', zorder=5, label='Esfuerzo de Cedencia')
    plt.axhline(y=interseccion_y_real, color='green', linestyle='--', label='Esfuerzo de Cedencia')
    
    # Anotar el valor del esfuerzo de cedencia en la gráfica
    plt.annotate(f'Esfuerzo de Cedencia: {interseccion_y_real:.2f} psi', 
                 xy=(interseccion_x, interseccion_y_real), 
                 xytext=(interseccion_x + 0.001, interseccion_y_real + 2000),
                 arrowprops=dict(arrowstyle='->', color='green'),
                 fontsize=10, color='green')

# Ajustar límites para ver toda la gráfica claramente
plt.xlim(0, 0.01)  # Limite del eje X ajustado para ver toda la gráfica
plt.ylim(0, 20000)  # Limite del eje Y ajustado para ver toda la gráfica
plt.title('Esfuerzo y deformación unitaria ampliada')
plt.xlabel('Deformación Unitaria')
plt.ylabel('Esfuerzo (psi)')
plt.grid(True)
plt.legend()
plt.show()

# Imprimir el esfuerzo de cedencia
if interseccion_y_real is not None:
    print(f'Esfuerzo de cedencia: {interseccion_y_real:.2f} psi')
