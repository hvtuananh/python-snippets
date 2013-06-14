import MySQLdb
import MySQLdb.cursors
import traceback

def getConn(host, user, passwd, db):
    conn = None
    try:
        conn = MySQLdb.connect(host = host,
                               user = user,
                               passwd = passwd,
                               db = db,
                               cursorclass = MySQLdb.cursors.DictCursor,
                               use_unicode=True,
                               charset="utf8",
                               init_command='SET NAMES utf8')
    except:
        traceback.print_exc()
    return conn;

def closeConn(conn):
    try:
        conn.close()
    except:
        pass
    
def escape(val):
    val = unicode(val)
    val = val.replace('\\', '\\\\')
    return val.replace('\'', '\\\'')

def getTypeMap(conn, table):
    typeMap = {}
    query = "DESCRIBE " + table
    cursor = conn.cursor()
    cursor.execute(query)
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        typeMap[row["Field"]] = re.sub('\(.*\)', '', row["Type"]).strip()
    cursor.close()
    return typeMap

def quote(val):
    return "'" + escape(val) + "'"