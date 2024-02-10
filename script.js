document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    // Get user input
    let location = document.getElementById('location').value;
    let category = document.getElementById('category').value;

    findComp('http://localhost:8000', {"location": location, "category" : category});
    const results = `Analysis for ${category} in ${location}: Moderate competition with 5 similar businesses nearby.`;
    
    //document.getElementById('resultsSection').innerHTML = `<p>${results}</p>`;
});

let categories = ['Restaurant', 'Retail', 'Service'];
let categorySelect = document.getElementById('category');
categories.forEach(cat => {
    let option = document.createElement('option');
    option.value = cat.toString();
    option.textContent = cat.toString();
    let select = document.getElementById('category')
    select.appendChild(option);
});
function testGet(url) {
  fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    }
  })
  .then(response => {
    response.json();
    document.getElementById('resultsSection').innerHTML = `<p>${response}</p>`;
    console.log(response)
  })
  .catch(error => error.toString())
  .catch(error => {
    console.error('Error:', error);
  });
}
function findComp(url, data) {
    console.log(data);
  fetch(url, {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': '*',
      'Access-Control-Allow-Headers': '*', 
    }
  })
  .then(response => {
    console.log(response);
    console.log(response.text());
  })
  .then(responseData => {
    console.log(responseData);
    document.getElementById('resultsSection').innerHTML = `<p>${responseData}</p>`;
  }).finally(() => {
    console.log('done');
  });
//   .catch(error => {
//     console.error('Error:', error);
//   });
}
