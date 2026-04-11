from product import Product
from inventory import Inventory
from user import AdminUser
from gui import InventoryGUI
from login import show_login_window
import tkinter as tk

# Initialize inventory, Test data, Start GUI
def main():
    logged_in_user = show_login_window()
    if not logged_in_user:
        print("Login cancelled. Exiting system.")
        return

    # create object
    inventoryA = Inventory()
    inventoryB = Inventory()
    # create user
    admin = AdminUser("admin_user")

    # add three test products
    try:
        p1 = Product("P001", "Laptop", 999.99, 10)
        p2 = Product("P002", "Mouse", 25.50, 50)
        p3 = Product("P003", "Keyboard", 45.00, 30)
        
        inventoryA.add_product(p1)
        inventoryA.add_product(p2)
        inventoryB.add_product(p2)
        inventoryB.add_product(p3)
        
        inventoryC = inventoryA + inventoryB
        print(Inventory.addProductCount)

    except ValueError as e:
        print(f"Error initializing products: {e}")

    # start GUI window
    root = tk.Tk()
    InventoryGUI(root, inventoryC, logged_in_user)
    root.mainloop()

if __name__ == "__main__":
    main()
