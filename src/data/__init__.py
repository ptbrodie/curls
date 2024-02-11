import os
import peewee


DB = None
CURLSDIR = os.path.join(os.getenv("HOME"), ".curls")
CURLSDB = os.path.join(CURLSDIR, "curls.db")
ID_REGEX = "^[0-9a-f]{8}[0-9a-f]{4}[0-5][0-9a-f]{3}[089ab][0-9a-f]{3}[0-9a-f]{12}$"


if not os.path.exists(CURLSDIR):
    os.mkdir(CURLSDIR)
DB = peewee.SqliteDatabase(CURLSDB)
DB.connect()
