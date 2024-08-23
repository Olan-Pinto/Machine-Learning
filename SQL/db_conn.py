import mysql.connector

class CUB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost',username='root',password='',database='sql_practice') #establishes connection
            self.mycursor = self.conn.cursor() #can talk to the database
        except:
            print("Something went wrong")
        else:
            print("Connection Established!!")
    def registration(self,email,password):
        try:
            self.mycursor.execute("""
            INSERT INTO `cub_student` (`student_id`,`student_email`,`student_password`) VALUES (NULL,'{}','{}')
            """.format(email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
    def login_student(self,email,password):
        try:
            self.mycursor.execute("""
                                select student_email,student_id from `cub_student` where student_email='{}' and student_password='{}'
                                """.format(email,password))
            output=self.mycursor.fetchall()
        except:
            return -1
        else:
            return output
