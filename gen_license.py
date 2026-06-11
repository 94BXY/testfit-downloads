#!/usr/bin/env python3
"""生成 TestFit 授权码并输出 hash，直接粘贴到 licenses.json"""
import hashlib, secrets, string, json, sys

def gen_code():
    """生成 TF-XXXX-XXXX 格式授权码"""
    chars = string.ascii_uppercase + string.digits
    part = lambda: ''.join(secrets.choice(chars) for _ in range(4))
    return f"TF-{part()}-{part()}"

def sha256(code):
    return hashlib.sha256(code.encode()).hexdigest()

# ── 主流程 ──
buyer = input("买家名称/备注（可留空）: ").strip() or "未备注"
count = int(input("生成几个授权码？[1]: ").strip() or "1")

results = []
for _ in range(count):
    code = gen_code()
    h = sha256(code)
    results.append({"code": code, "hash": h, "buyer": buyer})

print("\n" + "="*50)
print("✅ 生成完成！请把以下 hash 粘贴到 licenses.json")
print("="*50)

for r in results:
    print(f"\n授权码: {r['code']}")
    print(f"  hash: {r['hash']}")
    print(f"  JSON: {{\"hash\": \"{r['hash']}\", \"buyer\": \"{r['buyer']}\", \"active\": true}}")

print("\n" + "="*50)
print("📋 给用户的授权码（发给他）:")
for r in results:
    print(f"  → {r['code']}")
print()
