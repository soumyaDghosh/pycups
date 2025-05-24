import cups

dests = cups.getDests()

for printer in dests:
    print(f"Printer: {printer.name},\nIs Default: {printer.is_default}\nOptions: |")
    for opt in printer.options:
        print(f"  {opt.name}: {opt.value}")