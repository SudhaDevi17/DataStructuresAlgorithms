def numberOfWaysToTraverseGraph(width, height):
    """
    :param width: width of graph/grid
    :param height: height of grid
    :return: the number of ways to reach the bottom right corner of grid from top left corner as starting point
    """
    # Find the quesiton here- https://www.algoexpert.io/questions/Number%20Of%20Ways%20To%20Traverse%20Graph.
    widths = [1 for _ in range(width)]
    res = [widths for _ in range(height)]

    print(res[0][0])

    for h in range(1, height):
        for w in range(1, width):
            res[h][w]= res[h-1][ w]+ res[h][w-1]

    return res[height-1][width-1]

