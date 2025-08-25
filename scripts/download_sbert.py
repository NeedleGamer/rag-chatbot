# scripts/download_sbert.py
from sentence_transformers import SentenceTransformer
from src.config.settings import settings
model_id = "sentence-transformers/all-MiniLM-L6-v2"  # small, reliable
# cache_folder is supported by SentenceTransformer
SentenceTransformer(model_id, cache_folder=str(settings.DATA_DIR / "hf_home"))
print("downloaded:", model_id)
print("OK")