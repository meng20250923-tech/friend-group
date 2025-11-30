import yaml

# 1. 您提供的原始数据结构
group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}

file_name = "friend_group_data.yaml"

# --- 步骤 1: 将数据保存到 YAML 文件 (写入) ---
print(f"正在将数据保存到 {file_name}...")
try:
    with open(file_name, 'w', encoding='utf-8') as file:
        # 使用 default_flow_style=False 让 YAML 输出更具可读性
        yaml.dump(group, file, default_flow_style=False)
    print(f"✅ 保存成功。文件已创建。")
except Exception as e:
    print(f"❌ 错误: 保存文件时发生问题: {e}")


# --- 步骤 2: 从 YAML 文件中读取数据 (加载) ---
print("-" * 30)
print(f"正在从 {file_name} 读取数据...")
loaded_group = None
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        # 使用 safe_load 更安全地加载 YAML 内容
        loaded_group = yaml.safe_load(file)
    print(f"✅ 加载成功。")
except FileNotFoundError:
    print(f"❌ 错误: 文件 {file_name} 未找到。")
except Exception as e:
    print(f"❌ 错误: 加载文件时发生问题: {e}")


# --- 步骤 3: 检查结果是否与原始结构相同 (验证) ---
print("-" * 30)

if loaded_group is not None:
    print("原始数据结构 (group) 和加载数据结构 (loaded_group) 的比较:")
    
    # 比较两个 Python 字典是否完全相等
    is_identical = (group == loaded_group)
    
    # 打印比较结果
    print(f"加载后的结构是否与原始结构相同 (group == loaded_group)? **{is_identical}**")

    # 可选: 打印加载的数据以供查看
    # print("\n加载后的数据结构:")
    # print(loaded_group)
    
else:
    print("无法进行验证，因为数据加载失败。")

