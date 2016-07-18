import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

root = 'C:/Users/user/Documents/NetBeansProjects/JMetal4.5/Experiment/'
writePath = 'E:/Msc@BUET/Thesis/multiobjective transit network/Simulation/Fig/'
Algo = ['NSGAIII', 'ThetaDEA', 'MOEAD', 'SPEA2']
Selection = {'NSGAIII': 'RandomSelection', 'ThetaDEA': 'RandomSelection', 'SPEA2': 'BinaryTournament', 'MOEAD': 'RandomSelection'}
Mut = ['RouteSetAddDelRand','RouteSetAddDelTELRand','RouteSetAddDelTEORand', 'RouteSetCombinedRandomMutation', 'RouteSetCombinedGuidedMutation']
Xrate = ['0.0', '0.2', '0.4', '0.6', '0.8', '1.0']
Data = ['Mandl-4']

for data in Data:
    for algo in Algo:
        for mut in Mut:
            x = []
            df = pd.DataFrame(columns=Xrate)
            for xrate in Xrate:
                pathToHV = root + algo + '_20-6-16/' +'data/' + mut + '-' + Selection[algo] + '-' + xrate + '/' + data + '/HV'
                x = np.genfromtxt(pathToHV)
                df[xrate] = x
            df.boxplot() 
            plt.suptitle(data+' : '+algo+' : '+ mut )
            plt.ylabel('HV')
            plt.xlabel('Crossover rate')
            plt.savefig(writePath+data+'/'+algo + '/' + mut+'.png', format='png')
            plt.clf()
           