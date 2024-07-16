const response = fetch ('https://hellosalut.stefanbohacek.dev/?lang=fr');
response
.then(response => response.json())
.then(data => {
  console.log(data);

  const helloElement = document.getElementById("hello");

  helloElement.textContent = data.hello;
})
.catch(error => console.error('Error:', error));