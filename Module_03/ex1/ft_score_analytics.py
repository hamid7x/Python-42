import sys

if __name__ == "__main__":
    print('=== Player Score Analytics ===')
    if len(sys.argv) == 1:
        print('No scores provided. ', end='')
        print('Usage: python3 ft_score_analytics.py <score1> <score2> ...')
    else:
        scores = []
        for i in range(1, len(sys.argv)):
            try:
                scores.append(int(sys.argv[i]))
            except Exception:
                print(f"'{sys.argv[i]}' Not valid score ... [skipped]")
        print(f'Scores processed: {scores}')
        print(f'Total players: {len(scores)}')
        print(f'Total score: {sum(scores)}')
        print(f'Average score: {sum(scores) / len(scores)}')
        print(f'Hight score: {max(scores)}')
        print(f'Low score: {min(scores)}')
        print(f'Score range: {max(scores) - min(scores)}')
