import MySQLdb
connector = MySQLdb.connect(
    host="hostname", 
    db="database", 
    user="user", 
    passwd="yourpassword", 
    charset="utf8"
);
for line in open("kankore_result.txt","r"):
    ln = line[:-1].split('\t')
    cursor=connector.cursor();
    print ln
    sql = u"insert into tmp_kankore values(%s, '%s')" % (ln[0], unicode(ln[1],"utf-8").replace("\'","\\'"))
    cursor.execute(sql);
connector.commit()
