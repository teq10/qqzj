import os.path
from tornado.options import define

define("port", default=9001, help="run on given port",type=int)
define("mysql_host", default="teq6.com", help="mysql_host", type=str)
define("mysql_database", default="qqzj", help="mysql_database", type=str)
define("mysql_user", default="root", help="mysql_user", type=str)
define("mysql_password", default="123456", help="mysql_password", type=str)

settings = {}

# system path
settings['root_path'] = os.path.join(os.path.dirname(__file__), "")
settings['template_path'] = os.path.join(settings['root_path'], "template")
settings['static_path'] = os.path.join(settings['root_path'], "static")
settings['upload_path'] = os.path.join(settings['static_path'], "upload")
