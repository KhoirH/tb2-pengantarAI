from connection.database import conn
import sqlite3 as sql
from datetime import date


def createHistory(id_anggota):
  try:
    cur = conn.cursor()
    cur.execute("INSERT INTO history(id_anggota) VALUES (?)", (id_anggota) )
    conn.commit()
  except:
    conn.rollback()
    msg = "error in insert operation"

def checkHistoryNow(id_anggota):
  try:
    con.row_factory = sql.Row
    cur = conn.cursor()
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    cur.execute("select * from anggota where id=" + id_anggota + " and date like %" + d1 + "%")
    rows = cur.fetchall()
  except:
    conn.rollback()
    msg = "error in select operation"
  finally:
    return rows