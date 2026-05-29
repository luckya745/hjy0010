import glob

for filename in glob.glob('tabs/*.md'):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if line.strip() == '`python':
            new_lines.append('```python')
        elif line.strip() == '`':
            new_lines.append('```')
        else:
            new_lines.append(line)
            
    new_content = '\n'.join(new_lines)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {filename}')
