# scripts/test_chroma_persist.py
from src.config.settings import settings
import chromadb
from pathlib import Path

db_path = Path(settings.CHROMA_DIR)
client = chromadb.PersistentClient(path=str(db_path))
coll = client.get_or_create_collection("cp13_smoke")

# add tiny docs
coll.add(ids=["1","2"], documents=["hello world", "hola mundo"])

# query
result = coll.query(query_texts=["hello"], n_results=1)
print("query result:", result)

assert db_path.exists(), "CHROMA_DIR folder was not created"
print("chroma persisted at:", db_path)
