def welcome():
    print("歡迎來到 Python 程式教室！")
    print("讓我們開始學習函式吧。")

def calc_area(width, height):
    # 傳入的內容叫參數
    # function 中定義的變數，區域變數
    # 除非用方法傳出，否則 function 外無法取得與使用
    area = width * height
    return area

def get_user_info():
    name = "Ben"
    age = 38
    # 以 tuple 格式傳出
    return name, age



# 使用前需要先定義
welcome()
area1 = calc_area(5, 10)
# 使用 function 傳入的內容中文稱為引數
# function 沒有寫 return，預設值是 None
# function 沒有 return，無法把結果傳出給外部使用
print(f"面積是 {area1} 平方公分")
# print(width, height, area)    # 使用了區域變數
user_name, user_age = get_user_info()
print(f"姓名是 {user_name}，年紀是 {user_age}")

# 關鍵字引數：使用時就把參數名稱帶入的用法
area2 = calc_area(height=9, width=10)
print(area2)
print("-"*30)