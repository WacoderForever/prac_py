chrome.action.onClicked.addListener((tab) => {
    chrome.scripting.executeScript({
      target: {tabId: tab.id},
      function: sendVideoURL,
    });
  });
  
  function sendVideoURL() {
    const url = window.location.href;
    if (url.includes("youtube.com/watch")) {
      fetch('http://localhost:5000/download', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({url: url}),
      })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch((error) => {
        console.error('Error:', error);
      });
    } else {
      alert("This is not a YouTube video page.");
    }
  }
  