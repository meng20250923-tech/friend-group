import json
# 注意：不需要 import os，除非你想删除文件

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

file_name = "friend_group_data.json" # <--- 更改文件扩展名

# --- 步骤 1: 将数据保存到 JSON 文件 (写入) ---
print(f"正在将数据保存到 {file_name}...")
try:
    with open(file_name, 'w', encoding='utf-8') as file:
        # 使用 json.dump() 将 Python 对象写入文件
        # indent=4 用于美化输出，使其可读性更高
        json.dump(group, file, indent=4, ensure_ascii=False) 
    print(f"✅ 保存成功。文件已创建。")
except Exception as e:
    print(f"❌ 错误: 保存文件时发生问题: {e}")


# --- 步骤 2: 从 JSON 文件中读取数据 (加载) ---
print("-" * 30)
print(f"正在从 {file_name} 读取数据...")
loaded_group = None
try:
    with open(file_name, 'r', encoding='utf-8') as file:
        # 使用 json.load() 从文件中加载 JSON 内容
        loaded_group = json.load(file)
    print(f"✅ 加载成功。")
except FileNotFoundError:
    print(f"❌ 错误: 文件 {file_name} 未找到。")
except json.JSONDecodeError:
    print(f"❌ 错误: 文件 {file_name} 不是有效的 JSON 格式。")
except Exception as e:
    print(f"❌ 错误: 加载文件时发生问题: {e}")


# --- 步骤 3: 检查结果是否与原始结构相同 (验证) ---
print("-" * 30)

if loaded_group is not None:
    print("原始数据结构 (group) 和加载数据结构 (loaded_group) 的比较:")
    
    is_identical = (group == loaded_group)
    
    print(f"加载后的结构是否与原始结构相同 (group == loaded_group)? **{is_identical}**")
else:
    print("无法进行验证，因为数据加载失败。")