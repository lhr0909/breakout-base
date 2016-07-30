import stdlib

game = window.game

def preload():
    game.load.image('paddle', 'assets/paddle.png')
    game.load.image('block', 'assets/block.png')
    game.load.image('ball', 'assets/ball.png')

def create():
    game.stage.backgroundColor = '#0d7dc8'
    game.physics.startSystem(Phaser.Physics.ARCADE)
    game.world.enableBody = True

    window.paddle = game.add.sprite(150, 430, 'paddle') # createRectangle(150, 430, 100, 10)
    window.paddle.body.immovable = True
    window.leftButton = game.input.keyboard.addKey(Phaser.Keyboard.LEFT)
    window.rightButton = game.input.keyboard.addKey(Phaser.Keyboard.RIGHT)

    window.ball = game.add.sprite(50, 300, 'ball')
    window.ball.body.velocity.x = 200
    window.ball.body.velocity.y = 200

    window.ball.body.bounce.setTo(1)
    window.ball.body.collideWorldBounds = True

    window.blocks = game.add.group()

    blockWidth = 40
    blockHeight = 10
    gutterX = 25
    gutterY = 10
    left = 50
    top = 50
    rows = 4
    cols = 5

    while rows > 0:
        while cols > 0:
            block = game.add.sprite(left, top, 'block')
            block.body.immovable = True
            blocks.add(block)

            left = left + blockWidth + gutterX
            cols = cols - 1

        top = top + blockHeight + gutterY
        rows = rows - 1
        left = 50
        cols = 5

def update():
    if window.leftButton.isDown:
        paddle.body.position.x = paddle.body.position.x - 10
    elif window.rightButton.isDown:
        paddle.body.position.x = paddle.body.position.x + 10

    game.physics.arcade.collide(window.paddle, window.ball)
    game.physics.arcade.collide(window.ball, window.blocks, hit, None, self)

    if window.ball.y > window.paddle.y:
        game.state.start('main')

def hit(ball, block):
    block.kill()

# don't have to write anything in render()
def render():
    pass


window.gameState = {
  "preload": preload,
  "create": create,
  "update": update,
  "render": render
}
