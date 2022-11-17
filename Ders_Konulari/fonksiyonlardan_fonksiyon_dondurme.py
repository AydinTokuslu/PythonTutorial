def kisi_sec(kisi):
    def takim_sec(takim):
        return f"{kisi} {takim} takımını tutuyor."
    return takim_sec

a = kisi_sec("Ali")
b = kisi_sec("Veli")

print(a("Fenerbahçe"))  # Ali Fenerbahçe takımını tutuyor.
print(b("Beşiktaş"))  # Veli Beşiktaş takımını tutuyor.