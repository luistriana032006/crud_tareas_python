from pydantic import BaseModel
from models.task import taskmodel

class taskRequest(BaseModel):
    id: int
    name: str
    description: str
    complete: bool

    def to_model(self) -> taskmodel:
        return taskmodel(
            id = self.id,
            name = self.name,
            description = self.description,
            complete = self.complete
        )
        