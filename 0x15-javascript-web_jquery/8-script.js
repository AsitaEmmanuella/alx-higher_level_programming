const movieList = $('UL#list_movies');
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: (movies) => {
    $.each(movies.results, (i, movie) => {
      movieList.append('<li>' + movie.title + '</li>');
    });
  }
});