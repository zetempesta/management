import codecs
import os

def write_file(filename:str, data):
    file = codecs.open(filename=filename, mode='w')
    file.write(data)
    file.close()

def delete_file(file:str)->bool:

    try:
        os.remove(file)
        return True
    except:
        return False 

def delete_all_files(folder:str):
    for f in os.listdir(folder):
        file = folder + os.sep + f
        delete_file(file)