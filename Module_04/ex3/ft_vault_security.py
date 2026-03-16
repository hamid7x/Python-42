def ft_vault_security(file1: str, file2: str) -> None:
    try:
        print('Initiating secure vault access...')
        print('Vault connection established with failsafe protocols\n')
        print('SECURE EXTRACTION:')
        with open(file1, 'r') as f1:
            content = f1.read()
            print(content)
        print('\nSECURE PRESERVATION:')
        with open(file2, 'w') as f2:
            f2.write('[CLASSIFIED] New security protocols archived')
        with open(file2, 'r') as f2:
            print(f2.read())
        print('Vault automatically sealed upon completion')
        print('\nAll vault operations completed with maximum security.')
    except FileNotFoundError:
        print(f'{file1} not found')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print('=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n')
    file1 = 'classified_data.txt'
    file2 = 'security_protocols.txt'
    ft_vault_security(file1, file2)
