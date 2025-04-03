# Pandas OpenPyXl
import pandas

df = pandas.read_json('data.json')

print(df)

def verificaDuplicados():
    if (df.duplicated().any()):
        print("O arquivo contém registros duplicados!")
    else:
        print("Nenhum registro duplicado encontrado.")

def indentificaDuplicados():
    duplicados = df[df.duplicated()]
    
    if not duplicados.empty:
        print("\nRegistros duplicados encontrados:")
        print(duplicados)
    else:
        print("\nNenhum registro duplicado encontrado.")

def converteParaXls():
    df.to_excel('dados.xlsx', index=False)

def converteParaCsv():
    df.to_csv('dados.csv', index=False)

def converteParaXml():
    df.to_xml('dados.xml', index=False)

verificaDuplicados()
indentificaDuplicados() 
