from db import DBConnection as mydb


class Perawat:
    def __init__(self):
        self.__id = None
        self.__nip = None
        self.__nama = None
        self.__jk = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def nip(self):
        return self.__nip

    @nip.setter
    def nip(self, value):
        self.__nip = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__jk)
        sql = "INSERT INTO perawat (nip, nama, jk) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect()
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__nip, self.__nama, self.__jk, id)
        sql = "UPDATE perawat SET nip = %s, nama = %s, jk = %s WHERE id = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def updateByNIP(self, nip):
        self.conn = mydb()
        val = (self.__nama, self.__jk, self.__nip)
        sql = "UPDATE perawat SET nama = %s, jk = %s WHERE nip = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM perawat WHERE id = %s"
        self.affected = self.conn.delete(sql, (id,))
        self.conn.disconnect()
        return self.affected

    def deleteByNIP(self, nip):
        self.conn = mydb()
        sql = "DELETE FROM perawat WHERE nip='" + str(nip) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM perawat WHERE id = %s"
        self.result = self.conn.findOne(sql, (id,))
        if self.result:
            self.__nip = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
        else:
            self.__nip = ''
            self.__nama = ''
            self.__jk = ''
        self.conn.disconnect()
        return self.result

    def getByNIP(self, nim):
        a = str(nim)
        b = a.strip()
        self.conn = mydb()
        print(b)
        sql = "SELECT * FROM perawat WHERE nip='" + b + "'"
        self.result = self.conn.findOne(sql)
        if (self.result != None):
            self.__nip = self.result[1]
            self.__nama = self.result[2]
            self.__jk = self.result[3]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nip = ''
            self.__nama = ''
            self.__jk = ''
            self.affected = 0
        self.conn.disconnect
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM perawat"
        self.result = self.conn.findAll(sql)
        return self.result
