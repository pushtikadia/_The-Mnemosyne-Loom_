# 🧠 THE MNEMOSYNE LOOM

![Backend](https://img.shields.io/badge/Backend-Python_Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![AI Engine](https://img.shields.io/badge/Intelligence-BERT_Transformers-FFD700?style=for-the-badge&logo=huggingface&logoColor=black)
![Frontend](https://img.shields.io/badge/Frontend-WebGL_&_3D-F7DF1E?style=for-the-badge&logo=webgl&logoColor=black)
![Design](https://img.shields.io/badge/Design-Digital_Steampunk-A0522D?style=for-the-badge&logo=css3&logoColor=white)

**The Mnemosyne Loom** is a specialized cognitive mapping engine that demonstrates **Semantic AI** integration. It orchestrates a high-performance **Python (Flask)** backend that uses **BERT Transformers** to analyze human thought patterns, creating a self-organizing **3D Knowledge Graph** fronted by a vintage, Victorian-era terminal interface.

---

## ⚡ Key Features

* **🧠 Semantic Intelligence:** A neural search engine that analyzes natural language input (e.g., *"The stars are beautiful today"*) to extract meaning and context using `sentence-transformers`, going beyond simple keyword matching.
* **🕸️ Auto-Associative Graph:** Features a "Golden Thread" logic where the AI automatically detects connections between unrelated user inputs based on vector similarity, forging links in real-time.
* **🕰️ Digital Steampunk UI:** A highly stylized interface utilizing custom CSS variables, CRT scanline effects, and vintage typography (`Special Elite`, `Cinzel`) to evoke the feeling of a 19th-century supercomputer.
* **🚀 3D Visualization:** A reactive WebGL frontend using `3d-force-graph` that renders the "Hive Mind" as a rotatable, interactive constellation of glowing nodes.
* **💾 Persistent Archive:** A server-less architecture using **SQLite** to permanently store high-dimensional vector embeddings and user lineage data.

---

## 🛠️ Tech Stack

* **Server Core:** Python 3.10+ (Flask Web Framework)
* **AI Module:** HuggingFace `sentence-transformers` (BERT)
* **Frontend Engine:** HTML5, CSS3 (Custom Variables), JavaScript (WebGL)
* **Data Structure:** SQLite3 Relational Database
* **Math Engine:** Scikit-Learn & NumPy (Cosine Similarity)

---

## 🚀 Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/yourusername/brass-synapse.git](https://github.com/yourusername/brass-synapse.git)
    cd brass-synapse
    ```

2.  **Verify Prerequisites**
    * Ensure **Python 3.x** is installed.
    * Install the neural network dependencies:
    ```bash
    pip install flask sentence-transformers scikit-learn numpy
    ```

3.  **Initialize the Archive**
    * Run the database builder to generate the `synapse.db` file.
    ```bash
    python database_setup.py
    ```

4.  **Ignite the Server**
    * The system will download the AI models on the first run (approx. 10-20s).
    ```bash
    python app.py
    ```

5.  **Launch**
    * Open your browser and navigate to the terminal:
    * `http://127.0.0.1:5000`

---

## 🧩 System Architecture

**1. The Transmission (Input & Vectorization):**
Unlike standard forms, the input terminal acts as a "Neural Injector." When an operative submits a thought, Python intercepts the text and passes it through the **BERT Transformer**. This converts the abstract sentence into a **384-dimensional vector** array.

**2. The Synaptic Weaver (Similarity Engine):**
Before saving, the system performs a mathematical handshake. It retrieves all existing memory vectors from the `nodes` table and calculates the **Cosine Similarity** against the new input. If the angle between thoughts is sufficiently close (> 40%), a relationship is forged in the `links` table.

**3. The Visual Core (WebGL Projection):**
The frontend creates a dynamic **Force-Directed Graph**. It polls the `/graph_data` endpoint and renders nodes as glowing spheres. Relationships are visualized as "Golden Threads" for high-similarity matches and "Iron Cables" for structural links, creating an immersive, living data structure.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
<p align="center">
  <b> The Mnemosyne Loom </b> • Forging Thought into Matter
</p>

---

<p align="center">
  <b>The Mnemosyne Loom</b> • Created by <a href="https://github.com/pushtikadia"><b>Pushti Kadia</b></a>
</p>
