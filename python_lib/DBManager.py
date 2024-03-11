import cx_Oracle


class DBManager:
    def __init__(self):
        self.conn = None
        self.get_connection()

    def get_connection(self):
        self.conn = cx_Oracle.connect("study", "study", "Localhost:1521/xe")
        print("접속됨.")
        return self.conn

    def __del__(self):
        try:
            print("소멸자")
            if self.conn:
                self.conn.close()
                print("접속을 종료함.")
        except Exception as e:
            print("__del__", str(e))

    def insert(self, query, param):
        cursor = self.conn.cursor()
        cursor.execute(query, param)
        self.conn.commit()
        cursor.close()
if __name__ == '__main__':
    db = DBManager()