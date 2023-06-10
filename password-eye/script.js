var pass = document.querySelector('#password');
var showPass = document.querySelector('#showPassword');
var eyeIcon = document.querySelector('#eye');

showPass.addEventListener('click', () => {
    if (pass.getAttribute('type') === 'password' && pass.value !== '') {
        pass.setAttribute('type', 'text');
        eyeIcon.setAttribute('src', './view.png');
    } 
    else {
        pass.setAttribute('type', 'password');
        eyeIcon.setAttribute('src', './hide.png');
    }
});

pass.addEventListener('input', () => {
    if (pass.value === '') {
        eyeIcon.setAttribute('src', './hide.png');
    }
});
