const currentPage = document.querySelector('#body').dataset.currentpage;
document.querySelector('#'+currentPage+'-link').classList.add("active", "disabled");

var GRIDSYSTEM = new Object();
var addCharacterButton = document.getElementById("addCharacterButton");
var characterMovementButton = document.getElementById("moveCharacterButton");

var A1 = document.getElementById("A1");
var A2 = document.getElementById("A2");
var A3 = document.getElementById("A3");

var frog = "../static/assets/images/player.jpg";

if(currentPage == "battles"){
    // creates an empty grid system
    initializeGridSystem();
    initializeListeners();

    var addCharacterToGridActivated = false;
    var characterMovementActivated = false;

}

// base class for creating a character
class Character{
    characterName;
    characterImagePath;
    characterLocation;
    characterMovment

    constructor(name, imagePath, gridLocation, movement){
        this.characterName = name;
        this.characterImagePath = imagePath;
        this.characterLocation = gridLocation;
        this.characterMovment = movement;
        GRIDSYSTEM[gridLocation] = this;
    }
}

function createNewCharacter(name, imagePath, gridLocation, movement){
    return new Character(name, imagePath, gridLocation, movement);
}

function addCharacter(){
    document.getElementById("addCharacterButton").disabled = true;
    document.getElementById("messageHeader").innerText = "Place character on highlighted area";
    addCharacterToGridActivated = true; 
}

function moveCharacter(){
    console.log("YU MOVE NOW!");
}

function listenerForA1(){
    if(addCharacterToGridActivated){
        A1.src = frog;
        console.log(GRIDSYSTEM);
        GRIDSYSTEM["A1"] = createNewCharacter("Andy", frog, "A1", 1);
        addCharacterToGridActivated = false;
        console.log(GRIDSYSTEM);
    }
}

function listenerForA2(){
    if(addCharacterToGridActivated){
        A2.src = frog;
        GRIDSYSTEM["A2"] = createNewCharacter("Andy", frog, "A2", 1);
        addCharacterToGridActivated = false;
    }
}

function listenerForA3(){
    if(addCharacterToGridActivated){
        A3.src = frog;
        GRIDSYSTEM["A3"] = createNewCharacter("Andy", frog, "A3", 1);
        addCharacterToGridActivated = false;
    }
}


function initializeGridSystem(){
    GRIDSYSTEM["A1"] = null;
    GRIDSYSTEM["A2"] = null;
    GRIDSYSTEM["A3"] = null;
    GRIDSYSTEM["A4"] = null;
    GRIDSYSTEM["A5"] = null;
    GRIDSYSTEM["A6"] = null;
    GRIDSYSTEM["A7"] = null;
    GRIDSYSTEM["A8"] = null;
    GRIDSYSTEM["A9"] = null;
}

function initializeListeners(){
    addCharacterButton.addEventListener("click", addCharacter);
    characterMovementButton.addEventListener("click", moveCharacter);

    A1.addEventListener("click", listenerForA1);
    A2.addEventListener("click", listenerForA2);
    A3.addEventListener("click", listenerForA3);
}