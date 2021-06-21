const searchIcon = document.getElementById('search_icon');
const sBar = document.getElementById('search_bar');
const searchCancel = document.getElementById('search_cancel');


searchIcon.addEventListener('click', () => {
    sBar.classList.remove('search-bar');
    searchIcon.style.display = 'none';
});


searchCancel.addEventListener('click', () => {
    sBar.classList.add('search-bar');
    searchIcon.style.display = 'initial';
})