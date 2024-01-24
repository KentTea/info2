import pyxel

class Ball:
        Ball.speed=3


class Pad:
            return False


class App:
    score = 0
    miss = 0
    gameover = False

    def __init__(self):
        pyxel.init(400,200)
        pyxel.sound(0).set(notes='C0', tones='T', volumes='7', effects='N', speed=30)
        pyxel.sound(1).set(notes='B3G3', tones='P', volumes='3', effects='N', speed=10)
        App.p1 = Pad(15)
        App.p2 = Pad(385)
        App.b = [Ball(),Ball()]
        pyxel.run(self.update, self.draw)

    def update(self):
        for b in App.b:
            b.x += (b.vx * Ball.speed)
            b.y += (b.vy * Ball.speed)

            if b.x < 0:
                pyxel.play(0, 0)
                App.p1.miss += 1
                App.p2.score += 1
                b.restart()
            if b.x > 400:
                pyxel.play(0, 0)
                App.p2.miss += 1
                App.p1.score += 1
                b.restart()
            
            b.move()
            if self.p1.catch1(b) == True:
                b.vx*=-1
                pyxel.play(0, 1)
                Ball.speed += 0.1
            if self.p2.catch2(b) == True:
                b.vx*=-1
                pyxel.play(0, 1)
                Ball.speed += 0.1
            if pyxel.btn(pyxel.KEY_W):
                App.p1.y -= 8
            if pyxel.btn(pyxel.KEY_S):
                App.p1.y += 8
            if pyxel.btn(pyxel.KEY_UP):
                App.p2.y -= 8
            if pyxel.btn(pyxel.KEY_DOWN):
                App.p2.y += 8

            if App.p1.miss >= 3:
                App.gameover = True
            if App.p2.miss >= 3:
                App.gameover = True         

    def draw(self):
        if App.gameover:
            pyxel.text(80, 100, "GAME OVER", 0)
            if App.p1.miss >= 3:
                pyxel.text(80, 130, "Player 2 Wins", 0)
            if App.p2.miss >= 3:
                pyxel.text(80, 130, "Player 1 Wins", 0)

        else:
            pyxel.cls(7)
            pyxel.text(10, 10, "score : " + str(App.p1.score), 0)
            pyxel.text(350, 10, "score : " + str(App.p2.score), 0)
            pyxel.text(10, 20, "miss : " + str(App.p1.miss), 0)
            pyxel.text(350, 20, "miss : " + str(App.p2.miss), 0)
            for b in App.b:
                pyxel.circ(b.x, b.y, 10, 6)
            pyxel.rect(self.p1.x, self.p1.y, 5, 40, 14)
            pyxel.rect(self.p2.x, self.p2.y, 5, 40, 14)

App()
