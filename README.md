# Artificial Intelligence CS374
  This is a repository for my Computer Science level 374, Artificial Intelligence, class. While we did other coursework, these were the projects that were my own ideas and I saw through from start to finish. There is a huge emphasis on Object Orientented Programming throughout the files as you can see by the creation of Objects and their inheritance of the properties of several different classes. 
 
## Lights Out Puzzle
  The LightsOutPuzzle folder contains the very first project we were assigned. We were told to pick any game we want and run an appropriate algorithm on it in order to solve it or play it. Once we get it to work, we then have to upgrade that algorithm in some form to speed it up and decide the moves faster so that we can increase the size of the board and still solve it in a reasonable amount of time. The game I decided to make is called Light's Out. The rules are you have certain tiles in which they are turned off (represented by a 0) and tiles that are turned on (represented by a 1). The goal is to turn off all the lights. However, whenever you click on a "light" it changes the light you click on and it's neighbors (not the diagonals). To clarify, if a tile is clicked on and it is turned off and all its neighbors are turned off, you will result in all those tiles being turned on, and vice versa. When designing the puzzle, I currently have 4 boards set up, all of which take different number of moves to solve. The first algorithm I used to solve the puzzle is A* (A-star). I then upgraded it by using an iterative deepening A* which limits the depth of the search so that we are not wasting time searching possibilities that do not matter. I have added a file called LightsOutPuzzleWriteUp which has a fully detailed descripition of the game including pictures.
  
## Data Analytics
  The DataAnalytics folder contains two files with some excercises that I ran using SKlearn. The file called Pipelines utilizes the pipeline features in which we can run the same classification with as many settings as we want. The other file contains running data analytics on a specific dataset using different classifiers. There are very simple print statements added in their pretaining to simple questions that could be asked about datasets and parameters and why one would choose those over others. 
  
## Image Classification
  There are two examples within the image classification folder on the 10 monkey species data set. Since our data set is fairly small, we are able to upload it all at once. However, this is not advised considering learning models work best with the most amount of data. In order to ensure that this procedure still works within larger data sets, the data is loaded in through a data generator. First, we convert our data into a pandas data frame. Then, we use the flow_from_directory method through the generators to obtain our actual data. Once we have that, we can run our analysis on the data. In one example, I use a simple Sklearn Random Forest Classifier to get an accuracy score. In the second, I add several dense layers and build a convultional neural network using Tensorflow. Since the class was only one semester long and we were running out of time, we were encouraged to find real examples and then apply it to our dataset so I will not take full credit for implementing these as I searched through countless examples and then brought together what I learned from each. 
  
  
    
    
    
    
    
    
