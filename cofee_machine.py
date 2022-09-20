# 세분화 작업
# 보고서 작성 - report input 시 얼마나 남았는지 나온다.
# What would you like? (espresso/latte/cappuccino):

# 재료가 충분한지 확인
# report 입력 시 재료 남은 양이 나온다.
# =>What would you like? (espresso/latte/cappuccino): report
# What would you like? (espresso/latte/cappuccino): latte
# please insert coins.
# How many quartesrs?
# How many dimes?
# How many nickles?
# How many pennies?
# Here is $2.42 in change 거스름돈
# Here is your latte Enjoy!

# 커피 머신 프로젝트

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# 재료 양 비교하여 주문 가능여부 함수
def is_resource_enough(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough=False
    return is_enough

# 금액 계산 함수
def process_coin():
    print("please insert coins")
    total=int(input("how many quarters?: "))*0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# 구매 여부 판단 후 비용 적용 함수
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"here is ${change} in change")
        global money
        money +=drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False


# 재료 소진 적용 함수
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}")


# TODO 1. report 입력 상황 만들기
should_continue = False
while not should_continue:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        should_continue = True
    elif order == "report":
        print(f"Water:{resources['water']}ml\nMilk:{resources['milk']}ml\nCoffee:{resources['coffee']}g\nMoney:${money}")
    else:
        drink=MENU[order]
        if is_resource_enough(drink['ingredients']):
            payment= process_coin()
            if is_transaction_successful(payment,drink['cost']):
                make_coffee(order,drink["ingredients"])

## 개선해야 할 점
# 재료 소진에 대한 함수와 비용 증가에 대한 함수 적용 시 딕셔너리 비교에 대한 문제 해결되지 않음
# =>     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]: 과 같이 for문을 통해 각 item 별로 비교가 가능하다.