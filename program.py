import json
from functools import reduce
from operator import getitem
import sys

#function to update a dict with an list of keys
def set_nested_item(dataDict, mapList, val):
    """Set item in nested dictionary"""
    reduce(getitem, mapList[:-1], dataDict)[mapList[-1]] = val
    return dataDict

if(len(sys.argv) == 3):

    # Opening config JSON file, input changes and output file
    configF = open(sys.argv[1],"r")
    inputF = open(sys.argv[2], "r")
    outFile = open("out_file.json", "w")
    
    # returns JSON object as
    # a dictionary
    dataJSON = json.load(configF)

    for l in inputF:
        try:
            sp = l.split(":",1)
            p = json.loads(sp[0].replace("[", ".").replace("]", ""))
            key_lst = p.split(".")
            key_lst = [int(item) if item in '0123456789' else item for item in key_lst]
            value = json.loads(sp[1])
            d = set_nested_item(dataJSON, key_lst, value)
            dataJSON.update(d)
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")


    #write the outputfile from updated json
    json.dump(dataJSON, outFile)
    
    # Closing file
    configF.close()
    inputF.close()
    outFile.close()

else:
    print("Expected input python3 program.py configfile.json input_changes.txt")