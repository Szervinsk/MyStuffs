function switchSection(sectionId, title) {
    const sections = ['profile', 'password', 'tools'];
    sections.forEach(id => {
        document.getElementById(id).style.display = (id === sectionId) ? 'flex' : 'none';
    });
    document.querySelector('.namepage').textContent = title;
}

document.addEventListener('DOMContentLoaded', function() {
    var messageElement = document.getElementById('msg');
    if (messageElement) {
        messageElement.addEventListener('click', function() {
            messageElement.style.display = 'none'
        });

        setTimeout(function() {
            messageElement.style.display = 'none'
        }, 5000);
    }

    document.getElementById('confirm').addEventListener('input', (e) => {
        console.log('opa')
        const button = document.getElementById('alterar');
        const passwordValue = document.getElementById('newpassword').value;
        const spanAlert = document.getElementById('spanAlert');
        const confirmpassword = e.target;
    
        if (confirmpassword.value !== passwordValue) {
            confirmpassword.style.outlineColor = '#ff2c2c';
            spanAlert.style.color = '#ff2c2c';
            spanAlert.textContent = 'As senhas não batem';
            button.disabled = true;
            button.style.opacity = '0.5';
            
        } else {
            confirmpassword.style.outlineColor = '#00e45f';
            spanAlert.style.color = '#00e45f';
            spanAlert.textContent = 'As senhas coincidem';
            button.disabled = false;
            button.style.opacity = '1';
        }
    });
});

