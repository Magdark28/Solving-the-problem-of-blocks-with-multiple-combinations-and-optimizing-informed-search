# Solving-the-problem-of-blocks-with-multiple-combinations-and-optimizing-informed-search
This repository is a project that addresses the problem of blocks, a classic challenge in artificial intelligence that involves moving blocks from one place to another following certain rules. In this project, we developed solutions for two of the biggest challenges in this problem: dimensionality and informed search.
![](https://www.rose-hulman.edu/class/cs/archive/other-old/archive/fall06/materials/search_project_files/image003.gif)

The first achievement of this project was to solve the problem of dimensionality in the block environment. Traditionally, the block environment only allowed for a single possible combination of blocks, which limited the solution to a very small number of scenarios. We developed a general solution that allows for working with any number of blocks, greatly increasing the number of possible combinations and, therefore, the level of complexity of the problem.

The second achievement of this project was to develop two heuristics to optimize the CPU time of informed search algorithms. We used Dijkstra, A* and weighted A* algorithms for the heuristics, and managed to significantly reduce the time required to find the optimal solution. This is especially important in highly complex problems such as the block problem, where execution time can be extremely long.

This repository contains all the source code used in this project, as well as the results of our tests and experiments. We also include detailed documentation on how to use our solutions and how to reproduce our experiments.

Steps to use the repository:

  *1)Clone this repository to your local machine using the command "git clone https://github.com/[username]/[repository name]" in your terminal.
  
  *2)Explore the source code in the "src" folder, where you will find all our implementations to solve the block problem with multiple combinations and the     informed search heuristics.

