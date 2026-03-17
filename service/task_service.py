
from multiprocessing import Value
from sre_parse import NOT_LITERAL_UNI_IGNORE
from models.task import taskmodel
from service.task_Repository import task_repository


class TaskService(task_repository):
## listas de taras
    
    ## constructor￼

    def __init__(self):
        self.tasks: list[taskmodel] = []
        


    def create_task(self, task: taskmodel) -> None:
       resultado = self.find_by_id(task.id)
       if resultado is not None:
            raise ValueError("id duplicado")
       self.tasks.append(task)

      

    def find_by_id(self, id: int) -> taskmodel | None:
        if (id<=0):
            raise ValueError("el id que ingreso es negativo o cero")
        
        for t in self.tasks:
            if id == t.id:
                return t

        return None


    def update_task(self, task: taskmodel) -> taskmodel:
        tasklist = self.find_by_id(task.id)
        if tasklist is None:
            raise ValueError("no encontrado")

        tasklist.name = task.name
        tasklist.complete= task.complete
        tasklist.description=task.description


        return tasklist

    def delete(self, id: int) -> None:
        r = self.find_by_id(id)
        if r is None:
            raise ValueError("el id no se encontro")

        self.tasks.remove(r)
       

    def find_all(self) -> list[taskmodel]:
        return self.tasks
        


    