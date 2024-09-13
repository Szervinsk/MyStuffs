function switchSection(sectionId, title, content, createdAt, noteId) {
    const sections = ['add_notes', 'no_notes', 'edit_notes','delete_notes'];
    sections.forEach(id => {
        document.getElementById(id).style.display = (id === sectionId) ? 'flex' : 'none';
    });
    
    console.log(sectionId)
    console.log(title + '\n' + content + '\n' + createdAt + '\n' + noteId)

    article = document.querySelector('article')

    if (sectionId === 'edit_notes') {
        article.style.border = '2.5px solid #0085FF' //azul
        document.getElementById('title_ed').value = title;

        const formattedContent = content.replace(/<br\s*\/?>/gi, '\n');
        document.getElementById('content_ed').value = formattedContent;

        document.getElementById('noteId_ed').value = noteId;
        document.getElementById('noteId_del').value = noteId;
        
    } else if (sectionId === 'delete_notes') {
        article.style.border = '2.5px solid #ff2c2c' //red
        document.getElementById('title_del').value = title;
        const formattedContent = content.replace(/<br\s*\/?>/gi, '\n');
        document.getElementById('content_del').value = formattedContent;

        document.getElementById('noteId_delp').value = noteId;
        document.getElementById('noteId_res').value = noteId;
    } else {
        article.style.border = 'none'
    }
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
    }});

    let searchbar = document.getElementById('searchbar');

    searchbar.addEventListener('input', (e) => {
        e.preventDefault();
        
        let searchValue = searchbar.value.toLowerCase();  
        let blocks = document.querySelectorAll('.bloquin');  
        
        blocks.forEach(div => {
            let titleElement = div.querySelector('.title');  
            if (titleElement) {  
                let title = titleElement.textContent.toLowerCase().trim();  
                if (title.includes(searchValue)) {
                    div.style.display = 'flex'; 
                    div.querySelectorAll('hr').display = 'block'
                    div.style.flexDirection = 'column';  
                } else {
                    div.style.display = 'none'; 
                }
            }
        });
    });

    document.querySelectorAll('.bloquin p').forEach(p => {

        let text = p.textContent;
        let maxlength = 100;

        if (text.length >= maxlength) {
            p.textContent = text.slice(0,maxlength) + ' (...)';
        }
    })
    
    let pasta = document.getElementById('geral');
    pasta.addEventListener('click', (e) => {
        e.preventDefault();
        let div = document.getElementById('div_pasta');
        let icon = document.getElementById('icon')

        // Verificar o estilo atual de display da div
        if (div.style.display === 'flex') {
            div.style.display = 'none';  // Ocultar se estiver visível
            icon.classList.remove('bi-folder2-open');  // Remover o ícone de "aberto"
            icon.classList.add('bi-folder2');  // Adicionar o ícone de "fechado"
        } else {
            div.style.display = 'flex';  // Exibir se estiver oculto
            icon.classList.remove('bi-folder2');  // Remover o ícone de "fechado"
            icon.classList.add('bi-folder2-open');  // Adicionar o ícone de "aberto"
        }
        
    });

    let favoritos = document.getElementById('favoritos');
    favoritos.addEventListener('click', (e) => {
        e.preventDefault();
        let div = document.getElementById('div_favoritos');
        
        // Verificar o estilo atual de display da div
        if (div.style.display === 'flex') {
            div.style.display = 'none';  // Ocultar se estiver visível
        } else {
            div.style.display = 'flex';  // Exibir se estiver oculto
        }
    });

    let lixeira = document.getElementById('lixeira');
    lixeira.addEventListener('click', (e) => {
        e.preventDefault();
        let div = document.getElementById('div_lixeira');
        
        // Verificar o estilo atual de display da div
        if (div.style.display === 'flex') {
            div.style.display = 'none';  // Ocultar se estiver visível
        } else {
            div.style.display = 'flex';  // Exibir se estiver oculto
        }
    });

    function favorite(element, noteId) {

        if (element.style.color === 'gold') {
            console.log('desativou');
            element.style.color = 'grey';

            fetch(`/toggle-favorite`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',  // Informa que o conteúdo é JSON
                },
                body: JSON.stringify({
                    id: noteId,        // Envia o ID da nota
                    isFavorite: 0      // Indica que a nota foi marcada como favorita
                }),
            })
            .then(response => response.json())
        } else {
            console.log('ativou');
            element.style.color = 'gold';
    
            // Envia os dados via fetch
            fetch(`/toggle-favorite`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',  // Informa que o conteúdo é JSON
                },
                body: JSON.stringify({
                    id: noteId,        // Envia o ID da nota
                    isFavorite: 1      // Indica que a nota foi marcada como favorita
                }),
            })
            .then(response => response.json())
        }
    }
    
