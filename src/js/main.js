function createRectangle(startX, startY, width, height) {
  return new Phaser.Rectangle(startX, startY, width, height);
}

function displayRectangle(rect) {
  game.debug.geom(rect, '#ffffff');
}

var game = new Phaser.Game(400, 450);
game.state.add('main', window.gameState);
game.state.start('main');
