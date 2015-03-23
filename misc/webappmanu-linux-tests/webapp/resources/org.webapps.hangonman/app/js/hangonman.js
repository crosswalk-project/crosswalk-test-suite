/*
 * Copyright (c) 2012, Intel Corporation.
 *
 * This program is licensed under the terms and conditions of the
 * Apache License, version 2.0.  The full text of the Apache License is at
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 */

/*
  sounds needed:
  - ambient city
  - bird sounds
  - squeeky pulley
  - flapping wings
  - flapping sheet
  - button click
  - wrong guess (whoa)
  - right guess (yeah)
  - wire boing
  - falling man
*/
var soundBoard = new SoundBoard({
    "background": {url: "audio/Background.ogg", loop: true},
    "click": {url: "audio/ButtonClick.ogg"},
    "yeah": {url: "audio/Yeah.ogg"},
    "woah": {url: "audio/Whoa.ogg"},
    "lose": {url: "audio/LoseGame.ogg"},
    "dialog": {url: "audio/Banner.ogg"}
});

function getStyle (elem, prop)
{
    return document.defaultView.getComputedStyle(elem).getPropertyValue(prop);
}

////////////////////////////////////////////////////////////////////////////////
// Function to handle user input

function handleKeyDown(event)
{
    if (!gameInProgress || isDialogUp) return;
    if (event.ctrlKey) return;
    if ((event.which < 65)||(event.which > 90)) return; // PTWEB-1081

    // TODO: this is ASCII-specific, needs i18n.

    var char = String.fromCharCode(event.which).toUpperCase();
    var index = alphabet.string.indexOf(char);
    if ((index >= 0) && (index < alphabet.data.length)) {
        var data = alphabet.data[index];
        if (!data.selected) {
            var elem = data.elem;
            var cl = elem.classList;
            cl.add("letterPressed");
            cl.remove("letterNotGuessed");
        }
    }
}

function handleKeyUp(event)
{
    if (!gameInProgress || isDialogUp) return;
    if (event.ctrlKey) return;
    if ((event.which < 65)||(event.which > 90)) return; // PTWEB-1081

    // TODO: this is ASCII-specific, needs i18n.

    var char = String.fromCharCode(event.which).toUpperCase();
    var index = alphabet.string.indexOf(char);
    if ((index >= 0) && (index < alphabet.data.length)) {
        chooseLetter(index);
    }
}

function letterPressed (event)
{
    if (!gameInProgress || isDialogUp) return;

    var target = event.target;
    var cl = target.classList;
    if (!cl.contains("letterGuessed")) {
        target.pressed = true;
        cl.add("letterPressed");
        cl.remove("letterNotGuessed");
    }

    letterSelected(event);
}

function letterSelected (event)
{
    if (!gameInProgress || isDialogUp) return;

    var target = event.target;
    if (target.pressed) {
        target.pressed = false;
        chooseLetter(target.letterIndex);
    }
}

function chooseLetter (index)
{
    var data = alphabet.data[index];
    if (data.selected) return;

    data.selected = true;
    var elem = data.elem;
    var cl = elem.classList;
    cl.add("letterGuessed");
    cl.remove("letterPressed", "letterNotGuessed");
    elem.disabled = true;

    soundBoard.play("click");

    var letter = alphabet.string.charAt(index);

    var found = false;
    if (answer.string.indexOf(letter) >= 0) {
        guessedRight(letter);
        if (didWin()) {
            doWinLose(true);
        }
    }
    else {
        guessedWrong(letter);
        if (didLose()) {
            setTimeout("doWinLose(false)", 2000);
        }
    }

    saveGameState();
}


function initAlphabet ()
{
    var alphabetString = getMessage("alphabet");
    var alphabet = { "string": alphabetString, "data": new Array(alphabetString.length) };
    for (var i = 0; i < alphabet.string.length; ++i) {
        alphabet.data[i] = {"elem": undefined, "selected": false};
    }

    var fragment = document.createDocumentFragment();

    var numRows = 2;
    var fontSize = 70;
    var angleSweep = 2*Math.PI/10;
    var radius = 1200;

    for (var row = 0; row < numRows; ++row) {
        var rowElem = document.createElement("div");
        fragment.appendChild(rowElem);
        var startIndex = Math.round(alphabet.string.length * row/numRows);
        var endIndex = Math.round(alphabet.string.length * (row+1)/numRows);
        var alphabetRange = alphabet.string.slice(startIndex, endIndex);
        var angle = angleSweep/2;
        var angleDelta = angleSweep / (endIndex-startIndex);
        var rowRadius = radius + (row * fontSize * 2);
        for (var letterIndex = startIndex; letterIndex < endIndex; ++letterIndex) {
            var letter = alphabet.string.charAt(letterIndex);
            var x = 10 + Math.sin(angle) * -rowRadius;
            var y = (Math.cos(angle + Math.PI)+1) * -rowRadius + row*fontSize;
            var letterElem = document.createElement("div");
            alphabet.data[letterIndex].elem = letterElem;
            letterElem.classList.add("letter", "letterNotGuessed");
            letterElem.innerText = letter;
            letterElem.letterIndex = letterIndex;
            letterElem.style['font-size'] = fontSize + "px";
            letterElem.style.width = fontSize + "px";
            letterElem.style.top = y+"px";
            letterElem.style.left = x+"px";
            letterElem.style.webkitTransform = "rotate("+angle+"rad)";
            letterElem.addEventListener("click", letterPressed, false);
            fragment.appendChild(letterElem);
            angle -= angleDelta;
        }
    }

    var alphabetElem = document.getElementById("letters");
    while (alphabetElem.hasChildNodes()) {
        alphabetElem.removeChild(alphabetElem.firstChild);
    }
    alphabetElem.appendChild(fragment);

    return alphabet;
}

function updateAlphabet (alphabet, rightGuesses, wrongGuesses)
{
    if (!wrongGuesses) {
        wrongGuesses = "";
    }
    var guesses = rightGuesses + wrongGuesses;
    for (var i = 0; i < guesses.length; ++i) {
        var index = alphabet.string.indexOf(guesses[i]);
        if (index != -1) {
            var data = alphabet.data[index];
            var cl = data.elem.classList;
            cl.add("letterGuessed");
            cl.remove("letterNotGuessed");
            data.selected = true;
        }
    }
}

function updateAnswer (rightGuesses)
{
    if (!rightGuesses) {
        rightGuesses = "";
    }
    for (var i = 0; i < rightGuesses.length; ++i) {
        guessedRight(rightGuesses.charAt(i));
    }
}


function initGameState ()
{
    wrongGuesses = "";
    rightGuesses = "";
    word = "";
    matches = 0;
    gameType = 0;
    gameInProgress = false;
    localStorage["com.intel.hom.gameInProgress"] = false;
}

function restoreGameState ()
{
    if (localStorage && localStorage["com.intel.hom.word"] &&
	localStorage["com.intel.hom.gameInProgress"] && (localStorage["com.intel.hom.gameInProgress"] === "true"))
    {
	wrongGuesses = localStorage["com.intel.hom.wrongGuesses"] || "";
	rightGuesses = localStorage["com.intel.hom.rightGuesses"] || "";
	word = localStorage["com.intel.hom.word"];
	gameType = localStorage["com.intel.hom.gameType"] || 0;
	gameInProgress = true;
    }
    else {
	initGameState();
    }
}

function saveGameState ()
{
    localStorage["com.intel.hom.wrongGuesses"] = wrongGuesses;
    localStorage["com.intel.hom.rightGuesses"] = rightGuesses;
    localStorage["com.intel.hom.word"] = word;
    localStorage["com.intel.hom.gameType"] = gameType;
    localStorage["com.intel.hom.gameInProgress"] = gameInProgress;
}


function restoreSettings ()
{
    var muted;

    try {
        muted = JSON.parse(localStorage["com.intel.hom.muted"]);
    }
    catch (e) {
        muted = false;
        localStorage["com.intel.hom.muted"] = JSON.stringify(muted);
    }
    finally {
        soundBoard.muted = muted;
    }
}

function clearTimers ()
{
    [waitId, timeoutId].forEach(function(id) {
        if (id) {
	    clearInterval(id);
	    id = 0;
        }
    });
}

function initAnswer (answerString)
{
    if (!answerString) {
        return;
    }
    var alphabetString = getMessage("alphabet");
    var answerElem = document.getElementById("answer");
    while (answerElem.hasChildNodes()) {
        answerElem.removeChild(answerElem.firstChild);
    }

    var words = answerString.match(/\S+/g);
    var answer = { "string": words.join(" "),
                   "letters": "",
                   "numRight": 0,
                   "data": [] };
    var alphabetRegex = new RegExp("["+alphabetString+"]");

    for (var i in words) {
        var wordElem = document.createElement("div");
        wordElem.classList.add("answer_word");
        answerElem.appendChild(wordElem);

        var part = words[i];
        for (var j in part) {
            var letterContainer = document.createElement("div");
            letterContainer.classList.add("answerText_container");
            wordElem.appendChild(letterContainer);

            var letterElem = document.createElement("div");
            letterContainer.appendChild(letterElem);

            var letter = part[j];
            if (letter.match(alphabetRegex)) {
                letterElem.classList.add("answerText");
                letterElem.innerHTML = "&emsp;";
                answer.letters += letter;
                answer.data.push({ "elem": letterElem });
            }
            else {
                letterElem.classList.add("answerPunct");
                letterElem.innerText = letter;
            }
        }
    }
    return answer;
}


var faceElem;
function guessedRight (letter)
{
    soundBoard.play("yeah");

    faceElem = faceElem || document.querySelector("#hangman #face");
    faceElem.classList.add("guessedRight");
    rightGuesses = rightGuesses + letter;
    var string = answer.letters;
    var pos = string.indexOf(letter);
    while ((pos >= 0) && (pos < string.length)) {
        answer.data[pos].elem.innerText = letter;
        ++(answer.numRight);
        pos = string.indexOf(letter, pos+1);
    }
}


function guessedWrong (letter)
{
    wrongGuesses = wrongGuesses + letter;
    gameInProgress = !didLose();

    faceElem = faceElem || document.querySelector("#hangman #face");
    updateHangman();
    faceElem.classList.remove("guessedRight");
}

var hangmanElem;
var rightShoeElem;
function updateHangman(firstTime)
{
    hangmanElem = hangmanElem || document.getElementById("hangman");
    rightShoeElem = rightShoeElem || document.getElementById("right_shoe");

    var classList = hangmanElem.classList;
    var numFingers = maxWrongGuesses - wrongGuesses.length;
    var delay = 0;

    if (didLose()) {
        delay = 500;
        soundBoard.play("lose");
    }

    setTimeout(function() {
        classList.add("v"+numFingers);
        for (var i = 0; i <= maxWrongGuesses; ++i) {
            if (i !== numFingers) {
                classList.remove("v"+i);
            }
        }
        if (!firstTime) {
            restartBounce();
            if (numFingers <= 4) {
                rightShoeElem.classList.add("falling");
            }
            else {
                rightShoeElem.classList.remove("falling");
            }
        }
    }, delay);
}


function didWin ()
{
    return (answer.letters.length == answer.numRight);
}


function didLose ()
{
    return (wrongGuesses.length >= maxWrongGuesses);
}


function setLocaleString (domId, stringKey)
{
    if (stringKey == undefined) {
        stringKey = domId;
    }

    var elem = document.getElementById(domId);
    elem.innerText = getMessage(stringKey);
    return elem;
}


function showDialog (domId)
{
    if (isDialogUp) return;

    soundBoard.play("dialog");

    for(var i = 0; i < arguments.length; ++i) {
        isDialogUp = true;
        var currDomId = arguments[i];
        bodyElem.classList.add("isDialogUp");
        showElement(currDomId);
    }
}

function hideDialog (domId)
{
    for(var i = 0; i < arguments.length; ++i) {
        var currDomId = arguments[i];
        hideElement(currDomId);
        bodyElem.classList.remove("isDialogUp");
        setTimeout(function() {
            isDialogUp = false;
            soundBoard.play("dialog");
        }, 1000);
    }
}

function showElement (domId)
{
    for(var i = 0; i < arguments.length; ++i) {
        var currDomId = arguments[i];
        var elem = document.getElementById(currDomId);
        elem.classList.add("shown");
    }
}

function hideElement (domId)
{
    for(var i = 0; i < arguments.length; ++i) {
        var currDomId = arguments[i];
        var elem = document.getElementById(currDomId);
        elem.classList.remove("shown");
    }
}


function addButtonEffects (elem)
{
    elem.addEventListener("mousedown",
                          function (event) {
                              elem.classList.add("pressed");
                          }, false);
    elem.addEventListener("mouseup",
                          function (event) {
                              elem.classList.remove("pressed");
                          }, false);
    elem.addEventListener("mouseout",
                          function (event) {
                              elem.classList.remove("pressed");
                          }, false);
    return elem;
}


function initButton (domId, handler)
{
    var elem = setLocaleString(domId);
    elem.addEventListener("click", function(e) {
        soundBoard.play("click");
        handler(e);
    }, false);
    addButtonEffects(elem);  //TODO: what effects happen when you click a button?
}

var bodyElem;
function initDialogs ()
{
    var now = (new Date()).getHours();
    var morning =  6; // 6am
    var evening = 18; // 6pm
    bodyElem = bodyElem || document.querySelector("body");
    if ((now >= evening) || (now < morning)){
        bodyElem.classList.add("night");
    }

    if (gameInProgress) {
        showElement("skyline", "newGame", "giveUp", "letters", "answer",  "hangman");
        hideElement("help");
    }
    else {
        hideElement("skyline", "newGame", "hangman", "giveUp", "letters", "answer", "help");
    }
    hideDialog("newGame_dialog", "giveUp_dialog", "win_dialog", "lose_dialog", "learnMore_dialog");

    var helpElem = document.getElementById("help");
    helpElem.addEventListener("click", learnMore, false);

    initButton("play_button", firstStart);
    initButton("learnMore_close", learnLess);
    initButton("newGame_button", newGame);
    initButton("newGame_cancel", newGameCancel);
    initButton("giveUp_button", giveUp);
    initButton("giveUp_no", giveUpCancel);
    initButton("giveUp_yes", giveUpConfirm);
    initButton("win_playAgain", playAgain);
    initButton("lose_playAgain", playAgain);

    setLocaleString("learnMore_text");
    setLocaleString("giveUp_text");
    setLocaleString("win_text");
    setLocaleString("lose_text");

    inner = document.querySelector("#hangman #inner");
    inner.addEventListener("click", restartBounce, false);
}

var inner;
var innerStyle;
var lWireStyle;
var rWireStyle;
function restartBounce (isLast)
{
    setTimeout(function() {
        innerStyle = innerStyle || inner.style;
        lWireStyle = lWireStyle || document.querySelector("#hangman #left_wire").style;
        rWireStyle = rWireStyle || document.querySelector("#hangman #right_wire").style;
        innerStyle.webkitAnimationName = "none";
        lWireStyle.webkitAnimationName = "none";
        rWireStyle.webkitAnimationName = "none";
    }, 0);

    var numFingers = maxWrongGuesses - wrongGuesses.length;
    var bodyAnimation = "bounce";
    var leftWireAnimation = "bounce-wire-left";
    var rightWireAnimation = "bounce-wire-right-v"+numFingers;

    if (0 === numFingers) {
        bodyAnimation = "bounce-v0";
        leftWireAnimation = "bounce-wire-left-v0";
    }
    else if (8 === numFingers) {
        rightWireAnimation = "bounce-wire-right-v9";
    }

    setTimeout(function() {
        innerStyle.webkitAnimationName = bodyAnimation;
        rWireStyle.webkitAnimationName = rightWireAnimation;
        lWireStyle.webkitAnimationName = leftWireAnimation;

        if (!didLose()) {
            soundBoard.play("woah");
        }
    }, 0);
}

function readwordlist(item)
{
    var file = "data/"+item.src;
    var request = new XMLHttpRequest();
    request.open("GET", file, true);
    request.onload = function(e) {
        var requestStr = this.responseText;
        try {
	    item.data = JSON.parse(requestStr);
        }
        catch(err) {
	    console.log("Unable to read wordList: "+file);
        }
    }
    request.send();
}

function initWordLists (wordLists)
{
    var newGameList = document.getElementById("newGame_list");
    var gameTypeLabel = document.getElementById("game_type");
    for (var i = 0; i < wordLists.length; ++i) {
        var item = wordLists[i];
        if (item.hasOwnProperty("src")) {
            readwordlist(item);
        }
        var titleString = getMessage(item.title);
        var gameElem = document.createElement("div");
        var cl = gameElem.classList;
        gameElem.index = i;
        cl.add("newGame_type");
        addButtonEffects(gameElem);
        if (i == gameType) {
            cl.add("selected");
            gameTypeLabel.innerText = titleString;
        }
        gameElem.innerText = titleString;
        gameElem.addEventListener("click", selectGameType, false);
        newGameList.appendChild(gameElem);
    }
}


var newGameList;
var gameTypeLabel;
function selectGameType (event)
{
    if (gameType != this.index) {
        newGameList = newGameList || document.getElementById("newGame_list");
        var oldType = newGameList.querySelector(".selected");
        if (oldType) {
            oldType.classList.remove("selected");
        }
        this.classList.add("selected");
        gameType = this.index;
        gameTypeLabel = gameTypeLabel || document.getElementById("game_type");
        gameTypeLabel.innerText = event.target.innerText;
    }
    hideDialog("newGame_dialog");
    startGame();
}

function getNewWord ()
{
    var list = wordLists[gameType];
    if (list.hasOwnProperty("src")) {
        word = chooseLocalWord(list.data);
    }
}

function firstStart (event)
{
    if (isDialogUp) return;

    // TODO: use css for this!
    startElem.style.bottom = "-150px";
    var titleElem = document.getElementById("title");
    titleElem.style.left = "-1200px";

    // pop up the game category selector with no cancel
    var cancel = document.getElementById("newGame_cancel");
    cancel.style.visibility="hidden";
    hideElement("help");
    showDialog("newGame_dialog");
}

function startGame (event)
{
    gameInProgress = true;
    soundBoard.play("background");
    hideElement("hangman");
    rightGuesses = [];
    wrongGuesses = [];
    updateHangman(true);
    getNewWord();
    showElement("skyline", "newGame", "hangman", "giveUp", "letters", "answer");
    hideElement("help");
    alphabet = initAlphabet();
    answer = initAnswer(word);
    saveGameState();
}

function learnMore (event)
{
    soundBoard.play("click");
    showDialog("learnMore_dialog");
}

function learnLess (event)
{
    hideDialog("learnMore_dialog");
}

function newGame (event)
{
    if (!ignoreNewGame) {
        var cancel = document.getElementById("newGame_cancel");
        cancel.style.visibility="visible";
        showDialog("newGame_dialog");
    }
}


function newGameCancel (event)
{
    hideDialog("newGame_dialog");
}

function giveUp (event)
{
    if (gameInProgress) {
        showDialog("giveUp_dialog");
    }
}

function giveUpCancel (event)
{
    hideDialog("giveUp_dialog");
}

function giveUpConfirm (event)
{
    gameInProgress = false;
    hideDialog("giveUp_dialog");
    for (var i = 0; i < answer.letters.length; ++i) {
        answer.data[i].elem.innerText = answer.letters[i];
    }
    saveGameState();
}

function playAgain (event)
{
    ignoreNewGame = false;
    hideDialog("win_dialog", "lose_dialog");
    startGame();
}


function dontPlayAgain (event)
{
    ignoreNewGame = false;
    hideDialog("win_dialog", "lose_dialog");
}


function doWinLose (didWin)
{
    gameInProgress = false;
    ignoreNewGame = true;
    hideElement("hangman");
    if (didWin) {
        showDialog("win_dialog");
    }
    else {
        showDialog("lose_dialog");
        giveUpConfirm();
    }
    saveGameState();
}


function chooseLocalWord (wordList)
{
    if (wordList.length == 0) {
	console.log("No such words available!");
        return undefined;
    }
    else {
	var i = Math.floor(Math.random() * wordList.length);
	return wordList[i].toUpperCase();
    }
}

// Game state

var wrongGuesses, rightGuesses;
var answer;
var gameInProgress;
var ignoreNewGame = false;
var gameType;

// Derived state

var alphabet;
var locales;
var matches;
var waitId;    // timer ID for json call
var timeoutId; // timer ID for json call watchdog
var isDialogUp = false;

// Globals

var maxWrongGuesses = 10;

var wordLists = [
    {"title":"words_animals",   "src":"animals.json"},
    {"title":"words_wineTerms", "src":"wine.json"},
    {"title":"words_nations",   "src":"nations.json"},
    {"title":"words_phrases",   "src":"phrases.json"},
    {"title":"words_bodyParts", "src":"bodyparts.json"},
    //{"title":"words_common",    "method":""},
];

var numClouds = 0;
function destroyCloud (event)
{
    --numClouds;
    containerElem.removeChild(event.target);
}

var containerElem;
function createCloud ()
{
    if (numClouds < 8) {
        ++numClouds;
        var cloudElem = document.createElement("div");
        var classList = cloudElem.classList;
        classList.add("cloud");

        var version = Math.floor(Math.random() * 3 + 1);  //[1 to 3]
        classList.add("v" + version);

        var rnd = Math.random();
        var bottom   = Math.floor(rnd * 75 + 10); //[10 to 85]
        var opacity  = (rnd * -0.6 + 0.9);  //[0.8 to  0.3]
        var duration = (rnd * 20 + 30);  //[30.0 to 50.0]
        var scale    = (rnd * -0.7 + 1.0);  //[1.0 to  0.3]
        cloudElem.style.bottom = ""+bottom+"%";
        cloudElem.style.opacity = opacity;
        cloudElem.style.webkitTransform = "scale("+scale+","+scale+")";  //[0.3 to 1.0]
        cloudElem.style["-webkit-animation-duration"] = duration + "s";
        cloudElem.style["-webkit-animation-name"] = "cloud_move";
        containerElem.appendChild(cloudElem);

        var delay = Math.random() * 4000 + 1000; //[1 to 5]
        window.setTimeout(createCloud, delay);
    }
}

var BIRD_FRONT         = 0;
var BIRD_FRONT_BLINK   = 1;
var BIRD_FRONT_TILT    = 2;
var BIRD_FRONT_LOOK    = 3;
var BIRD_FRONT_PROFILE = 4;
var BIRD_SIDE          = 5;
var BIRD_SIDE_BLINK    = 6;
var BIRD_SIDE_DOWN     = 7;
var BIRD_SIDE_UP       = 8;
var BIRD_SIDE_PROFILE  = 9;
var BIRD_SIDE_TAIL     = 10;

var birdElems = [undefined, undefined, undefined, undefined];
function fidgetBirds (whichBird)
{
    setTimeout(function ()
    {
        if (gameInProgress) {
            return;
        }

        var birdElem = birdElems[whichBird];
        if (!birdElem) {
            var birdId = "bird_" + whichBird;
            birdElems[whichBird] = document.getElementById(birdId);
            birdElem = birdElems[whichBird];
        }

        var stateStr = getStyle(birdElem, "background-position");
        var state = parseInt(stateStr.match(/^(-?\d+)px/)[1]) / -100;

        var whichChange = Math.floor(Math.random() * 3);
        if (whichChange) {
            switch(state) {
            case BIRD_FRONT:
            case BIRD_FRONT_LOOK:
                if (whichChange == 1) fidgetToggle(birdElem, state, BIRD_FRONT_TILT);
                else fidgetToggle(birdElem, state, BIRD_FRONT_BLINK);
                break;
            case BIRD_SIDE:
                fidgetToggle(birdElem, state, BIRD_SIDE_BLINK);
                break;
            case BIRD_SIDE_PROFILE:
                if (whichChange == 1) fidgetToggle(birdElem, state, BIRD_SIDE_TAIL);
                else fidgetNod(birdElem);
                break;
            default:
                fidgetChange(birdElem, state);
            }
        }
        else {
            fidgetChange(birdElem, state);
        }
        fidgetBirds(whichBird);
    }, Math.random()*5000 + 2000);
}

function setBirdState (elem, state)
{
    elem.style.backgroundPosition = (-100 * state) + "px 0px";
}

function fidgetChange (elem, state)
{
    var newStates = [BIRD_FRONT, BIRD_FRONT_LOOK,
                     BIRD_FRONT_PROFILE, BIRD_SIDE, BIRD_SIDE_PROFILE];
    var newState = state;
    while (newState == state) {
        newState = newStates[Math.floor(Math.random() * newStates.length)];
    }
    setBirdState(elem, newState);
}

function fidgetToggle (elem, state, otherState)
{
    setTimeout(setBirdState.bind(undefined, elem, otherState),   0);
    setTimeout(setBirdState.bind(undefined, elem, state     ), 250);
    setTimeout(setBirdState.bind(undefined, elem, otherState), 500);
    setTimeout(setBirdState.bind(undefined, elem, state     ), 750);
}

function fidgetNod (elem)
{
    setTimeout(setBirdState.bind(undefined, elem, BIRD_SIDE_DOWN   ),   0);
    setTimeout(setBirdState.bind(undefined, elem, BIRD_SIDE_PROFILE), 250);
    setTimeout(setBirdState.bind(undefined, elem, BIRD_SIDE_UP     ), 500);
    setTimeout(setBirdState.bind(undefined, elem, BIRD_SIDE_PROFILE), 750);
}

var startElem;
window.addEventListener("DOMContentLoaded", function(event)
{
    license_init("license", "container");
    initStaticStrings();
    initDialogs();
    updateHangman(true);

    alphabet = initAlphabet();
    if (!gameInProgress) {
        startElem = document.getElementById("start_container");

        // animate the container in
        startElem.addEventListener("webkitAnimationEnd", function () {
          if (!gameInProgress) {
              showElement("help");
          }
        }, false);
        startElem.style["-webkit-animation-name"] = "start_container_slide_in";

        showElement("title", "wire");
        fidgetBirds(0);
        fidgetBirds(1);
        fidgetBirds(2);
        fidgetBirds(3);
    }
    else {
        answer = initAnswer(word);
        updateAnswer(rightGuesses);
        updateAlphabet(alphabet, rightGuesses, wrongGuesses);
    }

    initWordLists(wordLists);
    document.addEventListener("keydown", handleKeyDown, true);
    document.addEventListener("keyup", handleKeyUp, true);

    containerElem = document.getElementById("container");
    createCloud();
}, false);

window.addEventListener("load", function (event)
{
    // handlers to pause/play sound when window is hidden/visible
    var appHiddenCb = function () {
        soundBoard.pause();
    };

    var appVisibleCb = function () {
        soundBoard.play("background");

        if (isDialogUp)
        {
            soundBoard.play("dialog");
        }
    };

    if ("onvisibilitychange" in window) {
      window.addEventListener("visibilitychange", function () {
        if (window.hidden) {
            appHiddenCb();
        }
        else {
            appVisibleCb();
        }
      });
    }
    else {
        window.onblur = appHiddenCb;
        window.onfocus = appVisibleCb;
    }

    soundBoard.play("background");
    scaleBody(document.body, 720);
}, false);

// Start immediately

restoreSettings();
initGameState();
//restoreGameState(); removed for PTWEB-1053
initGetMessage();
clearTimers();
