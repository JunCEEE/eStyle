# eStyle
This module is to set plot style for scientific publications

## Installation
```
git clone https://github.com/ejcjason/eStyle.git
cd eStyle
bash ./install.sh
```

## Usage
```
from eStyle import *
```
When it is imported, it imports `numpy` as `np`, `matplotlib.pyplot` as `plt` automatically and changed the plot style immediately.

The setting is:
```
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
```
### Legend size and label size
Add these lines to `params` in `~/.ipython/eStyle.py`
```
'legend.fontsize': 12,
'xtick.labelsize': 12,
'ytick.labelsize': 12,
```
### Number of minor ticks
`setXminor(ax,nt)`

`setYminor(ax,nt)`

nt: number of ticks, default=5
