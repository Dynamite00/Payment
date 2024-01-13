
import tkinter as tk

class PaymentApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Payment App")

        self.restaurant_label = tk.Label(master, text="Choose a restaurant:")
        self.restaurant_label.pack()

        self.restaurant_name = "엄식당"
        self.menu_items = {
            "돈가스": 8000,
            "제육볶음": 8000,
            "김치찌개": 7000,
            "비빔밥": 7000,
            "삼겹살": 15000,
        }

        self.selected_menu = tk.StringVar(master)
        self.selected_menu.set("")  # 초기값은 빈 문자열

        self.menu_frame = tk.Frame(master)
        self.menu_frame.pack(pady=(0, 30))  # 3cm 간격

        # 각 음식에 대한 버튼을 생성
        self.menu_buttons = []
        for item in self.menu_items.keys():
            button = tk.Button(self.menu_frame, text=item, command=lambda i=item: self.select_menu(i))
            button.pack(side=tk.LEFT, padx=5)
            self.menu_buttons.append(button)

        self.order_label = tk.Label(master, text="Your order:")
        self.order_label.pack()

        self.order_entry = tk.Text(master, height=5, width=30)
        self.order_entry.pack()

        self.total_label = tk.Label(master, text="Total Amount: ₩0")
        self.total_label.pack()

        self.pay_button = tk.Button(master, text="Pay Now", command=self.pay_and_clear)
        self.pay_button.pack()

        # 구매 내역과 버튼 간격을 2cm로 조절
        self.purchase_label = tk.Label(master, text="Purchase History:")
        self.purchase_label.pack(pady=(20, 0))  # 2cm 간격

        self.purchase_history = tk.Text(master, height=10, width=40)
        self.purchase_history.pack()

        self.total_price = 0  # 누적 가격을 저장할 변수

        # 초기화 버튼 추가
        self.clear_button = tk.Button(master, text="Clear History", command=self.clear_history)
        self.clear_button.pack()

    def select_menu(self, menu):
        self.selected_menu.set(menu)
        current_order = self.order_entry.get("1.0", tk.END).strip()
        price = self.menu_items[menu]

        # 메뉴와 가격을 "Your order:" 입력 칸에 표시
        self.order_entry.insert(tk.END, f"{menu} - ₩{price}\n")

        self.total_price += price  # 누적 가격 업데이트
        self.total_label.config(text=f"Total Amount: ₩{self.total_price:,}")

    def pay_and_clear(self):
        self.pay()
        self.order_entry.delete("1.0", tk.END)  # "Your order:" 초기화

    def pay(self):
        selected_menu = self.selected_menu.get()
        order = self.order_entry.get("1.0", tk.END).strip()

        total_amount = self.calculate_total(order, selected_menu)
        self.total_label.config(text=f"Total Amount: ₩0")  # 지불 후 가격 초기화

        # 사용자가 입력한 메뉴와 가격을 차례대로 출력
        self.purchase_history.insert(tk.END, f"{order} - ₩{total_amount:,}\n")

        self.total_price = 0  # 지불 후 누적 가격 초기화

    def clear_history(self):
        self.purchase_history.delete(1.0, tk.END)  # 구매 내역 초기화

    def calculate_total(self, order, selected_menu):
        menu_price = self.menu_items[selected_menu]

        return len(order.split('\n')) * menu_price

if __name__ == "__main__":
    root = tk.Tk()
    app = PaymentApp(root)
    root.mainloop()