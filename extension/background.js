console.log("Privacy Agent background service worker started");

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.type === "PAGE_DATA") {
    console.log("Page data received from content script:");
    console.log("Title:", message.data.title);
    console.log("Content length:", message.data.content.length);

    sendResponse({
      status: "received"
    });
  }
});