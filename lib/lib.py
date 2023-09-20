'''
This is the library file that includes the shared code of 
Jupyter Notebook file and Python script
'''
import pandas as pd # noqa: F401
import matplotlib.pyplot as plt # noqa: F401
# import seaborn as sns 
# sns.set(style="darkgrid")

def plot(x, y, ax, title, y_label, debug=False):
    if debug is False:
        ax.set_title(title)
        ax.set_ylabel(y_label)
        ax.plot(x, y)
        ax.margins(x=0, y=0)
    
    return 'plot completed!'
    
def plot_with_std(x, y, stds, ax, title, y_label, debug=False):
    if debug is False:
        ax.fill_between(x, y - stds, y + stds, alpha=0.2)
        plot(x, y, ax, title, y_label)
    
    return 'plot_with_std completed!'