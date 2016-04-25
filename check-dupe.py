#!/usr/bin/env python3

import os, os.path
#import shutil
import time
import sys
import hashlib
import pprint

class ChecaDuplicatas():
    """check-dupe.py: Procura no diretório escolhido por arquivos que possuam
hash sum MD5 iguais fazendo uma lista dos arquivos duplicados.
Argumentos de linha de comando:
    1) Pasta onde procurar: -v para Videos; -p para Pictures;
    2) Subpasta a ser considerada.
    
    Ex.: ./check-dupe -p "2010/Dec" --> Pega arquivos da pasta ~/Pictures/2010/Dec e
procura por duplicatas.
"""
    def __init__(self, srcpath):
        self.srcpath=srcpath

    def ChecarArquivos(self):
        #Tempo inicial
        self.start=time.time()
        self.numberFiles=0
        self.fileHash={}
        self.duplicates={}
        #Iterando sobre o caminho e criando o dicionário de arquivos/MD5
        for foldername, subfolders, filenames in os.walk(self.srcpath):
            for filename in filenames:
                self.numberFiles+=1
                self.fileHash[str(os.path.join(foldername, filename))]=hashlib.md5(open\
                (str(os.path.join(foldername, filename)), 'rb').read()).hexdigest()
                self.duplicates[str(os.path.join(foldername, filename))]=hashlib.md5(open\
                (str(os.path.join(foldername, filename)), 'rb').read()).hexdigest()
        #Procurando por valores de MD5 duplicados
        self.uniques={}
        for key, value in self.fileHash.items():
            if value not in self.uniques.values():
                self.uniques[key]=value
                del self.duplicates[key]
        pprint.pprint(self.duplicates)

#        for key in self.duplicates:
#            #print (key)
#            try:
#                shutil.move(key, '/home/vicerodrigues/Downloads/teste/')
#            except:
#                pass

        print('\n')
        #Fechando o Script e imprimindo informações
        self.end=time.time()
        self.elapsed=self.end-self.start
        if self.elapsed>=3600:
           self.horas=self.elapsed//3600
           if self.elapsed%3600>=60:
               self.minutos=(self.elapsed%3600)//60
               self.segundos=(self.elapsed%3600)%60
               print('%i Arquivos processados em %i horas, %i minutos e %.2f\
 segundos' %(self.numberFiles, self.horas, self.minutos, self.segundos))
           else:
               print('%i Arquivos processados em %i horas e %.2f segundos'\
 %(self.numberFiles, self.horas, self.segundos))
        elif self.elapsed>=60:
            self.minutos=self.elapsed//60
            self.segundos=self.elapsed%60
            print('%i Arquivos processados em %i minutos e %.2f segundos'\
 %(self.numberFiles, self.minutos, self.segundos))
        else:
            print('%i Arquivos processados em %.2f segundos' %(self.numberFiles, \
self.elapsed))

        print('Total de arquivos duplicados: %i'%len(self.duplicates))

if __name__=='__main__':
    error="""check-dupe.py: Procura no diretório escolhido por arquivos que possuam
hash sum MD5 iguais fazendo uma lista dos arquivos duplicados.
Argumentos de linha de comando:
    1) Pasta onde procurar: -v para Videos; -p para Pictures;
    2) Subpasta a ser considerada.
    
    Ex.: ./check-dupe -p "2010/Dec" --> Pega arquivos da pasta ~/Pictures/2010/Dec e
procura por duplicatas.
"""
    if not len(sys.argv)==3:
        print(error)
    elif not(sys.argv[1]=='-v' or sys.argv[1]=='-p'):
        print(error)
    else:
        if sys.argv[1]=='-v':
            srcpath=os.path.join(os.path.expanduser('~/Videos'), sys.argv[2])
        elif sys.argv[1]=='-p':
            srcpath=os.path.join(os.path.expanduser('~/Pictures'), sys.argv[2])
        checkDupe=ChecaDuplicatas(srcpath)
        checkDupe.ChecarArquivos()
