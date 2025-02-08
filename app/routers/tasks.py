from fastapi import APIRouter

from app.schemas.task_logs import TaskLogCreate, TaskLogPydantic, TaskLogRequest
from app.schemas.tasks import TaskPydantic
from app.services.task_logs import create_task_log
from app.services.tasks import get_tasks


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/", response_model=list[TaskPydantic])
async def get_tasks_endpoint():
    return await get_tasks()

@router.get("/{task_id}", response_model=TaskPydantic)
async def get_task_endpoint(task_id: int):
    return await get_task(task_id)

@router.patch("/{task_id}", response_model=TaskPydantic)
async def update_task_endpoint(task_id: int):
    return await update_task(task_id)

@router.patch("/{task_id}/requeue", response_model=TaskPydantic)
async def requeue_task_endpoint(task_id: int):
    return await requeue_task(task_id)

@router.post("/{task_id}/logs", response_model=TaskLogPydantic)
async def create_task_log_endpoint(task_id: int, task_log: TaskLogRequest):
    task_log = TaskLogCreate(task_id=task_id, log_message=task_log.log_message)
    return await create_task_log(task_log)