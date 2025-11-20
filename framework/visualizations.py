#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Модуль для создания графических иллюстраций математических задач
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import io
import base64


def figure_to_base64(fig):
    """Конвертирует matplotlib figure в base64-encoded SVG"""
    buf = io.BytesIO()
    fig.savefig(buf, format='svg', bbox_inches='tight', transparent=True)
    buf.seek(0)
    svg_data = buf.getvalue().decode('utf-8')
    buf.close()
    plt.close(fig)
    return svg_data


def plot_vectors_2d_3d(vectors, labels=None, title="Векторы"):
    """
    Рисует векторы в 3D пространстве
    
    Args:
        vectors: список векторов [(x1,y1,z1), (x2,y2,z2), ...]
        labels: список меток для векторов
        title: заголовок графика
    """
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#f7b731', '#5f27cd']
    
    for idx, vec in enumerate(vectors):
        if len(vec) == 2:
            vec = (vec[0], vec[1], 0)
        
        ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], 
                 color=colors[idx % len(colors)], 
                 arrow_length_ratio=0.15, 
                 linewidth=2.5)
        
        label = labels[idx] if labels and idx < len(labels) else f'v{idx+1}'
        ax.text(vec[0], vec[1], vec[2], label, 
               color='white', fontsize=12, weight='bold')
    
    max_range = max([max(abs(v[0]), abs(v[1]), abs(v[2] if len(v) > 2 else 0)) 
                     for v in vectors]) * 1.2
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])
    
    ax.set_xlabel('X', color='white', fontsize=10)
    ax.set_ylabel('Y', color='white', fontsize=10)
    ax.set_zlabel('Z', color='white', fontsize=10)
    ax.set_title(title, color='white', fontsize=12, weight='bold')
    
    ax.grid(True, alpha=0.3)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    return figure_to_base64(fig)


def plot_parallelogram(vec_a, vec_b, title="Параллелограмм"):
    """Рисует параллелограмм на векторах"""
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Вершины параллелограмма
    O = np.array([0, 0, 0])
    A = np.array(vec_a)
    B = np.array(vec_b)
    C = A + B
    
    # Стороны параллелограмма
    vertices = [O, A, C, B, O]
    xs, ys, zs = zip(*vertices)
    ax.plot(xs, ys, zs, 'c-', linewidth=2)
    
    # Диагонали
    ax.plot([O[0], C[0]], [O[1], C[1]], [O[2], C[2]], 'r--', linewidth=2, label='d₁')
    ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'y--', linewidth=2, label='d₂')
    
    # Векторы
    ax.quiver(0, 0, 0, A[0], A[1], A[2], color='#ff6b6b', arrow_length_ratio=0.15, linewidth=2)
    ax.quiver(0, 0, 0, B[0], B[1], B[2], color='#4ecdc4', arrow_length_ratio=0.15, linewidth=2)
    
    # Метки
    ax.text(A[0], A[1], A[2], 'A', color='white', fontsize=12, weight='bold')
    ax.text(B[0], B[1], B[2], 'B', color='white', fontsize=12, weight='bold')
    ax.text(C[0], C[1], C[2], 'C', color='white', fontsize=12, weight='bold')
    
    ax.set_xlabel('X', color='white')
    ax.set_ylabel('Y', color='white')
    ax.set_zlabel('Z', color='white')
    ax.set_title(title, color='white', fontsize=12, weight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    return figure_to_base64(fig)


def plot_pyramid(vertices, title="Пирамида"):
    """
    Рисует пирамиду
    
    Args:
        vertices: список вершин [(x,y,z), ...]
        title: заголовок
    """
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    A, B, C, D = [np.array(v) for v in vertices]
    
    # Основание ABC
    base = [A, B, C, A]
    xs, ys, zs = zip(*base)
    ax.plot(xs, ys, zs, 'c-', linewidth=2)
    
    # Ребра к вершине D
    for point in [A, B, C]:
        ax.plot([point[0], D[0]], [point[1], D[1]], [point[2], D[2]], 
               'y-', linewidth=2)
    
    # Вершины
    labels = ['A', 'B', 'C', 'D']
    for vertex, label in zip(vertices, labels):
        ax.scatter(*vertex, color='red', s=100)
        ax.text(vertex[0], vertex[1], vertex[2], f'  {label}', 
               color='white', fontsize=12, weight='bold')
    
    ax.set_xlabel('X', color='white')
    ax.set_ylabel('Y', color='white')
    ax.set_zlabel('Z', color='white')
    ax.set_title(title, color='white', fontsize=12, weight='bold')
    ax.grid(True, alpha=0.3)
    
    return figure_to_base64(fig)


def plot_line_and_point(line_point, line_direction, point, projection=None, title="Прямая и точка"):
    """
    Рисует прямую и точку с проекцией
    
    Args:
        line_point: точка на прямой
        line_direction: направляющий вектор
        point: точка для проекции
        projection: координаты проекции (опционально)
        title: заголовок
    """
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Прямая
    t = np.linspace(-5, 5, 100)
    line_point = np.array(line_point)
    line_direction = np.array(line_direction)
    line = line_point[:, np.newaxis] + line_direction[:, np.newaxis] * t
    
    ax.plot(line[0], line[1], line[2], 'c-', linewidth=2, label='Прямая')
    
    # Точка
    point = np.array(point)
    ax.scatter(*point, color='red', s=100, label='M')
    ax.text(point[0], point[1], point[2], '  M', color='white', fontsize=12, weight='bold')
    
    # Проекция
    if projection is not None:
        projection = np.array(projection)
        ax.scatter(*projection, color='yellow', s=100, label='P')
        ax.text(projection[0], projection[1], projection[2], '  P', 
               color='white', fontsize=12, weight='bold')
        ax.plot([point[0], projection[0]], [point[1], projection[1]], [point[2], projection[2]], 
               'r--', linewidth=2, label='MP')
    
    ax.set_xlabel('X', color='white')
    ax.set_ylabel('Y', color='white')
    ax.set_zlabel('Z', color='white')
    ax.set_title(title, color='white', fontsize=12, weight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    return figure_to_base64(fig)


def plot_plane(plane_equation, point=None, intercepts=None, title="Плоскость"):
    """
    Рисует плоскость
    
    Args:
        plane_equation: коэффициенты (a, b, c, d) для ax + by + cz = d
        point: точка на плоскости (опционально)
        intercepts: отрезки на осях (опционально)
        title: заголовок
    """
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    a, b, c, d = plane_equation
    
    # Создаем сетку для плоскости
    if abs(c) > 0.01:
        x = np.linspace(-10, 10, 20)
        y = np.linspace(-10, 10, 20)
        X, Y = np.meshgrid(x, y)
        Z = (d - a*X - b*Y) / c
    elif abs(b) > 0.01:
        x = np.linspace(-10, 10, 20)
        z = np.linspace(-10, 10, 20)
        X, Z = np.meshgrid(x, z)
        Y = (d - a*X - c*Z) / b
    else:
        y = np.linspace(-10, 10, 20)
        z = np.linspace(-10, 10, 20)
        Y, Z = np.meshgrid(y, z)
        X = (d - b*Y - c*Z) / a
    
    ax.plot_surface(X, Y, Z, alpha=0.3, color='cyan')
    
    # Точка
    if point is not None:
        point = np.array(point)
        ax.scatter(*point, color='red', s=100)
        ax.text(point[0], point[1], point[2], '  P', 
               color='white', fontsize=12, weight='bold')
    
    # Отрезки на осях
    if intercepts is not None:
        a_int, b_int, c_int = intercepts
        ax.scatter([a_int, 0, 0], [0, a_int, 0], [0, 0, a_int], 
                  color='yellow', s=100)
    
    ax.set_xlabel('X', color='white')
    ax.set_ylabel('Y', color='white')
    ax.set_zlabel('Z', color='white')
    ax.set_title(title, color='white', fontsize=12, weight='bold')
    ax.grid(True, alpha=0.3)
    
    return figure_to_base64(fig)


def plot_two_lines(line1_point, line1_dir, line2_point, line2_dir, title="Две прямые"):
    """
    Рисует две прямые в пространстве
    
    Args:
        line1_point: точка на первой прямой
        line1_dir: направляющий вектор первой прямой
        line2_point: точка на второй прямой
        line2_dir: направляющий вектор второй прямой
        title: заголовок
    """
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    # Первая прямая
    t = np.linspace(-5, 5, 100)
    line1_point = np.array(line1_point)
    line1_dir = np.array(line1_dir)
    line1 = line1_point[:, np.newaxis] + line1_dir[:, np.newaxis] * t
    ax.plot(line1[0], line1[1], line1[2], 'c-', linewidth=2, label='L₁')
    
    # Вторая прямая
    line2_point = np.array(line2_point)
    line2_dir = np.array(line2_dir)
    line2 = line2_point[:, np.newaxis] + line2_dir[:, np.newaxis] * t
    ax.plot(line2[0], line2[1], line2[2], 'y-', linewidth=2, label='L₂')
    
    ax.set_xlabel('X', color='white')
    ax.set_ylabel('Y', color='white')
    ax.set_zlabel('Z', color='white')
    ax.set_title(title, color='white', fontsize=12, weight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    return figure_to_base64(fig)


def plot_matrix_heatmap(matrix, title="Матрица"):
    """
    Рисует матрицу как тепловую карту
    
    Args:
        matrix: numpy array или список списков
        title: заголовок
    """
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(6, 6))
    
    matrix = np.array(matrix)
    im = ax.imshow(matrix, cmap='coolwarm', aspect='auto')
    
    # Показываем значения
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            text = ax.text(j, i, f'{matrix[i, j]:.1f}' if isinstance(matrix[i, j], float) else str(matrix[i, j]),
                          ha="center", va="center", color="white", fontsize=12, weight='bold')
    
    ax.set_title(title, color='white', fontsize=12, weight='bold')
    plt.colorbar(im, ax=ax)
    
    return figure_to_base64(fig)

