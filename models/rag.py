import faiss
import numpy as np
from models.embedding import get_image_embedding, get_text_embedding
from ingest.utils import list_files_recursive

# Simple in-memory DB for demo
db = {}

def index_document(doc_id, image_paths, texts):
    # Compute embeddings
    vectors = []
    meta = []
    for img, txt in zip(image_paths, texts):
        img_emb = get_image_embedding(img)
        txt_emb = get_text_embedding(txt)
        combined = np.concatenate([img_emb, txt_emb])
        vectors.append(combined)
        meta.append({"image": img, "text": txt})
    vectors = np.stack(vectors)
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    db[doc_id] = {"index": index, "meta": meta}

def multimodal_query(doc_id, query):
    if doc_id not in db:
        # For demo: index on-the-fly
        from ingest.utils import list_files_recursive
        image_paths = list_files_recursive(f"data/samples/{doc_id}/slides", ".jpg") or \
                      list_files_recursive(f"data/samples/{doc_id}/frames", ".jpg")
        # Dummy: Assume 1:1 with empty text
        texts = [""] * len(image_paths)
        index_document(doc_id, image_paths, texts)
    qvec = np.concatenate([get_image_embedding(image_paths[0])*0, get_text_embedding(query)])
    D, I = db[doc_id]["index"].search(np.expand_dims(qvec, axis=0), k=3)
    results = []
    for idx in I[0]:
        results.append(db[doc_id]["meta"][idx])
    return results
