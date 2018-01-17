from json import dumps
from sqlite3 import connect

c = connect('HITODB.db').cursor()
print(c)
count = 0
datas = c.execute('SELECT HITO, SOURCE FROM HITOKOTO').fetchall()
with open('../hitodb.js', 'w+') as hito:
    # hito.write('[')
    # for x in datas:
    #     s = '["{}","{}"]'.format(x[0], x[1])
    #     hito.write(s)
    #     if x != datas[-1]:
    #         hito.write(',\n')
    # hito.write(']')
    hito.write(
        "var hito={}; function gethito() {{item=hito[Math.floor(Math.random()*hito.length)];document.write(item[0]+'&#10;——「'+item[1]+'」');}}".
        format(dumps(datas, ensure_ascii=False)))
