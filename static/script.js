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
            // Update this line to display the generated unit test
            document.getElementById("testResult").textContent = data.test;
        })
        .catch((error) => {
            console.error('Error:', error);
            // Optionally handle errors by displaying them to the user as well
            document.getElementById("testResult").textContent = "Error generating unit test.";
        });
    } else {
        alert("Please paste a block of code.");
    }
});