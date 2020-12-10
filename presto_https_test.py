from pyhive import presto
from requests.auth import HTTPBasicAuth
from sqlalchemy.engine import create_engine

from pyhive import presto

CERT_PATH = '/path/to/presto.pem'
HOST = 'insert.hostname'
PORT = 8080
CATALOG = 'hive'

USER = 'fvcamelo'
pwd = 'thepassword' # do not expose passwords in code, please

cursor = presto.connect(
    HOST,
    username=USER,
    protocol='https',
    port=PORT,
    requests_kwargs={
        'auth': HTTPBasicAuth(USER, pwd), 
        'verify': CERT_PATH
    },
    catalog=CATALOG
    ).cursor()


cursor.execute('SHOW SCEHMAS')

print (cursor.fetchone())
print (cursor.fetchall())