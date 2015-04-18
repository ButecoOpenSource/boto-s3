from boto.s3.connection import S3Connection
from boto.s3.key import Key

conn = S3Connection()
bucket = conn.get_bucket('meu_bucket')
k = Key(bucket)
k.key = 'arquivo.txt'
k.set_contents_from_filename('arquivo.txt')
