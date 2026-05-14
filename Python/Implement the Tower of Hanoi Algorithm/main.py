def hanoi_solver(n):
    # Initialize rods: Smallest disk is 1, largest is n
    rods = {
        'source': list(range(n, 0, -1)),
        'auxiliary': [],
        'target': []
    }
    
    moves_log = []

    def get_state():
        # Returns current state of rods as a space-separated string of lists
        return f"{rods['source']} {rods['auxiliary']} {rods['target']}"

    def move_disk(n_disks, source, target, auxiliary):
        if n_disks > 0:
            # Step 1: Move n-1 disks to auxiliary rod
            move_disk(n_disks - 1, source, auxiliary, target)
            
            # Step 2: Move the nth disk to the target rod
            disk = rods[source].pop()
            rods[target].append(disk)
            moves_log.append(get_state())
            
            # Step 3: Move the n-1 disks from auxiliary to target
            move_disk(n_disks - 1, auxiliary, target, source)

    # Initial arrangement
    moves_log.append(get_state())
    
    # Solve recursively
    move_disk(n, 'source', 'target', 'auxiliary')
    
    return "\n".join(moves_log)