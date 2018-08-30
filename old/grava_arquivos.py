__author__='AlVictor'

import csv
try:
    import json
except ImportError:
    import simplejson as json
    
class GravaArquivos:

        def __init__(self, filename, file):
            self.filename = filename
            self.file = file
    
        def save_json(self):
            with open(self.filename+'.json', 'w') as f:
                data_json = json.dumps(self.file)
                f.write(str(data_json))
                print ("Arquivo "+self.filename+'.json'+" criado com sucesso")
                f.close()
        def save_csv(self):
            with open(self.filename+'.csv', 'w', newline='') as f:
                data_csv =  csv.writer(f, delimiter=' ', quotechar=';', quoting=csv.QUOTE_MINIMAL)
                data_csv.writerow(self.file)



    
