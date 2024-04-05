function summarizeText() {
    // Show loader and disable button
    document.getElementById("loader").classList.remove("hidden");
    document.getElementById("summarize-text-btn").disabled = true;

    var text = document.getElementById("text-input").value;
    fetch('/text_summarization', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            text: text
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("summary-result").innerHTML = "<h2>Text Summary</h2><p>" + data.summary + "</p>";
    })
    .catch(error => console.error('Error:', error))
    .finally(() => {
        // Hide loader and enable button after response
        document.getElementById("loader").classList.add("hidden");
        document.getElementById("summarize-text-btn").disabled = false;
    });
}

function summarizeURL() {
    // Show loader and disable button
    document.getElementById("loader").classList.remove("hidden");
    document.getElementById("summarize-url-btn").disabled = true;

    var url = document.getElementById("url-input").value;
    fetch('/web_summarization', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            url: url
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("summary-result").innerHTML = "<h2>Web Summary</h2><p>" + data.summary + "</p>";
    })
    .catch(error => console.error('Error:', error))
    .finally(() => {
        // Hide loader and enable button after response
        document.getElementById("loader").classList.add("hidden");
        document.getElementById("summarize-url-btn").disabled = false;
    });
}

