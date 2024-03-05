from enum import Enum
from datetime import datetime

class Status(Enum):

    #using numbers to encod status
    TODO,DOING,CANCELED,DONE = range(1,5)
    

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
        return (f'{self.name} : {self.description}. Status: {self.status.value}. Creation date {self.date}')


    #Here are the Setters, not Pythonic(?)
    def setCompleted(self):
        self.status = Status.DONE

    def setStarted(self):
        self.status = Status.DOING

    def setCanceled(self):
        self.status = Status.CANCELED
        
    #mathod to format a Task for CSV file
    def toCsv(self):
        return (f'{self.name}, {self.description}, {self.status.value}, {self.date}\n')


def createNewTask():
    
    name = input("What is the task Name?\n")
    description = input("Do you whant to add a description?\n Add it here: ")
    status = input("Do you want to set a task's status between TODO,DOING,CANCELED,DONE (default: TODO)? \n")
    
    newTask = Task(name, description, status=Status.TODO)
    
    return newTask
    pass