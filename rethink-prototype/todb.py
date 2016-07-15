# This script writes input data to rethinkdb

from conn import conn
import rethinkdb as r
import sys


d = sys.stdin.readlines()


# execute insert
r.db('foo')
    .table('tweets')
    .insert(d)
    .run(conn)

def insert(some_json, conn):
    r.db('foo')
        .table('tweets')
        .insert(some_json)
        .run(conn)
