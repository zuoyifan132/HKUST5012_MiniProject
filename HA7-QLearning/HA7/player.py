# -*- coding: utf-8 -*-
import numpy as np
from ui import TicTacToeTUI
import pickle as pkl
import os.path
import random

class Player:
    __doc__ = r"""
    Base player class, define the interface.

    * :attr:`mark` keeps the role of player, can either be 1 (for the first player),
      or -1 (for the second).
    
    Args:
        mark (int): either 1 or -1, indicating first player or second player respectively.
    """

    def __init__(self, mark):
        assert mark in [1, -1], "A player's mark must be 1 (first) or -1 (second)"
        self.mark = mark

    def decide(self, obs):
        """
        Make move according to the observation. It will called by game to get an action.

        Args:
            obs (ndarray): a 2D numpy array, filled with 1, -1, 0,
                indicating mark of first player, second player, and place not yet occupied.

        Returns:
            action (tuple of (int, int)): indicates the coordinates to place mark,
                starting from 0, i.e. (0, 0) is the top left corner.
        """
        raise NotImplementedError

    def get_feedback(self, obs, reward, info, actor):
        """
        Receive feedback from the environment.
        It will be called by the game when anyone makes an action and steps the environment.

        Args:
            obs (ndarray): a 2D numpy array, filled with 1, -1, 0,
                indicating mark of first player, second player, and place not yet occupied.

            reward (float): a value indicating the reward got from moves of two players.
            
            info (dict): a dict, with keys like "on_move" and "terminate",
                telling who should move now and if game end.
            
            actor (int): can either be 1 or -1, indicating whose action results in this feedback.
                1 means the first player, -1 is the seond one.

        """
        raise NotImplementedError


class RandomPlayer(Player):
    __doc__ = r"""
    Example random player, which just randomly chooses a position to place mark.

    * :attr:`mark` keeps the role of player, can either be 1 (for the first player),
      or -1 (for the second).
    
    Args:
        mark (int): either 1 or -1, indicating first player or second player respectively.
    """
    def __init__(self, mark):
        super(RandomPlayer, self).__init__(mark)

    def decide(self, obs):
        """
        Make a random move according to the observation. It will called by game to get an action.

        Args:
            obs (ndarray): a 2D numpy array, filled with 1, -1, 0,
                indicating mark of first player, second player, and place not yet occupied.

        Returns:
            action (tuple of (int, int)): indicates the coordinates to place mark,
                starting from 0, i.e. (0, 0) is the top left corner.
        """
        x, y = np.where(obs == 0)
        assert len(x) > 0, "No empty place!"
        idx = np.random.randint(len(x))
        return (x[idx], y[idx])

    def get_feedback(self, obs, reward, info, actor):
        pass


class MLPlayer(Player):
    __doc__ = r"""
    A machine learning player class, YOU NEED TO FINISH THIS TO PERFORM Q-LEARNING.

    * :attr:`mark` keeps the role of player, can either be 1 (for the first player),
      or -1 (for the second).

    * :attr:`table` a dict maps encoding of states to another dict,
        which maps (int, int), action coordinates, to value.
    
    * :attr:`mode` either "train" or "eval", indicates the mode of the agent.
    
    * :attr:`...` You can add additional attributes for this class.
    
    Args:
        mark (int): either 1 or -1, indicating first player or second player respectively.

        ... (any, optional): You can add additional optional arguments,
            but ensure it works in main\*.py without changing them
    """
    def __init__(self, mark):
        super(MLPlayer, self).__init__(mark)
        self.table = {} # Here
        self.mode = "eval"
        self.traj = []

        #YOUR CODE HERE
        
        # initialize Q table 
        #a = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
        #self.table = {(i, j) : 0 for i, j in a}

        #END OF YOUR CODE


        #load if any save exists
        name = "player" + ("1" if mark == 1 else "2")
        if os.path.exists(name):
            self.load()

    def load(self, name=None):
        """
        load saved table.

        Args:
            name (str, optional): name of the pickle file saves the table,
                default to be player1 (mark == 1) or player 2 (mark == -1)
        """
        if not name:
            name = "player" + ("1" if self.mark == 1 else "2")
        with open(name, "rb") as f:
            self.table = pkl.load(f)

    def save(self, name=None):
        """
        save table to pickle file.

        Args:
            name (str, optional): name of the pickle file saves the table,
                default to be player1 (mark == 1) or player 2 (mark == -1)
        """
        if not name:
            name = "player" + ("1" if self.mark == 1 else "2")
        with open(name, "wb") as f:
            pkl.dump(self.table, f)

    def set_mode(self, mode):
        assert mode in ["train", "eval"]
        self.mode = mode

    def decide(self, obs):
        """
        decide action according to the observation.
        YOU NEED TO FINISH IT

        Args:
            obs (ndarray): a 2D numpy array, filled with 1, -1, 0,
                indicating mark of first player, second player, and place not yet occupied.

        Returns:
            action (tuple of (int, int)): indicates the coordinates to place mark,
                starting from 0, i.e. (0, 0) is the top left corner.        
        """
        obs_code = self._encode_obs(obs)
        #insert into table if it's new.
        if obs_code not in self.table:
            #set value as a dict maps all possible move to initial value.
            self.table[obs_code] = {(i, j): self._init_val for i, j in zip(*np.where(obs == 0))}

        #YOUR CODE HERE
        
        # explore probability
        explore = 0.01

        Q_value = self.table[obs_code]
        max_val = max(Q_value.values())
        move = (0,0)
        for key in Q_value.keys():
            if Q_value[key] == max_val:
                move = key
                break

        randfloat = random.random()
        if randfloat <= explore:
            x, y = np.where(obs == 0)
            assert len(x) > 0, "No empty place!"
            idx = np.random.randint(len(x)) 
            move = (x[idx], y[idx])

        #END OF YOUR CODE
        if self.mode == "train":
            self.traj.append((obs_code, move))

        return move
    
    @property
    def _init_val(self):
        """
        return the initial value for a new state.
        YOU NEED TO FINISH IT.

        Returns:
            val (float): the initial value for a new state.
        """
        #YOUR CODE HERE
        return -1e-14
        #END OF YOUR CODE

    def _encode_obs(self, obs):
        """
        encode the observation into hashable type
        YOU NEED TO FINISH IT
        
        Args:
            obs (ndarray): a 2D numpy array, filled with 1, -1, 0,
                indicating mark of first player, second player, and place not yet occupied.

        Returns:
            encode (a type hashable): the encoding of the observation.
        """
        #YOUR CODE HERE

        encode = tuple([tuple(ele) for ele in obs])
        return encode
        
        #END OF YOUR CODE

    def get_feedback(self, obs, reward, info, actor):
        """
        Receive feedback from the environment and update the agent.
        It will be called by the game when anyone makes an action and steps the environment.

        Args:
            obs (ndarray): a 2D numpy array, filled with 1, -1, 0,
                indicating mark of first player, second player, and place not yet occupied.

            reward (float): a value indicating the reward got from moves of two players.
            
            info (dict): a dict, with keys like "on_move" and "terminate",
                telling who should move now and if game end.
            
            actor (int): can either be 1 or -1, indicating whose action results in this feedback.
                1 means the first player, -1 is the seond one.

        """
        if self.mode == "train":
            if len(self.traj) > 0:
                if actor != self.mark:
                    last_obs_code, last_move, last_reward = self.traj[-1]
                    self.traj[-1] = last_obs_code, last_move, last_reward + reward
                else:
                    self.traj[-1] = *self.traj[-1], reward

            if info["terminate"]:
                self.update_table()
                #only use a trajectory once as the opponent is also being updated.
                self.traj = []
    
    def update_table(self):
        """
        Update the q-table with the trajectory recorded.
        YOU NEED TO FINISH IT
        """
        
        #YOUR CODE HERE
        
        alpha = 0.001
        gama = 0.9
        
        last_traj = self.traj[len(self.traj)-1]
        self.table[last_traj[0]][last_traj[1]] = last_traj[2]           # update Q table for the last trajectory

        # update Q table from last traj to the first traj
        for i in range(len(self.traj)-1, 0, -1):
            next_s, next_a, next_r = self.traj[i]
            s, a, r = self.traj[i-1]
            next_Q_table = self.table[next_s]
            max_next_Q_value = max(next_Q_table.values())
            #print(self.table[s][a] + alpha * (next_r + gama * max_next_Q_value - self.table[s][a]))
            self.table[s][a] = self.table[s][a] + alpha * (r + gama * max_next_Q_value - self.table[s][a])

        #END OF YOUR CODE


class HumanPlayer(Player):
    __doc__ = r"""
    An adapter for human player.

    * :attr:`mark` keeps the role of player, can either be 1 (for the first player),
      or -1 (for the second).
    
    * :attr:`ui` the user interface, a instance of TicTacToeUI class. 
    
    Args:
        mark (int): either 1 or -1, indicating first player or second player respectively.

        ui (TicTacToe): a instance of TicTacToeUI class, for rendering and interacting.
    """
    def __init__(self, mark, ui="tui"):
        super(HumanPlayer, self).__init__(mark)
        if ui == "tui":
            self.ui = TicTacToeTUI(mark)
        else:
            self.ui = ui

    def decide(self, obs):
        """
        Get action from user input.

        Args:
            obs (ndarray): a 2D numpy array, filled with 1, -1, 0,
                indicating mark of first player, second player, and place not yet occupied.

        Returns:
            action (tuple of (int, int)): indicates the coordinates to place mark,
                starting from 0, i.e. (0, 0) is the top left corner.
        """
        self.ui.render(obs)
        action = self.ui.get_action()
        return action

    def get_feedback(self, obs, reward, info, actor):
        """
        Pass feedback to user.

        Args:
            obs (ndarray): a 2D numpy array, filled with 1, -1, 0,
                indicating mark of first player, second player, and place not yet occupied.

            reward (float): a value indicating the reward got from moves of two players.
            
            info (dict): a dict, with keys like "on_move" and "terminate",
                telling who should move now and if game end.
            
            actor (int): can either be 1 or -1, indicating whose action results in this feedback.
                1 means the first player, -1 is the seond one.

        """
        self.ui.render(obs)
        if info["terminate"]:
            if reward == 1:
                self.ui.set_winner()
            elif reward == -1:
                self.ui.set_loser()
            else:
                self.ui.set_tie()
