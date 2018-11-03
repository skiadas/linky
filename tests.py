from main import app, db
from utils import makeBucketId, md5

session = db.session

BUCKET_ID = makeBucketId()
BUCKET_PASSWORD = "myPassword"
PASSWORD_HASH = md5(BUCKET_PASSWORD)

# ADD YOUR DB TESTS HERE
assert(len(db.getBuckets()) == 0)
db.addBucket()






# ADD YOUR API TESTS HERE
