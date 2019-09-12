# This module is to set plot style for scientific publications
# Juncheng E <ejcjason@gmail.com>

__all__ = ['plt','np','setXminor','setYminor','setXmajor','setYmajor']

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

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

def setXminor(ax,nt=5):
    minor_locator = AutoMinorLocator(nt)
    ax.xaxis.set_minor_locator(minor_locator)

def setYminor(ax,nt=5):
    minor_locator = AutoMinorLocator(nt)
    ax.yaxis.set_minor_locator(minor_locator)

def setXmajor(ax, nb=5):
    plt.locator_params(axis='x',nbins=nb)

def setYmajor(ax, nb=5):
    plt.locator_params(axis='y',nbins=nb)
