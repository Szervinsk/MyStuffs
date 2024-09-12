function switchSection(sectionId, element) {
    const sections = ['user_table', 'sessoes_table', 'perfis_table', 'notas_table', 'lixeira_table'];
    
    // Oculta todas as seções
    sections.forEach(id => {
        document.getElementById(id).style.display = (id === sectionId) ? 'flex' : 'none';
    });

    // Remove a classe 'selected' de todos os botões
    const allTags = document.querySelectorAll('.tags_table');
    allTags.forEach(tag => tag.classList.remove('selected'));

    // Adiciona a classe 'selected' ao botão clicado
    element.classList.add('selected');
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
})

document.querySelectorAll('.conteudo').forEach(p => {

    let text = p.textContent;
    let maxlength = 100;

    if (text.length >= maxlength) {
        p.textContent = text.slice(0,maxlength) + ' (...)';
    }
})

let searchbar = document.getElementById('filtro');

searchbar.addEventListener('input', () => {
    let searchValue = searchbar.value.toLowerCase();
    let tableRows = document.querySelectorAll('tbody tr');

    tableRows.forEach(row => {
        let rowText = '';

        let inputs = row.querySelectorAll('.inputs');
        
        inputs.forEach(input => {
            rowText += input.value.toLowerCase(); // Concatena o valor de cada input
        });

        if (rowText.includes(searchValue)) {
            row.style.display = '';  
        } else {
            row.style.display = 'none';  
        }
    });
});


let radio = document.querySelectorAll('.tr')
radio.addEventListener('click', (e)=> {
    console.log('opa')
})