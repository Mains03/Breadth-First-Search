# Breadth-First-Search
Performs a breadth first search to find the shortest path from start ('A') to finish ('B').

To edit the grid, in 'main.py' change the variable 'grid'. Characters can be added or removed however the length of each row must be the same. 'A' is the start, 'B' is the end - neither must occur more than once. An error will be thrown if there isn't a path from source to destination, as the graphics section expects a path from start to finsh when drawing the path taken.

'#' is wall. '.' is floor - cells which can be traversed.

Traversal only occurs horizontally and vertically, not diagonally.
