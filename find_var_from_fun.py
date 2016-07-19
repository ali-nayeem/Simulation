import numpy as np
import pandas as pd

Q = [130775.0, 5947.0324, 0.203, 0.0083, 144.0, 81.0, 1.0435]
columns = ['IVTT', 'WT', 'TP', 'UP', 'FS', 'RL', 'DO']
Run = 20
Decimal = 4
Data = 'Mandl-4'
root = 'C:/Users/user/Documents/NetBeansProjects/JMetal4.5/Experiment/'
writePath = 'E:/Msc@BUET/Thesis/multiobjective transit network/Simulation/Fig/'
Algo = ['NSGAIII', 'ThetaDEA', 'MOEAD', 'SPEA2']
Selection = {'NSGAIII': 'RandomSelection', 'ThetaDEA': 'RandomSelection', 'SPEA2': 'BinaryTournament', 'MOEAD': 'RandomSelection'}
Mut = ['RouteSetAddDelRand','RouteSetAddDelTELRand','RouteSetAddDelTEORand', 'RouteSetCombinedRandomMutation', 'RouteSetCombinedGuidedMutation']
Xrate = ['0.0', '0.2', '0.4', '0.6', '0.8', '1.0']
Query=''
TotalFound = 0
writeFile = open('find_var_from_fun.out', 'w')

Q = np.genfromtxt('find_var_from_fun.in')

for i in range(len(Q)):
    Q[i] = round(Q[i],Decimal)
    Query = Query + columns[i] + '==' + str( Q[i])
    if i < len(Q)-1:
        Query = Query + ' and '
writeFile.write('**************'+Query+'**************\n')    
for algo in Algo:
    pathToAF = root + algo + '_20-6-16/' +'referenceFronts/' + Data +'.rf'
    df_af = pd.read_csv(pathToAF, delimiter=' ', header=None, names=columns, index_col=False)
    df_af = df_af.round(Decimal)
    if len(df_af.query(Query)) == 0:
        continue

    for mut in Mut:
        for xrate in Xrate:
          for i in range(Run):
              pathToFUN =  root + algo + '_20-6-16/' +'data/' + mut + '-' + Selection[algo] + '-' + xrate + '/' + Data + '/FUN.'+ str(i) 
              df_fun = pd.read_csv(pathToFUN, delimiter=' ', header=None, names=columns, index_col=False)
              df_fun = df_fun.round(Decimal)
              query_result = df_fun.query(Query)
              if len(query_result) == 0 :
                  continue
              writeFile.write( algo+' : '+ mut +' : '+ xrate +' : '+ Data+' : Run ' + str(i) + '\n')
              print algo+' : '+ mut +' : '+ xrate +' : '+ Data+' : Run ' + str(i)
              mi = query_result.index.tolist()
              TotalFound = TotalFound + len(mi)
              pathToVAR = root + algo + '_20-6-16/' +'data/' + mut + '-' + Selection[algo] + '-' + xrate + '/' + Data + '/VAR.'+ str(i) 
              df_var = np.genfromtxt(pathToVAR, dtype=str, delimiter='#')
              for j in mi:
                  writeFile.write( df_var[j] + ' @line ' +str(j) + '\n')
                  print df_var[j] + ' @line ' +str(j)
              writeFile.write( '\n') 
              print '\n' 
              
writeFile.write('Total found: ' + str(TotalFound))
print 'Total found: ' + str(TotalFound)
writeFile.close()
                  
              
