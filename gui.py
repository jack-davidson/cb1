# Optional GUI
import pygame
import OpenGL.GL as gl

from imgui.integrations.pygame import PygameRenderer
import imgui

pygame.init()
size = 800, 600

pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)

while True:
    imgui.create_context()
    imgui.get_io().display_size = 100, 100
    imgui.get_io().fonts.get_tex_data_as_rgba32()

    imgui.new_frame()
    imgui.begin("Your first window!", True)
    imgui.text("Hello world!")
    imgui.end()

    imgui.render()
    imgui.end_frame()