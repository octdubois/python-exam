import tkinter as tk
from tkinter import ttk

# =========================
# Données
# =========================
dict_nombre_points = {
    "bashar": 10,
    "leo": 8,
    "sara": 12
}

# =========================
# Fonctions
# =========================
def ajouter_point():
    nom_joueur = entree_nom.get().strip().lower()

    if not nom_joueur:
        message.config(
            text="⚠ Veuillez entrer un nom de joueur.",
            foreground="#ff6b6b"
        )
        return

    if nom_joueur in dict_nombre_points:
        dict_nombre_points[nom_joueur] += 1
        message.config(
            text=f"✅ {nom_joueur.capitalize()} a maintenant {dict_nombre_points[nom_joueur]} points.",
            foreground="#51cf66"
        )
    else:
        dict_nombre_points[nom_joueur] = 1
        message.config(
            text=f"✨ {nom_joueur.capitalize()} a été ajouté avec 1 point.",
            foreground="#4dabf7"
        )

    entree_nom.delete(0, tk.END)
    afficher_joueurs()


def afficher_joueurs():
    liste_joueurs.delete(*liste_joueurs.get_children())

    classement = sorted(
        dict_nombre_points.items(),
        key=lambda x: x[1],
        reverse=True
    )

    for position, (joueur, points) in enumerate(classement, start=1):
        liste_joueurs.insert(
            "",
            "end",
            values=(position, joueur.capitalize(), points)
        )


# =========================
# Fenêtre
# =========================
fenetre = tk.Tk()
fenetre.title("🏆 Gestion des Joueurs")
fenetre.geometry("650x450")
fenetre.configure(bg="#1e1e2f")

# =========================
# Style ttk
# =========================
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Title.TLabel",
    background="#1e1e2f",
    foreground="white",
    font=("Segoe UI", 22, "bold")
)

style.configure(
    "Info.TLabel",
    background="#1e1e2f",
    foreground="#cccccc",
    font=("Segoe UI", 10)
)

style.configure(
    "Custom.TButton",
    font=("Segoe UI", 11, "bold"),
    padding=8
)

# =========================
# Titre
# =========================
titre = ttk.Label(
    fenetre,
    text="🏆 Gestion des Joueurs",
    style="Title.TLabel"
)
titre.pack(pady=(20, 5))

sous_titre = ttk.Label(
    fenetre,
    text="Ajoutez des points et suivez le classement en temps réel",
    style="Info.TLabel"
)
sous_titre.pack(pady=(0, 20))

# =========================
# Zone de saisie
# =========================
frame_saisie = tk.Frame(
    fenetre,
    bg="#1e1e2f"
)
frame_saisie.pack(pady=10)

ttk.Label(
    frame_saisie,
    text="Nom du joueur :",
    style="Info.TLabel"
).grid(row=0, column=0, padx=10)

entree_nom = ttk.Entry(
    frame_saisie,
    width=25,
    font=("Segoe UI", 11)
)
entree_nom.grid(row=0, column=1, padx=10)

btn = ttk.Button(
    frame_saisie,
    text="➕ Ajouter 1 point",
    command=ajouter_point,
    style="Custom.TButton"
)
btn.grid(row=0, column=2, padx=10)

# =========================
# Message
# =========================
message = ttk.Label(
    fenetre,
    text="",
    style="Info.TLabel"
)
message.pack(pady=10)

# =========================
# Tableau des joueurs
# =========================
frame_tableau = tk.Frame(
    fenetre,
    bg="#1e1e2f"
)
frame_tableau.pack(fill="both", expand=True, padx=20, pady=10)

colonnes = ("Rang", "Joueur", "Points")

liste_joueurs = ttk.Treeview(
    frame_tableau,
    columns=colonnes,
    show="headings",
    height=10
)

for col in colonnes:
    liste_joueurs.heading(col, text=col)

liste_joueurs.column("Rang", width=80, anchor="center")
liste_joueurs.column("Joueur", width=220, anchor="center")
liste_joueurs.column("Points", width=120, anchor="center")

scrollbar = ttk.Scrollbar(
    frame_tableau,
    orient="vertical",
    command=liste_joueurs.yview
)

liste_joueurs.configure(yscrollcommand=scrollbar.set)

liste_joueurs.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)

# =========================
# Chargement initial
# =========================
afficher_joueurs()

entree_nom.focus()

# =========================
# Lancement
# =========================
fenetre.mainloop()