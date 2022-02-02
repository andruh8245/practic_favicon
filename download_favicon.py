import urllib.request

import pickle, binascii,sys, requests

from PIL import Image
 

try:

    paramsUrl = sys.argv[1]

except IndexError:

    print("Parameter not specified")

    sys.exit(1)

 

webUrl = 'http://www.google.com/s2/favicons?domain={}'.format(paramsUrl)

 

try:

    resp = requests.get(webUrl, stream=True).raw

except requests.exceptions.RequestException as e:

    sys.exit(1)

 

try:

    img = Image.open(resp)

except IOError:

    print("Unabe to open image")

    sys.exit(1)

 
img.save('1.png','png')