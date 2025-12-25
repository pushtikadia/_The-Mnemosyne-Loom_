import sqlite3

def init_db():
    # Connect to (or create) the database file
    conn = sqlite3.connect('synapse.db')
    c = conn.cursor()
    
    # Table 1: Nodes (Memories & People)
    # We store the AI 'vector' as a text string because SQLite is simple
    c.execute('''
        CREATE TABLE IF NOT EXISTS nodes (
            id TEXT PRIMARY KEY,
            label TEXT,
            group_type TEXT,
            val INTEGER,
            vector_data TEXT 
        )
    ''')

    # Table 2: Links (Connections)
    c.execute('''
        CREATE TABLE IF NOT EXISTS links (
            source TEXT,
            target TEXT,
            color TEXT,
            FOREIGN KEY(source) REFERENCES nodes(id),
            FOREIGN KEY(target) REFERENCES nodes(id),
            UNIQUE(source, target)
        )
    ''')

    conn.commit()
    conn.close()
    print("✓ System Initialized: 'synapse.db' created successfully.")

if __name__ == '__main__':

    init_db()


