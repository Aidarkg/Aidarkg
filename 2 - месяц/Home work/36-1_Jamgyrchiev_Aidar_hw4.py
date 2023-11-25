from enum import Enum
from random import choice, randint


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    BLOCK_DAMAGE_AND_REVERT = 3
    HEAL = 4
    PARALYSIS = 5
    KEEPER = 6


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    @defence.setter
    def defence(self, value):
        self.__defence = value

    def choose_defence(self, heroes):
        random_hero = choice(heroes)
        self.__defence = random_hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if (hero.ability == SuperAbility.BLOCK_DAMAGE_AND_REVERT
                        and self.__defence != SuperAbility.BLOCK_DAMAGE_AND_REVERT):
                    hero.blocked_damage = int(self.damage / 5)
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.base_damage = self.damage
        if type(ability) == SuperAbility:
            self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeff = randint(2, 6)
        boss.health -= self.damage * coeff
        print(f'Warrior {self.name} hit critically {self.damage * coeff}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        bonus = randint(5, 10)
        for hero in heroes:
            hero.damage += bonus
        print(f'Magic {self.name} bonus {bonus}')


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted {self.__blocked_damage}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health += self.__heal_points
        print(f'Medic heal {self.__heal_points}')


class Thor(Hero, Boss):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.PARALYSIS)

    def apply_super_power(self, boss, heroes):
        boss_stunned = randint(1, 10)
        if boss_stunned < 3:
            boss.damage = 0
            print(f'Thor paralysis Boss')
        else:
            boss.damage = 50


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super(Witcher, self).__init__(name, health, damage, SuperAbility.KEEPER)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health == 0:
                hero.health = self.health
                self.health = 0
                print(f'Wicher sacrificed himself {hero.name}')


round_number = 0


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True

    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def show_stats(boss, heroes):
    print(f'ROUND {round_number} -----------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        hero.damage = hero.base_damage
        if (hero.health > 0 and boss.health > 0
                and boss.defence != hero.ability):
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_stats(boss, heroes)


def start_game():
    boss = Boss('Balmond', 1000, 50)

    warrior_1 = Warrior('Grid', 280, 10)
    warrior_2 = Warrior('Tigril', 270, 15)
    magic = Magic('Potter', 260, 20)
    berserk = Berserk('Aroot', 250, 10)
    doc = Medic('Stown', 240, 5, 15)
    assistant = Medic('Astes', 300, 5, 5)
    thor = Thor('Thor', 300, 20)
    witcher = Witcher('Kan Han Su', 500, 0)
    heroes_list = [warrior_1, warrior_2, magic, berserk, doc, assistant, thor, witcher]

    show_stats(boss, heroes_list)

    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


start_game()
