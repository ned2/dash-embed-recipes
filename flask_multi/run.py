from server import server
from app1.app1 import app as app1
from app2.app2 import app as app2

if __name__ == '__main__':
    app1.enable_dev_tools(debug=True)
    app2.enable_dev_tools(debug=True)
    server.run(debug=True)
