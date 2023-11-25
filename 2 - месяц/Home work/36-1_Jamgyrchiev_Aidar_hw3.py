class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        result = self.__cpu + ' ' + str(self.__memory)
        return f'{result}'

    def __str__(self):
        return f'Computer cpu: {self.__cpu}, memory: {self.__memory}'

    def __eq__(self, other):
        return self.__memory == other.memory

    def __lt__(self, other):
        return self.__memory < other.memory

    def __le__(self, other):
        return self.__memory <= other.memory

    def __gt__(self, other):
        return self.__memory > other.memory

    def __ge__(self, other):
        return self.__memory >= other.memory

    def __ne__(self, other):
        return self.__memory != other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        list_sim = self.__sim_cards_list[sim_card_number - 1]
        print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {list_sim}')

    def __str__(self):
        return f'Sim car list: {self.__sim_cards_list}'


class Smartphone(Computer, Phone):
    def __init__(self, cpu, memory, sim_card_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_card_list)

    @staticmethod
    def use_gps(location):
        print(f"Использование GPS навигации на '{location}'.")

    def __str__(self):
        return f'Smartphone cpu: {self.cpu}, memory: {self.memory}'


computer = Computer('core i5', 500)
phone = Phone(["Beeline", "O!", "Megacom"])
smartphone1 = Smartphone('A12', 128, ['Beeline', 'O!', 'Megacom'])
smartphone2 = Smartphone('Snapdragon 680', 64, ['Beeline', 'O!', 'Megacom'])

print(f'{computer}\n'
      f'{phone}\n'
      f'{smartphone1}\n'
      f'{smartphone2}')

phone.call(2, 996706183379)
print(computer.make_computations())
smartphone1.use_gps('Home')

if smartphone1 > smartphone2:
    print("Smartphone1 has more memory than Smartphone2.")
elif smartphone1 == smartphone2:
    print("Smartphone1 and Smartphone2 have the same amount of memory.")
else:
    print("Smartphone2 has more memory than Smartphone1.")
