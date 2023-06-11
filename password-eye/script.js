const pass = document.querySelector('#password');
const showPass = document.querySelector('#showPassword');
const eyeIcon = document.querySelector('#eye');

showPass.addEventListener('click', () => {
  if (pass.value && pass.type === 'password') {
    pass.type = 'text';
    eyeIcon.src = './view.png';
  } else {
    pass.type = 'password';
    eyeIcon.src = './hide.png';
  }
});

pass.addEventListener('input', () => {
  if (!pass.value) {
    eyeIcon.src = './hide.png';
  }
});
