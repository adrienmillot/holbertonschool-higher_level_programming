$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const movies = data.results;

  $.each(movies, function (key, movie) {
    $('UL#list_movies').append('<LI>' + movie.title + '</LI>');
  });
});
