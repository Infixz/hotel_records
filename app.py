"""setting tornado.web.Application"""
import os.path
import tornado.web as web
from handlers import IndexHandler, HotelRecordsIntro, HotelRecordsQuery, \
                    QueryBoxModule, RecordFieldModule, RecordItemModule, \
                    Trans, Chat

class App(web.Application):
    """define Application"""
    def __init__(self):
        handlers = [
            (r'/(favicon.ico)', web.StaticFileHandler, {"path": ""}),
            (r"/", IndexHandler),
            (r'/hotel_records', HotelRecordsIntro),
            (r'/hotel_records/query', HotelRecordsQuery),
            (r'/trans', Trans),
            (r'/onlinechat', Chat)
            ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "statics"),
            ui_modules={'QueryBox': QueryBoxModule,
                        'RecordField': RecordFieldModule,
                        'RecordItem': RecordItemModule
                       },
            debug=True
            )
        web.Application.__init__(self, handlers, **settings)
