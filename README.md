# Artificial Intelligence CS374
  This is a repository for my Computer Science level 374, Artificial Intelligence, class. It currently only contains my Project1 folder which is our very first project for the class. There is a huge emphasis on Object Orientented Programming throughout the files as you can see by the creation of Objects and their inheritance of the properties of several different classes. 
 
## Project 1
  The project 1 folder contains the very first project we were assigned. We were told to pick any game we want and run an appropriate algorithm on it in order to solve it or play it. Once we get it to work, we then have to upgrade that algorithm in some form to speed it up and decide the moves faster so that we can increase the size of the board and still solve it in a reasonable amount of time. The game I decided to make is called Light's Out. The rules are you have certain tiles in which they are turned off (represented by a 0) and tiles that are turned on (represented by a 1). The goal is to turn off all the lights. However, whenever you click on a "light" it changes the light you click on and it's neighbors (not the diagonals). To clarify, if a tile is clicked on and it is turned off and all its neighbors are turned off, you will result in all those tiles being turned on, and vice versa. When designing the puzzle, I currently have 4 boards set up, all of which take different number of moves to solve. The first algorithm I used to solve the puzzle is A* (A-star). I then upgraded it by using an iterative deepening A* which limits the depth of the search so that we are not wasting time searching possibilities that do not matter. 
  
  
    
    
    
    
    
    
