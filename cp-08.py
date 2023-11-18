class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate(self, quantity):
        total_price = self.price * quantity
        return total_price

coffee = Beverage("커피", 3000)
green_tea = Beverage("녹차", 2500)
ice_tea = Beverage("아이스티", 3000)

order_name = input("음료를 선택하세요 (커피, 녹차, 아이스티): ")

if order_name == "커피":
    selected_beverage = coffee
elif order_name == "녹차":
    selected_beverage = green_tea
elif order_name == "아이스티":
    selected_beverage = ice_tea
else:
    print("잘못된 음료 선택입니다.")
    exit()

quantity = int(input("수량을 입력하세요: "))

total_price = selected_beverage.calculate(quantity)
print(f"{order_name} {quantity}잔의 총 가격은 {total_price}원 입니다.")
