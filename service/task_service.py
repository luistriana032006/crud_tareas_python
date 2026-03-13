
from models.task import taskmodel
from service.task_Repository import task_repository


class TaskService(task_repository):
## listas de taras
    
    ## constructor
    def __init__(self):
        self.tasks: list[taskmodel] = []


    def create_task(self, task: taskmodel) -> None:
        
        raise NotImplementedError

    def find_by_id(self, id: int) -> taskmodel | None:
        raise NotImplementedError

    def update_task(self, task: taskmodel) -> taskmodel:
        raise NotImplementedError

    def delete(self, id: int) -> None:
        raise NotImplementedError

    def find_all(self) -> list[taskmodel]:
        raise NotImplementedError


    