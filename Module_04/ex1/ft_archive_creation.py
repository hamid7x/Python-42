def ft_archive_creation(file_name: str, data: list[str]) -> None:
    f = None
    try:
        print(f"Initializing new storage unit: {file_name}")
        f = open(file_name, 'w')
        print("Storage unit created successfully...\n")
        print('Inscribing preservation data...')
        for entry in data:
            f.write(entry)
            f.write('\n')
            print(entry)
        print("\nData inscription complete. Storage unit sealed.")
        print(
            f"Archive '{file_name}' "
            "ready for long-term preservation.")
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    data = [
        '[ENTRY 001] New quantum algorithm discovered',
        '[ENTRY 002] Efficiency increased by 347%',
        '[ENTRY 003] Archived by Data Archivist trainee'
    ]
    file_name = 'new_discovery.txt'
    ft_archive_creation(file_name, data)
