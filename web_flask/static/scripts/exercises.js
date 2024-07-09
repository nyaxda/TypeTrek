// Initiate the dropdown menu
document.querySelector('.dropdown-btn').addEventListener('click', function() {
    var dropdownContent = document.querySelector('.dropdown-content');
    dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
});

// Close the dropdown menu if the user clicks outside of it
document.addEventListener('click', function(event) {
    var dropdownBtn = document.querySelector('.dropdown-btn');
    var dropdownContent = document.querySelector('.dropdown-content');
    var isClickInside = dropdownBtn.contains(event.target) || dropdownContent.contains(event.target);

    if (!isClickInside) {
        dropdownContent.style.display = 'none';
    }
});

let selectedExerciseId = null;

// Handle the selection of an exercise
document.querySelectorAll('.exercise-item').forEach(function(item) {
    item.addEventListener('click', function() {
        // Highlight the selected item
        document.querySelectorAll('.exercise-item').forEach(function(item) {
            item.classList.remove('selected');
        });
        this.classList.add('selected');

        // Enable the "Start Exercise" button
        document.getElementById('start-exercise-btn').disabled = false;

        // Store the ID of the selected exercise
        selectedExerciseId = this.getAttribute('data-id');
    });
});

document.getElementById('start-exercise-btn').addEventListener('click', function() {
    if (selectedExerciseId) {
        // Navigate to the exercise page
        window.location.href = `/exercises/${selectedExerciseId}`;
    }
});
