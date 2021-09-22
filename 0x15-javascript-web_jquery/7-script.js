$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (person) {
  $('DIV#character').text(person.name);
});
