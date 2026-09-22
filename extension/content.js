console.log("Privacy Agent content script loaded");

const pageData = {
  title: document.title,
  content: document.body.innerText
};

console.log("Page title:", pageData.title);
console.log("Page text length:", pageData.content.length);

chrome.runtime.sendMessage({
  type: "PAGE_DATA",
  data: pageData
});