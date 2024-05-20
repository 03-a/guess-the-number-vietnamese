import random as r
import os
user = os.getlogin() 
print(f"Xin chào, {user}!")
print("Chào mừng bạn đến với RANDOMNUM - Chương trình Python dựa trên trò chơi Guess The Number của nền tảng ABCYa")
while True: 
    v = int(input("Nhập phiên bản cho trò chơi: v"))
    if v == 1: 
        print("Chọn cấp độ của bạn! ")
        print("Dễ: từ 1 đến 10")
        print("Trung bình: từ 1 đến 100")
        print("Khó: từ -500 đến 500")
        print("Nhập D với Dễ, TB với Trung Bình, K với Khó")
        lvl = input("Nhập cấp độ cho trò chơi: ")
        if lvl == "D": 
            rd = r.randint(1, 10)
            p = 0
            attempts = 5
            print("Tôi đang nghĩ một số giữa 1 và 10. Bạn hãy đoán số may mắn đó giúp tôi. ")
            while attempts > 0: 
                p = int(input("Số may mắn đó là: "))
                if p > rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải nhỏ hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p < rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải lớn hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p == rd: 
                    if attempts != 0: 
                        print(f"Xin chúc mừng bạn đã đoán được số may mắn sau {attempts} lần! Số đó là {rd}")
                        break
                    else: 
                        print(f"Bạn đã thua! Số đó là {rd}")
            if lvl == "TB": 
            rd = r.randint(1, 100)
            p = 0
            attempts = 7
            print("Tôi đang nghĩ một số giữa 1 và 100. Bạn hãy đoán số may mắn đó giúp tôi. ")
            while attempts > 0: 
                p = int(input("Số may mắn đó là: "))
                if p > rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải nhỏ hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p < rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải lớn hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p == rd: 
                    if attempts != 0: 
                        print(f"Xin chúc mừng bạn đã đoán được số may mắn sau {attempts} lần! Số đó là {rd}")
                        break
                    else: 
                        print(f"Bạn đã thua! Số đó là {rd}")
        if lvl == "K": 
            rd = r.randint(-500, 500)
            p = 0
            attempts = 10
            print("Tôi đang nghĩ một số giữa -500 và 500. Bạn hãy đoán số may mắn đó giúp tôi. ")
            while attempts > 0: 
                p = int(input("Số may mắn đó là: "))
                if p > rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải nhỏ hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p < rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải lớn hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p == rd: 
                    if attempts != 0: 
                        print(f"Xin chúc mừng bạn đã đoán được số may mắn sau {attempts} lần! Số đó là {rd}")
                        break
                    else: 
                        print(f"Bạn đã thua! Số đó là {rd}")
        t = input("Tiếp? : ")
        if t == "Không": 
            break
        else:
            continue
    elif v == 2: 
        print("Chọn cấp độ của bạn! ")
        print("Dễ: từ 1 đến 1000")
        print("Trung bình: từ -1000 đến 10000")
        print("Khó: từ -500000 đến 1000000")
        print("Nhập D với Dễ, TB với Trung Bình, K với Khó")
        lvl = input("Nhập cấp độ cho trò chơi: ")
        if lvl == "D": 
            rd = r.randint(1, 1000)
            p = 0
            attempts = 20
            print("Tôi đang nghĩ một số giữa 1 và 1000. Bạn hãy đoán số may mắn đó giúp tôi. ")
            while attempts > 0: 
                p = int(input("Số may mắn đó là: "))
                if p > rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải nhỏ hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p < rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải lớn hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p == rd: 
                    if attempts != 0: 
                        print(f"Xin chúc mừng bạn đã đoán được số may mắn sau {attempts} lần! Số đó là {rd}")
                        break
                    else: 
                        print(f"Bạn đã thua! Số đó là {rd}")
        if lvl == "TB": 
            rd = r.randint(-1000, 10000)
            p = 0
            attempts = 80
            print("Tôi đang nghĩ một số giữa -1000 và 10000. Bạn hãy đoán số may mắn đó giúp tôi. ")
            while attempts > 0: 
                p = int(input("Số may mắn đó là: "))
                if p > rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải nhỏ hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p < rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải lớn hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p == rd: 
                    if attempts != 0: 
                        print(f"Xin chúc mừng bạn đã đoán được số may mắn sau {attempts} lần! Số đó là {rd}")
                        break
                    else: 
                        print(f"Bạn đã thua! Số đó là {rd}")
        if lvl == "K": 
            rd = r.randint(-500000, 1000000)
            p = 0
            attempts = 160
            print("Tôi đang nghĩ một số giữa -5000000 và 1000000. Bạn hãy đoán số may mắn đó giúp tôi. ")
            while attempts > 0: 
                p = int(input("Số may mắn đó là: "))
                if p > rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải nhỏ hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p < rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải lớn hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p == rd: 
                    if attempts != 0: 
                        print(f"Xin chúc mừng bạn đã đoán được số may mắn sau {attempts} lần! Số đó là {rd}")
                        break
                    else: 
                        print(f"Bạn đã thua! Số đó là {rd}")
        t = input("Tiếp? : ")
        if t == "Không": 
            break
        else:
            continue
    elif v == 3: 
        print("Chọn cấp độ của bạn! ")
        print("Dễ: từ 100 đến 10000")
        print("Trung bình: từ -1000000 đến 10000000")
        print("Khó: từ -50000000 đến 1000000000")
        print("Nhập D với Dễ, TB với Trung Bình, K với Khó")
        lvl = input("Nhập cấp độ cho trò chơi: ")
        if lvl == "D": 
            rd = r.randint(100, 10000)
            p = 0
            attempts = 5
            print("Tôi đang nghĩ một số giữa 100 và 10000. Bạn hãy đoán số may mắn đó giúp tôi. ")
            while attempts > 0: 
                p = int(input("Số may mắn đó là: "))
                if p > rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải nhỏ hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p < rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải lớn hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p == rd: 
                    if attempts != 0: 
                        print(f"Xin chúc mừng bạn đã đoán được số may mắn sau {attempts} lần! Số đó là {rd}")
                        break
                    else: 
                        print(f"Bạn đã thua! Số đó là {rd}")
        if lvl == "TB": 
            rd = r.randint(-1000000, 10000000)
            p = 0
            attempts = 7
            print("Tôi đang nghĩ một số giữa -1000000 và 10000000. Bạn hãy đoán số may mắn đó giúp tôi. ")
            while attempts > 0: 
                p = int(input("Số may mắn đó là: "))
                if p > rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải nhỏ hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p < rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải lớn hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p == rd: 
                    if attempts != 0: 
                        print(f"Xin chúc mừng bạn đã đoán được số may mắn sau {attempts} lần! Số đó là {rd}")
                        break
                    else: 
                        print(f"Bạn đã thua! Số đó là {rd}")
        if lvl == "K": 
            rd = r.randint(-50000000, 1000000000)
            p = 0
            attempts = 10
            print("Tôi đang nghĩ một số giữa -50000000 và 1000000000. Bạn hãy đoán số may mắn đó giúp tôi. ")
            while attempts > 0: 
                p = int(input("Số may mắn đó là: "))
                if p > rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải nhỏ hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p < rd: 
                    attempts -= 1
                    print(f"Số bạn đoán phải lớn hơn {p}. Bạn còn {attempts} lần để đoán. ")
                elif p == rd: 
                    if attempts != 0: 
                        print(f"Xin chúc mừng bạn đã đoán được số may mắn sau {attempts} lần! Số đó là {rd}")
                        break
                    else: 
                        print(f"Bạn đã thua! Số đó là {rd}")
        t = input("Tiếp? : ")
        if t == "Không": 
            break
        else:
            continue
