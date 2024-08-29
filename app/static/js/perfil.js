function openPass(){
    page = document.getElementById('password')
    otherpage = document.getElementById('profile')
    page.style.display = 'flex'
    otherpage.style.display = 'none'
}
function openEdit(){
    page = document.getElementById('profile')
    otherpage = document.getElementById('password')
    page.style.display = 'flex'
    otherpage.style.display = 'none'
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
});