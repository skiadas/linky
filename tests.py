from main import app, db
from utils import makeId, getHash

session = db.session

BUCKET_ID = makeId()
BUCKET_PASSWORD = "myPassword"
PASSWORD_HASH = getHash(BUCKET_PASSWORD)
SHORTCUT_HASH = "mountains"
LINK = "https://en.wikipedia.org/wiki/List_of_mountains_by_elevation"
DESCR = "List of mountains by elevation"

print("################    DB TESTS   ###################")
# Provided DB tests
## No buckets to begin with
assert(len(db.getBuckets()) == 0)
## Adding a bucket
db.addBucket(id=BUCKET_ID, passwordHash = PASSWORD_HASH)
assert(len(db.getBuckets()) == 1)
bucket = db.getBucket(BUCKET_ID)
assert(bucket is not None)
assert(bucket.id == BUCKET_ID)
assert(bucket.passwordHash == PASSWORD_HASH)
assert(db.getBucket(BUCKET_ID + "bah") is None)
assert(db.getBuckets()[0] is bucket)
db.commit()
## Deleting the bucket
db.deleteBucket(bucket)
bucket = db.getBucket(BUCKET_ID)
assert(bucket is None)
db.commit()
## Re-adding the bucket to use in further tests
bucket = db.addBucket(id=BUCKET_ID, passwordHash = PASSWORD_HASH)
## Adding a shortcut
shortcut = db.addShortcut(SHORTCUT_HASH, bucket, LINK, DESCR)
assert(shortcut is not None)
assert(shortcut.linkHash == SHORTCUT_HASH)
assert(shortcut.bucket is bucket)
assert(shortcut.link == LINK)
assert(shortcut.description == DESCR)
assert(len(bucket.shortcuts) == 1)
assert(bucket.shortcuts[0] is shortcut)
assert(shortcut.bucket is bucket)
## Testing shortcut get
assert(db.getShortcut(SHORTCUT_HASH, bucket) is shortcut)
assert(db.getShortcut("Boo", bucket) is None)
db.commit()
## Testing shortcut delete
db.deleteShortcut(shortcut)
assert(db.getShortcut(SHORTCUT_HASH, bucket) is None)
shortcut = db.addShortcut(SHORTCUT_HASH, bucket, LINK, DESCR)
db.commit()
# ADD YOUR DB TESTS HERE
# OR USE THESE LINES TO JUST ADD MORE BUCKETS AND/OR SHORTCUTS TO THE DATABASE


print("################ DB TESTS DONE ###################")
# Provided API tests
print("################   API TESTS   ###################")

# ADD YOUR API TESTS HERE
