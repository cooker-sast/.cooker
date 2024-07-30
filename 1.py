import os

def remove_non_yaml_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file.endswith('.yaml') and not file.endswith('.yml'):
                file_path = os.path.join(root, file)
                print(f"Removing file: {file_path}")
                os.remove(file_path)

# 指定要遍历的目录路径
directory_path = 'semgrep'

# 调用函数删除非 YAML 文件
remove_non_yaml_files(directory_path)
