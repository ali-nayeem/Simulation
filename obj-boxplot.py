import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
obj = [ 'IVTT' , 'WT' , 'TP' , 'UP' , 'FS' , 'RL', 'DO']
pp = PdfPages('Mandl.pdf')

for i in range(0,7):
    x = np.genfromtxt("TNDP-FUN",delimiter=' ',usecols=i)
    plt.boxplot(x)
    plt.suptitle(obj[i])
    plt.savefig(pp, format='pdf')
    plt.clf()
pp.close()