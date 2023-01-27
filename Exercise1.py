n = 10

def leibniz(n):
    t_sum = 0
    for i in range(n):
        term = 8/((4*i)+1)((4*i)+3)
        t_sum = t_sum + term
    return t_sum*4
