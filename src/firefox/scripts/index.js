/**
 * Check and set a global guard variable.
 * If this content script is injected into the same page again,
 * it will do nothing next time.
 */
(() => {
  if (window.hasRun) {
  return;
  }
  window.hasRun = true;
})();

function encode(source) {
  let encoded = "";

  if (source.length > 0){
    for (let i = 0; i < source.length; i++) {
      encoded += `&#${source.charCodeAt(i)};`;
    }
  
    return {
      source,
      encoded,
    }
    }
  }
  

function clearInput() {
  const input = document.querySelector(".input-text");
  input.value = "";
}

const encodeButton = document.querySelector(".encode-btn");

if (encodeButton !== null) {
  encodeButton.addEventListener("click", async (event) => {
    event.preventDefault();
  
    const text = document.querySelector(".input-text");
  
    if (text.value.length > 0) {
      const encodedText = encode(text.value);
  
      try {
  
        await navigator.clipboard.writeText(encodedText.encoded).then(() => {
          console.log("GFY-dir.bg: Copied!");
          console.log(`Result: ${encodedText}`);
        });
    
        clearInput();
    
        encodeButton.innerText = 'Copied!'
    
        setTimeout(() => {
          encodeButton.innerText = 'Encode and Copy';
        }, 2 * 1000);
    
      } catch (error) {
        console.error(error.message);
      }
    
      clearInput();
    }
  });
}
