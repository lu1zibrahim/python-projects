var spaceOne = document.querySelector("#one")
var spaceTwo = document.querySelector("#two")
var spaceThree = document.querySelector("#three")
var spaceFour = document.querySelector("#four")
var spaceFive = document.querySelector("#five")
var spaceSix = document.querySelector("#six")
var spaceSeven = document.querySelector("#seven")
var spaceEight = document.querySelector("#eight")
var spaceNine = document.querySelector("#nine")
var restart = document.querySelector("#restart")

spaceOne.addEventListener("click",function(){
  spaceOne.textContent = "X";
})

spaceOne.addEventListener("dblclick",function(){
  spaceOne.textContent = "O";
})

spaceTwo.addEventListener("click",function(){
  spaceTwo.textContent = "X";
})


spaceTwo.addEventListener("dblclick",function(){
  spaceTwo.textContent = "O";
})

spaceThree.addEventListener("click",function(){
  spaceThree.textContent = "X";
})

spaceThree.addEventListener("dblclick",function(){
  spaceThree.textContent = "O";
})

spaceFour.addEventListener("click",function(){
  spaceFour.textContent = "X";
})

spaceFour.addEventListener("dblclick",function(){
  spaceFour.textContent = "O";
})

spaceFive.addEventListener("click",function(){
  spaceFive.textContent = "X";
})

spaceFive.addEventListener("dblclick",function(){
  spaceFive.textContent = "O";
})

spaceSix.addEventListener("click",function(){
  spaceSix.textContent = "X";
})

spaceSix.addEventListener("dblclick",function(){
  spaceSix.textContent = "O";
})

spaceSeven.addEventListener("click",function(){
  spaceSeven.textContent = "X";
})

spaceSeven.addEventListener("dblclick",function(){
  spaceSeven.textContent = "O";
})

spaceEight.addEventListener("click",function(){
  spaceEight.textContent = "X";
})

spaceEight.addEventListener("dblclick",function(){
  spaceEight.textContent = "O";
})

spaceNine.addEventListener("click",function(){
  spaceNine.textContent = "X";
})

spaceNine.addEventListener("dblclick",function(){
  spaceNine.textContent = "O";
})

restart.addEventListener("click",function(){
  spaceOne.textContent = "";
  spaceTwo.textContent = "";
  spaceThree.textContent = "";
  spaceFour.textContent = "";
  spaceFive.textContent = "";
  spaceSix.textContent = "";
  spaceSeven.textContent = "";
  spaceEight.textContent = "";
  spaceNine.textContent = "";
  spaceFour.textContent = "";

})
