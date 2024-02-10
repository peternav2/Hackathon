const url = 'http://127.0.0.1:5000';
document.getElementById('searchForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    // Get user input
    let location = document.getElementById('location').value;
    let category = document.getElementById('category').value;
    await test().then(data => {
      console.log(data);
    });
    await test2().then(data => {
      document.getElementById('resultsSection').innerHTML = `<p>${data}</p>`;
      console.log(data);
    })
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
async function test() {
  const response = await fetch('http://127.0.0.1:5000/')
  const data = await response.json();
  console.log(data);
}
async function test2(data) {
  const response = await fetch('http://127.0.0.1:5000/', {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    },
  })
  const responseData = await response.json();
  console.log(responseData);

}











function testGet(url) {
  fetch(url, {
    method: 'GET'
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
    }
  })
  .then(response => {
    console.log(response.result);
    console.log(response.text());
  })
  .then(responseData => {
    console.log(responseData);
    document.getElementById('resultsSection').innerHTML = `<p>${responseData}</p>`;
  }).finally((res) => {
    console.log('done');
  });
//   .catch(error => {
//     console.error('Error:', error);
//   });
}
