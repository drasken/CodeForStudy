from enum import Enum
from datetime import datetime

class Status(Enum):

    #using numbers to encod status
    TODO,DOING,CANCELED,COMPLETED = range(1,5)
    

class Task:
    def __init__(self, name, description, status = Status.TODO ):
        self.name = name
        self.description = description
        self.status = status
        self.date = None
        
        #maybe pass None as standars value instead of if...
        if not self.date:
            self.date = datetime.now()

    def __str__(self):
        return (f'{self.name} : {self.description}. Status: {self.status.value}')


    #Here are the Setters, not Pythonic(?)
    def setCompleted(self):
        self.status = Status.COMPLETED

    def setStarted(self):
        self.status = Status.DOING

    def setCanceled(self):
        self.status = Status.CANCELED


