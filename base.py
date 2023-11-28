import mysql.connector

#------------------------mysql連線------------------------------
connection = mysql.connector.connect(host='127.0.0.1',
                                   port='3306',
                                   user='root',
                                   password='hdsfysfbskj',
                                   autocommit=True)  # 啟用自動提交
cursor = connection.cursor(dictionary=True)  # 確定使用
cursor.execute("USE whale_base;")  # 使用whale_base資料庫
cursor.execute("DROP TABLE IF EXISTS test")#刪除表格
#---------------------創建資料庫------------------------------
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS test (
#         ID INT AUTO_INCREMENT PRIMARY KEY,
#         Ts TIMESTAMP,
#         Open FLOAT,
#         High FLOAT,
#         Low FLOAT,
#         Close FLOAT,
#         Volume INT,
#         Amount FLOAT
#     )
# """)
cursor.close()
connection.close()