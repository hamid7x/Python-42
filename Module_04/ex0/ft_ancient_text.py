if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file_name = 'ancient_fragment.txt'
    f = None
    try:
        f = open(file_name, 'r')
        content = f.read()
        print(f'Accessing Storage Vault: {file_name}')
        print('Connection established...\n')
        print('RECOVERED DATA:')
        print(content)
        print('\nData recovery complete. Storage unit disconnected.')
    except FileNotFoundError:
        print('ERROR: Storage vault not found. Run data generator first.')
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()
