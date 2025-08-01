document.addEventListener('DOMContentLoaded', () => {
  const placeId = getPlaceIdFromURL();
  checkAuthentication(placeId);
});


// Get place ID from URL
function getPlaceIdFromURL() {
    const urlParams = new URLSearchParams(window.location.search);
    const idFromQuery = urlParams.get('id');

    if (idFromQuery) return idFromQuery;

    const pathParts = window.location.pathname.split('/').filter(Boolean);   
    return pathParts[pathParts.length - 1]; // Last part of the path is the place ID
  }

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

function checkAuthentication(placeId) {
  const token = getCookie('token');
  const addReviewSection = document.getElementById('add-review');

  if (!token) {
    addReviewSection.style.display = 'none'; // Hide add review section if not logged in
    fetchPlaceDetails(null, placeId);
  } else {
    addReviewSection.style.display = 'block'; // Show add review section if logged in
    fetchPlaceDetails(token, placeId);  // Fetch place details if logged in
    }
  return token; // Return token for use in review submission
}

// Get facility details from API
async function fetchPlaceDetails(token, placeId) {
  try {
    const headers = token ? { 'Authorization': `Bearer ${token}` } : {};
    const response = await fetch(`http://localhost:5000/api/v1/places/${placeId}`, {
      headers: headers,
      credentials: 'include'  // Include cookies for session management
    });

    if (!response.ok) throw new Error('Data acquisition failed');
    const place = await response.json();

    displayPlaceDetails(place);
  } catch (error) {
    console.error('Error getting place details:', error);
    }
}

// Add details to HTML
function displayPlaceDetails(place) {

    const container = document.getElementById('place-details');
    container.innerHTML = ''; // Clear any existing content
    
    // --- Place title ---
    const title = document.createElement('h1');
    title.textContent = place.title;
    title.className = 'place-title';
    container.appendChild(title);


    // --- Place detail card ---
    const placeCard = document.createElement('div');
    placeCard.className = 'place-card';

    const ownerName = document.createElement('p');
    if (place.owner && place.owner.first_name && place.owner.last_name) {
        ownerName.innerHTML = `<strong>Owner: </strong> ${place.owner.first_name} ${place.owner.last_name}`;
    } else {
        ownerName.innerHTML = '<strong>Owner: </strong>Unknown';
    }

    const desc = document.createElement('p');
    desc.innerHTML =  `<strong>Description: </strong> ${place.description}`;

    const price = document.createElement('p');
    price.innerHTML = `<strong>Price per night: </strong> $${place.price}`;

    const amenitiesTitle = document.createElement('h4');
    amenitiesTitle.innerHTML = '<strong>Amenities:</strong>';

    const amenities = document.createElement('ul');
    amenities.className = 'amenities-list';

    (place.amenities || []).forEach(item => {
        const li = document.createElement('li');
        li.textContent = item.name || item;
        amenities.appendChild(li);
    });

    placeCard.appendChild(ownerName);
    placeCard.appendChild(desc);
    placeCard.appendChild(price);
    placeCard.appendChild(amenitiesTitle);
    placeCard.appendChild(amenities);
    container.appendChild(placeCard);

    // --- Reviews section ---
    const reviewsHeader = document.createElement('h1');
    reviewsHeader.textContent = 'Reviews:';
    reviewsHeader.className = 'reviews-header';
    container.appendChild(reviewsHeader);

    (place.reviews || []).forEach(review => {
        const reviewCard = document.createElement('div');
        reviewCard.className = 'review-card';

        const userName = document.createElement('p');
        userName.innerHTML = `<strong>${review.user_name}:</strong>`;

        const reviewText = document.createElement('p');
        reviewText.textContent = review.text;

        const rating = document.createElement('p');
        rating.innerHTML = `<strong>Rating:</strong> ${renderStars(review.rating)}`;

        reviewCard.appendChild(userName);
        reviewCard.appendChild(reviewText);
        reviewCard.appendChild(rating);
        container.appendChild(reviewCard);
    });

    function renderStars(rating) {
      const maxStars = 5;
      let stars = '';
      for (let i = 1; i <= maxStars; i++) {
        stars += i <= rating ? '★' : '☆';
      }
      return stars;
    }
}
