#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 13:51:59 2023

@author: cpe28
"""
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as NC
import glob
from matplotlib.pyplot import cm

locs = ["PAED","PAEI","CYEV","CYZF","CYFB","CYRB","CYAB","BGTL","BIKF"]

models = ["ACCESS-CM2","ACCESS-ESM1-5","BCC-CSM2-MR","CanESM5","CMCC-CM2-SR5","CMCC-ESM2","CNRM-CM6-1","CNRM-ESM2-1","EC-Earth3","FGOALS-g3","GFDL-CM4","GFDL-ESM4","INM-CM4-8","INM-CM5-0","IPSL-CM6A-LR","KIOST-ESM","MIROC-ES2L","MIROC6","MPI-ESM1-2-HR","MPI-ESM1-2-LR","MRI-ESM2-0","NESM3","NorESM2-LM","NorESM2-MM","TaiESM1"]

file = "/Volumes/Elements/arctic/tas_ssp245/"

files = glob.glob("/Volumes/Elements/arctic/tas_ssp245/PAED/*.nc")
data = NC.Dataset(files[0])
lat = np.array(data.variables['lat'])
lon = np.array(data.variables['lon'])
tasmin = np.array(data.variables['tasmin'][:,0,0])

mins = np.empty([4])
counter = 0
for i in range(0,1460,365):
    mins[counter] = np.amin(tasmin[i:(i+365)])
    counter = counter + 1



#Count of days per year with daily minimum temperature above -65F/ -53.9

counts = np.empty([9,25,4])
counter = 0
for i in locs:
    path = file+str(i)
    files = glob.glob(str(path)+str("/*.nc"))
    for j in range(25):
        data = NC.Dataset(files[j])
        tasmin = np.array(data.variables['tasmin'][:,0,0])
        tasmin = tasmin - 273.15
        counter1 = 0
        for k in range(0,1460,365):
            
            counts[counter,j,counter1] = np.count_nonzero(tasmin[k:(k+365)] > -53.9)
            counter1 = counter1 + 1
    counter = counter + 1
            
        
mean = np.mean(counts,axis=1)   
    
# =============================================================================
# new approach - plot yearly minimum temperature for each model
# =============================================================================
mins = np.empty([9,24,4])
for i in range(9):
    files = glob.glob("/Volumes/Elements/arctic/tas_ssp245/"+str(locs[i])+"/*.nc")
    for j in range(24):
        data = NC.Dataset(files[j])
        tasmin = np.array(data.variables['tasmin'][:,0,0])
        tasmin = (tasmin - 273.15) * (9./5.) + 32.
        counter = 0
        for k in range(0,1460,365):
            mins[i,j,counter] = np.amin(tasmin[k:(k+365)])
            counter = counter + 1
            

for i in range(9):
    fig = plt.figure(figsize=(10,8))
    color = iter(cm.tab20(np.linspace(0, 1, 25)))
    for j in range(24):
        plt.plot(mins[i,j,:],color=next(color),label=str(models[j]),ls='--',lw=2)
    plt.plot(np.mean(mins[i,:,:],axis=0),color='k',lw=4,label="Ens. Mean")
    plt.scatter(np.arange(4),np.mean(mins[i,:,:],axis=0),color='k',marker='d',s=200)
    plt.xticks([0,1,2,3],["2045","2055","2065","2075"],fontsize=12)
    plt.ylabel("Minimum Temperature (°F)",fontsize=12)
    plt.title("Yearly Minimum Temperature: " + str(locs[i])+"\nSSP245",fontsize=20)
    plt.legend(bbox_to_anchor=(1.05, 1),fontsize=10)
    plt.savefig(str(locs[i])+"_ssp245_min_temps.jpeg",dpi=500,bbox_inches='tight')
    plt.show()
    plt.close()




mins_585 = np.empty([9,24,4])
for i in range(9):
    files = glob.glob("/Volumes/Elements/arctic/tas_ssp585/"+str(locs[i])+"/*.nc")
    for j in range(24):
        data = NC.Dataset(files[j])
        tasmin = np.array(data.variables['tasmin'][:,0,0])
        tasmin = (tasmin - 273.15) * (9./5.) + 32.
        counter = 0
        for k in range(0,1460,365):
            mins_585[i,j,counter] = np.amin(tasmin[k:(k+365)])
            counter = counter + 1
            

for i in range(9):
    fig = plt.figure(figsize=(10,8))
    color = iter(cm.tab20(np.linspace(0, 1, 25)))
    for j in range(24):
        plt.plot(mins_585[i,j,:],color=next(color),label=str(models[j]),ls='--',lw=2)
    plt.plot(np.mean(mins_585[i,:,:],axis=0),color='k',lw=4,label="Ens. Mean")
    plt.scatter(np.arange(4),np.mean(mins_585[i,:,:],axis=0),color='k',marker='d',s=200)
    plt.xticks([0,1,2,3],["2045","2055","2065","2075"],fontsize=12)
    plt.ylabel("Minimum Temperature (°F)",fontsize=12)
    plt.title("Yearly Minimum Temperature: " + str(locs[i])+"\nSSP585",fontsize=20)
    plt.legend(bbox_to_anchor=(1.05, 1),fontsize=10)
    plt.savefig(str(locs[i])+"_ssp585_min_temps.jpeg",dpi=500,bbox_inches='tight')
    plt.show()
    plt.close()
