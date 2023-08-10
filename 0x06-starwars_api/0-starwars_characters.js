#!/usr/bin/node
/* Star Wars Characters - Using the request module */
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a movie ID as a command-line argument.');
  process.exit(1);
}

const baseUrl = 'https://swapi.dev/api';
const filmUrl = `${baseUrl}/films/${movieId}/`;

request(filmUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie information:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie information. Status code:', response.statusCode);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character information:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error('Failed to fetch character information. Status code:', charResponse.statusCode);
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
