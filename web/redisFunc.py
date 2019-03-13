import datetime
import time
import redis


class redisConn:
    def __init__(self):
        self.pool = redis.ConnectionPool(host="140.143.149.154", port=6370)
        self.r = redis.Redis(connection_pool=self.pool)

    def addBlogInfo(self, title, author):
        id = self.mkId()
        print(id)
        self.r.hmset(id, {'author': author, 'title': title})
        return True

    def getBlogInfo(self, id):
        author = self.r.hget(id, 'author')
        title = self.r.hget(id, 'title')
        d = {}
        d['author'] = author.decode()
        d['title'] = title.decode()
        print(d)
        return d

    def mkId(self, userId=9):
        return str(userId) + '_' + str(int(time.mktime(datetime.datetime.now().timetuple())))
