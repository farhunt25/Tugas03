class GameEntry:
    jml_pemain = 0

    def __init__(self, nama, score, waktuq):
        self.nama = nama
        self.score = score
        self.waktu = waktuq

        GameEntry.jml_pemain += 1

    def setName(self, nama):
        self.nama = nama

    def getName(self):
        return self.nama

    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score

    def setTime(self, waktuq):
        self.time = waktuq

    def getTime(self):
        return self.waktu

    def getTotal():
        return GameEntry.jml_pemain


class ScoreBoard:

    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.board = [None] * self.kapasitas
        self.n = 0

    def getCapacity(self):
        return self.kapasitas

    def sumEntries(self):
        return self.n

    def addItem(self, entry):
        score = entry.getScore()

        kondisi = len(self.board) > self.n or score > self.board[self.kapasitas - 1].getScore()
        

        if kondisi:
            if self.n < self.kapasitas:
                self.n += 1

            j = self.n - 1

            while j > 0 and self.board[j - 1].getScore() < score:
                self.board[j] = self.board[j - 1]
                j -= 1
            self.board[j] = entry
            print(f"Data {score} ditambahkan!")

    def listEntries(self):
        for i in range(0, self.n):
            print(i + 1, ":", getattr(self.board[i], 'nama'), getattr(self.board[i], 'score'))


board = ScoreBoard(10)

active = True

while active:
    print("")
    start = input("Opsi: \n 1 = Tambah Data Baru \n 2 = Lihat List ScoreBoard \n 3 = Keluar \n")
    print("")
    if start == '2':
        board.listEntries()
    elif start == '1':
        name = input("Masukan nama pemain : ")
        skor = int(input("Masukan score : "))
        waktu = int(input("Masukan waktu : "))

        in_score = GameEntry(name, skor, waktu)
        set_board = board.addItem(in_score)

        print(f"Entri telah ditambahkan: {in_score.getName()} {in_score.getScore()} {in_score.getTime()}")
    else:
        break
