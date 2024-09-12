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

document.getElementById('delete').addEventListener('click', (e) => {
    e.preventDefault();

    const fundoblur = document.getElementById('fundoblur');
    const modal = document.getElementById('modal_deleteUser');

    // Exibe o fundo e o modal
    fundoblur.style.display = 'block';
    modal.style.display = 'flex';
});

document.getElementById('fundoblur').addEventListener('click', () => {
    const fundoblur = document.getElementById('fundoblur');
    const modal = document.getElementById('modal_deleteUser');

    // Oculta o fundo e o modal quando o fundo é clicado
    fundoblur.style.display = 'none';
    modal.style.display = 'none';
});

document.getElementById('cancelar').addEventListener('click', () => {
    const fundoblur = document.getElementById('fundoblur');
    const modal = document.getElementById('modal_deleteUser');

    // Oculta o fundo e o modal quando o fundo é clicado
    fundoblur.style.display = 'none';
    modal.style.display = 'none';
});

