from milvus import default_server
from pymilvus import connections, utility

# Optional, if you want store all related data to specific location
# default it wil using:
#   %APPDATA%/milvus-io/milvus-server on windows
#   ~/.milvus-io/milvus-server on linux
default_server.set_base_dir('milvus_data')

# Optional, if you want cleanup previous data
default_server.cleanup()

# star you milvus server
default_server.start()

print(default_server.listen_port)

# Now you could connect with localhost and the port
# The port is in default_server.listen_port
# connections.connect(host='127.0.0.1', port=default_server.listen_port)

# https://github.com/milvus-io/milvus-lite

with default_server:
    connections.connect(host='localhost', port=default_server.listen_port)
    print(utility.get_server_version())

# ============================================

# The above lines only can work in Linux.
# In Windows, Use this link, https://github.com/matrixji/milvus/releases.

