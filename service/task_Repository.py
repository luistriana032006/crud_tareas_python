from abc import ABC, abstractmethod
from typing import Optional
from models.task import taskmodel 
"""
abc -> clase que debemos implemenar
abstractmethod -> es el decorador que marca cada metodo como abstracto

"""
class task_repository(ABC):

    ## crear una tarea
    @abstractmethod
    def create_task(self, task: taskmodel) -> None:
        pass

    ## ver una tarea
    @abstractmethod
    def find_by_id(self, id: int) -> Optional[taskmodel]:
        pass

    ## actualizar una tarea
    @abstractmethod
    def update_task(self, task: taskmodel) -> taskmodel:
        pass

    ## eliminar una tarea
    @abstractmethod
    def delete(self, id:int) -> None:
        pass

    ## retornar todos en una lista 
    @abstractmethod
    def find_all(self) -> list[taskmodel]: 
        pass

