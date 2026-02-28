if __name__ == "__main__":
    print('=== Achievement Tracker System ===\n')
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasuer_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}

    print(f'Player alice achievements: {alice}')
    print(f'Player bob achievements: {bob}')
    print(f'Player charlie achievements: {charlie}')

    print('\n=== Achievement Analytics ===')
    unique = alice.union(bob, charlie)
    print(f'All unique achievements: {unique}')
    print(f'Total unique achievements: {len(unique)}\n')

    common = alice.intersection(bob, charlie)
    rare = alice.difference(bob, charlie).union(bob.difference(alice, charlie),
                                                charlie.difference(alice, bob))
    print(f'Common to all players: {common}')
    print(f'Rare achievements (1 player): {rare}\n')

    print(f'Alice vs Bob common: {alice.intersection(bob)}')
    print(f'Alice unique: {alice.difference(bob)}')
    print(f'Bob unique: {bob.difference(alice)}')
