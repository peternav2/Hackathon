let map;
const url = 'http://127.0.0.1:5000/get_locations';

// Initialize the Google Map
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 37.0902, lng: -95.7129 }, // Center of the US
        zoom: 5
    });
}

// Add a submit event listener to the search form
document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const state = document.getElementById('state').value;
    document.getElementById('selectedState').textContent = state;

    fetch(url, {
        method: 'POST',
        body: JSON.stringify({ 'state': state }),
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        // Check if the data includes the locations key
        if (!data || !data.locations) {
            throw new Error('No locations data in response');
        }

        // Clear the map
        initMap();

        // Place markers on the map for each location
        data.locations.forEach(function(location) {
            const marker = new google.maps.Marker({
                position: { lat: location.lat, lng: location.lng },
                map: map,
                title: location.name
            });

            // Add an info window for each marker
            const infowindow = new google.maps.InfoWindow({
                content: location.name
            });

            marker.addListener('click', function() {
                infowindow.open(map, marker);
            });
        });
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error loading locations: ' + error.message);
    });
});

// Assign the initMap function to the window object so it can be called when the Google Maps script loads
window.initMap = initMap;
