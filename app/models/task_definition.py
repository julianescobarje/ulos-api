from tortoise import fields
from tortoise.models import Model

class TaskDefinition(Model):
    id = fields.IntField(pk=True)
    type_name = fields.CharField(max_length=255, unique=True)
    type_description = fields.TextField()
    created_by = fields.ForeignKeyField("models.SysUser", related_name="task_definitions")
    creation_timestamp = fields.DatetimeField(auto_now_add=True)
