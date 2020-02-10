from turingmachine import TuringMachine

def main():
    initial_state = "init",
    accepting_states = ["final"],
    transition_function = {("init","0"):("init", "1", "R"),
                           ("init","1"):("init", "0", "R"),
                           ("init"," "):("final"," ", "N"),
                           }
    final_states = {"final"}

    tm = TuringMachine("010011 ",
                      initial_state = initial_state,
                      final_states = final_states,
                      transition_function=transition_function)

    print("Input on Tape:{}\n".format(tm.get_tape()))

    while not tm.final():
        tm.step()

    print("Result of the Turing machine calculation:")
    print(tm.get_tape())

if __name__ == '__main__':
    main()
