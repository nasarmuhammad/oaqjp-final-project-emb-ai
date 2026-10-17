function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const resultElement = document.getElementById("system_response");

    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            if (this.status === 200 || this.status === 400) {
                resultElement.textContent = this.responseText;
            } else {
                resultElement.textContent =
                    "Unable to analyze the text. Please try again.";
            }
        }
    };

    const url = "/emotionDetector?textToAnalyze=" +
        encodeURIComponent(textToAnalyze);

    xhttp.open("GET", url, true);
    xhttp.send();
}
