try:
    with open(file_path,"r")as file:
        content=file.read()
        print(content)
except Exception as e:
    print(f"As error occured:{e}")
finally:
    print("closingvthe file,")+9