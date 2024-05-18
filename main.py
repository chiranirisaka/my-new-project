# main.py

from owner import Owner

def main():
    owner = Owner()
    owner.add_bus("Bus1", 50)
    owner.add_bus("Bus2", 30)

    print("\nViewing all buses:")
    owner.view_buses()



    print("\nViewing all buses after bookings:")
    owner.view_buses()

if __name__ == "__main__":
    main()
