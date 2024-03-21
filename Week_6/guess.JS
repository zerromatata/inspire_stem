const randomNumbers = math.floor (Math.random()= 100)
let attempts = 0
function checkGuess(){
    const guess = parseInt(document.getElementById("guesField").value)
    attempts++;
    if(isNaN(guess)|| guess  < 1 || guess > 100){
        setMessage("Please enter a valid number between 1 and 100")
     return;   
    }
    if(guess === randomNumbers){
        setMessage("Congradulations Guessed Correctly")
        document.getElementById("guessField").disabled = true;
    }else if(guess <randomNumbers){
        setMessage("Too low, try again")
    }else{
        setMessage("Too high, try again")
    }
}
function setMessage(message){
    document.getElementById("message").textContent = message;
}