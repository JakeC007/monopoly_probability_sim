# monopoly_probability_sim
A quick implementation of simulating monopoly board probabilities

### Rules Implemented
- Chance Card Rules

- Community Chest Rules

## Set up
1. You must have `numpy` installed
    - to install numpy on Ubuntu systems use `pip3` instead of `pip`
2. You must ensure that the file has execute permissions
    - Simply run `$ chmod u+x generate_prob.py`
3. Run the file. There are several optional command line arguments. Type `$ ./generate_prob.py -h` to learn more.

## FAQ
Q: *Why didn't you add command line arguments to specify two die with independent distributions?*   
A: I thought about having two die that each had their own respective probability distributions, but I decided that it would be too clunky to have a user input 12 (!) fractions into the terminal.

Q:
