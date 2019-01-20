from server import server
from app1 import app as app1
from app2 import app as app2
app1.enable_dev_tools(debug=True)
app2.enable_dev_tools(debug=True)


