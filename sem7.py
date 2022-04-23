#7 sqlite


#def foo(items:list[tuple[str,str]])->str # описание функций надо подробнее


import sqlite3
con = sqlite3.connect('works.sqlite')
cur = con.cursor()
def dict_factory(cursor,row):
    d = {}
    for idx,col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

con.row_factory = dict_factory #преобразование в другие типы
#запросы на подсчет строк
print(cur.execute('''SELECT COUNT(*) FROM WORKS''').fetchall()) #fetchall() выдает нам список
res = cur.execute("SELECT * FROM WORKS LIMIT 2;")
print(list(res))
res = cur.execute("SELECT count(*) AS NUM FROM WORKS;")
print(list(res))
res = cur.execute("SELECT *  FROM WORKS LIMIT?;", (1,))# ВМЕСТО ? параметр подставит
print(list(res))
