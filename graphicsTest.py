from graphics.GraphicsHandler import GraphicsHandler

handler = GraphicsHandler()
config = {
    "callback" : handler.changeScreen
}
handler.changeScreen("HOME", config)