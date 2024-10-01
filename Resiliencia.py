import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
epsilon = np.array([0, 0.00044, 0.00076, 0.00144, 0.00216, 0.0029, 0.0033, 0.00346, 0.0037, 0.00424, 
                    0.01, 0.016, 0.026, 0.062, 0.28, 0.484])
sigma = np.array([0, 5094.24, 10188.48, 20376.98, 30565.46, 40753.95, 
         45848.19, 47885.89, 49923.58, 51451.86, 53998.98, 
         56036.68, 61130.92, 66225.16, 72338.25, 59857.36])

# Limite proporcional (índice del último punto en la región elástica)
indice_limite_proporcional = 3  # Asumimos que el tercer índice corresponde al final de la zona elástica

# Cálculo de la resiliencia (área bajo la curva en la región elástica)
resiliencia = np.trapz(sigma[:indice_limite_proporcional + 1], epsilon[:indice_limite_proporcional + 1])

# Gráfica de esfuerzo vs. deformación para resiliencia
plt.figure(figsize=(10, 6))
plt.plot(epsilon, sigma, marker='o', color='b', label='Esfuerzo vs Deformación Unitaria')

# Colorear la zona de resiliencia (área bajo la curva en la región elástica)
plt.fill_between(epsilon[:indice_limite_proporcional + 1], 0, sigma[:indice_limite_proporcional + 1], 
                 color='yellow', alpha=0.5, label='Resiliencia')

# Etiquetas y título
plt.title('Esfuerzo vs. Deformación Unitaria - Resiliencia', fontsize=16)
plt.xlabel('Deformación Unitaria', fontsize=14)
plt.ylabel('Esfuerzo (psi)', fontsize=14)
plt.legend()
plt.grid(True)

# Mostrar valor de la resiliencia en la gráfica
plt.annotate(f'Resiliencia: {resiliencia:.2f} psi', 
             xy=(epsilon[indice_limite_proporcional], sigma[indice_limite_proporcional]), 
             xytext=(epsilon[indice_limite_proporcional] + 0.01, sigma[indice_limite_proporcional] + 10000),
             arrowprops=dict(arrowstyle='->', color='black'),
             fontsize=12, color='black')

plt.show()

# Imprimir valor calculado
print(f"Resiliencia: {resiliencia:.2f} psi*ε")
