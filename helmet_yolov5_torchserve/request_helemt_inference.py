import matplotlib.pyplot as plt
import tempfile
from six.moves.urllib.request import urlopen
from six import BytesIO
import requests
import numpy as np
import numpy as np
from PIL import Image
from PIL import ImageOps
from IPython.core.display import HTML
import io
import json

# Access fastrcnn by restful API
url="http://10.186.99.223:20011/predictions/helmet_detection"


image_path = './man.jpg'


def make_request(url, image_path):
    headers = {
        'Content-Type': 'image/jpeg'
    }
    
    with open(image_path, "rb") as image:
        f = image.read()
        payload = bytearray(f)
        
    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)

detections = make_request(url, image_path)

print(json.dumps(detections, indent=4))

Selection deleted
import matplotlib.pyplot as plt
import tempfile
from six.moves.urllib.request import urlopen
from six import BytesIO
import requests
import numpy as np
import numpy as np
from PIL import Image
from PIL import ImageOps
from IPython.core.display import HTML
import io
import json

# Access fastrcnn by restful API
url="http://10.186.99.223:20011/predictions/helmet_detection"


image_path = './man.jpg'


def make_request(url, image_path):
    headers = {
        'Content-Type': 'image/jpeg'
    }
    
    with open(image_path, "rb") as image:
        f = image.read()
        payload = bytearray(f)
        
    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)

detections = make_request(url, image_path)

print(json.dumps(detections, indent=4))

Selection deleted
import matplotlib.pyplot as plt
import tempfile
from six.moves.urllib.request import urlopen
from six import BytesIO
import requests
import numpy as np
import numpy as np
from PIL import Image
from PIL import ImageOps
from IPython.core.display import HTML
import io
import json

# Access fastrcnn by restful API
url="http://10.186.99.223:20011/predictions/helmet_detection"


image_path = './man.jpg'


def make_request(url, image_path):
    headers = {
        'Content-Type': 'image/jpeg'
    }
    
    with open(image_path, "rb") as image:
        f = image.read()
        payload = bytearray(f)
        
    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)

detections = make_request(url, image_path)

print(json.dumps(detections, indent=4))
# the output is
# [
#     {
#         "x1": 0.3336566090583801,
#         "y1": 0.003293550107628107,
#         "x2": 0.49829187989234924,
#         "y2": 0.24848513305187225,
#         "type": "wcaqm",
#         "value": "1",
#         "conf": 0.8556397557258606,
#         "label": "No wear hat"
#     }
# ]