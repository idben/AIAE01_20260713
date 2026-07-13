def welcome():
    print("歡迎來到 Python 程式教室！")
    print("讓我們開始學習函式吧。")

def calc_area(width, height):
    area = width * height
    return area

# 使用前需要先定義
welcome()
area1 = calc_area(5, 10)
# function 沒有寫 return，預設值是 None
# function 沒有 return，無法把結果傳出給外部使用
print(f"面積是 {area1} 平方公分")