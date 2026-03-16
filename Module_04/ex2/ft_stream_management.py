import sys


def ft_stream_management() -> None:
    try:
        archivist_id = input('Input Stream active. Enter archivist ID: ')
        status_report = input('Input Stream active. Enter status report: ')

        print(f'\n[STANDARD] Archive status from {archivist_id}:'
              f' {status_report}')
        print('[ALERT] System diagnostic: '
              'Communication channels verified', file=sys.stderr)
        print('[STANDARD] Data transmission complete')
        print('\nThree-channel communication test successful.')
    except KeyboardInterrupt:
        print('\nProgram stoped by user')


if __name__ == "__main__":
    print('=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n')
    ft_stream_management()
