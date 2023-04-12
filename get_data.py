#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:43:27 2023

@author: cpe28
"""
import numpy as np
import wget
import os

def get_data(var,experiment,model,run,yr1,yr2,lat1,lat2,lon1,lon2,grid):
    for i in range(int(yr1),int(yr2)+1):
        file = 'https://ds.nccs.nasa.gov/thredds2/ncss/AMES/NEX/GDDP-CMIP6/'+str(model)+'/'+str(experiment)+'/'+str(run)+'/'+str(var)+'/'+str(var)+'_day_'+str(model)+'_'+str(experiment)+'_'+str(run)+'_'+str(grid)+'_'+str(i)+'.nc?var='+str(var)+'&north='+str(lat2)+'&west='+str(lon1)+'&east='+str(lon2)+'&south='+str(lat1)+'&horizStride=1&time_start='+str(i)+'-01-01T12%3A00%3A00Z&time_end='+str(i)+'-12-31T12%3A00%3A00Z&timeStride=1'
        wget.download(file)
###
#PAED - Anchorage, Alaska
#PAEI - Fairbanks, Alaska
#CYEV - Inuvik, Canada
#CYZF - Yellowknife, Canada
#CYFB - Iqaluit, Canada
#CYRB - Resolute Bay, Canada
#CYAB - Arctic Bay, Canada
#BGTL - Thule Air Base, Thule, Greenland
#BIKF - Reykjavik, Iceland
locs = ["PAED","PAEI","CYEV","CYZF","CYFB","CYRB","CYAB","BGTL","BIKF"]
coords = np.empty([9,2])
coords[::] = ([61.251389,210.193611],[64.6656444,212.8985611],[68.303889,226.516944],[62.463056,245.559722],[63.756667,291.443889],[74.716944,265.030556],[73.006389,274.95277799999997],[76.531111,291.296944],[63.985,337.394444])

models = ["ACCESS-CM2","ACCESS-ESM1-5","BCC-CSM2-MR","CanESM5","CMCC-CM2-SR5","CMCC-ESM2","CNRM-CM6-1","CNRM-ESM2-1","EC-Earth3","FGOALS-g3","GFDL-CM4","GFDL-ESM4","INM-CM4-8","INM-CM5-0","IPSL-CM6A-LR","KIOST-ESM","MIROC-ES2L","MIROC6","MPI-ESM1-2-HR","MPI-ESM1-2-LR","MRI-ESM2-0","NESM3","NorESM2-LM","NorESM2-MM","TaiESM1"]

var = 'tasmin'
experiment = 'ssp585'
years = [2045,2055,2065,2075]

for k in years:
    for i in models:
        if i in {'CESM2-WACCM','FGOALS-g3'}:
            run = 'r3i1p1f1'
        elif i == 'CESM2':
            run = 'r4i1p1f1'
        elif i in {'HadGEM3-GC31-MM', 'HadGEM3-GC31-LL'}:
            run = 'r1i1p1f3'
        elif i in {'CNRM-CM6-1', 'CNRM-ESM2-1','GISS-E2-1-G','MIROC-ES2L','UKESM1-0-LL'}:
            run = 'r1i1p1f2'
        else:
            run = 'r1i1p1f1'
        
        if i in {"ACCESS-CM2","ACCESS-ESM1-5","BCC-CSM2-MR","CanESM5","CESM2-WACCM","CESM2","CMCC-CM2-SR5","CMCC-ESM2","FGOALS-g3","GISS-ES-1-G","HadGEM3-GC31-LL","HadGEM3-GC-31-MM","IITM-ESM","MIROC-ES2L","MIROC6","MPI-ESM1-2-HR","MPI-ESM1-2-LR","MRI-ESM2-0","NESM3","NorESM2-LM","NorESM2-MM","TaiESM1","UKESM1-0-LL"}:
            grid = "gn"
        elif i in {"CNRM-CM6-1","CNRM-ESM1-1","EC-Earth3-Veg-LR","EC-Earth3","IPSL-CM6A-LR","KACE-1-0-G"}:
            grid = "gr"
        elif i in {"GFDL-CM4","GFDL-ESM4","INM-CM4-8","INM-CM5-0","KIOST-ESM"}:
            grid = "gr1"
        elif i in {"GFDL-CM4_gr2"}:
            grid = "gr2"
            
        for j in range(9):
            get_data(var,experiment,i,run,k,k,coords[j][0],coords[j][0],coords[j][1],(coords[j][1]+0.05),grid)
        
            os.rename("tasmin_tasmin_day_"+str(i)+'_ssp585_'+str(run)+'_'+str(grid)+'_'+str(k)+'.nc', str(locs[j])+"_tasmin_tasmin_day_"+str(i)+'_ssp585_'+str(run)+'_'+str(grid)+'_'+str(k)+'.nc')
