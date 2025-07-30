# Multimodal RAG for Image + Text Search

This repository implements a Multimodal Retrieval-Augmented Generation (RAG) system allowing users to search for specific content in YouTube videos or PDF decks using natural language queries. For example:  
> “Find me the slide where person X talks about success in life.”

The system combines image (slide/video frame) and text (speech/slide text) representations, enabling semantic search and retrieval across modalities.

---

## Features

- **Video & PDF Ingestion:** Automatically extracts frames, slides, and associated text from YouTube videos and PDF decks.
- **Multimodal Embeddings:** Uses vision-language models to generate joint embeddings for frames/slides and text.
- **RAG Pipeline:** Natural language queries are used to retrieve relevant slide/frame + transcript pairs.
- **Simple Web UI:** Users can upload content, run queries, and view results interactively.

---

## Folder Structure

```
multimodal-rag/
│
├── app/
│   ├── main.py          # FastAPI app serving endpoints and UI
│   └── templates/
│       └── index.html   # Simple HTML web interface
│
├── data/
│   └── samples/         # Example videos, PDFs, and processed outputs
│
├── ingest/
│   ├── video_ingest.py  # Extracts frames & transcripts from YouTube videos
│   ├── pdf_ingest.py    # Extracts slides & text from PDFs
│   └── utils.py         # Shared helpers
│
├── models/
│   ├── embedding.py     # Loads and applies multimodal embedding models
│   └── rag.py           # Retrieval & generation pipeline logic
│
├── requirements.txt     # Python dependencies
├── Dockerfile           # For easy deployment
├── .gitignore
└── README.md
```

---

## Quickstart

1. **Clone the repo and install dependencies**
    ```bash
    git clone https://github.com/Ahmad-Khalil-LEEA/multimodal-rag.git
    cd multimodal-rag
    pip install -r requirements.txt
    ```

2. **Run the app**
    ```bash
    uvicorn app.main:app --reload
    ```

3. **Open the UI**  
    Go to `http://localhost:8000` in your browser.

---

## Technologies

- **Python 3.10+**
- **FastAPI** for serving the API and UI
- **PyPDF2, OpenCV, ffmpeg** for data extraction
- **HuggingFace Transformers & CLIP** for multimodal embeddings
- **FAISS** for similarity search
- **TTS/STT APIs** for transcript extraction (YouTube)

---

## Example Usage

- Upload a YouTube video or PDF deck.
- Ask: _“Find me the slide where person X talks about success in life”._
- Get: The relevant slide/frame, timestamp, and matching transcript.

---

## TODO

- [ ] Add support for more vision-language models
- [ ] Improve UI for displaying results
- [ ] Add batch processing and storage options

---

## License

MIT License
