import stdlib

window.blocks = []
window.speedX = 2.5
window.speedY = 2.5

def setUpGame():
    window.blocks = []
    createBlocksA()
    window.speedX = 2.5
    window.speedY = 2.5
    window.paddle.x = 150
    window.paddle.y = 430
    window.ball.x = 50
    window.ball.y = 300

def createBlocksA():
    blockWidth = 40
    blockHeight = 10
    gutterX = 25
    gutterY = 10
    left = 50
    right = left + 5 * (gutterX + blockWidth)
    top = 50
    bottom = top + 4 * (gutterY + blockHeight)
    for i in range(left, right, gutterX + blockWidth):
        for j in range(top, bottom, gutterY + blockHeight):
            block = createRectangle(i, j, blockWidth, blockHeight)
            window.blocks.append(block)

def createBlocksB():
    pass

def renderBlocks():
    for block in window.blocks:
        displayRectangle(block)

def detectWorldCollision():
    if window.ball.x + 10 > 400 or window.ball.x < 0:
        window.speedX = -window.speedX

    if window.ball.y + 10 > 450 or window.ball.y < 0:
        window.speedY = -window.speedY

def detectPaddleCollision():
    if window.ball.y + 10 > window.paddle.y and window.paddle.x - 10 < window.ball.x < window.paddle.x + 100:
        window.speedY = -window.speedY

def detectBlockCollision():
    ball = window.ball
    for i in range(len(window.blocks)):
        block = window.blocks[i]

        if ball.y + 10 > block.y and ball.y < block.y + 10 and block.x - 10 < ball.x < block.x + 40:
            window.speedY = -window.speedY
            window.blocks.pop(i)
            break

        if ball.x + 10 > block.x and ball.x < block.x + 40 and block.y - 10 < ball.y < block.y + 10:
            window.speedX = -window.speedX
            window.blocks.pop(i)
            break

def detectGameOver():
    if len(window.blocks) <= 0:
        setUpGame()

    if window.ball.y > window.paddle.y + 5:
        setUpGame()

def movePaddle():
    if window.leftButton.isDown and window.paddle.x >= 0:
        window.paddle.x = window.paddle.x - 5

    if window.rightButton.isDown and window.paddle.x + 100 <= 400:
        window.paddle.x = window.paddle.x + 5

def moveBall():
    window.ball.x = window.ball.x + window.speedX
    window.ball.y = window.ball.y + window.speedY

def preload():
    pass

def create():
    game.stage.backgroundColor = '#0d7dc8'
    window.paddle = createRectangle(150, 430, 100, 10)
    window.ball = createRectangle(50, 300, 10, 10)
    createBlocksA()

    window.leftButton = game.input.keyboard.addKey(Phaser.Keyboard.LEFT)
    window.rightButton = game.input.keyboard.addKey(Phaser.Keyboard.RIGHT)

def update():
    movePaddle()

    detectWorldCollision()
    detectPaddleCollision()
    detectBlockCollision()

    detectGameOver()
    moveBall()

def render():
    displayRectangle(window.paddle)
    displayRectangle(window.ball)
    renderBlocks()


window.gameState = {
  "preload": preload,
  "create": create,
  "update": update,
  "render": render
}
