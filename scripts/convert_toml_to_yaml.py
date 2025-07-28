import re
import os


def convert_toml_to_yaml(content):
    # 提取 +++ ... +++ 之间的 front matter
    match = re.search(r"^\+\+\+\n(.*?)\n\+\+\+", content, re.DOTALL)
    if not match:
        return content  # 如果没有匹配，不处理

    toml_block = match.group(1)
    yaml_lines = []

    for line in toml_block.split("\n"):
        line = line.strip()
        if not line or "=" not in line:
            continue
        key, value = map(str.strip, line.split("=", 1))

        # 处理字符串（去除首尾引号）
        if re.match(r"^(['\"]).*\1$", value):
            value = value.strip("\"'")
            value = f"'{value}'"
        # 处理布尔
        elif value in ["true", "false"]:
            value = value.lower()
        # 处理数组
        elif value.startswith("[") and value.endswith("]"):
            # 提取数组中的每个项，去除引号、空格
            items = re.findall(r'"(.*?)"|\'(.*?)\'', value)
            clean_items = [f"'{item[0] or item[1]}'" for item in items]
            value = f"[{', '.join(clean_items)}]"
        # 其他（如时间戳）
        else:
            value = f"'{value}'"

        yaml_lines.append(f"{key}: {value}")

    yaml_block = "---\n" + "\n".join(yaml_lines) + "\n---"
    new_content = re.sub(r"^\+\+\+\n.*?\n\+\+\+", yaml_block, content, flags=re.DOTALL)
    return new_content


def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = convert_toml_to_yaml(content)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)


# 示例：处理整个目录下的 md 文件
def process_directory(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            full_path = os.path.join(folder_path, filename)
            process_file(full_path)


# 用法示例：
# process_file("example.md")
process_directory(".")
