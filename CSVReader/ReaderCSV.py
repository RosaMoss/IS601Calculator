import csv
from FileUtilities import absolutepath
import csv
from Fileutilities.absolutepath import absolute_path


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)
'''
helper method return_data_as_objs
'''
def return_data_as_objs(classname, dictData):
    listofobjs = []
    if len(dictData) == 0:
        raise IndexError
    else:
        for row in dictData:
            listofobjs.append(classfactory(classname, row))
    return listofobjs

class CsvReader:
    data = []

    def __init__(self, filepapa):
        self._newData = []
        self._filepapa = filepapa
        with open(absolutepath.absolutepath(filepapa)) as textToRead:
            csvrow = csv.DictReader(textToRead, delimiter=",")
            for row in csvrow:
                self._newData.append(row)
        textToRead.close()

    def create_class_dynamically(self, classname):
        return return_data_as_objs(classname, self._newData)
