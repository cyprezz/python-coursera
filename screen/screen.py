#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import random
import math

import logging
import sys

SCREEN_DIM = (800, 600)

log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)

# =======================================================================================
# Класс для работы с векторами
# =======================================================================================
class Vec2d:

    def sub(self, x, y):
        """"возвращает разность двух векторов"""
        return x[0] - y[0], x[1] - y[1]

    def add(self, x, y):
        """возвращает сумму двух векторов"""
        return x[0] + y[0], x[1] + y[1]

    def len(self, x):
        """возвращает длину вектора"""
        return math.sqrt(x[0] * x[0] + x[1] * x[1])

    def mul(self, v, k):
        """возвращает произведение вектора на число"""
        return v[0] * k, v[1] * k

    def vec(self, x, y):
        """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
        координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
        return self.sub(y, x)

    def int_pair(self, pos):
        return pos


class Polyline:
    def __init__(self, point: Vec2d, points):
        self.point = point
        self.points = points

    # =======================================================================================
    # Функции отрисовки
    # =======================================================================================
    def draw_points(self, points, style="points", width=3, color=(255, 255, 255)):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color,
                                 (int(points[p_n][0]), int(points[p_n][1])),
                                 (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0]), int(p[1])), width)

    # =======================================================================================
    # Функции, отвечающие за расчет сглаживания ломаной
    # =======================================================================================
    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return self.point.add(self.point.mul(points[deg], alpha), self.point.mul(self.get_point(points, alpha, deg - 1), 1 - alpha))

    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def set_points(self, speeds):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.point.add(self.points[p], speeds[p])
            if self.points[p][0] > SCREEN_DIM[0] or self.points[p][0] < 0:
                speeds[p] = (- speeds[p][0], speeds[p][1])
            if self.points[p][1] > SCREEN_DIM[1] or self.points[p][1] < 0:
                speeds[p] = (speeds[p][0], -speeds[p][1])


class Knot(Polyline):

    def get_knot(self, steps):
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append(self.point.mul(self.point.add(self.points[i], self.points[i + 1]), 0.5))
            ptn.append(self.points[i + 1])
            ptn.append(self.point.mul(self.point.add(self.points[i + 1], self.points[i + 2]), 0.5))

            res.extend(self.get_points(ptn, steps))
        return res


def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = list()
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])
    data.append([str(len(knots)), "Current knots"])

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (800, 0), (800, 600), (0, 600)], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")
    point = Vec2d()

    steps = 35
    working = True
    knots = []
    points = []
    vectors = []
    speeds = []
    speeds2 = []
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)
    knot = Knot(point, points)
    knots.append(knot)
    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0
                if event.key == pygame.K_k:
                    knots.append(Knot(point, points))

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(event.pos)

                vectors.append({'len': point.len, 'pos': point.int_pair(event.pos)})
                log.info(points)

                speeds.append((random.random() * 2, random.random() * 2))
                speeds2.append((random.random() * 3, random.random() * 3))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)



        for knotObj in knots:
            knotObj.draw_points(points)
            knotObj.draw_points(knot.get_knot(steps), "line", 5, color)
            if not pause:
                knotObj.set_points(speeds)

        # knot2 = Knot(point, points)
        # knot2.draw_points(points)
        # knot2.draw_points(knot2.get_knot(steps), "line", 1, color)

        # if not pause:
        #
        #     knot.set_points(speeds)
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
