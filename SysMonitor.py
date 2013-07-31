#!/usr/bin/python2
#import tornado.web
#import tornado.websocket
#import tornado.ioloop
import OsInfo
import json
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.gen
from tornado.options import define, options

clients = []
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("SysMonitor.html")
 
class WebSocketHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		print "New connection"
		clients.append(self)
		self.write_message("connected")

	def on_message(self, message):
		print "Tornado received from client: %s" % message
		self.write_message(u"OK: " + message)

	def on_close(self):
		print 'connection closed'
		clients.remove(self)

def main():
	application = tornado.web.Application([
		(r"/", MainHandler),
		(r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "./static"}),
		(r"/websocket", WebSocketHandler),
	])
	application.listen(8888)
 
	def SysStatus():
		osi=OsInfo.OsInfo()
		dataSystemUsing = json.dumps({"cpu":100 - osi.GetFreeCPU(),"ram":osi.GetUsedMemory(),"swap":osi.GetUsedSwap()})
		print dataSystemUsing
		# Loop for client response
		for c in clients:
			print "-",dataSystemUsing
			c.write_message(unicode(dataSystemUsing))

	mainLoop = tornado.ioloop.IOLoop.instance()
	scheduler = tornado.ioloop.PeriodicCallback(SysStatus, 1000, io_loop = mainLoop)
	scheduler.start()
	mainLoop.start()
	
if __name__ == "__main__":
	main()
