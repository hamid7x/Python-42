players_data = [
    {
        'name': 'alice', 'score': 2300, 'active': True,
        'achievement':
            {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    },
    {
        'name': 'bob', 'score': 1800, 'active': True,
        'achievement':
            {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    },
    {
        'name': 'charlie', 'score': 2150, 'active': True,
        'achievement':
            {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    },
    {
        'name': 'diana', 'score': 2050, 'active': False,
        'achievement':
            {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    },
    ]
if __name__ == "__main__":
    print('=== Game Analytics Dashboard ===\n')

    print('=== List Comprehension Examples ===')
    high_scores = [p['name'] for p in players_data if p['score'] > 2000]
    score_double = [p['score'] * 2 for p in players_data]
    active_player = [p['name'] for p in players_data if p['active']]

    print(f'High scores: {high_scores}')
    print(f'Scores doubled: {score_double}')
    print(f'Active players: {active_player}')

    print('=== Dict Comprehension Examples ===')
    player_score = {d['name']: d['score'] for d in players_data if d['active']}
    print(f'Player scores: {player_score}')
    high = 0
    med = 0
    low = 0
 
    category = {'hight': sum(1 for d in player_score if d['score'] > 2200)}
    print(category)
