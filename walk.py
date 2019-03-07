import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap=plt.cm.Blues, edgecolor = 'none',s = 1)

    # Emphasize the beginning and end
    plt.scatter(0, 0, c = 'green', edgecolors= 'none', s = 100)

    plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors=  'none', s= 100)

    # Removing the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)


    # Setting the size of plotting window
    # plt.figure(dpi = 200,figsize=(10,8))
    plt.savefig('new.png', dpi = 200)
    plt.show()

    # keep_running = input('Make another walk? (y/n):')
    # if keep_running == 'n':
    #     break
