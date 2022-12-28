function handle_update(element) {
    fetch('http://127.0.0.1:5000/process', {
        method: 'POST',
        body: element.innerText
    })
    .then(response => response.json())
    .then((data) => {
        element.innerHTML = data.formatting;
        let suggestions = document.getElementById('suggestions')
        suggestions.innerHTML = '';
        for (const suggestion of data.suggestions) {
            console.log(suggestion);
            let button = document.createElement('code');
            button.setAttribute('class', 'suggestion');
            button.setAttribute('onclick', 'autocomplete(this);');
            button.innerHTML = suggestion;
            suggestions.appendChild(button);
        }
    });
}

function register() {
    console.log('here')
    codeInput.registerTemplate("syntax-highlighted", codeInput.templates.custom(
        handle_update,
        true, /* Optional - Is the `pre` element styled as well as the `code` element? Changing this to false uses the code element as the scrollable one rather than the pre element */
        true, /* Optional - This is used for editing code - setting this to true overrides the Tab key and uses it for indentation */
        false /* Optional - Setting this to true passes the `<code-input>` element as a second argument to the highlight function to be used for getting data- attribute values and using the DOM for the code-input */,
        [] // Array of plugins (see below)
    ));
}

function autocomplete(suggestion) {
    let editor_parent = document.getElementById('editor');
    let editor_textarea = editor_parent.getElementsByTagName('textarea')[0];
    let editor_value = editor_parent.getElementsByTagName('pre')[0].getElementsByTagName('code')[0];
    console.log(editor_parent, editor_textarea, editor_value);
    text = suggestion.getElementsByTagName('span')[0].innerText;
    editor_value.innerHTML += text;
    editor_parent.value += text;
    editor_textarea.dispatchEvent(new Event('input'));
}
/* document.addEventListener('keydown', function(key) {
  if (key.keyCode != 9) { // not a tab key
    return;
  }
  key.preventDefault();
  key.stopPropagation();
  console.log(key);
  autocomplete();
}); */