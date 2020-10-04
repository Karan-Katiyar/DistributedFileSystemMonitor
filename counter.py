
if __name__ == "__main__":
    filename = "LogContainer1.txt"
    with open(filename) as f:
        content = f.readlines()
    CreatedFiles = 0
    DeletedFiles = 0
    ModifiedFiles = 0
    MovedFiles = 0
    linecount = 0
    for line in content:
        linecount = linecount + 1
        line.strip().split('/n')
        if 'Created' in line:
            CreatedFiles = CreatedFiles +1
        elif line.startswith('Deleted'):
            DeletedFiles = CreatedFiles +1
        elif 'Modified' in line:
            ModifiedFiles = CreatedFiles +1
        elif line.startswith('Moved'):
            MovedFiles = CreatedFiles +1
    print(CreatedFiles , DeletedFiles, ModifiedFiles, MovedFiles)
    print(linecount)

