document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
          event.preventDefault();
          const email = document.getElementById('email').value.trim();
          const password = document.getElementById('password').value.trim();

          if (!email || !password) {
             alert('Please enter both email and password.');
              return;
          }

          try{
            await loginUser(email, password);
          } catch(error) {
              console.error('Login failed:', error);
              alert('An error occurred during login. Please try again.');
          }
        });
      }
  });

  async function loginUser(email, password) {
    const response = await fetch('http://localhost:5000/api/v1/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
        body: JSON.stringify({ email, password }),
        credentials: 'include'  // Include cookies for session management
    });

    if (response.ok) {
      const data = await response.json();
      document.cookie = `token=${data.access_token}; path=/`;
      window.location.href = '/index';
    } else {
      const errorData = await response.json();
      const errorMsg = errorData.message || response.statusText;
      alert('Login failed: ' + errorMsg);
    }
  }