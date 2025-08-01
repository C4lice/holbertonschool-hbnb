:root {
	--color-primary: #ff375c;
	--color-black: #090909;
	--color-white: #fafafa;
	--color-light-grey: #f2f2f2;
	--color-medium-grey: #dbdbdb;
	--color-dark-grey: #606060;
    --text-color: var(--color-black);
	--font-family-base: "Open Sans", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
	--font-family-title: "Raleway", "Helvetica Neue", "Helvetica", "Arial", sans-serif;
	--font-size-small: 1.2rem;
	--font-size-medium: 1.6rem;
	--font-size-large: 1.8rem;
	--font-size-x-large: 2.3rem;
	--font-size-xx-large: 4.8rem;
    --font-weight-regular: 400;
	--font-weight-bold: 700;
	--line-height-small: 1.2;
	--line-height-base: 1.5;
	--line-height-big: 1.8;
}

/* ----- GENERAL ----- */

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: var(--font-family-base);
}

html {
	scroll-behavior: smooth;
	font-size: 62.5%;
    width: 100%;
    height: 100%;
}

body {
    background-color: var(--color-light-grey);
    line-height: var(--line-height-base);
    color: var(--color-dark-grey);
    font-size: var(--font-size-medium);
}

h1,
h2,
h3,
h4,
h5,
h6 {
	font-family: var(--font-family-title);
	font-weight: var(--font-weight-bold);
}

h3 {
    border-bottom: 3px solid var(--color-medium-grey);
    font-size: var(--font-size-x-large);
    padding-bottom: 5px;
    margin-bottom: 10px;
}

h4 {
    border-bottom: 3px solid var(--color-medium-grey);
    font-size: var(--font-size-large);
    padding-bottom: 5px;
    margin-bottom: 10px;
}

h5 {
    height: 25px;
    font-size: var(--font-size-medium);
    font-weight: var(--font-weight-bold);
    font-size: var(--font-size-medium);
    color: var(--color-dark-grey);
}

h6 {
    font-size: var(--font-size-x-large);
    font-weight: var(--font-weight-bold);
}

#logo {
    align-items: center;
    transition: transform 0.5s ease-in-out;
}

#logo:hover {
    transform: scale(1.1);
}

/* ----- HEADER ----- */

header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: var(--color-primary);
    color: var(--color-white);
    /* border-radius: 15rem; */
    /* margin: 2rem; */
    padding: 2rem 4rem;
    height: 100px;
    box-shadow:
		0 10px 15px rgba(0, 0, 0, 0.1),
		0 8px 10px rgba(0, 0, 0, 0.1);
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1;
}

header button {
    padding: 1rem 2rem;
    background-color: var(--color-primary);
    border-color: var(--color-white);
    border-style: solid;
    color: var(--color-white);
    font-weight: var(--font-weight-bold);
    transition-duration: 0.25s;
    font-size: medium;
    border-width: 3px;
    border-radius: 999px;
    right: 10rem;
    cursor: pointer;
}

header button:hover {
    background-color: var(--color-white);
    color: var(--color-primary);
}

#login-link {
    display: none;
}

#logout-link {
    display: none;
}

/* ----- MAIN ----- */

main {
    padding: 2rem;
    height: 100vh;
}

.center {
    height: 100vh;
    display: flex;
    justify-content: center;
    flex-direction: column;
    margin-top: none;
}

#filter,
#place-details {
    margin-top: 100px;
}

.link {
    margin-top: 5px;
    text-align: center;
    font-size: var(--font-size-small);
    text-decoration: underline;
    color: var(--color-primary);
    cursor: pointer;
}

.container {
	width: 100%;
    height: 100%;
	margin-left: auto;
	margin-right: auto;
    display: flex;
    align-items: center;
    justify-content: center;
}

.row {
    width: 75%;
}

ul {
    list-style: none;
}

.place-amenities li {
    list-style-type: disc;
}

main button {
    border-radius: 999px;
    border-color: var(--color-dark-grey);
    border-style: solid;
    color: var(--color-dark-grey);
    transition-duration: 0.25s;
    padding: 0.5rem 1rem;
    cursor: pointer;
}

main button:hover {
    background-color: var(--color-dark-grey);
    color: var(--color-light-grey);
}

main #account-form button,
main #login-form button,
main .review-submission button,
main .place-submission button {
    margin-left: 7em;
    margin-right: 7em;
}

main #account-form input,
main #login-form input,
main #review input {
    height: 4rem;
}

.col-3 {
    float: left;
	width: 33.33%;
    height: 100%;
}

#new-place {
    display: none;
    position: fixed;
    right: 50px;
    bottom: 100px;
    z-index: 1;
}

#new-place button {
    padding: 1rem 2rem;
    background-color: var(--color-white);
    color: var(--color-primary);
    border-color: var(--color-primary);
    font-weight: var(--font-weight-bold);
    transition-duration: 0.25s;
    font-size: medium;
    border-width: 3px;
    border-radius: 999px;
    box-shadow:
		0 10px 15px rgba(0, 0, 0, 0.05),
		0 8px 10px rgba(0, 0, 0, 0.05);
}

#new-place button:hover {
    background-color: var(--color-primary);
    color: var(--color-white);
}

/* ----- ANIMATION ----- */

#animation {
    height: 100%;
    display: none;
}

.logo-grey {
    fill: none;
    stroke: #eeeeee;
    stroke-miterlimit: 10;
    stroke-width: 5px;
}

.logo-red-top {
    fill: none;
    stroke: #ff375c;
    stroke-linecap: round;
    stroke-miterlimit: 10;
    stroke-width: 5px;
    stroke-dasharray: 103.75;
    stroke-dashoffset: 103.75;
    animation: top-draw 4.5s linear;
}

@keyframes top-draw {
    from {
        stroke-dashoffset: 622.5;
    }
    to {
        stroke-dashoffset: 103.75;
    }
}

.logo-red-bottom {
    fill: none;
    stroke: #ff375c;
    stroke-linecap: round;
    stroke-miterlimit: 10;
    stroke-width: 5px;
    stroke-dasharray: 103.75;
    stroke-dashoffset: 415;
    animation: bottom-draw 4.5s linear;
}

@keyframes bottom-draw {
    to {
        stroke-dashoffset: 0;
    }
}

/* ----- FILTERS ----- */

#filter,
#places,
#reviews,
#place-details {
    min-width: 1200px;
}

select,
input[type="number"],
input[type="text"],
input[type="email"],
input[type="email"],
input[type="password"],
textarea {
    background-color: var(--color-medium-grey);
    border-radius: 3px;
    text-align: center;
    border: none;
    height: 2em;
}

textarea {
    text-align: left;
    padding: 5px;
    resize: none;
}

textarea::placeholder {
    text-align: center;
    line-height: 90px;
}

#amenities {
    position: absolute;
    background-color: var(--color-light-grey);
    border-radius: 10px;
    z-index: 1;
}

#amenities,
#amenities fieldset,
#amenities ul {
    border-radius: 10px;
    border-width: 3px;
    border-style: none;
}

.amenities-filter summary:hover,
.amenities-filter input:hover {
    cursor: pointer;
}

#amenities ul {
    background-color: var(--color-medium-grey);
    display: flex;
    flex-direction: column;
}

#amenities li {
    width: 100%;
    margin: 5px
}

#amenities li input {
    margin-right: 5px;
}

/* ----- CARDS ----- */

.filter-card {
    display: flex;
    align-items: center;
    justify-content: space-around;
}

.login-card,
.account-card,
.filter-card,
.place-card,
.place-details,
.place-submission,
.review-card,
.review-submission {
    min-height: 75px;
    margin: 20px;
    padding: 20px;
    background-color: var(--color-white);
    border-radius: 10px;
    transition: transform 0.25s ease-in-out;
    box-shadow:
		0 10px 15px rgba(0, 0, 0, 0.05),
		0 8px 10px rgba(0, 0, 0, 0.05);
}

.details-button,
.review-button,
.edit-button {
    border: 3px solid var(--color-medium-grey);
    border-radius: 10px;
    margin-top: 25px;
    width: 100%;
}

.details-button:hover,
.review-button:hover,
.edit-button:hover {
    background-color: var(--color-medium-grey);
    color: var(--color-dark-grey);
}

.place-card {
    min-height: 150px;
}

.info {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.review-rating {
    display: flex;
}

.review-bottom {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
}

.place-owner,
.review-user {
    margin-top: 15px;
    margin-right: 15px;
    margin-left: auto;
    text-align: right;
    font-weight: var(--font-weight-bold);
    color: var(--color-dark-grey);
}

.place-card .details,
.place-card .element {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.place-card .block {
    text-align: center;
}

.place-card .element {
    padding: 0 10px;
}

.place-card .place-description,
#reviews .review-text {
    text-align: justify;
}

.place-card .properties {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin: 25px 0;
}

.place-card .details .amenities {
    width: 25%;
    margin-left: 50px;
}

.place-card .details .info {
    width: 75%;
}

.account-card,
.login-card,
.review-submission,
.place-submission {
    width: 350px;
    height: 350px;
}

.place-submission {
    width: 350px;
    height: 600px;
}

.account-card #account,
.account-card #animation,
.login-card #login,
.login-card #animation,
.place-submission #place,
.review-submission #review {
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.amenity-item {
    margin: 10px;
    display: flex;
    height: 25px;
    align-items: center;
    text-align: center;
}

.amenity-item h5 {
    margin-left: 10px;
}

.place-submission textarea,
.review-submission textarea {
    width: 100%;
    height: 100px;
}

.place-card:hover,
.review-card:hover {
    transform: scale(1.05);
}

/* ----- STARS ----- */

.rating {
    display: flex;
    justify-content: center;
    cursor: pointer;
}

.rating path,
.rating div:hover ~ div svg path {
    fill: var(--color-medium-grey);
}

.rating:hover path {
    fill: var(--color-dark-grey);
}

/* ----- FOOTER ----- */

.footer {
    background-color: var(--color-light-grey);
    box-shadow: 
        0 0 75px 0 var(--color-dark-grey),
        0 0 100px 0 var(--color-medium-grey);
    color: var(--text-color);
    position: fixed;
    bottom: 0;
    width: 100%;
}

.footer p {
    padding: 1rem 1rem;
    text-align: center;
    font-size: var(--font-size-small);
}
