

root = 'C:/Users/user/Documents/NetBeansProjects/JMetal4.5/Experiment/'
writePath = 'E:/Msc@BUET/Thesis/multiobjective transit network/Simulation/Front/'
Algo = ['NSGAIII', 'ThetaDEA', 'MOEAD', 'SPEA2']
Data = ['Mandl-4']

for data in Data:
    pathToRF = root + 'RF_20-6-16/' + data +'.pf'
    writeFile = open(writePath+ data + '/RF/'+ data + '.pf', 'w')
    writeFile.write('IVTT WT TP UP FS RL DO' )
    with open(pathToRF) as f:
        for line in f:
            line = line.rstrip()
            writeFile.write('\n'+line)   
    writeFile.close() 
    for algo in Algo:
        pathToAF = root + algo + '_20-6-16/' +'referenceFronts/' + data +'.rf'
        writeFile = open(writePath + data + '/'+algo + '/' + data + '.rf', 'w')
        writeFile.write('IVTT WT TP UP FS RL DO' )
        with open(pathToAF) as f:
            for line in f:
                line = line.rstrip()
                writeFile.write('\n'+line)   
        writeFile.close()

#path = 'C:/Users/user/Documents/NetBeansProjects/JMetal4.5/Experiment/SPEA2_20-6-16/referenceFronts/'
#writePath = 'E:/Msc@BUET/Thesis/multiobjective transit network/Simulation/'
#frontlist = ['Mandl-4.rf']
##columns = ['IVTT', 'WT', 'TP', 'UP', 'FS', 'RL', 'DO']
#
#for front in frontlist:
#    #df = pd.read_csv(path+frontlist[0], delimiter=' ', header=None, names=columns, index_col=False)
#    #df = df.drop_duplicates()
#    #df.to_csv(writePath+'processed1_'+front, sep=' ', header=True, index = False)
#    writeFile = open(writePath+'processed_'+front, 'w')
#    writeFile.write('IVTT WT TP UP FS RL DO' )
#    with open(path+front) as f:
#        for line in f:
#            line = line.rstrip()
#            writeFile.write('\n'+line)   
#    writeFile.close()    