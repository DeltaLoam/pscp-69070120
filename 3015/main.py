"""Promotion"""
pro_person = int(input())
pro_pay = int(input())
price = int(input())
person = int(input())

print(int(((person // pro_person) * pro_pay + (person % pro_person)) * price))
