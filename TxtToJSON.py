import sys
import glob
import json
from collections import OrderedDict

year=str(sys.argv[1])
filename=str(sys.argv[2]) ####if txt files are Run2017_24Feb2020_runEtaR9Gain_v2_scales/smearing.dat then filename=Run2017_24Feb2020_runEtaR9Gain_v2


filename_scales=filename+"_scales.dat"
filename_smearing=filename+"_smearings.dat"

outfilename_scales=filename+"_scales.json"
outfilename_smearing=filename+"_smearings.json"






def _checkKey(key, dict):
    if key not in dict:
        return True
    else:
        False


def _convertScalestoJSON():
    dict_scales = OrderedDict() #OrderedDict keeps the order in which elements are inserted into the dictionary
    with open(filename_scales, 'r') as data:
        for line in data:
            line = line.strip()
            ldata = line.split()
            #print ldata[0]
            #dict_scales = OrderedDict() #OrderedDict keeps the order in which elements are inserted into the dictionary 
            runkey = "run:[%s,%s]"%(ldata[0], ldata[1])
            etakey = "eta:[%s,%s]"%(ldata[2], ldata[3])
            r9key = "r9:[%s,%s]"%(ldata[4], ldata[5])
            ptkey = "pt:[%s,%s]"%(ldata[6], ldata[7])
            gainkey = "gain:%s"%(ldata[8])
            
            #namekey = "ScaleCorrection";
            #if(_checkKey(namekey, dict_scales)): dict_scales[namekey] = OrderedDict() 
            

            if(_checkKey(runkey, dict_scales)): dict_scales[runkey] = OrderedDict() 
            if(_checkKey(etakey, dict_scales[runkey])): dict_scales[runkey][etakey]  = OrderedDict()
            if(_checkKey(r9key, dict_scales[runkey][etakey])): dict_scales[runkey][etakey][r9key]   = OrderedDict()
            if(_checkKey(ptkey, dict_scales[runkey][etakey][r9key])): dict_scales[runkey][etakey][r9key][ptkey]  = OrderedDict() 
            if(_checkKey(gainkey, dict_scales[runkey][etakey][r9key][ptkey])): dict_scales[runkey][etakey][r9key][ptkey][gainkey] = OrderedDict()
            

            dict_scales[runkey][etakey][r9key][ptkey][gainkey]["runMin"] = int(ldata[0])
            dict_scales[runkey][etakey][r9key][ptkey][gainkey]["runMax"] = int(ldata[1])
            dict_scales[runkey][etakey][r9key][ptkey][gainkey]["etaMin"] = float(ldata[2])
            dict_scales[runkey][etakey][r9key][ptkey][gainkey]["etaMax"] = float(ldata[3])
            dict_scales[runkey][etakey][r9key][ptkey][gainkey]["r9Min"] = float(ldata[4])
            dict_scales[runkey][etakey][r9key][ptkey][gainkey]["r9Max"] = float(ldata[5])
            dict_scales[runkey][etakey][r9key][ptkey][gainkey]["ptMin"] = float(ldata[6])
            dict_scales[runkey][etakey][r9key][ptkey][gainkey]["ptMax"] = float(ldata[7])
            dict_scales[runkey][etakey][r9key][ptkey][gainkey]["gain"] = int(ldata[8])
            
            dict_scales[runkey][etakey][r9key][ptkey][gainkey]["scale"] = float(ldata[9])
            dict_scales[runkey][etakey][r9key][ptkey][gainkey]["scaleErr"] = float(ldata[10])
            

            
            '''
            dict_scales[namekey]["runMin"] = ldata[0]
            dict_scales[namekey]["runMax"] = ldata[1]
            dict_scales[namekey]["etaMin"] = ldata[2]
            dict_scales[namekey]["etaMax"] = ldata[3]
            dict_scales[namekey]["r9Min"] = ldata[4]
            dict_scales[namekey]["r9Max"] = ldata[5]
            dict_scales[namekey]["ptMin"] = ldata[6]
            dict_scales[namekey]["ptMax"] = ldata[7]
            dict_scales[namekey]["gain"] = ldata[8]

            dict_scales[namekey]["scale"] = ldata[9]
            dict_scales[namekey]["scaleErr"] = ldata[10] 
            '''
    with open(outfilename_scales, 'w') as fp:
        json.dump(dict_scales, fp, sort_keys=False,indent=4 )
    


def _convertSmearingtoJSON():
    dict_smearing = OrderedDict() #OrderedDict keeps the order in which elements are inserted into the dictionary
    with open(filename_smearing, 'r') as data:
        for line in data:
            if line.startswith("#"):
                continue

            line = line.strip()
            ldata = line.split()
            
            catkey = "category:[%s]"%(ldata[0])
            
            if(_checkKey(catkey, dict_smearing)): dict_smearing[catkey]  = OrderedDict()
            
            dict_smearing[catkey]["category"] = ldata[0]
            dict_smearing[catkey]["Emean"] = float(ldata[1])
            dict_smearing[catkey]["EmeanErr"] = float(ldata[2]) 
            dict_smearing[catkey]["rho"] = float(ldata[3]) 
            dict_smearing[catkey]["rhoErr"] = float(ldata[4])
            dict_smearing[catkey]["phi"] = ldata[5]
            dict_smearing[catkey]["phiErr"] = ldata[6]
            
            '''
            dict_smearing[namekey]["etaMin"] = ldata[0] 
            dict_smearing[namekey]["etaMax"] = ldata[1] 
            dict_smearing[namekey]["r9Min"] = ldata[2] 
            dict_smearing[namekey]["r9Max"] = ldata[3] 

            dict_smearing[namekey]["Emean"] = ldata[4] 
            dict_smearing[namekey]["EmeanErr"] = ldata[5] 
            dict_smearing[namekey]["rho"] = ldata[6] 
            dict_smearing[namekey]["rhoErr"] = ldata[7] 
            dict_smearing[namekey]["phi"] = ldata[8] 
            dict_smearing[namekey]["phiErr"] = ldata[9] 
            '''

    with open(outfilename_smearing, 'w') as fp:
        json.dump(dict_smearing, fp, sort_keys=False,indent=4 )
    
_convertScalestoJSON()
_convertSmearingtoJSON()
