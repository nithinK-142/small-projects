//code for blocking dark-reader extension
const lock = document.createElement('meta');
lock.name = 'darkreader-lock';
document.head.appendChild(lock);

// Get the progress bar elements
const scrollBar1 = document.querySelector('.leftToRight');
const scrollBar2 = document.querySelector('.rightToLeft');
const scrollBar3 = document.querySelector('.topToBottom');
const scrollBar4 = document.querySelector('.bottomToTop');

// scroll event
window.addEventListener('scroll', () => {

  // Get the current scroll position
  const scrollTop1 = document.documentElement.scrollTop || document.body.scrollTop;

  // Calculate the scrollable height
  const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;

  // Calculate the scroll progress in percentage
  const progress = (scrollTop1 / scrollHeight) * 100;

  // Update the width of progress bars
  scrollBar1.style.width = progress + '%';
  scrollBar2.style.width = progress + '%';

  // Update the height of progress bars
  scrollBar3.style.height = progress + '%';
  scrollBar4.style.height = progress + '%';

});