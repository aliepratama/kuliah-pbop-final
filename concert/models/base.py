import sqlite3

class ModelBase:
    def __init__(self, file):
        self.file = file

    def connect(self):
        try:
            self.db = sqlite3.connect(self.file)
            self.cur = self.db.cursor()
        except:
            print('Terjadi kesalahan koneksi database!')
            exit()

    def insert(self, table, data):
        self.connect()
        keys = ', '.join(data.keys())
        values = ', '.join(['?'] * len(data))
        sql = 'insert into %s (%s) values (%s)' % (table, keys, values)
        try:
            self.cur.execute(sql, tuple(data.values()))
            self.db.commit()
            self.cur.close()
        except Exception as e:
            print(e)
            self.db.rollback()
    
    def update(self, table, data, condition):
        self.connect()
        keys = ', '.join(['%s=%s' % (k, '?') for k in data.keys()])
        sql = 'update %s set %s where %s' % (table, keys, condition)
        try:
            self.cur.execute(sql, tuple(data.values()))
            self.db.commit()
            self.cur.close()
        except Exception as e:
            print(e)
            self.db.rollback()

    def delete(self, table, condition):
        self.connect()
        sql = 'delete from %s where %s' % (table, condition)
        try:
            self.cur.execute(sql)
            self.db.commit()
            self.cur.close()
        except Exception as e:
            print(e)
            self.db.rollback()

    def select(self, table, condition='', fields='*', order='id desc'):
        self.connect()
        sql = 'select %s from %s' % (fields, table)
        if condition:
            sql = '%s where %s' % (sql, condition)
        if order:
            sql = '%s order by %s' % (sql, order)
        try:
            self.cur.execute(sql)
            res = self.cur.fetchall()
            self.cur.close()
            return res
        except Exception as e:
            print(e)
            self.db.rollback()
            
    def count_rows(self, table, condition=''):
        self.connect()
        sql = 'select count(*) from %s' % (table,)
        if condition:
            sql = '%s where %s' % (sql, condition)
        try:
            self.cur.execute(sql)
            res = self.cur.fetchone()
            self.cur.close()
            return res
        except Exception as e:
            print(e)
            self.db.rollback()