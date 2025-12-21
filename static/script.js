const elem = document.getElementById('graph-container');

// 1. Initialize 3D Graph
const Graph = ForceGraph3D()
    (elem)
    .jsonUrl('/graph_data')
    .nodeLabel('label')
    .nodeAutoColorBy('group')
    .backgroundColor('#000000')
    .linkColor(link => link.color)
    .linkWidth(link => link.color === '#c5a059' ? 2 : 1) // Thicker gold lines
    .linkOpacity(0.5)
    .nodeThreeObject(node => {
        // Custom Spheres
        const group = node.group;
        const color = group === 'author' ? '#00f3ff' : '#c5a059'; // Cyan vs Gold
        
        const geometry = new THREE.SphereGeometry(node.val / 2);
        const material = new THREE.MeshLambertMaterial({
            color: color,
            transparent: true,
            opacity: 0.9,
            emissive: color,
            emissiveIntensity: 0.6
        });
        return new THREE.Mesh(geometry, material);
    });

// 2. Transmit Data
function transmitData() {
    const textInput = document.getElementById('memory');
    const authorInput = document.getElementById('author');
    const btn = document.getElementById('btn');

    const text = textInput.value;
    const author = authorInput.value || "Anonymous";

    if (!text) return;

    // UI Feedback
    btn.innerHTML = "PROCESSING <i class='ri-loader-4-line ri-spin'></i>";
    
    fetch('/transmit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text, author: author })
    })
    .then(res => res.json())
    .then(data => {
        if(data.status === 'success') {
            // Refresh Graph Data from Server
            // We reload the scene data to see new nodes
            // In a pro app, we might just append locally, but this ensures sync
            fetch('/graph_data').then(res => res.json()).then(newData => {
                Graph.graphData(newData);
            });

            textInput.value = "";
            btn.innerHTML = "TRANSMIT TO HIVE <i class='ri-send-plane-fill'></i>";
        }
    })
    .catch(err => console.error(err));
}