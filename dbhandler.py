# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 10:30:58 2017

@author: lenovo
"""

import sqlite3

class dbhandler(object):
    def __init__(self,dbname):
        self.conn = sqlite3.connect(dbname)
    def create_table(self,nama):
        self.conn.execute("""
            CREATE TABLE %s(id PRIMARY_KEY AUTO_INCREMENT,pesanan TEXT,jumlah INTEGER,tanggal DATETIME)  
            """ %(nama))
        self.conn.commit()
    def insert_value(self,name,pesanan,jumlah):
        row_number = [i for i in self.conn.execute("select count(id) from %s" %(name))][0][0]
        pesan = "'" + ",".join(pesanan) +"'"
        self.conn.execute("""
            INSERT INTO %s(id,pesanan,jumlah,tanggal) VALUES(%s,%s,%s,date())  
            """ %(name,str(row_number+1),pesan,str(jumlah)))
        self.conn.commit()
        
    def delete_all(self,nama):
        self.conn.execute("DELETE  FROM %s" %(nama))
        self.conn.commit()
    def show_value(self,name):
        for i in self.conn.execute("SELECT * FROM %s" %(name)):
            print(i)
    def close(self):
        self.conn.close()
"""
kluntung = dbhandler('mayam.db')
#kluntung.insert_value('pelanggan',['teh','ayam'],192)
kluntung.insert_value('pelanggan',['teh','ayam'],192)
kluntung.delete_all('pelanggan')
"""
kluntung = dbhandler('mayam.db')
kluntung.show_value('pelanggan')
