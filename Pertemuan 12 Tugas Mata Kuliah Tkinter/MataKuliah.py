from db import DBConnection as mydb


class MataKuliah:
    def __init__(self):
        self.__id = None
        self.__kodemk = None
        self.__mk = None
        self.__sks = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def kodemk(self):
        return self.__kodemk

    @kodemk.setter
    def kodemk(self, value):
        self.__kodemk = value

    @property
    def mk(self):
        return self.__mk

    @mk.setter
    def mk(self, value):
        self.__mk = value

    @property
    def sks(self):
        return self.__sks

    @sks.setter
    def sks(self, value):
        self.__sks = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kodemk, self.__mk, self.__sks)
        sql = "INSERT INTO matakuliah (kodemk, namamk, sks) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect()
        return self.affected

    def updateByKodeMk(self, kodemk):
        self.conn = mydb()
        val = (self.__mk, self.__sks)
        sql = "UPDATE matakuliah SET namamk = %s, sks = %s WHERE kodemk ='" + \
            str(kodemk) + "'"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM matakuliah WHERE id = %s"
        self.affected = self.conn.delete(sql, (id,))
        self.conn.disconnect()
        return self.affected

    def deleteByKodeMk(self, kodemk):
        self.conn = mydb()
        sql = "DELETE FROM matakuliah WHERE kodemk='" + str(kodemk) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM matakuliah WHERE id = %s"
        self.result = self.conn.findOne(sql, (id,))
        if self.result:
            self.__kodemk = self.result[1]
            self.__mk = self.result[2]
            self.__jk = self.result[3]
        else:
            self.__kodemk = ''
            self.__mk = ''
            self.__jk = ''
        self.conn.disconnect()
        return self.result

    def getByKodeMk(self, kodemk):
        a = str(kodemk)
        b = a.strip()
        self.conn = mydb()
        print(b)
        sql = "SELECT * FROM matakuliah WHERE kodemk='" + b + "'"
        self.result = self.conn.findOne(sql)
        if (self.result != None):
            self.__kodemk = self.result[1]
            self.__mk = self.result[2]
            self.__sks = self.result[3]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kodemk = ''
            self.__mk = ''
            self.__sks = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM matakuliah"
        self.result = self.conn.findAll(sql)
        return self.result
