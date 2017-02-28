"""define http_server or app.listen"""
# coding: utf-8

import tornado.httpserver
import tornado.ioloop as ioloop
import tornado.options

from tornado.options import define, options
define("port", default=8080, help='run on given port', type=int)

from app import App

if __name__ == "__main__":
    """
    if setting.IPV4_ONLY:
        import socket
        sockets = bind_socket(80, famimly=socket.AF_INET)
    else:
        sockets = bind_socket(80)
    if not setting.DEBUG_MODE:
        import tornado.process
        tornado.process.fork_processes(0)
    """
    tornado.options.parse_command_line()
    App().listen(options.port)
    ioloop.IOLoop.current().start()
