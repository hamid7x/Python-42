def ft_crisis_response(file_name: str) -> None:
    try:
        with open(file_name, 'r') as f:
            content = f.read()
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            print(f'SUCCESS: Archive recovered - {content}')
            print('STATUS: Normal operations resumed')
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print('RESPONSE: Archive not found in storage matrix')
        print('STATUS: Crisis handled, system stable\n')
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print('RESPONSE: Security protocols deny access')
        print('STATUS: Crisis handled, security maintained\n')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print('=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n')
    files = ['lost_archive.txt', 'classified_vault.txt',
             'standard_archive.txt']
    for file in files:
        ft_crisis_response(file)
    print('\nAll crisis scenarios handled successfully. Archives secure.')
