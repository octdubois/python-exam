<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🏆 Gestion des Joueurs</title>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Segoe UI", sans-serif;
}

body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
}

.container {
    width: 90%;
    max-width: 800px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

h1 {
    text-align: center;
    margin-bottom: 10px;
    font-size: 2rem;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 25px;
}

.input-group {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
}

input {
    flex: 1;
    padding: 12px;
    border: none;
    border-radius: 10px;
    font-size: 1rem;
    outline: none;
}

button {
    padding: 12px 20px;
    border: none;
    border-radius: 10px;
    background: #3b82f6;
    color: white;
    font-weight: bold;
    cursor: pointer;
    transition: 0.25s;
}

button:hover {
    background: #2563eb;
    transform: translateY(-2px);
}

.message {
    text-align: center;
    margin-bottom: 20px;
    font-weight: bold;
    min-height: 25px;
}

.table-container {
    overflow-x: auto;
}

table {
    width: 100%;
    border-collapse: collapse;
    overflow: hidden;
    border-radius: 12px;
}

thead {
    background: #334155;
}

th, td {
    padding: 14px;
    text-align: center;
}

tbody tr {
    background: rgba(255,255,255,0.05);
    transition: 0.2s;
}

tbody tr:hover {
    background: rgba(255,255,255,0.12);
}

.gold {
    color: gold;
    font-weight: bold;
}

.silver {
    color: silver;
    font-weight: bold;
}

.bronze {
    color: #cd7f32;
    font-weight: bold;
}
</style>
</head>
<body>

<div class="container">

    <h1>🏆 Gestion des Joueurs</h1>
    <p class="subtitle">
        Ajoutez des points et suivez le classement en temps réel
    </p>

    <div class="input-group">
        <input
            type="text"
            id="playerName"
            placeholder="Nom du joueur"
        >
        <button onclick="ajouterPoint()">
            ➕ Ajouter 1 point
        </button>
    </div>

    <div id="message" class="message"></div>

    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th>Rang</th>
                    <th>Joueur</th>
                    <th>Points</th>
                </tr>
            </thead>
            <tbody id="playersTable"></tbody>
        </table>
    </div>

</div>

<script>
let joueurs = {
    bashar: 10,
    leo: 8,
    sara: 12
};

function afficherJoueurs() {
    const table = document.getElementById("playersTable");

    const classement = Object.entries(joueurs)
        .sort((a, b) => b[1] - a[1]);

    table.innerHTML = "";

    classement.forEach(([nom, points], index) => {

        let medal = "";

        if (index === 0)
            medal = '<span class="gold">🥇</span>';

        else if (index === 1)
            medal = '<span class="silver">🥈</span>';

        else if (index === 2)
            medal = '<span class="bronze">🥉</span>';

        table.innerHTML += `
            <tr>
                <td>${medal} ${index + 1}</td>
                <td>${nom.charAt(0).toUpperCase() + nom.slice(1)}</td>
                <td>${points}</td>
            </tr>
        `;
    });
}

function ajouterPoint() {

    const input = document.getElementById("playerName");
    const message = document.getElementById("message");

    let nom = input.value.trim().toLowerCase();

    if (!nom) {
        message.style.color = "#ff6b6b";
        message.textContent =
            "⚠ Veuillez entrer un nom.";
        return;
    }

    if (joueurs[nom]) {

        joueurs[nom]++;

        message.style.color = "#4ade80";
        message.textContent =
            `✅ ${nom} a maintenant ${joueurs[nom]} points.`;

    } else {

        joueurs[nom] = 1;

        message.style.color = "#60a5fa";
        message.textContent =
            `✨ ${nom} a été ajouté avec 1 point.`;
    }

    input.value = "";
    afficherJoueurs();
}

document
    .getElementById("playerName")
    .addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            ajouterPoint();
        }
    });

afficherJoueurs();
</script>

</body>
</html>