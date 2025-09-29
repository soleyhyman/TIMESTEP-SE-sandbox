"""
Core quadratic class for sandbox code
"""

import numpy as np
import matplotlib.pyplot as plt

class quadratic:
    """
    Add description of class here and format the quadratic equation (i.e., y = ax^2 + bx + c) in rst/LaTeX. 

    Attributes
    ----------
    Add the attributes, which IN THIS CASE are the same as the __init__ parameters
    (if other functions set attributes, you'll need to add them here too)

    Examples
    --------
    Add an example of how to use the class with a >>> code marker and the printout result below it.
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
        _summary_

        Parameters
        ----------
        x : _type_
            _description_

        Returns
        -------
        _type_
            _description_
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
        _summary_

        Returns
        -------
        _type_
            _description_
        """
        foura = 4.*self.a
        D = self.b*self.b - foura*self.c
        return np.array([-self.b/(2.*self.a),-D/(foura)])
    
    def plot(self, x, roots=True, originAxes=True, showPlot=True, styleKwargs={"color":"k", "lw":1}):
        """
        _summary_

        Parameters
        ----------
        x : _type_
            _description_
        roots : bool, optional
            _description_, by default True
        originAxes : bool, optional
            _description_, by default True
        showPlot : bool, optional
            _description_, by default True
        styleKwargs : dict, optional
            _description_, by default {"color":"k", "lw":1}

        Returns
        -------
        _type_
            _description_

        Raises
        ------
        TypeError
            _description_
        """
        x = np.array([x])
        if np.issubdtype(x.dtype,np.number) and x.ndim==1 and x.size>=3:
            pass
        else:
            raise TypeError("x must be a 1d list or ndarray with at least 3 elements.")

        fig,ax = plt.subplots()

        if originAxes==True:
            ax.axhline(0, **styleKwargs)
            ax.axvline(0, **styleKwargs)

        ax.plot(x, self.__call__(x))
        ax.set(xlabel="x", ylabel="y")

        if roots==True:
            allRoots = self.roots()
            realRoots = allRoots[np.isreal(allRoots)]
            ax.plot(realRoots, np.zeros_like(realRoots), marker="o", ls="None")
        
        if showPlot==True:
            plt.show()
        else:
            return fig, ax