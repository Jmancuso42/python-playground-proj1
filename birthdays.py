import logging


birthdays = {"Declan": "June 3rd", "Mum": "July 22nd", "Dad": "June 12"}

while True: 
    input_name = input("Enter a name: (blank to quit): ").strip().capitalize()
    if input_name == "":
        break
    elif not input_name.isalpha():
        print("Invalid input. Please enter a valid name.")
        continue
    if input_name in birthdays:
        print(birthdays[input_name] + " is the birthday of " + input_name)
    if input_name not in birthdays:
        print("That birthday is not in my database. Would you like to add it?")
        
        if input("Y/N: ").upper() == "Y":
            while True:
               
               try:
                    input_name = input("Enter a name: (blank to quit): ").strip().capitalize()
                    if len(input_name) > 22:
                        print("Name is too long. Please enter a name with 22 characters or less.")
                        continue
                    if input_name == "":
                        break
                    elif not input_name.isalpha():
                        print("Invalid input. Please enter a valid name.")
                        continue
                    try:
                        input_birthday = "Enter the birthday: "
                        if input_name in birthdays:
                            print(birthdays[input_name] + " is the birthday of " + input_name)
                        if input_name not in birthdays:
                            print("That birthday is not in my database. Would you like to add it?")  
                            if input("Y/N: ").upper() == "Y":
                                birthdays[input_name] = input(input_birthday)
                                print("Birthday database updated")
                                print(birthdays)
                    except Exception as e:
                        print("An error occurred:", str(e))
                        # Additional error handling code or actions
                        # Import the logging module
                        # Log the error
                        logging.error("An error occurred: " + str(e))
                        # Display a specific error message
                        print("Oops! Something went wrong. Please try again later.")
                     # Perform cleanup tasks
                     # ...
                        print("Invalid input. Please enter a valid name.")
                        continue

        elif input("Y/N: ").upper() == "N":
            print("Ok, I won't add it")
        else: 
             print("Something's up and I'm super confused, please try again") 
