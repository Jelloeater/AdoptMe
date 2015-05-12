import sys
from app import app
import logging
logging.basicConfig(format="[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(lineno)s)",
                    level=logging.DEBUG)
app.run(host='0.0.0.0', port=80, debug=True)

