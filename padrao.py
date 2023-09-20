def door_mat_design(n, m):
    pattern = []
    # Generate the top half
    for i in range(1, n, 2):
        pattern.append(('.|.' * i).center(m, '-'))
    
    # Add the WELCOME line
    pattern.append('WELCOME'.center(m, '-'))
    
    # Generate the bottom half
    for i in range(n-2, 0, -2):
        pattern.append(('.|.' * i).center(m, '-'))
    
    return '\n'.join(pattern)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(door_mat_design(n, m))
