# Pandas OpenPyXl
import pandas
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from logs.logger import logger

class FileHandler:
    def __init__(self):
        self.df = pandas.read_json('data.json')

    def verificaDuplicados(self):
        logger.info("Iniciando processo de verificar duplicados")
        
        if (self.df.duplicated().any()):
            print("\nO arquivo contém registros duplicados!\n")
        else:
            print("\nNenhum registro duplicado encontrado.\n")
            
        logger.info("Processo finalizado")

    def indentificaDuplicados(self):
        logger.info("Iniciando processo de identificar duplicados")
        
        duplicados = self.df[self.df.duplicated()]
        
        if not duplicados.empty:
            print("\nRegistros duplicados encontrados:")
            print(duplicados)
        else:
            print("\nNenhum registro duplicado encontrado.")
        
        logger.info("Processo finalizado")

    def excluiDuplicados(self):
        logger.info("Iniciando processo para excluir registros duplicados")
        
        if (self.df.duplicated().any()):
            self.df = self.df.drop_duplicates()
            self.df.to_json('data.json', orient='records', indent=4)
            print("\nRegistros duplicados excluidos\n")
        else:
            print("\nNenhum registro duplicado encontrado.\n")

        logger.info("Processo finalizado")

    def converteParaXlsx(self):
        logger.info("Iniciando de conversao de arquivo json -> xlsx")
        self.df.to_excel('dados.xlsx', index=False)
        logger.info("Processo finalizado")

    def converteParaCsv(self):
        logger.info("Iniciando de conversao de arquivo json -> csv")
        self.df.to_csv('dados.csv', index=False)
        logger.info("Processo finalizado")

    def converteParaXml(self):
        logger.info("Iniciando de conversao de arquivo json -> xml")
        self.df.to_xml('dados.xml', index=False)
        logger.info("Processo finalizado")

if __name__ == "__main__":
    automacao = FileHandler()
    automacao.indentificaDuplicados()
