import peewee

from src.data import DB

class BaseModel(peewee.Model):

    id = peewee.CharField(max_length=32, primary_key=True, unique=True, null=False)

    class Meta:
        database = DB
