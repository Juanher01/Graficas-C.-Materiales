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

# Resistencia a la Tensión (máximo esfuerzo)
resistencia_tension = np.max(sigma)

# Gráfica de esfuerzo vs. deformación
plt.figure(figsize=(10, 6))
plt.plot(epsilon, sigma, marker='o', color='b', linestyle='-', linewidth=2)

# Marcar la resistencia a la tensión
plt.scatter(epsilon[np.argmax(sigma)], resistencia_tension, color='purple', zorder=5)
plt.annotate(f'Resistencia a la Tensión: {resistencia_tension:.2f} psi', 
             xy=(epsilon[np.argmax(sigma)], resistencia_tension), 
             xytext=(epsilon[np.argmax(sigma)] + 0.005, resistencia_tension + 5000),
             arrowprops=dict(arrowstyle='->', color='purple'),
             fontsize=10, color='purple')

# Etiquetas y título
plt.title('Esfuerzo vs. Deformación Unitaria - Resistencia a la Tensión', fontsize=16)
plt.xlabel('Deformación Unitaria', fontsize=14)
plt.ylabel('Esfuerzo (psi)', fontsize=14)
plt.grid()
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')

# Mostrar la gráfica
plt.show()
