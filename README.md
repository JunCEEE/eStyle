# eStyle
This module is to create a default plot style environment for scientific publications.

VERSION: 0.0.1

## Installation
```
git clone https://github.com/ejcjason/eStyle.git
cd eStyle
python ./install.sh install
```

## Usage
```
from eStyle import *
```
When it is imported, it imports `numpy` as `np`, `matplotlib.pyplot` as `plt` automatically and changes the plot style immediately.

The setting is :
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
and you can modify it as you like.

### Legend size and label size
To set default size of legends and labels, add these lines to `params` in `eStyle.py` before installing this module.
```
'legend.fontsize': 12,
'xtick.labelsize': 12,
'ytick.labelsize': 12,
```
### Number of minor ticks
`setXminor(ax,nt)`

`setYminor(ax,nt)`

`setNminor(ax,nbx=5,nby=5)`

nt: number of ticks, default = 5

### Number of major ticks
`setXmajor(ax,nb)`

`setYmajor(ax,nb)`

`setNmajor(ax,nbx=5,nby=5)`

nb: number of tick bins, default = 5
