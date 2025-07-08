from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

movies = {
    "Action": [("Mad Max: Fury Road", 2015, 8.1), ("John Wick", 2014, 7.4), ("Gladiator", 2000, 8.5)],
    "Comedy": [("Superbad", 2007, 7.6), ("Step Brothers", 2008, 6.9), ("The Hangover", 2009, 7.7)],
    "Horror": [("The Conjuring", 2013, 7.5), ("It", 2017, 7.3), ("A Nightmare on Elm Street", 1984, 7.5)],
    "Sci-Fi": [("Inception", 2010, 8.8), ("Interstellar", 2014, 8.6), ("The Matrix", 1999, 8.7)],
    "Mystery": [("Se7en", 1995, 8.6), ("Gone Girl", 2014, 8.1), ("Shutter Island", 2010, 8.2)]
}

music = {
    "Pop": ["Blinding Lights - The Weeknd", "Shape of You - Ed Sheeran", "Uptown Funk - Bruno Mars"],
    "Rock": ["Bohemian Rhapsody - Queen", "Hotel California - Eagles", "Sweet Child O' Mine - Guns N' Roses"],
    "Hip-Hop": ["Lose Yourself - Eminem", "Sicko Mode - Travis Scott", "God's Plan - Drake"],
    "Jazz": ["Take Five - Dave Brubeck", "Feeling Good - Nina Simone", "My Favorite Things - John Coltrane"],
    "Bollywood": ["Tum Hi Ho - Arijit Singh", "Chaiyya Chaiyya - Sukhwinder Singh", "Jai Ho - A.R. Rahman"]
}

story_templates = {
    "Fantasy": "In the mystical kingdom of Eldoria, a young wizard named Aric discovered a hidden spellbook that could change the fate of the realm. As he chanted the incantations, the skies darkened and a portal to an unknown world opened...",
    "Mystery": "Detective Roy was called to a grand mansion where a billionaire had vanished. With a single clue—a torn letter—he pieced together a puzzle leading him through hidden passageways and long-buried family secrets. As he reached the final door, a shocking revelation awaited...",
    "Sci-Fi": "Captain Vega activated the warp drive, launching the spaceship into the unknown. As they approached a distant planet, strange signals disrupted their systems. What they found next would change humanity's understanding of the universe forever...",
    "Adventure": "Lena clutched the ancient map and ventured into the lost temple. The walls bore cryptic inscriptions, and hidden traps lay in wait. But at the heart of the temple, a legendary artifact glowed, promising untold power...",
    "Horror": "The candle flickered as Mark stepped deeper into the abandoned house. Suddenly, a whisper echoed from the shadows. The old journal warned of a ghostly presence—but Mark had already crossed the line between the living and the dead..."
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_movies', methods=['POST'])
def get_movies():
    genre = request.json.get("genre")
    selected_movies = movies.get(genre, [])
    return jsonify(selected_movies)

@app.route('/get_music', methods=['POST'])
def get_music():
    genre = request.json.get("genre")
    selected_music = music.get(genre, [])
    return jsonify(selected_music)

@app.route('/generate_story', methods=['POST'])
def generate_story():
    genre = request.json.get("genre")
    story = story_templates.get(genre, "A mysterious event unfolded...")
    return jsonify(story)

if __name__ == '__main__':
    app.run(debug=True)
