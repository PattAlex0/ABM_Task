# Agent Based Model Task
This repository contains an Agent Based Model (ABM) created as part of my MSc. 
The ABM simulates agents in an environment from which they can 'eat'; they can share what they eat with other agents, steal from other agents if they are low on food, and also 'vomit' if they eat too much.

# Overview
This ABM achieves several things:
* It represents numerous agents on a 2 dimensional grid
* Each agent can communicate with other agents
* Agents can move through and modify the environment
* The entire process (inclding movement and environment modification) is animated
* The environment data is read in and the changed environment is saved out
* A report for how much each agent was able to eat is produced as an output

# Agent Framework
The agents are generated as a class which contains several different functions:
* Generates random x and y coordinates
* Randomly moves through the environment
* Can calculate the distance between agents
* Takes information from the environment (eating)
* Can share information with other agents in close proximity
* Can steal information from other agents in close proximity
* Will expunge information if they take too much (vomiting)
	
# Model
The ABM works in several steps:
1. Import modules, including the agent framework
2. Create several global lists that all agents can access
3. Import raster data to create the environment
4. Assign initial starting positions for agents
5. Create an animation function which includes agent behaviours
6. Create a generator function which determines how long the animation/model will run for.
7. Run the model/animation
8. Determine the maximum and minimum distance between agents
9. Save modified environment to txt file

# Modules
This ABM utilises several modules:
* CSV: To read in the environment data
* random: To generate random integers and floats
* matplotlib: the pyplot and animation modules to display the ABM process
