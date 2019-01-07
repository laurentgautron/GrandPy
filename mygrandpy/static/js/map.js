function displayMap(coord) {
    mapboxgl.accessToken = 'pk.eyJ1IjoidXNodWFuZ28iLCJhIjoiY2pxZ3Eyd2JmNTE5YjQ4ank5YzBqMG1neCJ9.DVSLrBIEeZzjU2e3GY17dQ';
    let map = new mapboxgl.Map({
        container: 'map', // HTLM container
        style: 'mapbox://styles/mapbox/streets-v9', //style URL
        center: coord, // starting position as [lng, lat]
        zoom: 13
    });

    let marker = new mapboxgl.Marker()
        .setLngLat(coord)
        .addTo(map)
}