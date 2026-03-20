from fastapi import FastAPI
from service.task_service import TaskService
from models.task_requests import taskRequest

app = FastAPI()
service = TaskService()


@app.get("/tasks")
def find_all():
    return service.find_all()


## traer tarea por id
@app.get("/tasks/{id}")
def find_by_id(id: int):
    return service.find_by_id(id)


### crear una tarea


@app.post("/tasks")
def create_task(request: taskRequest):
    request= request.to_model()
    return service.create_task(request)


## eliminar una tarea


@app.delete("/tasks/{id}")
def delete_task(id: int):
    return service.delete(id)


@app.put("/tasks")
def update_task(request: taskRequest):
    request= request.to_model()
    return service.update_task(request)
