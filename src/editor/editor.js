var updating = false;
var need_update = false;


var editor_parent;
var editor_textarea;
var editor_value;
var suggestions_list;

function escapeHtml(unsafe) {
    return unsafe
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
}

function get_cursor() {
    return editor_textarea.selectionStart;
}

function set_cursor(pos) {
    editor_textarea.selectionStart = pos;
    editor_textarea.selectionEnd = pos;
}

async function handle_update(element) {
    if (editor_parent === undefined) {
        editor_parent = document.getElementById('editor');
        editor_textarea = editor_parent.getElementsByTagName('textarea')[0];
        editor_value = editor_parent.getElementsByTagName('pre')[0].getElementsByTagName('code')[0];
        suggestions_list = document.getElementById('suggestions');
    }
    if (updating) {
        console.log('already updating');
        need_update = true;
        return;
    }
    console.log('cursor', get_cursor());
    updating = true;
    let response = await fetch('http://127.0.0.1:5000/process', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'text': element.innerText, 'cursor': get_cursor()})
    });
    let data = await response.json();
    console.log('Formatting:', data.formatting);
    element.hidden = true;
    element.innerHTML = data.formatting;
    let suggestions = document.getElementById('suggestions');
    suggestions.innerHTML = '';
    data.suggestions.length = Math.min(data.suggestions.length, 9);
    console.log('Suggestions:', data.suggestions);
    for (const suggestion of data.suggestions) {
        console.log(suggestion);
        let li = document.createElement('li');
        li.setAttribute('class', 'suggestion');
        li.setAttribute('onclick', 'autocomplete(this);');
        li.setAttribute('data-complete', suggestion.complete);
        li.innerHTML = suggestion.full;
        suggestions.appendChild(li);
    }
    element.hidden = false;
    updating = false;
    if (need_update) {
        update();
    }
    need_update = false;
}


function update() {
    editor_textarea.dispatchEvent(new Event('input'));
}
function append_text(text) {
    editor_parent.value += text;
    update();
}

function insert_text(str, pos) {
    text = editor_parent.value;
    editor_parent.value = text.substring(0, pos) + str + text.substring(pos, text.length);
    editor_textarea.selectionStart = pos + str.length;
    editor_textarea.selectionEnd = pos + str.length;
    editor_textarea.dispatchEvent(new Event('input'));
}

function register() {
    codeInput.registerTemplate("syntax-highlighted", codeInput.templates.custom(
        handle_update,
        true, /* Optional - Is the `pre` element styled as well as the `code` element? Changing this to false uses the code element as the scrollable one rather than the pre element */
        true, /* Optional - This is used for editing code - setting this to true overrides the Tab key and uses it for indentation */
    ));
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Tab') { // not a tab key
            event.preventDefault();
            event.stopPropagation();
            insert_text('    ', get_cursor());
            return;
        } else if (event.ctrlKey && event.key >= 1 && event.key <= 9) {
            suggestions = suggestions_list.getElementsByTagName('li');
            if (suggestions.length < event.key) {
                return;
            }
            event.preventDefault();
            event.stopPropagation();
            autocomplete(suggestions[event.key - 1]);
        } else if (event.key === `"` || event.key === `'`) {
            insert_text(event.key, get_cursor());
            set_cursor(get_cursor() - 1);
        } else if (event.key === '(') {
            insert_text('()', get_cursor());
            set_cursor(get_cursor() - 1);
            event.preventDefault();
            event.stopPropagation();
        } else if (event.key === '[') {
            insert_text('[]', get_cursor());
            set_cursor(get_cursor() - 1);
            event.preventDefault();
            event.stopPropagation();
        } else if (event.key === '{') {
            insert_text('{}', get_cursor());
            set_cursor(get_cursor() - 1);
            event.preventDefault();
            event.stopPropagation();
        }
    });
}

function autocomplete(suggestion) {
    console.log(suggestion);
    text = suggestion.dataset.complete;
    console.log('value:', text);
    insert_text(text, get_cursor());
}
