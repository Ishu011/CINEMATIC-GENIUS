function getRecommendations() {
  const movie = document.getElementById("movieInput").value;

  // Example API request (replace URL with Flask or FastAPI endpoint)
  fetch(`http://127.0.0.1:5000/recommend?movie=${encodeURIComponent(movie)}`)
    .then((res) => res.json())
    .then((data) => {
      const container = document.getElementById("recommendations");
      container.innerHTML = "";

      data.recommendations.forEach((movie) => {
        const card = document.createElement("div");
        card.className = "movie-card";
        card.innerHTML = `
          <img src="${movie.poster}" alt="${movie.title}" />
          <h3>${movie.title}</h3>
        `;
        container.appendChild(card);
      });
    })
    .catch((err) => {
      alert("Movie not found or API error.");
      console.error(err);
    });
}
