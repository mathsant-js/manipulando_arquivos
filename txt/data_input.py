def write_info(info):
    while True:
        response = input(f"Type your {info}: ")
        
        if response.strip():
            break
    
    return response

def write_in_file(filename, name, age):
    with open(f"{filename}.txt", "a") as f:
        f.write(f"Name: {name} | Age: {age}")
        
def write_in_last_row(filename, name, age):
    with open(f"{filename}.txt", "a") as f:
        f.write(f"\nName: {name} | Age: {age}")

name = write_info("name")
age = write_info("age")

write_in_file("data", name, age)

print()

name = write_info("name")
age = write_info("age")

write_in_last_row("data", name, age)