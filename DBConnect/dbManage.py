import pymysql

class MysqlController:
    def __init__(self, host, id, pw, db_name,portNumber):
        self.conn=pymysql.connect(host=host, user=id, password=pw, db=db_name,port=portNumber,charset='utf8')
        self.curs=self.conn.cursor()
    def insert_user(self, number, name):
        sql="INSERT into concentration values(%s,%s,%s,%s,%s,%s,%s,%s)"
        self.curs.execute(sql,(number,name,0,0,0,0,0,70))
        self.conn.commit()
    def update_attendMessage(self,number,point,total):
        sql="""UPDATE concentration 
        set attendMessage=%s, totalPoint=%s 
        WHERE studentNumber=%s"""
        self.curs.execute(sql,(point,total,number))
        self.conn.commit()
    def update_outOfSight(self, number,point,total):
        sql="""UPDATE concentration 
        set outOfSight=%s, totalPoint=%s 
        WHERE studentNumber=%s"""
        self.curs.execute(sql,(point,total,number))
        self.conn.commit()
    def update_laughDetection(self,number,point,total):
        sql="""UPDATE concentration 
        set laughDetection=%s, totalPoint=%s 
        WHERE studentNumber=%s"""
        self.curs.execute(sql,(point,total,number))
        self.conn.commit()
    def update_outOfPosition(self, number,point,total):
        sql="""UPDATE concentration 
        set outOfPosition=%s, totalPoint=%s 
        WHERE studentNumber=%s"""
        self.curs.execute(sql,(point,total,number))
        self.conn.commit()
    def update_addPoint(self, number,point,total):
        sql="""UPDATE concentration 
        set addPoint=%s, totalPoint=%s 
        WHERE studentNumber=%s"""
        self.curs.execute(sql,(point,total,number))
        self.conn.commit()

# conn=pymysql.connect(host='127.0.0.1', user='root', password='dPdms7942', db='concentration', port=3300,charset='utf8')
# cur=conn.cursor()

# sql="CREATE TABLE IF NOT EXISTS userTable(id char(4), userName char(10), email char(15), birthYear int)"
# cur.execute(sql)

# conn.commit()
# conn.close()