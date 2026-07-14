import tkinter as tk
from tkinter import ttk, messagebox
import json


class Bibliotheque:
    def __init__(self, nom: str, addresse: str):
        self.nom = nom
        self.addresse = addresse
        self.dict_livres: dict[str, dict] = {}

    def ajouter_livre(self, titre: str, auteur: str, annee: str):

        titre = titre.strip()

        if titre == "":
            return "Titre vide non accepté."

        if titre in self.dict_livres:
            return f"Le titre '{titre}' existe déjà."

        self.dict_livres[titre] = {
            "auteur": auteur,
            "annee": annee,
            "titre": titre
        }

        return "Livre ajouté avec succès."

    def trouver_livre(self, titre: str):

        if titre in self.dict_livres:
            return self.dict_livres[titre]

        return None


class BibliothequeGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Bibliothèque - Dictionnaire Imbriqué")
        self.root.geometry("1400x850")

        self.biblio = Bibliotheque(
            "Biblio de Bashar",
            "1970 rue Montréal"
        )

        # ==========================
        # EXEMPLES INITIAUX
        # ==========================

        self.biblio.ajouter_livre(
            "bashar est beau",
            "simon barette",
            "1999"
        )

        self.biblio.ajouter_livre(
            "complement de programmation",
            "bashar",
            "2025"
        )

        # ==========================
        # FRAME PRINCIPAL
        # ==========================

        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # ==========================
        # COLONNE GAUCHE
        # ==========================

        left_frame = tk.Frame(main_frame)
        left_frame.pack(side="left", fill="y", padx=10)

        tk.Label(
            left_frame,
            text="Ajouter un livre",
            font=("Arial", 14, "bold")
        ).pack(pady=5)

        tk.Label(left_frame, text="Titre")
        self.entry_titre = tk.Entry(left_frame, width=40)
        self.entry_titre.pack()

        tk.Label(left_frame, text="Auteur")
        self.entry_auteur = tk.Entry(left_frame, width=40)
        self.entry_auteur.pack()

        tk.Label(left_frame, text="Année")
        self.entry_annee = tk.Entry(left_frame, width=40)
        self.entry_annee.pack()

        tk.Button(
            left_frame,
            text="Ajouter",
            bg="#4CAF50",
            fg="white",
            command=self.ajouter_livre
        ).pack(pady=10)

        ttk.Separator(
            left_frame,
            orient="horizontal"
        ).pack(fill="x", pady=10)

        tk.Label(
            left_frame,
            text="Rechercher un livre",
            font=("Arial", 14, "bold")
        ).pack()

        self.entry_recherche = tk.Entry(
            left_frame,
            width=40
        )
        self.entry_recherche.pack()

        tk.Button(
            left_frame,
            text="Trouver",
            command=self.trouver_livre
        ).pack(pady=5)

        self.label_resultat = tk.Label(
            left_frame,
            text="",
            justify="left",
            fg="blue"
        )

        self.label_resultat.pack(pady=10)

        # ==========================
        # COLONNE DROITE
        # ==========================

        right_frame = tk.Frame(main_frame)
        right_frame.pack(
            side="left",
            fill="both",
            expand=True
        )

        # ==========================
        # JSON
        # ==========================

        tk.Label(
            right_frame,
            text="Dictionnaire Imbriqué (JSON)",
            font=("Arial", 14, "bold")
        ).pack()

        self.text_json = tk.Text(
            right_frame,
            height=18,
            font=("Consolas", 11),
            bg="#1e1e1e",
            fg="#d4d4d4",
            insertbackground="white"
        )

        self.text_json.pack(
            fill="both",
            expand=True,
            pady=5
        )

        # ==========================
        # ARBRE
        # ==========================

        tk.Label(
            right_frame,
            text="Vue Arbre du Dictionnaire",
            font=("Arial", 14, "bold")
        ).pack()

        self.text_tree = tk.Text(
            right_frame,
            height=12,
            font=("Consolas", 11)
        )

        self.text_tree.pack(
            fill="both",
            expand=True,
            pady=5
        )

        self.mettre_a_jour_affichage()

    # ===================================
    # AJOUT LIVRE
    # ===================================

    def ajouter_livre(self):

        titre = self.entry_titre.get()
        auteur = self.entry_auteur.get()
        annee = self.entry_annee.get()

        message = self.biblio.ajouter_livre(
            titre,
            auteur,
            annee
        )

        messagebox.showinfo(
            "Information",
            message
        )

        self.mettre_a_jour_affichage()

        self.entry_titre.delete(0, tk.END)
        self.entry_auteur.delete(0, tk.END)
        self.entry_annee.delete(0, tk.END)

    # ===================================
    # RECHERCHE
    # ===================================

    def trouver_livre(self):

        titre = self.entry_recherche.get()

        livre = self.biblio.trouver_livre(titre)

        if livre is None:

            self.label_resultat.config(
                text=f"Aucun livre avec le titre:\n{titre}",
                fg="red"
            )

        else:

            self.label_resultat.config(
                fg="green",
                text=
                f"Titre : {livre['titre']}\n"
                f"Auteur : {livre['auteur']}\n"
                f"Année : {livre['annee']}"
            )

    # ===================================
    # RAFRAICHIR LES VUES
    # ===================================

    def mettre_a_jour_affichage(self):

        # -----------------------
        # JSON
        # -----------------------

        self.text_json.delete("1.0", tk.END)

        pretty_json = json.dumps(
            self.biblio.dict_livres,
            indent=4,
            ensure_ascii=False
        )

        self.text_json.insert(
            tk.END,
            pretty_json
        )

        # -----------------------
        # ARBRE
        # -----------------------

        self.text_tree.delete("1.0", tk.END)

        arbre = "dict_livres\n"

        for titre, info in self.biblio.dict_livres.items():

            arbre += "│\n"
            arbre += f"├── '{titre}'\n"
            arbre += "│   │\n"
            arbre += f"│   ├── auteur : '{info['auteur']}'\n"
            arbre += f"│   ├── annee  : '{info['annee']}'\n"
            arbre += f"│   └── titre  : '{info['titre']}'\n"

        self.text_tree.insert(
            tk.END,
            arbre
        )


# ===================================
# PROGRAMME PRINCIPAL
# ===================================

root = tk.Tk()

app = BibliothequeGUI(root)

root.mainloop()