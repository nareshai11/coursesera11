#generating a classic multiplication table
for i in range(1,11):
    for j in range(1,11):
        print("classsic multiplication ", "*", j, "=", i * j, end="\t")
    print()