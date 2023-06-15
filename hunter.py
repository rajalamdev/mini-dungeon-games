# Nama: Raj Alam
# NRP: 1152200003

# Membangun dungeon dengan matriks 2D
dungeon = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', 'X', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '+', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

# membuat class Hunter
class Hunter:
    def __init__(self):
        self.id = "P"
        self.name = "Hunter"
        self.hp = 1000
        self.armor = 10
        self.power = 50
        self.currentCoordinateRow = 1
        self.currentCoordinateCol = 1
        self.status = "ALIVE"

    def menyerang(self, target):
        target.hp -= self.power

    def diserang(self, target):
        self.hp -= target.power

    def moveToTop(self):
        dungeon[self.currentCoordinateRow][self.currentCoordinateCol] = " "
        self.currentCoordinateRow -= 1
    
    def moveToBottom(self):
        dungeon[self.currentCoordinateRow][self.currentCoordinateCol] = " "
        self.currentCoordinateRow += 1

    def moveToRight(self):
        dungeon[self.currentCoordinateRow][self.currentCoordinateCol] = " "
        self.currentCoordinateCol += 1
    
    def moveToLeft(self):
        dungeon[self.currentCoordinateRow][self.currentCoordinateCol] = " "
        self.currentCoordinateCol -= 1

# membuat class Enemy
class Enemy:
    def __init__(self, id, name, hp, power, coordinatRow, coordinatCol):
        self.id = id
        self.name = name
        self.hp = hp
        self.power = power
        self.coordinatRow = coordinatRow
        self.coordinatCol = coordinatCol
        self.status = "ALIVE"

    def menyerang(self, target):
        target.hp -= self.power

    def diserang(self, target):
        self.hp -= target.power

# membuat class Boss
class Boss(Enemy):
    def __init__(self, id, name, hp, power, coordinatRow, coordinatCol, armor):
        super().__init__(id, name, hp, power, coordinatRow, coordinatCol)
        self.armor = armor

# membuat class MiniMonster
class MiniMonster(Enemy):
    def __init__(self, id, name, hp, power, coordinatRow, coordinatCol):
        super().__init__(id, name, hp, power, coordinatRow, coordinatCol)

# membuat class Monster
class Monster(Enemy):
    def __init__(self, id, name, hp, power, coordinatRow, coordinatCol):
        super().__init__(id, name, hp, power, coordinatRow, coordinatCol)

# objek hunter
hunter = Hunter()

# objek boss
boss = Boss("B", "Diablo", 3000, 100, 4, 6, 10)

# objek monster
miniMonster1 = MiniMonster("m", "Slime 1", 50, 1, 13, 1)
miniMonster2 = MiniMonster("m", "Slime 2", 50, 1, 7, 3)
miniMonster3 = MiniMonster("m", "Slime 3", 50, 1, 9, 6)
miniMonster4 = MiniMonster("m", "Slime 4", 50, 1, 9, 11)
miniMonster4 = MiniMonster("m", "Slime 5", 50, 1, 7, 13)
miniMonster5 = MiniMonster("m", "Slime 6", 50, 1, 1, 13)
miniMonster6 = MiniMonster("m", "Slime", 50, 1, 1, 5)
miniMonster7 = MiniMonster("m", "Slime", 50, 1, 7, 9)
miniMonster8 = MiniMonster("m", "Slime", 50, 1, 13, 13)

# objek big monster
bigMonster1 = Monster("M", "Wrath 1", 100, 10, 11, 3)
bigMonster2 = Monster("M", "Wrath 2", 100, 10, 11, 7)

# list objek big monster
bigMonsterList = [bigMonster1, bigMonster2]
# list objek mini monster
miniMonsterList = [miniMonster1, miniMonster2, miniMonster3, miniMonster4,
               miniMonster5, miniMonster6, miniMonster7, miniMonster8]

# Fungsi untuk mencetak dungeon
def print_dungeon():
    print()
    for row in range(len(dungeon)):
        for col in range(len(dungeon[row])):
            if row == hunter.currentCoordinateRow and col == hunter.currentCoordinateCol:
                dungeon[row][col] = hunter.id

            # looping mini monster list
            for m in miniMonsterList:
                if (row == m.coordinatRow and col == m.coordinatCol) and m.status == "ALIVE":
                    dungeon[row][col] = m.id

            for M in bigMonsterList:
                if (row == M.coordinatRow and col == M.coordinatCol) and M.status == "ALIVE":
                    dungeon[row][col] = M.id

            if (row == boss.coordinatRow and col == boss.coordinatCol) and boss.status == "ALIVE":
                dungeon[row][col] = boss.id
            print("", dungeon[row][col], end="")
        print()
    print()

# fungsi untuk mencetak status hunter
def displayHunterStats():
    print(f"\n==================== Informasi Hunter ====================\nMonster: {hunter.name}\nJenis: {hunter.id}\nHP: {hunter.hp}\nPower: {hunter.power}\nArmor: {hunter.armor}")

# fungsi untuk mencetak status enemy
def displayEnemyStats(enemy):
    print(f"\n==================== Informasi Musuh ====================\nMonster: {enemy.name}\nJenis: {enemy.id}\nHP: {enemy.hp}\nPower: {enemy.power}\nArmor: {enemy.armor if enemy.id == 'B' else 0}")

# fungsi ketika hunter dan enemy bertumbuk / berantem
def fight(hunter, enemy):
    print("\nKamu menemukan Monster!")
    global hunterTurn
    hunterTurn = True

    while True:
        if enemy.hp <= 0:
            if enemy.id == "B":
                enemy.hp = 0
                enemy.status = "DEAD"
                displayHunterStats()
                displayEnemyStats(enemy)
                victory()
            else:
                print("\nMonster berhasil dikalahkan!")
                enemy.hp = 0
                enemy.status = "DEAD"
                displayHunterStats()
                displayEnemyStats(enemy)
            break

        if hunter.hp <= 0:
            displayHunterStats()
            displayEnemyStats(enemy)
            gameOver()
            break

        displayHunterStats()
        displayEnemyStats(enemy)

        if hunterTurn:
            print("\nGILIRAN KAMU")
            print("1. Basic Attack\n2. Skill 1\n3. Skill 2\n4. Ulti")
            inputAttack = input("Masukkan serangan: ")

            if inputAttack == "1":
                hunter.menyerang(enemy)
            elif inputAttack == "2":
                print("\n>>> Sementara belum ada fitur skill!")
            elif inputAttack == "3":
                print("\n>>> Sementara belum ada fitur skill!")    
            elif inputAttack == "4":
                print("\n>>> Sementara belum ada fitur skill!")
            else:
                print("\n>>> Input Salah!")
                continue
            hunterTurn = False
        else:
            print("\nGILIRAN MONSTER")
            print("\nMONSTER MENYERANG...")
            enemy.menyerang(hunter)
            hunterTurn = True

# fungsi untuk mendapatkan enemy
def getEnemy(currentRow, currentCol):
    for M in bigMonsterList:
        if (currentRow == M.coordinatRow and currentCol == M.coordinatCol) and M.status == "ALIVE":
            return M
        
    for m in miniMonsterList:
        if (currentRow == m.coordinatRow and currentCol == m.coordinatCol) and m.status == "ALIVE":
            return m

    if (currentRow == boss.coordinatRow and currentCol == boss.coordinatCol) and boss.status == "ALIVE":
        return boss
    
    return {}

# fungsi ketika player berhasil mengalahkan boss di dungeon
def victory():
    global playing
    print("\nBOSS berhasil dikalahkan!")
    print("Keluar dungeon....")
    playing = False

# fungsi ketika player meninggal :v
def gameOver():
    global playing
    print("\nKamu meninggal wkwk :D")
    print("Game Over")
    hunter.status = "DEAD"
    hunter.hp = 0
    playing = False

playing = True
def play():
    global currentEnemy
    currentEnemy = {}
    
    print("\nSelamat datang, Hunter! Temukan dan kalahkan monster yang ada di dalam dungeon.")

    while playing:
        print_dungeon()
        move = input("Masukkan arah pergerakanmu (W/A/S/D): ").lower()

        # Mengubah posisi berdasarkan input pergerakan
        if move == "w" and dungeon[hunter.currentCoordinateRow - 1][hunter.currentCoordinateCol] != '#':
            hunter.moveToTop()
        elif move == "s" and dungeon[hunter.currentCoordinateRow + 1][hunter.currentCoordinateCol] != '#':
            hunter.moveToBottom()
        elif move == "a" and dungeon[hunter.currentCoordinateRow][hunter.currentCoordinateCol - 1] != '#':
            hunter.moveToLeft()
        elif move == "d" and dungeon[hunter.currentCoordinateRow][hunter.currentCoordinateCol + 1] != '#':
            hunter.moveToRight()

        # Memeriksa apakah pemain menemukan harta karun
        if dungeon[hunter.currentCoordinateRow][hunter.currentCoordinateCol] == "X":
            print("Kamu Menemukan Harta karun!")
            print("Harta karun dibuka: ")
            print("Kamu mendapatkan buff!")
            print("Power+++")
            print("Power+++")
            print("Power+++")
            print("HP+++")
            print("HP+++")
            print("HP+++")
            print("HP+++")
            hunter.hp += 1000
            hunter.power += 500
            displayHunterStats()
        if dungeon[hunter.currentCoordinateRow][hunter.currentCoordinateCol] == "+":
            print("Healing...")
            print("HP+++")
            print("HP+++")
            print("HP+++")
            print("HP+++")
            hunter.hp += 500
            displayHunterStats()

        # Memeriksa apakah pemain menemukan monster
        currentEnemy = getEnemy(hunter.currentCoordinateRow, hunter.currentCoordinateCol)

        if currentEnemy != {}:
            fight(hunter, currentEnemy)
play()
