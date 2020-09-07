# -*- coding:utf-8 -*-
import pymysql


class ConnectSql():
    def __init__(self, host, user, password, database, port):
        self.host = host
        self.user = user
        self.passwd = password
        self.dbName = database
        self.port = port

    def connect(self):
        self.db = pymysql.connect(self.host, self.user, self.passwd, self.dbName, self.port)
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self, sql):
        res = None
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
        except Exception as e:
            print(e)
            print("查询失败")
        finally:
            self.close()
        return res

    def get_all(self, sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
        except Exception as e:
            print(e)
            print("查询失败")
        finally:
            self.close()
        return res

    # 自己再加的
    def get_all_obj(self, sql, tableName, *args):
        res = []
        filedList = []
        if (len(args) > 0):
            for item in args:
                filedList.append(item)
        else:
            filedSql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '%s' and table_schema = '%s'" % (
                tableName, self.dbName)
            fileds = self.get_all(filedSql)
            for item in fileds:
                filedList.append(item[0])

        # 执行查询结果数据sql
        res = self.get_all(sql)
        resList = []
        for item in res:
            obj = {}
            count = 0
            for x in item:
                obj[filedList[count]] = x
                count += 1
            resList.append(obj)

        return resList

    def insert(self, sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            print("插入数据成功")
            self.db.commit()
        except Exception as e:
            print(e)
            print("插入数据失败")
            self.db.rollback()
        finally:
            self.close()
        return count

    def update(self, sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            print("数据更新成功")
            self.db.commit()
        except Exception as e:
            print(e)
            print("数据更新失败")
            self.db.rollback()
        finally:
            self.close()
        return count

    def delete(self, sql):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql)
            print("删除数据成功")
            self.db.commit()
        except Exception as e:
            print(e)
            print("数据删除失败")
            self.db.rollback()
        finally:
            self.close()
        return count


if __name__ == '__main__':
    s = SunckSql(host="xxx", user='xxx', password='xxx', database='xx', port=xx)
    # res = s.get_all("select * from ce")
    # for row in res:
    #     print("%d----%s" % (row[0], row[1]))
    # s.delete("delete from ceshi where id=10")
    # s.insert("insert into bk values (3,'bk')")
    # t=s.get_one("select * from bk where id=15")
    # print(t)
    # s.update("update bk set name='hg1' where id=3")
    s.delete("delete from bk where id=3")
