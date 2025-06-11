import time

print("ロケット発射まで...")
for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)
print("🚀発射！！！")