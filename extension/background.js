console.log("Privacy Agent background service worker started");

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "PAGE_DATA") {
    console.log("Sending page data to FastAPI...");

    fetch("http://127.0.0.1:8000/api/capture", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        content: message.data.content
      })
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("FastAPI response:", data);
        sendResponse({
          status: "success",
          backendResponse: data
        });
      })
      .catch((error) => {
        console.error("Error sending data to FastAPI:", error);
        sendResponse({
          status: "error",
          message: error.message
        });
      });

    return true;
  }
});