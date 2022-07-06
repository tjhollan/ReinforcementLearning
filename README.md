# Reinforcement Learning
A Jupyter notebook that is generic to the type and implementation of both a neural network and a game to do reinforcement learning.

## Game
The basic game to use that takes the least amount of time/effort to make is tic-tac-toe. Other games should work as long as they fit the basic criteria of the reinforcement learning notebook. Checkers should be interchangeable, for example.

## Neural Network
It doesn't have to be a neural network, but it does have to have the requisite initialize, train, and use functions. The more complex the game, the more time training will take. A tic-tac-toe network will be simple enough that using a numpy array based network will be more efficient than using tensors. More complicated games, like chess or playing the stock market, are more likely to have more complicated training mathematics and will therefore benefit more from the use of tensors. The overhead for using tensors in training tic-tac-toe networks is too high to make using them in that game efficient.
