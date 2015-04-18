#
# Exemplo obtido em: http://boto.readthedocs.org/en/latest/s3_tut.html#storing-large-data
#

import math, os
import boto

# Necessário instalar esta lib caso você não possua
from filechunkio import FileChunkIO

# Conecta ao S3
c = boto.connect_s3()
b = c.get_bucket('meu_bucket')

# Arquivo a ser enviado
source_path = 'path/para/meu/arquivo.mkv'
source_size = os.stat(source_path).st_size

# Cria um request de upload multipart
mp = b.initiate_multipart_upload(os.path.basename(source_path))

# Usa um chunk de 50 MB (altere de acordo com seu desejo)
chunk_size = 52428800
chunk_count = int(math.ceil(source_size / float(chunk_size)))

# Envia as partes do aquivo, usando o FileChunkIO
# para criar um arquivo que aponte para 
# determinadas partes do arquivo original
for i in range(chunk_count):
    offset = chunk_size * i
    bytes = min(chunk_size, source_size - offset)
    with FileChunkIO(source_path, 'r', offset=offset, bytes=bytes) as fp:
        mp.upload_part_from_file(fp, part_num=i + 1)

# Termina o upload
mp.complete_upload()
