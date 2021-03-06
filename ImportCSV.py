import csv

'''
constructs a class at runtime like (class_name, (objects,), dictionary) 
'''
def classfactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)

'''
helper method return_data_as_objs
@:param IS 601
@:return an object list ie for addition: type('addition',()  )
'''

def return_data_as_objs(classname, dictData):
    listofobjs = []
    for row in dictData:
        listofobjs.append(classfactory(classname, row))
    return listofobjs

'''
This class only reads a file in CSV
'''
class ReaderOfCSVs:
    data = [] #this var ruined it all for me
    '''
    Constructor
    @:param filepath
    open a file path specified for reading a csv
    Each row in the csvRow is then added to a list
    '''
    def __init__(self, filepapa):
        self._newData = []
        self._filepapa = filepapa
        with open(self._filepapa) as textToRead:
            csvrow = csv.DictReader(textToRead, delimiter=",")
            for row in csvrow:
                self._newData.append(row)
        textToRead.close()

    def create_class_dynamically(self, classname):
        return return_data_as_objs(classname, self._newData)
