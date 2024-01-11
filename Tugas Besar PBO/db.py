import mysql.connector as mc


class DBConnection:

    def __init__(self):
        self.host = "localhost"
        self.port = 3306
        self.name = "mytabungan"
        self.user = "root"
        self.password = ""
        self.conn = None
        self.cursor = None
        self.result = None
        self.connected = False
        self.affected = 0
        self.connect()

    @property
    def connection_status(self):
        return self.connected

    def connect(self):
        try:
            self.conn = mc.connect(host=self.host,
                                   port=self.port,
                                   database=self.name,
                                   user=self.user,
                                   password=self.password)

            self.connected = True
            self.cursor = self.conn.cursor()
        except mc.Error as e:
            self.connected = False
        return self.conn

    def disconnect(self):
        if (self.connected == True):
            self.conn.close
        else:
            self.conn = None

    def create_table_menabung_uang(self):
        self.connect()
        try:
            # Membuat query untuk membuat tabel menabung_uang
            query = '''
            CREATE TABLE IF NOT EXISTS menabung_uang (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nama VARCHAR(100) NOT NULL,
                saldo DECIMAL(10, 2) DEFAULT 0
            )
            '''

            # Eksekusi query
            self.cursor.execute(query)
            self.conn.commit()
            print("Tabel 'menabung_uang' berhasil dibuat.")
        except mc.Error as e:
            print(f"Error creating table: {e}")

    @property
    def info(self):
        if (self.connected == True):
            return "Server is running on " + self.host + ' using port ' + str(self.port)
        else:
            return "Server is offline."


db = DBConnection()

# Create the table
db.create_table_menabung_uang()
