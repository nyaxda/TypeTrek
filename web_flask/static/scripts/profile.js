document.getElementById('user-info-btn').addEventListener('click', function() {
    document.getElementById('user-info').style.display = 'block';
    document.getElementById('change-password').style.display = 'none';
    this.classList.add('active');
    document.getElementById('change-password-btn').classList.remove('active');
});

document.getElementById('change-password-btn').addEventListener('click', function() {
    document.getElementById('user-info').style.display = 'none';
    document.getElementById('change-password').style.display = 'block';
    this.classList.add('active');
    document.getElementById('user-info-btn').classList.remove('active');
});

document.getElementById('change-password-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const currentPassword = document.getElementById('current-password').value;
    const newPassword = document.getElementById('new-password').value;
    const confirmNewPassword = document.getElementById('confirm-new-password').value;

    if (newPassword !== confirmNewPassword) {
        document.getElementById('change-password-message').textContent = 'New passwords do not match.';
        document.getElementById('change-password-message').style.color = 'red';
        return;
    }

    fetch('{{ url_for('main.change_password') }}', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            current_password: currentPassword,
            new_password: newPassword
        })
    }).then(response => response.json())
    .then(data => {
        document.getElementById('change-password-message').textContent = data.message;
        document.getElementById('change-password-message').style.color = data.status === 'success' ? 'green' : 'red';
    }).catch((error) => {
        console.error('Error:', error);
        document.getElementById('change-password-message').textContent = 'An error occurred: ' + error.message;
        document.getElementById('change-password-message').style.color = 'red';
    });
});
