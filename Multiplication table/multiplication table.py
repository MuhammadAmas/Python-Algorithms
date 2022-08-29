for i in range (2, 21):
    with open (f"multplicaiton table of {i}.txt", 'w') as f:
        for j in range (11):
            f.write(f"{i}x{j}={i*j}\n")