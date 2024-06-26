# Introducción a los Métodos Numéricos para ODEs

Este documento proporciona una visión general y guías de uso para los métodos numéricos implementados para resolver ecuaciones diferenciales ordinarias (ODEs). Los métodos cubiertos incluyen el Método de Euler, Runge-Kutta de segundo orden (rk2) y Runge-Kutta de cuarto orden (rk4).

## Métodos Numéricos Implementados

### Método de Euler

El Método de Euler es uno de los algoritmos más simples para la integración numérica de ecuaciones diferenciales ordinarias. La ecuación básica del Método de Euler es:

$$
y_{n+1} = y_n + h \cdot f(t_n, y_n)
$$

donde \( y_{n+1} \) es la aproximación de la solución en el tiempo \( t_{n+1} \), \( y_n \) es la solución aproximada en el tiempo \( t_n \), \( h \) es el tamaño del paso, y \( f(t, y) \) es la función derivada de la ODE.

### Método Runge-Kutta de Segundo Orden (RK2)

El método RK2, también conocido como método del punto medio, mejora la precisión del método de Euler tomando en cuenta la pendiente en el punto medio del intervalo. La fórmula para RK2 es:

$$
y_{n+1} = y_n + h \cdot f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} \cdot f(t_n, y_n)\right)
$$

### Método Runge-Kutta de Cuarto Orden (RK4)

El método RK4 es uno de los métodos más utilizados debido a su gran precisión y estabilidad. La ecuación para RK4 se expresa como:

$$
\begin{aligned}
y_{n+1} &= y_n + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4), \\
k_1 &= f(t_n, y_n), \\
k_2 &= f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} \cdot k_1\right), \\
k_3 &= f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} \cdot k_2\right), \\
k_4 &= f(t_n + h, y_n + h \cdot k_3)
\end{aligned}
$$
