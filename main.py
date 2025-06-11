import random

運勢 = random. randint(1, 100)
print(f"今日の運勢は・・・{運勢}点！")

if 運勢 >= 80:
    print("⭐️ 大吉！素晴らしい１日になるで！")
elif 運勢 >= 60:
    print("😆 中吉！いい事あるかも！")
elif 運勢 >=40:
    print("🙂　小吉！10円拾うかも")
else:
    print("💪 今日は自力で切り開け！")