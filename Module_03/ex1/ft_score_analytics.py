import sys


def process_scores(args: list[str]) -> list[int]:
    if len(args) == 0:
        raise ValueError('No scores provided. Usage: '
                         'python3 ft_score_analytics.py <score1> <score2> ...')
    scores = []
    for arg in args:
        try:
            scores += [int(arg)]
        except ValueError:
            print(f"'{arg}' Not valid score ... [skipped]")
    if not scores:
        raise ValueError('No valid scores provided.')

    return scores


if __name__ == "__main__":
    print('=== Player Score Analytics ===')

    try:
        scores = process_scores(sys.argv[1:])
        print(f'Scores processed: {scores}')
        print(f'Total players: {len(scores)}')
        print(f'Total score: {sum(scores)}')
        print(f'Average score: {sum(scores) / len(scores)}')
        print(f'High score: {max(scores)}')
        print(f'Low score: {min(scores)}')
        print(f'Score range: {max(scores) - min(scores)}')
    except Exception as e:
        print(e)
