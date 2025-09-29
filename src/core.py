"""
Core quadratic class for sandbox code
"""

import numpy as np
import matplotlib.pyplot as plt

class quadratic:
    """
    This class stores parameters for the quadratic equation
     
    .. math::
        y = ax^2 + bx + c
    
    and performs related operations, such as vertex and root finding.

    Attributes
    ----------
    a : float
            a parameter in quadratic equation
    b : float
        b parameter in quadratic equation
    c : float
        c parameter in quadratic equation

    Examples
    --------
    After importing the class, you can define a quadratic object as:
    
    >>> from core import quadratic
    >>> quad = quadratic(1.,2.,3.)    

    To calculate the slope, run:

    >>> quad(1.)
    6.0

    To calculate the roots (or x-intercepts), run:

    >>> quad.roots()
    ((-1+1.4142135623730951j), (-1-1.4142135623730951j))

    Notice that both roots are imaginary. 

    To calculate the y-intercept, run:

    >>> quad.yIntercept()
    3.0

    To plot the quadratic equation, we need to supply an array of x-value and then can use ``quadratic.plot``:

    >>> import numpy as np
    >>> x = np.array(-10.,10.)
    >>> quad.plot(x)

    In this case, the roots are imaginary, so they're not plotted here, but if we specify an equation with negative roots, we'll see them plotted on the graph:

    >>> import numpy as np
    >>> from core import quadratic
    >>> x = np.linspace(-10.,10.)
    >>> quad = quadratic(1.,2.,-3.)
    >>> quad.plot(x)
    """
    def __init__(self, a, b, c):
        """
        Parameters
        ----------
        a : float
            a parameter in quadratic equation
        b : float
            b parameter in quadratic equation
        c : float
            c parameter in quadratic equation
        """
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        """
        Get the value of the quadratic for x

        Parameters
        ----------
        x : float or ndarray
            Value(s) of x at which to evaluate the quadratic

        Returns
        -------
        float or ndarray
            Value(s) of the quadratic at x
        """
        return self.a*x**2 + self.b*x + self.c
    
    def roots(self):
        """
        Finds roots (real and imaginary) of quadratic equation.

        Returns
        -------
        ndarray
            Complex data-type array of quadratic roots
        """
        twoa = 2.*self.a
        radical = np.sqrt(self.b**2 - 4.*self.a*self.c + 0.j)/twoa
        b2a = -self.b/twoa
        return np.array([b2a + radical, b2a - radical])
        
    def yIntercept(self):
        """
        Calculate y-intercept of quadratic equation.

        Returns
        -------
        float
            Quadratic equation y-intercept
        """
        return self.c
    
    def vertex(self):
        """
        Calculate the vertex of the quadratic

        Returns
        -------
        2x1 array
            (x,y) coordinate of the vertex
        """
        foura = 4.*self.a
        D = self.b*self.b - foura*self.c
        return np.array([-self.b/(2.*self.a),-D/(foura)])
    
    def plot(self, x, roots=True, originAxes=True, showPlot=True, styleKwargs={"color":"k", "lw":1}):
        """
        Plot the quadratic with the roots shown and the origin axes plotted, if desired.

        Parameters
        ----------
        x : array_like
            1-d array of x values to plot the quadratic at, must have at least 3 elements
        roots : bool, optional
            Roots (x-intercepts) of the quadratic, by default True
        originAxes : bool, optional
            Plot origin axes (x=0,y=0) if True, by default True
        showPlot : bool, optional
            Show plot if True, return fig,ax objects if False, by default True
        styleKwargs : dict, optional
            kwargs for origin axes, by default {"color":"k", "lw":1}

        Returns
        -------
        None or fig, ax
            Matplotlib figure and axes if showPlot is False, otherwise returns None

        Raises
        ------
        TypeError
            Raises error if supplied x is not 1d array_like object with at least 3 elements
        """
        if not isinstance(x,np.ndarray):
            x = np.array([x])
        if np.issubdtype(x.dtype,np.number) and x.ndim==1 and x.size>=3:
            pass
        else:
            raise TypeError("x must be a 1d list or ndarray with at least 3 elements.")

        fig,ax = plt.subplots()
        ax.set_title(r'$y = {}x^2 {:+}x {:+}$'.format(self.a,self.b,self.c))

        if originAxes==True:
            ax.axhline(0, **styleKwargs)
            ax.axvline(0, **styleKwargs)

        ax.plot(x, self.__call__(x))
        ax.set(xlabel="x", ylabel="y")

        if roots==True:
            allRoots = self.roots()
            realRoots = np.real(allRoots[np.isreal(allRoots)])
            ax.plot(realRoots, np.zeros_like(realRoots), marker="o", ls="None")
        
        if showPlot==True:
            plt.show()
        else:
            return fig, ax