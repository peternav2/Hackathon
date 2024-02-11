
let map;
const url = 'http://127.0.0.1:5000/';

// Initialize the Google Map
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 37.0902, lng: -95.7129 }, // Center of the US
        zoom: 5
    });
}

// Add a submit event listener to the search form
document.getElementById('searchForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const state = document.getElementById('state').value;
    document.getElementById('selectedState').textContent = state;

    const response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify({ 'state': state }),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    const data = await response.json();

    
    // Check if the data includes the locations key
        if (!data || !data.coords) {
            throw new Error('No locations data in response');
        }

        // Clear the map
        initMap();

        // Place markers on the map for each location
        data.coords.forEach(function(location) {
            const marker = new google.maps.Marker({
                position: { lat: location[0], lng: location[1] },
                // position: { lat: location.lat, lng: location.lng },
                map: map,
                title: location.name
            });
            console.log(location[0] + " " + location[1])
            // Add an info window for each marker
            const infowindow = new google.maps.InfoWindow({
                content: location.name
            });

            marker.addListener('click', function() {
                infowindow.open(map, marker);
            });
        });
    // .catch(error => {
    //     console.error('Error:', error);
    //     alert('Error loading locations: ' + error.message);
    // });

    });
// Assign the initMap function to the window object so it can be called when the Google Maps script loads
window.initMap = initMap;