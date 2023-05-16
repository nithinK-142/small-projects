const scrollProgress = document.getElementById('scroll-progress');

window.addEventListener('scroll', () => {

  const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
  const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const progress = (scrollTop / scrollHeight) * 100;

  scrollProgress.style.width = progress + '%';
});