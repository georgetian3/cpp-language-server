var updating = false;
var need_update = false;

async function handle_update(element) {
    if (updating) {
        console.log('already updating');
        need_update = true;
        return;
    }
    updating = true;
    let response = await fetch('http://127.0.0.1:5000/process', {
        method: 'POST',
        body: element.innerText
    });
    let data = await response.json();
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
    updating = false;
    if (need_update) {
        append_text('');
    }
    need_update = false;
}

function append_text(text) {
    console.log('Appending text');
    var editor_parent = document.getElementById('editor');
    var editor_textarea = editor_parent.getElementsByTagName('textarea')[0];
    var editor_value = editor_parent.getElementsByTagName('pre')[0].getElementsByTagName('code')[0];
    
    editor_value.innerHTML += text;
    editor_parent.value += text;
    editor_textarea.dispatchEvent(new Event('input'));
}

function register() {
    console.log('here')
    codeInput.registerTemplate("syntax-highlighted", codeInput.templates.custom(
        handle_update,
        true, /* Optional - Is the `pre` element styled as well as the `code` element? Changing this to false uses the code element as the scrollable one rather than the pre element */
        true, /* Optional - This is used for editing code - setting this to true overrides the Tab key and uses it for indentation */
    ));
    document.addEventListener('keydown', function(key) {
        if (key.keyCode != 9) { // not a tab key
            return;
        }
        key.preventDefault();
        key.stopPropagation();
        append_text('    ');
    });
    
}

function autocomplete(suggestion) {
    text = suggestion.getElementsByTagName('span')[0].innerText;
    append_text(text);
}
