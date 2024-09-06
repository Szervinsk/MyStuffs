function switchSection(sectionId, title, content, createdAt, noteId) {
    console.log('Abrindo do lado');

    const sections = ['add_notes', 'no_notes', 'edit_notes'];
    sections.forEach(id => {
        document.getElementById(id).style.display = (id === sectionId) ? 'flex' : 'none';
    });

    if (sectionId === 'edit_notes') {
        document.getElementById('title_ed').value = title;
        document.getElementById('content_ed').value = content;
        console.log(noteId)
        document.getElementById('noteId_ed').value = noteId;
        document.getElementById('noteId_del').value = noteId;
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