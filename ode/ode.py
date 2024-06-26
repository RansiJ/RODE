
def euler(func, y0, t0, tf, h):
    """
    Resuelve una ecuación diferencial usando el método de Euler.
   
    Esta función numérica aproxima la solución de una ecuación diferencial ordinaria
    dada una condición inicial y un intervalo de tiempo. Utiliza el método de Euler,
    un método de paso simple para integrar ecuaciones diferenciales ordinarias.
    
    Examples:
        >>> t, y = euler(-2*y + t, y0=1.0, t0=0, tf=5, h=0.1)
        [0. , 0.1, 0.2, 0.3, 0.4] , ([1, 0.9, 0.82, 0.758, 0.7112]

    Args:
        func (callable): La función que representa la derivada de y respecto a t.
                         Debe aceptar dos argumentos flotantes, t y y, y devolver un flotante.
        y0 (float): El valor inicial de y en t = t0.
        t0 (float): El tiempo inicial.
        tf (float): El tiempo final.
        h (float): El tamaño del paso de la integración.

    Returns:
        ty (tuple): Dos arreglos de numpy. El primer arreglo contiene los valores del tiempo t
               desde t0 hasta tf con pasos de tamaño h. El segundo arreglo contiene los
               valores aproximados de y en esos tiempos.
    """
    n_steps = int((tf - t0) / h)  # Número de pasos
    t = np.linspace(t0, tf, n_steps + 1)
    y = np.zeros(n_steps + 1)
    y[0] = y0

    for i in range(1, n_steps + 1):
        y[i] = y[i - 1] + h * func(t[i - 1], y[i - 1])

    return t, y

def rk2(f, y0, t0, tf, h):
    """
    Resuelve una ecuación diferencial usando el método Runge-Kutta de segundo orden.

    Args:
        f (callable): Función que representa la derivada dy/dt.
        y0 (float): Valor inicial de y en t = t0.
        t0 (float): Tiempo inicial.
        tf (float): Tiempo final.
        h (float): Tamaño del paso.

    Returns:
      ty (tuple): Tupla que contiene dos arrays, uno para los tiempos y otro para los valores de y.

    Examples:
        >>> t, y = rk2(-2*y + t, y0=1.0, t0=0, tf=5, h=0.1)
        [0, 0.1, 0.2, 0.3, 0.4] , [1, 0.896, 0.80192, 0.71692672, 0.64068659]
    """
    n_steps = int((tf - t0) / h)
    t = np.linspace(t0, tf, n_steps + 1)
    y = np.zeros(n_steps + 1)
    y[0] = y0

    for i in range(1, n_steps + 1):
        k1 = f(t[i-1], y[i-1])
        k2 = f(t[i-1] + h, y[i-1] + h * k1)
        y[i] = y[i - 1] + (h / 2) * (k1 + k2)

    return t, y
def rk4(f, y0, t0, tf, h):
    """
    Resuelve una ecuación diferencial usando el método Runge-Kutta de cuarto orden.

    Args:
        f (callable): Función que representa la derivada dy/dt.
        y0 (float): Valor inicial de y en t = t0.
        t0 (float): Tiempo inicial.
        tf (float): Tiempo final.
        h (float): Tamaño del paso.

    Returns:
        ty (tuple): Tupla que contiene dos arrays, uno para los tiempos y otro para los valores de y.

    Examples:
        >>> t, y = rk4( -2 * y + t  , y0=1.0, t0=0, tf=5, h=0.1)
        [0. , 0.1, 0.2, 0.3, 0.4] , [1, 0.89504483, 0.79928296, 0.71315142, 0.63587735]
    """
    n_steps = int((tf - t0) / h)
    t = np.linspace(t0, tf, n_steps + 1)
    y = np.zeros(n_steps + 1)
    y[0] = y0

    for i in range(1, n_steps + 1):
        k1 = f(t[i-1], y[i-1])
        k2 = f(t[i-1] + h/2, y[i-1] + h/2 * k1)
        k3 = f(t[i-1] + h/2, y[i-1] + h/2 * k2)
        k4 = f(t[i-1] + h, y[i-1] + h * k3)
        y[i] = y[i - 1] + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)

    return t, y


