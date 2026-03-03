players_data = [
    {
        'name': 'alice', 'score': 2300, 'active': True,
        'achievements':
            {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon',
             'collector'},
        'region': 'north'
    },
    {
        'name': 'bob', 'score': 1800, 'active': True,
        'achievements': {'first_kill', 'level_10', 'boss_slayer'},
        'region': 'east'
    },
    {
        'name': 'charlie', 'score': 2150, 'active': True,
        'achievements': {
            'first_kill', 'level_10', 'treasure_hunter', 'speed_demon',
            'collector', 'perfectionist', 'boss_slayer'
        },
        'region': 'central'
    },
    {
        'name': 'diana', 'score': 2050, 'active': False,
        'achievements': {'first_kill', 'level_10'},
        'region': 'west'
    },
    ]


def list_comprehension(players_data: list[dict]) -> None:
    high_scores = [p['name'] for p in players_data if p['score'] > 2000]
    score_double = [p['score'] * 2 for p in players_data]
    active_player = [p['name'] for p in players_data if p['active']]

    print(f'High scores: {high_scores}')
    print(f'Scores doubled: {score_double}')
    print(f'Active players: {active_player}')


def dictionary_comprehension(players_data: list[dict]) -> None:
    categories_ranges = {
        'high': (2000, 9000),
        'medium': (2000, 2200),
        'low': (0, 2000)
    }
    player_score = {p['name']: p['score'] for p in players_data if p['active']}
    score_categories = {
        category: sum(
            1 for p in players_data
            if low <= p['score'] < high
        )
        for category, (low, high) in categories_ranges.items()
    }
    achievement_counts = {p['name']: len(p['achievements'])
                          for p in players_data if p['active']}

    print(f'Player scores: {player_score}')
    print(f'Score categories: {score_categories}')
    print(f'Achievements counts: {achievement_counts}')


def set_comprehension(players_data: list[dict]) -> None:
    unique_players = {d['name'] for d in players_data}
    unique_achievements = {
        achievement
        for p in players_data
        for achievement in p['achievements']
        }
    active_region = {p['region'] for p in players_data if p['active']}

    print(f'Unique players: {unique_players}')
    print(f'Unique achievements: {unique_achievements}')
    print(f'Active regions: {active_region}')


def combined_analysis(players_data: list[dict]) -> None:
    unique_achievements = {
        achievement
        for p in players_data
        for achievement in p['achievements']
        }
    average_score = sum(p['score'] for p in players_data) / len(players_data)
    max_score = max(p['score'] for p in players_data)
    top_performers = [p for p in players_data if p['score'] == max_score]
    print(f'Total players: {len(players_data)}')
    print(f'Total unique achievements: {len(unique_achievements)}')
    print(f'Average score: {average_score}')
    print('Top performer: ', end='')
    for p in top_performers:
        print(
              f" {p['name']} ({p['score']} points, "
              f"{len(p['achievements'])} achievements)",
              end=' '
            )
    print()


if __name__ == "__main__":
    print('=== Game Analytics Dashboard ===\n')

    print('=== List Comprehension Examples ===')
    try:
        list_comprehension(players_data)
    except Exception as e:
        print(e)

    print('\n=== Dict Comprehension Examples ===')
    try:
        dictionary_comprehension(players_data)
    except Exception as e:
        print(e)

    print('\n=== Set Comprehension ===')
    try:
        set_comprehension(players_data)
    except Exception as e:
        print(e)

    print('\n=== Combined Analysis ===')
    try:
        combined_analysis(players_data)
    except Exception as e:
        print(e)
