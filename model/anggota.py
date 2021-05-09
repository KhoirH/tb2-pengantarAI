from connection.database import conn
import sqlite3 as sql

def createAnggota(nama, path):
  try:
    cur = conn.cursor()
    cur.execute("INSERT INTO anggota (nama, path) VALUES (?,?)", (nama, path) )
    conn.commit()
  except:
    conn.rollback()
    msg = "error in insert operation"

def checkLastId():
  rows = []
  try:
    cur = conn.cursor()
    conn.row_factory = sql.Row
    cur.execute("select * from anggota")
    rows = cur.fetchall()
  except:
    msg = "error in select operation"
  finally:
    return rows[len(rows) - 1]
