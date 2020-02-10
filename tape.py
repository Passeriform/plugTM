class Tape(object):

    blank_symbol = " "

    def __init__(self, tape_string = ""):
        self.__tape = dict((enumerate(tape_string)))

    def __str__(self):
        str = ""
        min_used_index = min(self.__tape.keys())
        max_used_index = max(self.__tape.keys())
        for i in range(min_used_index, max_used_index):
            str += self.__tape[i]
        return str

    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return Tape.blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char
