import os
from django.shortcuts import render, redirect
from .models import Product, Add_WarehouseItem
from .forms import Add_WarehouseItemForm
import subprocess



def home(request):
    products = Product.objects.all()
    low_stock = Product.objects.filter(quantity__lt=5)
    recent = Product.objects.order_by('-added_on')[:5]
    sno_total = len(recent) * (len(recent) + 1) // 2
    return render(request, 'home.html', {
        'total': products.count(),
        'low_stock': low_stock.count(),
        'recent': recent
    })


def add_item(request):
    if request.method == 'POST':
        form = Add_WarehouseItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            
            # 👇 Call your C function to add item to C linked list (if using ctypes or subprocess)
            # add_item_to_c_linked_list(item.name, item.quantity, item.location, item.description)
            
            return redirect('item_list')  # redirect to item list view
    else:
        form = Add_WarehouseItemForm()
    return render(request, 'add_item.html', {'form': form})


# def view_item(request):
#     items = Add_WarehouseItem.objects.all()
#     return render(request, 'view_itemList.html', {'items': items})

def view_item(request):
    # Export Django DB items to input file
    items = Add_WarehouseItem.objects.all()
    with open("items_input.txt", "w") as f:
        for item in items:
            f.write(f"{item.name}|{item.quantity}|{item.Price}|{item.description}\n")

    # Call C sorting executable
    exe_path = os.path.join("F:\\", "Project", "WarehouseWebApp", "linkedlist_sort.exe")
    output = subprocess.check_output([exe_path]).decode().splitlines()

    # Process the output safely
    sorted_items = []
    for line in output:
        print("DEBUG LINE:", line)  # optional for debugging
        parts = line.strip().split("|")
        if len(parts) == 4:
            name, quantity, Price, description = parts
            sorted_items.append({
                'name': name,
                'quantity': int(quantity),
                'Price': Price,
                'description': description,
            })
        else:
            print(f"Skipping malformed line: {line}")

    return render(request, 'view_itemList.html', {'items': sorted_items})


