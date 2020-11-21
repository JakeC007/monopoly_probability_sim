# Monopoly Probability Sim
A quick implementation of simulating monopoly board probabilities. 


### Rules Implemented
- Chance Card Rules

- Community Chest Rules

### How to read the board output
This board starts with GO at index 0 and boardwalk at index 39. In addition to the 40 squares on the board, I created a special index for players who are in jail and not just visiting because the jail square (index 10) pulls double duty as "just visiting" and the jail itself. Thus, the index `IN_JAIL` to denotes the turns that a player is in the jail portion of index 10. 

## Set up
1. You must have `numpy` installed
    - to install numpy on Ubuntu systems use `pip3` instead of `pip`
2. You must ensure that the file has execute permissions
    - Simply run `$ chmod u+x generate_prob.py`
3. Run the file. There are several optional command line arguments. Type `$ ./generate_prob.py -h` to learn more.

## FAQ
Q: *Why didn't you add command line arguments to specify two die with independent distributions?*   
A: I thought about having two die that each had their own respective probability distributions, but I decided that it would be too clunky to have a user input 12 (!) fractions into the terminal.

Q: *Can this program play Monopoly?*

A: No. My script merely keeps track of where players land in Monopoly. I added the subset of movement rules found in the community chest and chance cards to make the simulation more accurate. 
