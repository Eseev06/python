document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.registration-form');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            const password1 = document.getElementById('id_password1').value;
            const password2 = document.getElementById('id_password2').value;
            const terms = document.getElementById('id_terms').checked;
            
            if (password1 !== password2) {
                e.preventDefault();
                alert('Пароли не совпадают!');
                document.getElementById('id_password1').focus();
                return;
            }
            
            if (password1.length < 8) {
                e.preventDefault();
                alert('Пароль должен содержать минимум 8 символов!');
                document.getElementById('id_password1').focus();
                return;
            }
            
            if (!terms) {
                e.preventDefault();
                alert('Необходимо согласиться с условиями использования!');
                return;
            }
        });
    }
});