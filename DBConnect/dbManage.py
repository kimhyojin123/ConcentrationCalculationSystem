import pymysql
from openpyxl import Workbook
from openpyxl import load_workbook

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
    def select_all_to_excel(self):
        try:
            with self.conn.cursor() as curs:
                sql = "select * from concentration"
                curs.execute(sql)
                rs = curs.fetchall()
 
                wb = Workbook()
                ws = wb.active
 
                #첫행 입력
                ws.append(('학번','이름','출석확인메시지','시선 벗어남', '웃음감지','자리벗어남','가점','총 집중도 점수'))
 
                #DB 모든 데이터 엑셀로
                for row in rs:
                    ws.append(row)
 
                wb.save('C:/Users/XNOTE/Documents/GitHub/ConcentrationCalculationSystem/집중도 리스트.xlsx')
        finally:
            self.conn.close()
            wb.close()

# conn=pymysql.connect(host='127.0.0.1', user='root', password='dPdms7942', db='concentration', port=3300,charset='utf8')
# cur=conn.cursor()

# sql="CREATE TABLE IF NOT EXISTS userTable(id char(4), userName char(10), email char(15), birthYear int)"
# cur.execute(sql)

# conn.commit()
# conn.close()