def pillars(num_pill, dist, width):
    if num_pill == 1: return 0
    return num_pill * width + num_pill * (dist * 100) - (dist * 100) - width * 2
