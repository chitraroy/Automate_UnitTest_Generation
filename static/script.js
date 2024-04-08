document.getElementById("generateTestButton").addEventListener("click", function() {
    const codeBlock = document.getElementById("codeInput").value;
    if (codeBlock) {
        fetch('/generate-test', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ code: codeBlock }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            // Display the generated unit test
            document.getElementById("testResult").textContent = data.test;
            // Display the explanation for the generated unit test
            document.getElementById("testExplanation").textContent = data.explanation;
        })
        .catch((error) => {
            console.error('Error:', error);
            document.getElementById("testResult").textContent = "Error generating unit test.";
            document.getElementById("testExplanation").textContent = "Error generating explanation.";
        });
    } else {
        alert("Please paste a block of code.");
    }
});