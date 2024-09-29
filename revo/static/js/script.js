// var editor = CodeMirror(document.getElementById("codeEditor"), {
//     value: `{{ request.form.get('code_snippet', '') }}`,
//     mode: "javascript", // Change to the appropriate mode for your code
//     lineNumbers: true,
//     theme: "dracula", // You can change this to other themes like "monokai", "dracula", etc.
//     lineWrapping: true,
//     viewportMargin: Infinity,
//     styleActiveLine: true, // Optional: highlight the active line
//     lineHeight: 1.5, // Optional: adjust line height for better readability
// });

// // Set the background color to match bg-gray-800
// editor.getWrapperElement().style.backgroundColor = '#2D3748';  
// editor.getWrapperElement().style.color = 'white'; 
// editor.getWrapperElement().style.height = 'screen'; 
// // Set the background color of the line numbers to match the editor's background
// var lineNumberWrapper = editor.getWrapperElement().getElementsByClassName   ('CodeMirror-gutter')[0];
// lineNumberWrapper.style.backgroundColor = '#2D3748'; // Match the editor's background
// lineNumberWrapper.style.color = 'white'; // Set line number color to white  

// To handle form submission, you can get the value from CodeMirror
document.querySelector('form').onsubmit = function() {
    document.querySelector('textarea[name="code_snippet"]').value = editor.getValue();
};
hljs.highlightAll();

function copyToClipboard() {
    const code = document.querySelector('.language-cpp').textContent;
    navigator.clipboard.writeText(code).then(() => {
        alert('Code copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy: ', err);
    });
}
function updateComplexity(complexity) {
    const complexityValue = document.getElementById('complexityValue');
    const complexityBar = document.getElementById('complexityBar');
    
    complexityValue.textContent = complexity;
    
    switch (complexity.toLowerCase()) {
        case 'low':
            complexityBar.className = 'bg-green-500 w-1/3 h-2.5 rounded-full';
            break;
        case 'medium':
            complexityBar.className = 'bg-orange-500 w-2/3 h-2.5 rounded-full';
            break;
        case 'high':
            complexityBar.className = 'bg-red-500 w-full h-2.5 rounded-full';
            break;
        default:
            complexityBar.className = 'bg-gray-500 w-0 h-2.5 rounded-full';
    }
}