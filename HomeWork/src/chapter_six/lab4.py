# Lab 4 work
def kinetic_energy(velocity, mass):
    energy = (.5 * mass) * (velocity * velocity)
    print(f"The Mass is {mass}\nThe Velocity is {velocity}\nThe Kinetic Energy is {energy}")


def main():
    answer = 'y'
    while answer == 'y':
        try:
            answer = input("Do you wish to process mass and velocity? y or n ").lower()

            if answer == 'y':
                mass = float(input("Please enter in the mass: "))
                velocity = float(input("Please enter in the velocity: "))

                kinetic_energy(mass, velocity)

            else:
                print("Good bye!")

        except ValueError:
            print("Incorrect Value Entered!")
            answer = 'y'


main()
