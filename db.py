import json
from pathlib import Path

class DatabaseManager():
    def __init__(self,dbname):
        self.path_db = './db/'
        self.db = self.path_db+dbname
        self.db_obj = None

        Path_db = Path(self.path_db)

        if not (Path_db.exists()):
            self.db_obj=dict()
            Path_db.mkdir()
            self.manag_conn('w')


    def manag_conn(self,tipo):
        try:
            if tipo == 'r':
                with open(self.db+'.db',tipo) as db:
                    self.db_obj = json.load(db)
                    db.close()
            elif tipo == 'w':
                with open(self.db+'.db','w') as db:
                    json.dump(self.db_obj,db)
                    db.close()

        except Exception as err:
            print('manag_conn:',err)
            return False

    def get_data(self,indice,campo=0):
        try:
            self.manag_conn('r')

            for i in self.db_obj:
                if indice == i:
                    if(campo):
                        return self.db_obj[i][campo]
                    else:
                        return i

            return False

        except Exception as err:
            print(err)
            return False

    def upsert_data(self,indice,dado,campo=0):
        try:
            self.manag_conn('r')

            if not (campo):
                if indice not in self.db_obj.keys():
                    self.db_obj.update({indice:dado})
                    self.db_obj[indice].update({'saldo':0,'mov':[]})
            else:
                for i in self.db_obj:
                    if i == indice:
                        if campo != 'mov':
                             self.db_obj[i].update({campo:dado})
                        else:
                             self.db_obj[i]['mov'].append(dado)

            self.manag_conn('w')

        except Exception as err:
            print('insert_data:',err)
            return False

        else:
            return True



'''
    def update_data(self,indice,dado,campo=0):
        self.get_data(indice)

        try:
                for i in self.db_obj[self.srcName]:
                    if indice == i:
                        if(campo):
                            self.db_obj[self.srcName][i][campo] = dado
                        else:
                            self.db_obj[self.srcName][i] = dado

                self.manag_conn('w')


        except Exception as err:
            print('update data:',err)

'''
