document.addEventListener("DOMContentLoaded", () => {
    const API_URL = 'http://localhost:5001/api/v1'; // <-- Change this if needed

    // Vérifie le statut de l’API
    fetch(`${API_URL}/status/`)
        .then(response => response.json())
        .then(data => {
            if (data.status === 'OK') {
                console.log("API status: OK");
                document.querySelector("#api_status")?.classList.add("available");
            } else {
                console.warn("API not OK");
            }
        })
        .catch(err => {
            console.error("Erreur de connexion à l'API", err);
        });

    // Charge tous les lieux
    const loadPlaces = (filters = {}) => {
        fetch(`${API_URL}/places_search/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(filters)
        })
        .then(response => response.json())
        .then(places => {
            const placesContainer = document.getElementById("places");
            if (!placesContainer) return;
            placesContainer.innerHTML = "";

            places.forEach(place => {
                const placeCard = document.createElement("div");
                placeCard.className = "place-card";
                placeCard.innerHTML = `
                    <h4>${place.name}</h4>
                    <div class="properties">
                        <div>${place.max_guest} Guests</div>
                        <div>${place.number_rooms} Rooms</div>
                        <div>${place.number_bathrooms} Bathrooms</div>
                    </div>
                    <p class="place-description">${place.description || ''}</p>
                `;
                placesContainer.appendChild(placeCard);
            });
        })
        .catch(error => console.error("Erreur lors du chargement des places:", error));
    };

    loadPlaces(); // Appel initial

    // Filtrage par amenities
    document.getElementById("filter-button")?.addEventListener("click", () => {
        const amenityIds = Array.from(document.querySelectorAll("input[type='checkbox']:checked"))
            .map(checkbox => checkbox.dataset.id);
        loadPlaces({ amenities: amenityIds });
    });

    // Soumission d'un avis (review-form)
    const reviewForm = document.getElementById("review-form");
    if (reviewForm) {
        reviewForm.addEventListener("submit", (e) => {
            e.preventDefault();
            const user_id = reviewForm.querySelector("input[name='user_id']")?.value;
            const place_id = reviewForm.querySelector("input[name='place_id']")?.value;
            const text = reviewForm.querySelector("textarea[name='text']")?.value;

            if (!user_id || !place_id || !text) {
                alert("Merci de remplir tous les champs du formulaire d'avis.");
                return;
            }

            fetch(`${API_URL}/reviews/`, {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user_id, place_id, text })
            })
            .then(res => res.json())
            .then(review => {
                alert("Avis envoyé avec succès !");
                reviewForm.reset();
            })
            .catch(error => {
                console.error("Erreur lors de l'envoi de l'avis:", error);
                alert("Une erreur est survenue lors de l'envoi de l'avis.");
            });
        });
    }
});
