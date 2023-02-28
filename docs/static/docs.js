const _starter_btn = document.getElementById("starter-btn");
const _starter_text = document.getElementById("starter-text");

_starter_btn.addEventListener("click", () => {
  navigator.clipboard.writeText(_starter_text.innerText);

  // alert("Copied to clipboard!");
});
