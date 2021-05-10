import pymysql.cursors

def select():
    conn = pymysql.connect(host='localhost', user='sh', password='921292', db='namecards', charset='utf8')
    cursor = conn.cursor()
    sql = "select *from card"
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    print(rows)
    return rows

def select_name():
    conn = pymysql.connect(host='localhost', user='sh', password='921292', db='namecards', charset='utf8')
    cursor = conn.cursor()
    sql = "select name from card"
    cursor.execute(sql)
    name = cursor.fetchone()
    conn.close()
    return name



def insert(image,info):
    conn = pymysql.connect(host='localhost', user='sh', password='921292', db='namecards', charset='utf8')
    cursor = conn.cursor()
    sql = "INSERT INTO card VALUES (%s, %s, %s, %s)"
    cursor.execute(sql,(image, info[0], info[1], info[2]))
    conn.commit()
    conn.close()
