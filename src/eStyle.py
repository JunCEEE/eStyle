"""eStyle: to set plot style for scientific publications

This module is to set plot style for scientific publications.

When execute ::

    from eStyle import *
    
``numpy`` and ``matplotlib.pyplot`` will be imported as
``np`` and ``plt``, respectively.

Author: Juncheng E <ejcjason@gmail.com>
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

__all__ = ['plt', 'np', 'setXminor', 'setYminor',
           'setXmajor', 'setYmajor', 'setNmajor', 'setNminor']


plt.rc('font', family="Arial")
params = {
    'axes.labelsize': 14,
    'font.size': 12,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'text.usetex': False,
    'mathtext.fontset': 'custom',
    'mathtext.rm': 'Arial',
    'mathtext.it': 'Arial:italic',
    'mathtext.bf': 'Arial:bold',
    'lines.linewidth': 1.5
}
plt.rcParams.update(params)


def func(arg1, arg2):
    """Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value

    """
    return True


def setXminor(ax, nt=5):
    """Set the number of x-axis minor ticks

    Parameters
    ----------
    ax : axes.Axes object
        The axes object to be changed
    nt : int, default: 5
        The number of minor tics on x-axis
    """

    minor_locator = AutoMinorLocator(nt)
    ax.xaxis.set_minor_locator(minor_locator)


def setYminor(ax, nt=5):
    """Set the number of y-axis minor ticks

    Parameters
    ----------
    ax : axes.Axes object
        The axes object to be changed
    nt : int, default: 5
        The number of minor tics on y-axis
    """

    minor_locator = AutoMinorLocator(nt)
    ax.yaxis.set_minor_locator(minor_locator)


def setNminor(ax, ntx=5, nty=5):
    """Set the number of minor ticks

    Parameters
    ----------
    ax : axes.Axes object
        The axes object to be changed
    ntx : int, default: 5
        The number of minor tics on x-axis
    nty : int, default: 5
        The number of minor tics on y-axis
    """

    setXminor(ax, ntx)
    setYminor(ax, nty)


def setXmajor(ax, nb=5):
    """Set the number of x-axis major ticks

    Parameters
    ----------
    ax : axes.Axes object
        The axes object to be changed
    nb : int, default: 5
        Maximum number of intervals on x-axis
    """

    ax.locator_params(axis='x', nbins=nb)


def setYmajor(ax, nb=5):
    """Set the number of y-axis major ticks

    Parameters
    ----------
    ax : axes.Axes object
        The axes object to be changed
    nb : int, default: 5
        Maximum number of intervals on y-axis
    """

    ax.locator_params(axis='y', nbins=nb)


def setNmajor(ax, nbx=5, nby=5):
    """Set the number of major ticks

    Parameters
    ----------
    ax : axes.Axes object
        The axes object to be changed
    nbx : int, default: 5
        Maximum number of intervals on x-axis
    nby : int, default: 5
        Maximum number of intervals on y-axis
    """

    setXmajor(ax, nbx)
    setYmajor(ax, nby)
