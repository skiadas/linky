import string
import random
from hashlib import md5

alphabet = string.ascii_uppercase + string.digits

def makeBucketId():
   return ''.join([random.choice(alphabet) for _ in range(6)])

def md5(password):
   return md5(password).hexdigest()
