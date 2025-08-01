document.addEventListener('DOMContentLoaded', () => {
    const reviewForm = document.getElementById('review-form');
    const token = checkAuthentication();  // Check authentication and get token
    const placeId = getPlaceIdFromURL();

    if (reviewForm) {
        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const reviewText = document.getElementById('review-text').value;
            const rating = document.getElementById('rating').value;

            try {
                const response = await submitReview(token, placeId, reviewText, rating);
                await handleResponse(response);
            } catch (error) {
                console.error('Error submitting review:', error);
                alert('An error occurred while submitting the review.');
            }
        });
    }
});


// --- Review submission logic ---
async function submitReview(token, placeId, reviewText, rating) {

    console.log('Submitting review:', { token, placeId, reviewText, rating });
    console.log("Parsed rating:", parseInt(rating), typeof parseInt(rating));

    return await fetch('http://localhost:5000/api/v1/reviews/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            text: reviewText,
            place_id: placeId,
            rating: parseInt(rating)   
        })
    });
}

// --- Handle response ---
async function handleResponse(response) {
    if (response.ok) {
        alert('Review submitted successfully!');
        document.getElementById('review-form').reset();
        location.reload();  // Reload to show the new review
    } else {
        const data = await response.json();
        alert(`Failed to submit review: ${data.error || 'Unknown error'}`);
    }
}
