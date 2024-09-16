function switchSection(sectionId, element) {
    const sections = ['user_table', 'sessoes_table', 'perfis_table', 'notas_table', 'lixeira_table'];
    const tables = ['users', 'sessions', 'perfil', 'notes', 'lixeira'];

    const div_text = document.getElementById('div_text');
    let selectedTable = 'user';  // Define 'user' como valor padrão

    // Oculta todas as seções
    sections.forEach((id, index) => {
        document.getElementById(id).style.display = (id === sectionId) ? 'flex' : 'none';

        // Atualiza a tabela se houver uma correspondência com sectionId
        if (sectionId === sections[index]) {
            selectedTable = tables[index];  // Atualiza a tabela com base no index
        }
    });

    // Remove a classe 'selected' de todos os botões
    const allTags = document.querySelectorAll('.tags_table');
    allTags.forEach(tag => tag.classList.remove('selected'));

    // Adiciona a classe 'selected' ao botão atual, se houver
    if (element) {
        element.classList.add('selected');
    }

    // Adiciona eventos a todos os checkboxes
    let checkboxes = document.querySelectorAll('.row-select');
    let antigo = null;  // Variável para armazenar o checkbox anteriormente selecionado

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('click', function () {
            let type = selectedTable;  // Usa a tabela selecionada

            // Se houver outro checkbox já marcado, desmarque-o
            if (antigo && antigo !== this) {
                antigo.checked = false;  // Desmarca o anterior
                antigo.closest('tr').style.backgroundColor = '';  // Remove a cor de fundo do anterior
            }

            if (this.checked) {
                this.closest('tr').style.backgroundColor = '#0084ff75';
                div_text.style.opacity = '1';
                div_text.querySelector('#selec_table').innerText = 'TABELA ' + type.toUpperCase() + ' SELECIONADA';
                
                // Atualiza o checkbox previamente selecionado
                antigo = this;
            } else {
                this.closest('tr').style.backgroundColor = '';
                div_text.style.opacity = '0';
                
                // Se o checkbox atual for desmarcado, zera a variável
                antigo = null;
            }
            // Função para preencher formulário e exibir o div correspondente
            function preencherFormularioEExibirDiv(type, action) {
                var div = document.getElementById(action + '_row_' + type);
                let fechar = document.querySelectorAll('.fechar'); // Seleciona os botões de fechar

                // Pega os valores da linha selecionada
                let linhaSelecionada = document.querySelector('tr .row-select:checked').closest('tr'); // Busca a linha com o checkbox marcado
                let inputs = linhaSelecionada.querySelectorAll('input.inputs');

                // Preenche o primeiro input com o valor do tipo (type)
                let formInputs = document.querySelectorAll('#' + action + '_row_' + type + ' .form input');
                formInputs[0].value = type;  // O primeiro input recebe o valor de `type`

                // Preenche os demais campos do formulário com os valores da linha selecionada
                formInputs.forEach((formInput, index) => {
                    if (index > 0 && inputs[index - 1]) {  // Começa a partir do segundo input do form
                        formInput.value = inputs[index - 1].value;
                    }
                });

                // Exibe o div correspondente ao tipo selecionado
                if (div) {
                    div.style.display = 'flex';
                    fechar.forEach(fecha => {
                        fecha.addEventListener('click', (e) => {
                            div.style.display = 'none';
                        });
                    });
                } else {
                    console.log('Elemento não encontrado para o tipo: ' + type);
                }
            }

            // Evento de clique no botão 'alterar'
            document.getElementById('alterar').addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                preencherFormularioEExibirDiv(type, 'edit');
            });

            // Evento de clique no botão 'deletar'
            document.getElementById('deletar').addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                preencherFormularioEExibirDiv(type, 'delete');
            });

        });
    });
}


document.addEventListener('DOMContentLoaded', function() {
    switchSection('user_table', null);
    
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
