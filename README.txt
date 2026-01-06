# Aurore-Boréale – Assistant IA pour les étudiants de l’Université Paris Nanterre

Aurore-Boréale est une application web Flask proposant un chatbot IA
pour répondre aux questions des étudiants sur la scolarité, l’inscription,
la vie de campus et les services de l’Université Paris Nanterre.

---

## 1. Fonctionnalités principales

- Création de compte, connexion et déconnexion avec gestion de session
- Interface de chat avec un assistant IA
- Enregistrement des questions/réponses en base de données SQLite,
  associées à l’utilisateur connecté
- Historique des échanges (date, question, réponse, pseudo)
- Bouton pour effacer l’historique visible d’un utilisateur
- Interface responsive adaptée à un usage étudiant

---

## 2. Pré-requis

- Python 3.8 ou supérieur
- Accès à une clé API valide (Mistral ou OpenAI)
- Git
- Navigateur web moderne (Chrome, Firefox, Edge, …)
- (Optionnel) WSL Ubuntu si vous êtes sous Windows

---

## 3. Installation

```bash
# Cloner le dépôt
git clone https://github.com/TODO_TON_COMPTE/TODO_NOM_DU_DEPOT.git
cd TODO_NOM_DU_DEPOT

# Créer et activer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate      # Linux / Mac
# venv\Scripts\activate       # Windows (PowerShell / CMD)

# Installer les dépendances
pip install -r requirements.txt


## 4. Lancement

Ensuite il faut lancer le projet sur un éditeur comme VScode avec "python3 app.py" et aller sur l'adresse donnée.
