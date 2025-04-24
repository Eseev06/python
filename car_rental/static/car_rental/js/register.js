document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.registration-form');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            const password1 = document.getElementById('id_password1');
            const password2 = document.getElementById('id_password2');
            const terms = document.getElementById('id_terms');
            let isValid = true;

            // Очистка предыдущих сообщений об ошибках
            document.querySelectorAll('.error-message').forEach(el => el.remove());

            // Проверка совпадения паролей
            if (password1.value !== password2.value) {
                isValid = false;
                showError(password1, 'Пароли не совпадают!');
                showError(password2, 'Пароли не совпадают!');
            }

            // Проверка длины пароля
            if (password1.value.length < 8) {
                isValid = false;
                showError(password1, 'Пароль должен содержать минимум 8 символов!');
            }

            // Проверка согласия с условиями
            if (!terms.checked) {
                isValid = false;
                showError(terms, 'Необходимо согласиться с условиями использования!');
            }

            if (!isValid) {
                e.preventDefault();
            }
        });
    }

    function showError(element, message) {
        const error = document.createElement('div');
        error.className = 'error-message';
        error.style.color = 'red';
        error.style.fontSize = '12px';
        error.textContent = message;
        element.parentNode.appendChild(error);
        element.focus();
    }
});