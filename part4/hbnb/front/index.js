document.addEventListener('DOMContentLoaded', () => {
  checkAuthentication();
  populatePriceOptions();
  addFilterListener();
});

let allPlaces = []; // Save place data globally

// Check login status
function checkAuthentication() {
  const token = getTokenFromCookie();
  const loginLink = document.getElementById('login-link');
  
  if(!token) {
    loginLink.style.display = 'block';
    fetchPlaces(); 
  } else {
    loginLink.style.display = 'none';
    fetchPlaces(token);
  }
}

function getTokenFromCookie() {
  const name = 'token=';
  const decodedCookie = decodeURIComponent(document.cookie);
  const ca = decodedCookie.split(';');
  for (let c of ca) {
    c = c.trim();
    if (c.indexOf(name) === 0) {
      return c.substring(name.length, c.length);
    }
  }
  return '';
}

// Get all places once on initial display
async function fetchPlaces(token) {
  try {
    const headers = {};
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }

   const response = await fetch('http://localhost:5000/api/v1/places/', {
    headers: headers,
    credentials: 'include'
   });

   if (!response.ok) {
     throw new Error(`HTTP error! status: ${response.status}`);
   }

   allPlaces = await response.json();
   displayPlaces(allPlaces);

  } catch (error) {
   console.error('Failed to fetch places:', error);
  }
}


// Display places in HTML
function displayPlaces(places) {
  const container = document.getElementById('places-list');
  container.innerHTML = '';

  places.forEach(place => {
    const card = document.createElement('div');
    card.className = 'place-card';

    const title = document.createElement('h2');
    title.textContent = place.title;

    const price = document.createElement('p');
    price.textContent = `Price per night: $${place.price}`;

    const detailsButton = document.createElement('button');
    detailsButton.className = 'details-button';
    detailsButton.textContent = 'View Details';
    detailsButton.addEventListener('click', () => {
      window.location.href = `/place/${place.id}`;
    });
    
    card.appendChild(title);
    card.appendChild(price);
    card.appendChild(detailsButton);
    container.appendChild(card);
  });
}

// Set the dropdown options (10, 50, 100, All)
function populatePriceOptions() {
  const select = document.getElementById('price-filter');
  const prices = [10, 50, 100, 'All'];

  prices.forEach(price => {
    const option = document.createElement('option');
    option.value = price;
    option.textContent = price === 'All' ? 'All Prices' : `$${price}`;
    select.appendChild(option);
  });
}

// Add a listener for the filter
function addFilterListener() {
 document.getElementById('price-filter').addEventListener('change', (event) => {
  const selected = event.target.value;
  let filteredPlaces = [];

  if (selected === 'All') {
    filteredPlaces = allPlaces;
  }
  else {
    const maxPrice = parseInt(selected, 10);
    filteredPlaces = allPlaces.filter(place => place.price <= maxPrice);
  }

  displayPlaces(filteredPlaces);
 });
}
