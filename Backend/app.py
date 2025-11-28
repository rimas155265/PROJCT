def product_price_calculator():
    products_data = [
        ("منتج 1", 10.0),
        ("منتج 2", 20.0),
        ("منتج 3", 30.0),
        ("منتج 4", 40.0),
        ("منتج 5", 50.0)
    ]
    TAX_RATE = 0.15

    while True:
        print("\n--- قائمة المنتجات المتوفرة ---")
        for i, (name, price) in enumerate(products_data, 1):
            print(f"{i} - {name}")

        selection = input("\nيرجى إدخال رقم المنتج المطلوب (أو اكتب 'q' للخروج): ").strip()

        if selection.lower() == 'q':
            print("شكرًا لك. وداعاً!")
            break

        try:
            choice_index = int(selection) - 1
            
            if 0 <= choice_index < len(products_data):
                product_name, base_price = products_data[choice_index]
                
                price_with_tax = base_price * (1 + TAX_RATE)
                
                print(f"\n--- تفاصيل المنتج ---")
                print(f"السعر شامل الضريبة : {price_with_tax:.2f} ريال")
            else:
                print("⚠ خطأ: الرقم المُدخل خارج نطاق قائمة المنتجات. يرجى الاختيار من 1 إلى 5.")
        
        except ValueError:
            print("⚠ خطأ: يرجى إدخال رقم صحيح للمنتج.")

product_price_calculator()