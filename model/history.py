from connection.database import conn
import sqlite3 as sql
from datetime import date


def createHistory(id_anggota):
  try:
    cur = conn.cursor()
    today = date.today()
    cur.execute("INSERT INTO history (id_anggota, date) VALUES (?,?)", (id_anggota,today) )
    conn.commit()
  except:
    conn.rollback()
    msg = "error in insert operation"

def checkHistoryNow(id_anggota):
  rows = []
  try:
    cur = conn.cursor()
    conn.row_factory = sql.Row
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    cur.execute("select * from history where id=" + id_anggota + " and date like '%" + d1 + "%'")
    rows = cur.fetchall()
    id = len(rows)[0]
  except:
    conn.rollback()
    msg = "error in select operation"
  finally:
    return rows