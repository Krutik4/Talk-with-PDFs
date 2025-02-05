# Talk-with-PDFs - Document Database and Query System

A Python-based system for managing and querying a document database. It uses **Chroma** as the backend and a **language model** for natural language queries.

---

## Features

- **Database Population:**  
  Load PDF documents, split into manageable chunks, and store them in a Chroma database with unique IDs. Avoids duplicates during updates.

- **Interactive Querying:**  
  Perform semantic searches on documents and generate natural language answers using a language model.

---

## File Overview

### `populate_database.py`  
Loads, splits, and stores PDF data in a Chroma database. Use `--reset` to clear the database before repopulating.  
**Run:**  
```bash
python populate_database.py [--reset]
```

### `query_data.py`  
Interactive CLI to query the database and get answers using the language model.  
**Run:**  
```bash
python query_data.py
```

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Krutik4/Talk-with-PDFs.git
   cd Talk-with-PDFs
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add PDFs to the `data` directory.
4. Populate the database:
   ```bash
   python populate_database.py --reset
   ```
5. Query the database:
   ```bash
   python query_data.py
   ```

---
## Credits

This project was built with the help of the following resource:

- https://www.youtube.com/watch?v=2TJxpyO3ei4

This video provided valuable insights into building a Retrieval-Augmented Generation (RAG) system, which helped shape the implementation of this project.

---

## License

Licensed under the MIT License. See `LICENSE` for details.
