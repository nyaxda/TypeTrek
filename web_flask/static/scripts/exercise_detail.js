document.addEventListener('DOMContentLoaded', () => {
    let startTime;
    const content = "{{ exercise.content }}";
    const userInput = document.getElementById('user-input');
    const exerciseText = document.getElementById('exercise-text');
    const accuracyElem = document.getElementById('accuracy');
    const wpmElem = document.getElementById('wpm');
    const spmElem = document.getElementById('spm');
    const nextExerciseBtn = document.getElementById('next-exercise-btn');
    const backBtn = document.getElementById('back-btn');
    const cancelBtn = document.getElementById('cancel-btn');
    const redoExerciseBtn = document.getElementById('redo-exercise-btn');
    const completionButtons = document.getElementById('completion-buttons');

    userInput.addEventListener('input', function() {
        if (!startTime) {
            startTime = new Date();
        }

        const userText = userInput.value;
        const accuracy = calculateAccuracy(content, userText);
        const timeElapsed = (new Date() - startTime) / 1000 / 60; // time in minutes
        const wordsTyped = userText.split(' ').filter(Boolean).length;
        const strokesTyped = userText.length;
        const wpm = (wordsTyped / timeElapsed).toFixed(2);
        const spm = (strokesTyped / timeElapsed).toFixed(2);

        accuracyElem.textContent = `${accuracy}%`;
        wpmElem.textContent = wpm;
        spmElem.textContent = spm;

        updateExerciseText(content, userText);

        if (userText.length >= content.length) {
            userInput.disabled = true;
            completionButtons.style.display = 'flex';
            nextExerciseBtn.disabled = false;
            cancelBtn.style.display = 'none';
        }
    });

    function calculateAccuracy(content, userText) {
        const contentChars = content.split('');
        const userChars = userText.split('');
        let correctChars = 0;

        contentChars.forEach((char, index) => {
            if (userChars[index] === char) {
                correctChars++;
            }
        });

        return ((correctChars / contentChars.length) * 100).toFixed(2);
    }

    function updateExerciseText(content, userText) {
        let updatedText = '';
        for (let i = 0; i < content.length; i++) {
            if (i < userText.length) {
                if (content[i] === userText[i]) {
                    updatedText += `<span class="correct">${content[i]}</span>`;
                } else {
                    updatedText += `<span class="incorrect">${content[i]}</span>`;
                }
            } else {
                updatedText += `<span>${content[i]}</span>`;
            }
        }
        exerciseText.innerHTML = updatedText;
    }

    function saveProgress(accuracy, wpm, spm) {
        return fetch('{{ url_for('main.save_progress') }}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                exercise_id: {{ exercise.id }},
                accuracy: accuracy,
                wpm: wpm,
                spm: spm
            })
        }).then(response => response.json())
        .then(data => {
            console.log('Progress saved:', data);
        }).catch((error) => {
            console.error('Error:', error);
        });
    }

    nextExerciseBtn.addEventListener('click', function() {
        const accuracy = accuracyElem.textContent.replace('%', '');
        const wpm = wpmElem.textContent;
        const spm = spmElem.textContent;
        saveProgress(accuracy, wpm, spm).then(() => {
            fetch('{{ url_for('main.next_exercise') }}?current_exercise_id={{ exercise.id }}&difficulty_level={{ exercise.difficulty_level }}')
                .then(response => response.json())
                .then(data => {
                    if (data.next_exercise_id) {
                        window.location.href = "{{ url_for('main.exercise', exercise_id=0) }}".replace('0', data.next_exercise_id);
                    } else {
                        window.location.href = "{{ url_for('main.exercises') }}";
                    }
                });
        });
    });

    backBtn.addEventListener('click', function() {
        const accuracy = accuracyElem.textContent.replace('%', '');
        const wpm = wpmElem.textContent;
        const spm = spmElem.textContent;
        saveProgress(accuracy, wpm, spm).then(() => {
            window.location.href = "{{ url_for('main.exercises') }}";
        });
    });

    cancelBtn.addEventListener('click', function() {
        if (confirm('Are you sure you want to cancel the exercise?')) {
            window.location.href = "{{ url_for('main.exercises') }}";
        }
    });

    redoExerciseBtn.addEventListener('click', function() {
        userInput.value = '';
        accuracyElem.textContent = '0%';
        wpmElem.textContent = '0';
        spmElem.textContent = '0';
        exerciseText.innerHTML = content;
        userInput.disabled = false;
        startTime = null;
        completionButtons.style.display = 'none';
        nextExerciseBtn.disabled = true;
        cancelBtn.style.display = 'inline-block';
    });

    // Prevent pasting in the textarea
    userInput.addEventListener('paste', function(e) {
        e.preventDefault();
    });

    // Prevent selecting and copying the exercise content
    exerciseText.addEventListener('copy', function(e) {
        e.preventDefault();
    });

    exerciseText.addEventListener('mousedown', function(e) {
        e.preventDefault();
    });

    exerciseText.addEventListener('selectstart', function(e) {
        e.preventDefault();
    });
});
