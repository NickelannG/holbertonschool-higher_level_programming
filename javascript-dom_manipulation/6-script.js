const response = fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
response
  .then(response => response.json())
  .then(data => {
    console.log(data);

    const name = document.getElementById("character");
    name.textContent = data.name;
  });
