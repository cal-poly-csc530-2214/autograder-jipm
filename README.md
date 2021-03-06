# autograder-jipm
Jiwon Lee
<br />
Parker Mitchell

We found this paper very interesting, and at-a-glance, much more approachable and digestable for us. The concept and technologies used were very interesting, and provided a very tangible application of SAT/SMT solvers for us to see.

We first started by just reading the full paper and getting a better grasp of what was going on. Following this, and thanks to some helpful pointers on Piazza, we used [Armando Solar-Lezama's build guide](https://github.com/asolarlez/sketch-frontend/wiki) for Sketch to try and install all the dependencies we needed to run Sketch. After installing for about 20 minutes, we tried to fully make Sketch, but ran into an issue we were not able to solve, namely this:
<br />
<br />
![Sketch make failed :(](images/sketch_make_fail.png)

Since we could not build and run Sketch, we focused on getting things working prior to running Sketch. So we started by creating a sample Python file with a simple function to act as the "student's submission", and generated a "rules.eml" file to server as our error model.

We wrote generateMPY function that generated MPy files to feed to sketch translator based on our EML rules. The function takes the expression to work on and assumes it's in correct syntax. Our "sample" student program was writing a function that added three numbers that were supposed to sum to 10, assign that to a variable, and return that result. For simplicity, our rule in the function was to simply leave the code as is, add 1, or subtract 1. This was for the proof of the concept to get sketch working. 

Unfortunately, as mentioned above, we were not able to get Sketch working. Additionally, we had trouble converting our .mpy file into a .sk file. The translation of set-expr choices in MPY to Sketch functions was difficult for us to wrap our head around, and pushed us past our time limit trying to understand. That concluded our work on the project.

To see our generated .mpy file, one can simply run the following:
```
python3 createMPY.py > addToTen.mpy
```

After running this, the file "addToTen.mpy" will contain the translated .mpy code.
