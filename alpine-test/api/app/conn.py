# The api connection to rethinkdb

import rethinkdb as r


c = r.connect(
        host='db',
        port='28015')

def init_dbs():

    DB = 'test'
    TABLE = 'foo'

    r.table_create( TABLE ).run(c)
    tab = r.db( DB ).table( TABLE )

    tab.insert({
        'numbers':[ 50, 60, 70, 80, 90, 120, 160, 200, 260 ]
        }).run(c)

    return tab
