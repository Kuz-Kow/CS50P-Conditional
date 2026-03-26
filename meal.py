def main():
    time = input("What time is it? :  ").strip()
    time = convert(time)
    
    if 7<= time <= 8:
        print("Breakfest time")

    elif 12<= time <= 13:
        print("Lunch time")

    elif 18<= time <= 19:
        print("Dinner time")



def convert(time):
    hours, minutes = time.split(":")
    return (int(hours) + int(minutes)/60)


if __name__ == "__main__":
    main()