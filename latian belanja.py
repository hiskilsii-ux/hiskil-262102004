hari_pertama = {"keju", "tepung", "garam", "gula", "coklat"}
hari_kedua = {"garam", "gula", "coklat", "kecap"}
print()
hari_kedua.add("keju")
print("b. Hari kedua setelah ditambah 'keju':", hari_kedua)
barang_sama = hari_pertama & hari_kedua
print("c. Barang yang sama:", barang_sama)
hanya_hari_pertama = hari_pertama - hari_kedua
print("d. Dibeli di hari pertama, tidak di hari kedua:", hanya_hari_pertama)
hari_pertama.remove("garam")
print("e. Hari pertama setelah 'garam' dihapus:", hari_pertama)
hanya_hari_kedua = hari_kedua - hari_pertama
print("f. Dibeli di hari kedua, tidak di hari pertama:", hanya_hari_kedua)
barang_tidak_sama = hari_pertama ^ hari_kedua
print("g. Barang yang tidak sama:", barang_tidak_sama)
print("h. Semua keperluan hari pertama:")
for item in hari_pertama:
    print("   -", item)
print("i. Semua keperluan hari kedua:")
for item in hari_kedua:
    print("   -", item)

