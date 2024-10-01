import matplotlib.pyplot as plt
import numpy as np

# Datos
# Deformación unitaria (epsilon)
epsilon = np.array([0, 0.00022, 0.00038, 0.00072, 0.00108, 0.00145, 
                    0.00165, 0.00173, 0.00185, 0.00212, 0.005, 0.008, 
                    0.013, 0.031, 0.14, 0.242])

# Esfuerzo (sigma) en psi
sigma = np.array([0, 5094.24, 10188.48, 20376.98, 30565.46, 40753.95, 
                  45848.19, 47885.89, 49923.58, 51451.86, 53998.98, 
                  56036.68, 61130.92, 66225.16, 72338.25, 59857.36])

# Cálculos
# Limite Proporcional
limite_proporcional = sigma[3]  # Primer punto no lineal
deformacion_limi_proporcional = epsilon[3]

# Gráfica de esfuerzo vs. deformación
plt.figure(figsize=(10, 6))
plt.plot(epsilon, sigma, marker='o', color='b', linestyle='-', linewidth=2)

# Marcar el límite proporcional
plt.scatter(deformacion_limi_proporcional, limite_proporcional, color='red', zorder=5)
plt.annotate(f'Límite Proporcional: {limite_proporcional:.2f} psi', 
             xy=(deformacion_limi_proporcional, limite_proporcional), 
             xytext=(deformacion_limi_proporcional + 0.005, limite_proporcional + 5000),
             arrowprops=dict(arrowstyle='->', color='red'),
             fontsize=10, color='red')

# Etiquetas y título
plt.title('Esfuerzo vs. Deformación Unitaria - Límite Proporcional', fontsize=16)
plt.xlabel('Deformación Unitaria', fontsize=14)
plt.ylabel('Esfuerzo (psi)', fontsize=14)
plt.grid()
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')

# Mostrar la gráfica
plt.show()
