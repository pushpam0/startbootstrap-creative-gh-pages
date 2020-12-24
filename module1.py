import pyodbc
from flask import jsonify
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

@app.route('/home')
def hello_world():
     return render_template('index.html')

@app.route('/registration')
def data_base():
      conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=DESKTOP-O42EL64\SQLEXPRESS;"
        "Database=Test;"
        "UID=DESKTOP-O42EL64\pushpam;"
        "Trusted_Connection=yes;"
        )
      cursor = conn.cursor()
      cursor.execute(
        'insert into dummy(name,mno) values(?,?);',
        ('abc', 123)
        )
      conn.commit()
      conn.close()
      return 'Hello, World'

@app.route('/login')
def read():
     conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=DESKTOP-O42EL64\SQLEXPRESS;"
        "Database=Test;"
        "UID=DESKTOP-O42EL64\pushpam;"
        "Trusted_Connection=yes;"
        )
     cursor = conn.cursor()
     cursor.execute("SELECT id FROM dummy WHERE CONVERT(VARCHAR, name) ='abc'; ")
     for row in cursor:
        print(f'row = {row}')
     conn.commit()
     conn.close()
     print(cursor);
     if cursor.rowcount==0:
        return jsonify(authenticaton=bool(False), name="abs",pno=123,ip="127.45.10.1")
     else:
        return jsonify(authenticaton=bool(True) , name="abs",pno=123,ip="127.45.10.0")



if __name__ == '__main__':
    app.run('localhost', 4449)
