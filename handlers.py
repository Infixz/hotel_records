"""handler set"""
# coding: utf-8
import urllib
import json

import tornado.web as web
import tornado.gen as gen
import tornado.websocket as websocket
import tornado.httpclient as httpclient
import pymysql
# from models import tndb
import tasks

class IndexHandler(web.RequestHandler):
    """handler for index"""
    def get(self):
        # greeting = self.get_argument('greeting', 'hello')
        # self.write(greeting+',friendly user!')
        self.render('index.html',
                    page_title="Resume | Home",
                    header_text="Nav should be set in here")
    def write_error(self, status_code, **kwargs):
        self.write("<h1>You caused a %d error.</h>" % status_code)

# hotel_records
class HotelRecordsIntro(web.RequestHandler):
    """GET return intro page,and the enterance of querying records"""
    def get(self):
        self.render('record_intro.html',
                    page_title="开房记录-chengs.site",
                    header_text="2000W条开房记录")


class HotelRecordsQuery(web.RequestHandler):
    """qureying"""
    @gen.coroutine
    def get(self):
        name = self.get_argument('Name', None)
        gender = self.get_argument('Gender', None)
        ctfid = self.get_argument('CtfId', None)
        mobile = self.get_argument('Mobile', None)
        if not (name or gender or ctfid or mobile):
            self.set_status(403)
            self.render('record_query.html',
                        page_title="开房记录-chengs.site",
                        header_text="你的查询请求 is a bad request",
                        result=None)
        else:
            result = yield tasks.get_db_record(name)
            self.render('record_query.html',
                        page_title="Querying result",
                        header_text="查询结果如下",
                        result=result)


class QueryBoxModule(web.UIModule):
    def render(self):
        return self.render_string('modules/querybox.html')


class RecordFieldModule(web.UIModule):
    def render(self):
        return self.render_string('modules/record-field.html')


class RecordItemModule(web.UIModule):
    def render(self, result):
        return self.render_string('modules/record-item.html', result=result)


# async trans trying
class Trans(web.RequestHandler):
    @web.asynchronous
    @gen.engine
    def get(self):
        query = self.get_argument('q')
        type(query)
        url = 'http://fanyi.youdao.com/openapi.do?keyfrom=sorrible&key=1660616686&type=data&doctype=json&version=1.1&q='+query
        client = httpclient.AsyncHTTPClient()
        resp = yield gen.Task(client.fetch, url)
        result = resp.body
        self.write(result)
        self.finish()


# online chat
class Chat(web.RequestHandler):
    pass


class ChatHandler(websocket.WebSocketHandler):
    pass
