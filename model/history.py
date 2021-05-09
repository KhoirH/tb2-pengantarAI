from connection.database import conn
import sqlite3 as sql

def createHistory(id_anggota):
  try:
    cur = conn.cursor()
    cur.execute("INSERT INTO history(id_anggota) VALUES (?)", (id_anggota) )
    conn.commit()
  except:
    conn.rollback()
    msg = "error in insert operation"

def checkHistory(id_anggota):
  try:
    con.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("select * from anggota where id=" + id_anggota)
    rows = cur.fetchall()
  except:
    conn.rollback()
    msg = "error in select operation"
  finally:
    return rows