import os
from flask import Flask, render_template, request, jsonify
from mistralai import Mistral

app = Flask(__name__, static_url_path='/static')

# =======================
# CONFIGURATION IA
# =======================
API_KEY = os.environ.get("MISTRAL_API_KEY")  # ou mettre directement ta clé ici
AGENT_ID = "ag_019b136c0dce7649bd2f80e79717b1c1"

client = Mistral(api_key=API_KEY)

# =======================
# ROUTES PRINCIPALES
# =======================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/about")
def about():
    return render_template("about.html")

# =======================
# ROUTE CHATBOT
# =======================
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "").strip()

    if not user_msg:
        return jsonify({"reply": "Message vide"}), 400

    try:
        # Appel au Mistral avec ton agent
        response = client.beta.conversations.start(
            agent_id=AGENT_ID,
            inputs=user_msg
        )
        # Récupération du texte de sortie
        ai_reply = response.get("outputs", "Erreur : réponse vide")
        return jsonify({"reply": ai_reply})

    except Exception as e:
        print("ERREUR IA :", e)
        return jsonify({"reply": "Erreur du serveur IA"}), 500

# =======================
# SERVIR FICHIERS STATIQUES
# =======================
@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

# =======================
# PAGE 404
# =======================
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 — Page non trouvée</h1>", 404

# =======================
# LANCEMENT DU SERVEUR
# =======================
if __name__ == "__main__":
    app.run(debug=True)


