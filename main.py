import random
import tkinter as tk
import tkinter.messagebox as msgbox

total = ""

def add_to_total(character):
    global total
    total += str(character)
    text_box.delete(1.0, "end")
    text_box.insert(1.0, total)


def evaluate_total():
    global total
    if check_duplicate_num(total) is True:
        clear_field()
        text_box.insert(1.0, "Duplicate number detected. Retry 🔄")
    elif check_four_num(total) != 4:
        clear_field()
        text_box.insert(1.0, "You must use all 4 numbers. Retry 🔄")
    else:
        try:
            total = str(eval(total))
            text_box.delete(1.0, "end")
            text_box.insert(1.0, total)
        except:
            clear_field()
            text_box.insert(1.0, "Error")
        if float(total) == 24.0:
            clear_field()
            victory_msg()
        else:
            clear_field()
            text_box.insert(1.0, "That's not 24.\nRetry 🔄")
        

def clear_field():
    global total
    total = ""
    text_box.delete(1.0, "end")


def victory_msg():
    msgbox.showinfo(title = "", message = "You made 24.\nYou Won! 🎉")
    root.destroy()


def generate_unique_numbers():
    list = []
    while len(list) != 4:
        random_num = random.randint(1, 9)
        if random_num not in list:
            list.append(random_num)
    return list


def check_duplicate_num(character): # Players are only allowed to use each number once when making 24
    count_1 = 0; count_2 = 0; count_3 = 0; count_4 = 0
    for char in character:
        if char == str(numbers[0]):
            count_1 += 1
        elif char == str(numbers[1]):
            count_2 += 1
        elif char == str(numbers[2]):
            count_3 += 1
        elif char == str(numbers[3]):
            count_4 += 1
    if count_1 > 1 or count_2 > 1 or count_3 > 1 or count_4 > 1:
        return True
    else:
        return False


def check_four_num(character): # Players must use all four numbers when making 24
    count = 0
    for char in character:
        if char.isdigit():
            count += 1
    return count


if __name__ == "__main__":
    print("""Welcome to Make 24
    
    Rules:
        1. You have to use the numbers and operations provided to you to get the number '24'.
        2. You are allowed to use each number provided to you once and only once.
        3. You must use all four numbers provided to you.
        4. Basic PEMDAS order of operations for calculation. (Look this up if you need to).""")

    while True:
        player_input = input("Are you ready to play? Enter 'R' if you're ready.\n> ").upper()
        if player_input not in "R":
            print("Enter 'R' when you're ready.")
        else:
            break
    
    if player_input == "R":
        numbers = generate_unique_numbers() # Generating four unique one digit numbers
        
        # Setting up the GUI
        root = tk.Tk()
        root.geometry("304x259")
        text_box = tk.Text(root, height = 2, width = 15, font = ("Arial", 24))
        text_box.grid(columnspan = 5)

        # Setting up the buttons of the GUI
        button_1 = tk.Button(root, text = str(numbers[0]), command=lambda: add_to_total(numbers[0]), width = 6, height = 2, font = ("Arial", 14))
        button_1.grid(row = 2, column = 0)
        button_2 = tk.Button(root, text = str(numbers[1]), command=lambda: add_to_total(numbers[1]), width = 6, height = 2, font = ("Arial", 14))
        button_2.grid(row = 2, column = 1)
        button_3 = tk.Button(root, text = str(numbers[2]), command=lambda: add_to_total(numbers[2]), width = 6, height = 2, font = ("Arial", 14))
        button_3.grid(row = 2, column = 2)
        button_4 = tk.Button(root, text = str(numbers[3]), command=lambda: add_to_total(numbers[3]), width = 6, height = 2, font = ("Arial", 14))
        button_4.grid(row = 2, column = 3)
        button_add = tk.Button(root, text = "+", command=lambda: add_to_total("+"), width = 6, height = 2, font = ("Arial", 14))
        button_add.grid(row = 3, column = 0)
        button_subtract = tk.Button(root, text = "-", command=lambda: add_to_total("-"), width = 6, height = 2, font = ("Arial", 14))
        button_subtract.grid(row = 3, column = 1)
        button_multiply = tk.Button(root, text = "*", command=lambda: add_to_total("*"), width = 6, height = 2, font = ("Arial", 14))
        button_multiply.grid(row = 3, column = 2)
        button_divide = tk.Button(root, text = "/", command=lambda: add_to_total("/"), width = 6, height = 2, font = ("Arial", 14))
        button_divide.grid(row = 3, column = 3)
        button_open = tk.Button(root, text = "(", command=lambda: add_to_total("("), width = 6, height = 2, font = ("Arial", 14))
        button_open.grid(row = 4, column = 0)
        button_close = tk.Button(root, text = ")", command=lambda: add_to_total(")"), width = 6, height = 2, font = ("Arial", 14))
        button_close.grid(row = 4, column = 1)
        button_equals = tk.Button(root, text = "=", command = evaluate_total, width = 6, height = 2, font = ("Arial", 14))
        button_equals.grid(row = 4, column = 2)
        button_clear = tk.Button(root, text = "🔄", command = clear_field, width = 6, height = 2, font = ("Arial", 14))
        button_clear.grid(row = 4, column = 3)

        root.mainloop()






