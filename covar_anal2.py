import numpy as np
import mdtraj as md
import os
import shutil
import subprocess

List=['X','Y']

#1->4 1000 ns
#5: 750 ns
#6-> 500 ns


for i in range(0,10):
    pathor=os.getcwd()
    newpath=pathor+'/'+List[i]+'/RNA/md/'
    
    #shutil.copy2('md-2.mdp', newpath)
    #if(i<4):
    shutil.copy2('script_pca_cg.sh', newpath)
        
    #elif(i==4):
    #    shutil.copy2('script_pca1.sh', newpath)
    #else:
    #    shutil.copy2('script_pca2.sh', newpath)
    os.chdir(newpath)
    
    #if(i<4):
    subprocess.call('sh script_pca_cg.sh',shell=True)
    #elif(i==4):
    #    subprocess.call('sh script_pca1.sh',shell=True)
    #else:
    #    subprocess.call('sh script_pca2.sh',shell=True)
        
    os.chdir(pathor)
  
