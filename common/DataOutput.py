import sqlite3


class DataOutput(object):
    
    def __init__(self):
        self.conn = sqlite3.connect('MTime.db')
        self.create_table()
    
    def create_table(self):
        self.conn.execute('''
        CREATE TABLE MTIME
           (ID VARCHAR(20) PRIMARY KEY NOT NULL,
           ISRELEASE BOOLEAN,
           MOVIETITLE VARCHAR(100),
           RATINGFINAL VARCHAR(10),
           TOTALBOXOFFICEUNIT VARCHAR(10),
           SHOWDAYS INT);
       ''')
        self.conn.commit()
        
    def store_data(self, items):
        for item in items:
            self.conn.execute("INSERT INTO MTIME (ID,ISRELEASE,MOVIETITLE,RATINGFINAL,TOTALBOXOFFICEUNIT,SHOWDAYS) \
              VALUES (%s, %s, %s, %s, %s, %s)" % (item[0], item[1], item[2], item[3], item[4], item[5]));
              
        self.conn.commit()
        
    def close_connect(self):    
        self.conn.close()
        
        