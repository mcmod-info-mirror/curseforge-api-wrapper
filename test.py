from curseforge_api_wrapper import *

client = Client(api_key="$2a$10$2DOXBr1x82Acn1A6GGw5b.psdLVOo29u5gEahTQSiGYmDOp2QXFSu")

res = client.search_mods(gameId=432, pageSize=1, searchFilter="fabric-api")

pass
