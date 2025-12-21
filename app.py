import sqlite3
import json
import numpy as np
from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# --- Load the AI Model ---
print("⚙️  Igniting Neural Engine... (Please wait)")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("✓ Engine Online.")

def get_db():
    conn = sqlite3.connect('synapse.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transmit', methods=['POST'])
def transmit():
    data = request.json
    text = data.get('text', '')
    author = data.get('author', 'Unknown Agent')

    if not text: return jsonify({"status": "error"}), 400

    # 1. AI Analysis: Convert text to math
    vector = model.encode(text).tolist()
    vector_json = json.dumps(vector) # Store as string
    
    # Generate unique IDs
    memory_id = f"MEM_{np.random.randint(10000, 99999)}"
    
    conn = get_db()
    cursor = conn.cursor()

    # 2. Insert Nodes (Author & Memory)
    # Insert Author (Ignore if already exists)
    cursor.execute("INSERT OR IGNORE INTO nodes (id, label, group_type, val, vector_data) VALUES (?, ?, ?, ?, ?)", 
                   (author, author, 'author', 20, ''))
    
    # Insert Memory
    cursor.execute("INSERT INTO nodes (id, label, group_type, val, vector_data) VALUES (?, ?, ?, ?, ?)", 
                   (memory_id, text, 'memory', 10, vector_json))

    # 3. Create Link: Author -> Memory
    cursor.execute("INSERT INTO links (source, target, color) VALUES (?, ?, ?)", 
                   (author, memory_id, '#555'))

    # 4. AI Semantic Linking (The Magic)
    # Fetch all other memories to compare
    cursor.execute("SELECT id, vector_data FROM nodes WHERE group_type = 'memory' AND id != ?", (memory_id,))
    existing_memories = cursor.fetchall()

    for row in existing_memories:
        try:
            past_vector = json.loads(row['vector_data'])
            # Math: Calculate similarity (0.0 to 1.0)
            similarity = cosine_similarity([vector], [past_vector])[0][0]
            
            # If > 40% similar, create a GOLD link
            if similarity > 0.4:
                cursor.execute("INSERT INTO links (source, target, color) VALUES (?, ?, ?)", 
                               (memory_id, row['id'], '#c5a059')) # Gold color
        except:
            continue

    conn.commit()
    conn.close()
    return jsonify({"status": "success"})

@app.route('/graph_data')
def graph_data():
    conn = get_db()
    
    # Fetch data safely (handle empty DB case)
    try:
        nodes_db = conn.execute("SELECT * FROM nodes").fetchall()
        links_db = conn.execute("SELECT * FROM links").fetchall()
    except sqlite3.OperationalError:
        # If tables don't exist yet
        return jsonify({"nodes": [], "links": []})
        
    conn.close()

    nodes = [{"id": row['id'], "label": row['label'], "group": row['group_type'], "val": row['val']} for row in nodes_db]
    links = [{"source": row['source'], "target": row['target'], "color": row['color']} for row in links_db]

    return jsonify({"nodes": nodes, "links": links})

if __name__ == '__main__':
    # This 0.0.0.0 allows it to be accessed, but 127.0.0.1 is standard for local
    app.run(debug=True, port=5000)