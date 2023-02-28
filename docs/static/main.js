const _alart = document.getElementById("construction-alart");
const _alart_button = document.getElementById("construction-alart-button");

_alart_button.addEventListener("click", () => {
  _alart.classList.add("hidden");
  setTimeout(() => {
    _alart.remove();
  }, 550);
});

const _install_button = document.getElementById("pip-install");
const _install_button_text = document.getElementById("pip-install-text");

_install_button.addEventListener("click", () => {
  _install_button_text.innerText = "Copied!";
  navigator.clipboard.writeText("pip install fronty");
  _install_button_text.classList.remove("code-install");
  _install_button_text.classList.add("code-string");
  setTimeout(() => {
    _install_button_text.innerText = "pip install fronty";
    _install_button_text.classList.remove("code-string");
    _install_button_text.classList.add("code-install");
  }, 1000);
});
