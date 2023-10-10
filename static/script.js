document.addEventListener('DOMContentLoaded', function () {
    const summarizeButton = document.getElementById('summarize-button');
    const inputText = document.getElementById('input-text');
    const outputText = document.getElementById('output-text');

    summarizeButton.addEventListener('click', async () => {
        const textToSummarize = inputText.value;

        // Send a POST request to your Flask route
        const response = await fetch('/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ text: textToSummarize }),
        });

        if (response.ok) {
            const result = await response.json();
            outputText.textContent = result.summary;
        } else {
            outputText.textContent = 'Error occurred while summarizing.';
        }
    });
});
