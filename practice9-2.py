number = int(input("数字を入力してください:"))
found = True
def search_nember(date, key):
    found, Index = True, 0
    try:
        Index = date.index(key)
    except ValueError:
        found = False
    return Index, found

if found:
    print("%d 番目に %d がありました。" % (Index, number))
else:
    print("見つかりませんでした。")
