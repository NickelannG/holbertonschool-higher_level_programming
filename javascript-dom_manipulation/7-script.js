const response = fetch('https://swapi-api.hbtn.io/api/films/?format=json');
response
  .then(response => response.json())
  .then(data => {
    console.log(data);

    const moviesList = document.getElementById("list_movies");
    
    for (const movie of data.results) {
      const newMovie = document.createElement("li");
      newMovie.textContent = movie.title;
      moviesList.appendChild(newMovie);
    }
  })
  .catch(error => console.error('Error:', error));