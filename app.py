import pickle
import streamlit as st
import requests
import os
import gdown
from dotenv import load_dotenv

# --- PAGE CONFIG ---
st.set_page_config(page_title="Made by Ishu", page_icon="", layout="wide")

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0f2027 !important; color: white; font-family: 'Segoe UI', sans-serif; }
    .stButton>button {
        background-color: #ff3f6c; color: white; font-weight: bold;
        border: none; border-radius: 8px; padding: 10px 20px; font-size: 16px;
    }
    .stSelectbox label { color: white !important; font-size: 18px; }
    .stMarkdown h1 { margin-bottom: 40px; }
    img.poster { width: 200px; height: auto; border-radius: 10px; }
    .movie-card {
        display: flex; gap: 20px; background-color: #1e1e1e;
        border-radius: 10px; padding: 20px; margin-bottom: 20px;
    }
    .movie-info { color: white; font-size: 16px; max-width: 800px; }
    .movie-title { font-size: 24px; color: #ff3f6c; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# --- ENV LOADING & FILE DOWNLOAD ---
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
MODEL_URL = os.getenv("SIMILARITY_MODEL_URL")

os.makedirs("model", exist_ok=True)

SIMILARITY_PATH = "model/similarity.pkl"
if not os.path.exists(SIMILARITY_PATH):
    with st.spinner("Downloading model file..."):
        gdown.download(MODEL_URL, SIMILARITY_PATH, quiet=False)

# --- LOAD DATA ---
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open(SIMILARITY_PATH, 'rb'))

# --- TMDB FETCHING ---
def fetch_movie_details(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}"

        movie_data = requests.get(url).json()
        credits_data = requests.get(credits_url).json()

        title = movie_data.get('title', 'Unknown')
        poster_path = movie_data.get('poster_path')
        poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else "https://via.placeholder.com/200x300?text=No+Image"
        overview = movie_data.get('overview', 'No description available.')
        rating = movie_data.get('vote_average', 'N/A')
        release_date = movie_data.get('release_date', 'Unknown')
        release_year = release_date[:4] if release_date else "Unknown"
        tagline = movie_data.get('tagline', 'No tagline')
        genres = ", ".join([genre['name'] for genre in movie_data.get('genres', [])]) or "N/A"
        cast = [member['name'] for member in credits_data.get('cast', [])[:3]]
        cast_str = ", ".join(cast) if cast else "Cast info not available"

        return poster_url, title, release_year, release_date, rating, overview, cast_str, genres, tagline

    except Exception:
        return (
            "https://via.placeholder.com/200x300?text=No+Image",
            "Unknown", "Unknown", "Unknown", "N/A", "No data found.",
            "Cast not available", "N/A", "No tagline"
        )

# --- RECOMMENDER LOGIC ---
def get_tmdb_id(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
    response = requests.get(url)
    
    if response.status_code != 200:
        st.error("Failed to fetch data from TMDb.")
        return None
    
    data = response.json()
    if "results" not in data or not data["results"]:
        st.warning(f"No TMDb results found for: {title}")
        return None

    return data["results"][0]["id"]


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommendations = []

    for i in distances[1:11]:
        title = movies.iloc[i[0]].title
        tmdb_id = get_tmdb_id(title)
        if tmdb_id:
            details = fetch_movie_details(tmdb_id)
            recommendations.append(details)
        else:
            recommendations.append((
                "https://via.placeholder.com/200x300?text=No+Image",
                title, "Unknown", "Unknown", "N/A", "No data found.",
                "Cast not available", "N/A", "No tagline"
            ))
    return recommendations

# --- TITLE ---
st.markdown("""
    <h1 style="text-align: center; color: #ff3f6c; font-size: 70px;">
        🍿 CINEMATIC GENIUS 🍿
    </h1>
""", unsafe_allow_html=True)

# --- USER INPUT ---
st.markdown("## Choose how many recommendations you want:")
num_recs = st.slider("Number of Recommendations", 1, 7, 5)

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie", movie_list, index=0, label_visibility="visible")

# --- RECOMMENDATION SECTION ---
if st.button('Show Recommendations'):
    with st.spinner("Fetching movie magic..."):
        recommendations = recommend(selected_movie)
        for i in range(num_recs):
            poster, title, year, release_date, rating, overview, cast, genres, tagline = recommendations[i]
            st.markdown(f"""
                <div class="movie-card">
                    <div>
                        <img src="{poster}" class="poster" alt="{title} Poster" />
                    </div>
                    <div class="movie-info">
                        <div class="movie-title">{title} ({year})</div>
                        <p><b>Release Date:</b> {release_date}</p>
                        <p><b>Cast:</b> {cast}</p>
                        <p><b>Genres:</b> {genres}</p>
                        <p><b>Rating:</b> {rating}</p>
                        <p><b>Tagline:</b> {tagline}</p>
                        <p><b>Overview:</b> {overview[:500]}...</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)
