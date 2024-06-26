// Toggle dropdown menu on button click
document.querySelector('.dropdown-btn').addEventListener('click', function() {
    var dropdownContent = document.querySelector('.dropdown-content');
    dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
});

// Close dropdown menu when clicking outside of it
document.addEventListener('click', function(event) {
    var dropdownBtn = document.querySelector('.dropdown-btn');
    var dropdownContent = document.querySelector('.dropdown-content');
    var isClickInside = dropdownBtn.contains(event.target) || dropdownContent.contains(event.target);

    if (!isClickInside) {
        dropdownContent.style.display = 'none';
    }
});
