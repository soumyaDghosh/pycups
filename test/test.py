import cups

dests = cups.getDests()

for dest in dests:
    _dest = dests[dest]
    print(
        f"Name: {_dest.name}\nInstance: {_dest.instance}\nIs Default: {_dest.is_default}"
    )
    for option in _dest.options:
        _option = _dest.options[option]
        print(f"{_option.name}:  {_option.value}")

key_0 = list(dests.keys())[0]

print(cups.getOption("printer-uri-supported", dests[key_0].options))
