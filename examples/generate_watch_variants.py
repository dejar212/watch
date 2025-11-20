#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генератор вариантов дизайна для часов (Watch Format)
Генерирует 4 варианта (Dark, Light, Terminal, Blueprint) для сравнения.
"""

import sys
import os

# Добавляем путь к фреймворку
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../framework'))

from generator import CompactFramework, create_task, TaskCategory

def create_universal_tasks():
    """Создает набор задач из разных областей для тестирования универсальности"""
    tasks = []

    # 1. Математика (Short)
    tasks.append(create_task(1, 'short', r'''
        <strong>Diff. Eq:</strong> \( y' + 2y = 0 \)
        <br>
        Char. eq: \( \lambda + 2 = 0 \Rightarrow \lambda = -2 \)
        <br>
        \( y = Ce^{-2x} \)
        <div class="answer-box">Ans: \( y = Ce^{-2x} \)</div>
    '''))

    # 2. Программирование (Medium)
    tasks.append(create_task(2, 'medium', r'''
        <strong>Reverse Linked List</strong>
        <pre><code class="language-python">def reverse(head):
    prev = None
    curr = head
    while curr:
        next_n = curr.next
        curr.next = prev
        prev = curr
        curr = next_n
    return prev</code></pre>
        <div class="answer-box">Time: O(n), Space: O(1)</div>
    '''))

    # 3. Физика (Medium/Long)
    tasks.append(create_task(3, 'medium', r'''
        <strong>Kinematics</strong>
        <br>
        \( v_0 = 0, a = 2 m/s^2, t = 5s \)
        <br>
        Find distance \( d \):
        \[ d = v_0t + \frac{1}{2}at^2 \]
        \[ d = 0 + 0.5 \cdot 2 \cdot 25 = 25 \]
        <div class="answer-box">d = 25 m</div>
    '''))
    
    return tasks

def generate_variant(theme_name, filename):
    """Генерирует HTML для конкретной темы"""
    framework = CompactFramework(
        title=f"Watch: {theme_name}",
        author="AI Assistant",
        date="2025"
    )
    
    tasks = create_universal_tasks()
    for task in tasks:
        framework.add_task(task)
        
    output_path = os.path.join(os.path.dirname(__file__), filename)
    
    # Используем новый параметр watch_mode и theme
    framework.generate_standalone(output_path, watch_mode=True, theme=theme_name)

if __name__ == "__main__":
    print("Generating Watch Design Variants...")
    
    themes = [
        ("dark", "watch_variant_dark.html"),
        ("light", "watch_variant_light.html"),
        ("terminal", "watch_variant_terminal.html"),
        ("blueprint", "watch_variant_blueprint.html")
    ]
    
    for theme, filename in themes:
        generate_variant(theme, filename)
        
    print("\nDone! Open the generated HTML files in 'examples/' to compare designs.")

