# Problem: Climbing Stairs
# You can climb 1 or 2 steps at a time
# How many ways to reach step n?
# This is basically Fibonacci!

def climb_stairs(n):
    if n <= 2:
        return n
    
    one_step = 1
    two_steps = 2

    for i in range(3, n + 1):
        current = one_step + two_steps
        one_step = two_steps
        two_steps = current

    return two_steps

print(climb_stairs(2))    # 2
print(climb_stairs(3))    # 3
print(climb_stairs(5))    # 8