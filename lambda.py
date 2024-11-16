from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue au serveur Flask avec des routes pour un véhicule, un instrument de musique et un blog !"

# Route pour Véhicule
@app.route('/vehicule')
def vehicule():
    return jsonify({"vehicule": "Voiture", "description": "Une voiture est un véhicule motorisé utilisé pour le transport terrestre, capable de transporter plusieurs passagers et leurs bagages."})

# Route pour Instrument de Musique
@app.route('/instrument_musique')
def instrument_musique():
    return jsonify({"instrument_musique": "Guitare", "description": "La guitare est un instrument de musique à cordes pincées qui produit un son lorsque les cordes sont grattées ou pincées. Elle est utilisée dans de nombreux genres musicaux."})

# Route pour Blog
@app.route('/blog')
def blog():
    return jsonify({"blog": "Blog", "description": "Un blog est une plateforme en ligne où les individus peuvent publier des articles, partager des idées et discuter de divers sujets. C'est un excellent moyen de communiquer avec un large public et d'engager des conversations significatives."})

if __name__ == '__main__':
    app.run(debug=True)
