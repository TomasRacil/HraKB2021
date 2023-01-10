from csv import reader
from os.path import join, realpath, dirname

def get_text_by_id(text_id:str):
    language= 'cz' # get from main...
    with open(join(dirname(dirname(realpath(__file__))),"Static" ,"texts.csv"), "r", encoding="utf-8") as file:
        texts = reader(file, delimiter=';')
        header = []
        header = next(texts)
        col=header.index(language)
        for row in texts:
            if row[0]==text_id:
                return row[col]