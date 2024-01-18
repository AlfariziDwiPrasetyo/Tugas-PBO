import bcrypt
from db import DBConnection as mydb


class Users:
    def __init__(self):
        self.__id = None
        self.__email = None
        self.__nama = None
        self.__password = None
        self.__level = None
        self.__uservalid = None
        self.__passwordvalid = None
        self.__loginvalid = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    @property
    def loginvalid(self):
        return self.__loginvalid

    @loginvalid.setter
    def loginvalid(self, value):
        self.__loginvalid = value

    def cekUsername(self, email):
        self.conn = mydb()
        sql = "SELECT * FROM users WHERE email='" + email + "'"
        self.result = self.conn.findOne(sql)
        if (self.result != None):
            self.__email = self.result[1]
            self.__nama = self.result[2]
            self.__password = self.result[3]
            self.__level = self.result[4]
            self.affected = self.conn.cursor.rowcount
            self.__uservalid = True
        else:
            self.__email = ''
            self.__nama = ''
            self.__password = ''
            self.__level = ''
            self.affected = 0
            self.__uservalid = False
        return self.__uservalid

    def cekPassword(self, password):
        hashedpass = self.__password.encode('utf-8')
        c = password.encode('utf-8')
        d = bcrypt.checkpw(c, hashedpass)
        if (d):
            self.__passwordvalid = True
        else:
            self.__passwordvalid = False
        return self.__passwordvalid

    def Validasi(self, email, password):
        a = self.cekUsername(email)
        if (a == True):
            b = self.cekPassword(password)
            if (b == True):
                self.__loginvalid = True
            else:
                self.__loginvalid = False
        else:
            self.__loginvalid = False

        val = []
        val = [self.__level, self.__loginvalid]
        return val


"""A = Users()
print("\n\n")
print("Username BENAR, dan password BENAR")
B = A.Validasi('nurjati@umc.ac.id', '123')
print(B)

print("\n\nUsername BENAR, dan password SALAH")
C = A.Validasi('nurjati@umc.ac.id', '1234')
print(C)

print("\n\nUsername SALAH, dan password BENAR")
D = A.Validasi('baim@umc.ac.id', '123')
print(D)

print("\n\nUsername SALAH, dan password SALAH")
E = A.Validasi('baim@umc.ac.id', '1234')
print(E)
print("\n\n")
"""
