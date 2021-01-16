from random import randint

class Game:
    def __init__(self, game_mode):
        self.game_mode = game_mode
        if self.game_mode == "PC":
            print("Введите, чтобы сгенерировать игровое поле: \nsession.generate_field(число открытых клеток)")
            print("\nВведите, чтобы компьютер предложил решение данной задачи: \nsession.solution()")
        elif self.game_mode == "Human":
            print("Введите, чтобы загрузить сохранение: \nsession.upload_session()")
            print("\nВведите, чтобы сохранить игру: \nsession.save_session()")
            print("\nВведите, чтобы начать новую игру(старые сохранения будут утеряны!):\nsession.generate_field(число открытых клеток)")
            print("\nЧтобы заполнять поле вводите: \nsession.update_cell(i, j, v)\ni - номер строки от 1 до 9 \nj - номер колонки от 1 до 9 \nv - значение от 1 до 9")
            print("\nПриятной игры:)")
        else:
            print("ERROR: некорректный режим игры")
        self.field = [[0 for j in range(9)] for i in range(9)]
        self.finished = False

    def print_field(self):
        for i in range(13):
            print('-', end = ' ')
        print()
        for i in range(9):
            print('|', end = ' ')
            for j in range(9):
                print(self.field[i][j], end = ' ')
                if (j + 1) % 3 == 0 and j != 8:
                    print('|', end = ' ')
            print('|', end = ' ')
            print()
            if (i + 1) % 3 == 0 and i != 8:
                for i in range(13):
                    print('-', end = ' ')
                print()
        for i in range(13):
            print('-', end = ' ')
        print()

    def possible(self, y, x, n):
        for i in range(9):
            if self.field[y][i] == n:
                return False
        for i in range(9):
            if self.field[i][x] == n:
                return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(3):
            for j in range(3):
                if self.field[y0+i][x0+j] == n:
                    return False
        return True

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.field[i][j] == 0:
                    for n in range(1, 10):
                        if self.possible(i, j, n):
                            self.field[i][j] = n
                            self.solve()
                            if not self.finished:
                                self.field[i][j] = 0
                    return
        self.finished = True

    def solution(self):
        tmp = self.field
        self.solve()
        if not self.finished:
            print("Неразрешимая головоломка")
            return
        for i in range(9):
            for j in range(9):
                if tmp[i][j] == 0:
                    print("Строка", i+1, "Колнонка", j+1, "Значение", self.field[i][j])
        self.print_field()

    def generate_field(self, opened_cells):
        self.opened_cells = opened_cells
        cells_set = set()
        while len(cells_set) < self.opened_cells:
            cells_set.add((randint(0, 8), randint(0, 8)))

        while len(cells_set) > 0:
            cell = cells_set.pop()
            for n in range(1, 10):
                if self.possible(cell[0], cell[1], n):
                    self.field[cell[0]][cell[1]] = n
                    break
        self.print_field()
    
    def update_cell(self, i, j, v):
        if not(1 <= i <= 9):
            print("ERROR: некорректый номер строки")
            return
        if not(1 <= j <= 9):
            print("ERROR: некорректый номер колонки")
            return
        if not(1 <= v <= 9):
            print("ERROR: некорректное значение ячейки поля")
            return
        if self.possible(i-1, j-1, v):
            self.field[i-1][j-1] = v
            self.print_field()
        else:
            print("Ops... Try to put another number")

    def save_session(self):
        f = open("game.pkl", "w")
        for i in range(9):
            print(*self.field[i], file=f)
        print("Игровое поле успешно сохранено")

    def upload_session(self):
        try:
            f = open("game.pkl", "r")
        except FileNotFoundError:
            print("ERROR: нет сохранений")
            return
        tmp = f.readline()
        if tmp == "":
            print("ERROR: нет сохранений")
            return
        self.field[0] = list(map(int, tmp.split()))
        for i in range(1, 9):
            self.field[i] = list(map(int, f.readline().split()))
        self.print_field()


print("Привет! Чтобы начать игру, введи: \nsession = Game('режим игры')")
print("\nРежимы игры: \n'PC' - играет компьютер \n'Human' - играет пользователь")

