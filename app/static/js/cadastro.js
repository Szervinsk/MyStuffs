document.addEventListener('DOMContentLoaded', function() {

    const btns = document.querySelectorAll('.scroll_btn');
    const radios = document.querySelectorAll('input[name="ball"]');
    const scrollbar = document.getElementById('form_scroll');
    const scrollAmount = scrollbar.scrollWidth / 3; // Um terço do tamanho do scroll

    // Função para rolar o formulário
    function scrollToPosition(position) {
        scrollbar.scrollTo({ left: position * scrollAmount, behavior: "smooth" });
        radios[position].checked = true;
    }

    // Adiciona evento aos botões "Próximo"
    btns.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const newScrollPosition = scrollbar.scrollLeft + scrollAmount; //mover a barra 
            scrollToPosition(Math.round(newScrollPosition / scrollAmount)); // Atualiza o rádio correspondente
        });
    });

    // Adiciona evento aos rádios para controlar o scrollbar
    radios.forEach((radio, index) => {
        radio.addEventListener('change', (e) => {
            e.preventDefault()
            if (radio.checked) {
                scrollToPosition(index);
            }
        });
    });

    document.getElementById('confirm_password').addEventListener('input', (e) => {
        const passwordValue = document.getElementById('password').value;
        const confirmpassword = e.target;
    
        if (confirmpassword.value !== passwordValue) {
            confirmpassword.style.outlineColor = '#ff2c2c';
        } else {
            confirmpassword.style.outlineColor = '#00e45f';
        }
    });
});


