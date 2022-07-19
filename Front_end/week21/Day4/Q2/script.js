
var word = document.querySelector('#input');
var inputBtn = document.querySelector('#check');
var feedback = document.querySelector('#feedback');
var checkfb = function(fb_text){
    if (feedback.hasChildNodes()){
        
        feedback.replaceChild(fb_text, feedback.childNodes[0]);
    } else {
        
        feedback.appendChild(fb_text);
    } 
}; 
var checkWord = function(){
    var original = word.value.split(''); 
    var toBeReversed = word.value.split(''); 
    var reversed = toBeReversed.reverse(); 
    for (var letter=0;letter<original.length;letter++){
        
  var fb;
  var fb_text;
        if (reversed[letter]!=original[letter]){
            fb = word.value + ' is not a palindrome!';
            fb_text = document.createTextNode(fb);
            feedback.setAttribute('class','notpalindrome');
            checkfb(fb_text,fb); 
            break; 
        } else if (letter == original.length-1){
            
            fb = word.value + ' is a palindrome!';
            fb_text = document.createTextNode(fb);
            feedback.setAttribute('class','palindrome');
            checkfb(fb_text); 
        }
    }
}; 
inputBtn.addEventListener('click',function(e){
    e.preventDefault(); 
    checkWord();
});


var checkForEnter = function(e){
    if (e.keyCode == 13){ 
        e.preventDefault();
        checkWord();
    }
};