#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генератор компактного HTML-представления математических задач
"""

import json
import os
from typing import List, Optional, Dict, Any
from enum import Enum


class TaskCategory(Enum):
    """Категории задач по размеру"""
    SHORT = "short"      # Короткая задача - 1/2 колонки
    MEDIUM = "medium"    # Средняя задача - 1 колонка
    LONG = "long"        # Длинная задача - 2 колонки


class Task:
    """Класс представления задачи"""
    
    def __init__(self, 
                 number: int,
                 category: TaskCategory,
                 solution: str,
                 visualization_svg: Optional[str] = None,
                 custom_class: str = ""):
        """
        Инициализация задачи
        
        Args:
            number: номер задачи
            category: категория размера (SHORT/MEDIUM/LONG)
            solution: текст решения с LaTeX формулами
            visualization_svg: SVG-код визуализации (опционально)
            custom_class: дополнительные CSS классы
        """
        self.number = number
        self.category = category
        self.solution = solution
        self.visualization_svg = visualization_svg
        self.custom_class = custom_class
    
    def to_html(self) -> str:
        """Конвертирует задачу в HTML"""
        category_class = f"task-{self.category.value}"
        all_classes = f"task {category_class} {self.custom_class}".strip()
        
        visualization_html = ""
        if self.visualization_svg:
            visualization_html = f'''
            <div class="task-visualization">
                {self.visualization_svg}
            </div>
            '''
        
        html = f'''
        <div class="{all_classes}">
            <div class="task-header">
                <div class="task-number">Задача {self.number}</div>
                <div class="task-category">{self.category.value}</div>
            </div>
            <div class="task-content">
                <div class="task-solution">
                    {self.solution}
                </div>
                {visualization_html}
            </div>
        </div>
        '''
        return html


class CompactFramework:
    """Фреймворк для генерации компактного HTML документа"""
    
    def __init__(self, 
                 title: str = "Математическая работа",
                 author: str = "Студент",
                 date: str = "",
                 config_path: Optional[str] = None):
        """
        Инициализация фреймворка
        
        Args:
            title: заголовок документа
            author: автор
            date: дата
            config_path: путь к config.json
        """
        self.title = title
        self.author = author
        self.date = date
        self.tasks: List[Task] = []
        self.custom_styles = ""
        
        # Загружаем конфигурацию
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                self.config = json.load(f)
        else:
            self.config = self._default_config()
    
    def _default_config(self) -> Dict[str, Any]:
        """Конфигурация по умолчанию"""
        return {
            "page_settings": {
                "background": "#000000",
                "text_color": "#ffffff",
                "square_size": "15cm"
            },
            "task_categories": {
                "short": {"width": "0.5", "height": "1"},
                "medium": {"width": "1", "height": "1"},
                "long": {"width": "2", "height": "1"}
            }
        }
    
    def add_task(self, task: Task):
        """Добавляет задачу в документ"""
        self.tasks.append(task)
    
    def add_custom_styles(self, styles: str):
        """Добавляет пользовательские стили"""
        self.custom_styles += styles + "\n"
    
    def _optimize_layout(self) -> List[Task]:
        """
        Оптимизирует расположение задач для компактности
        Группирует короткие задачи вместе
        """
        optimized = []
        short_tasks = [t for t in self.tasks if t.category == TaskCategory.SHORT]
        medium_tasks = [t for t in self.tasks if t.category == TaskCategory.MEDIUM]
        long_tasks = [t for t in self.tasks if t.category == TaskCategory.LONG]
        
        # Сначала добавляем короткие задачи (они будут парами)
        optimized.extend(short_tasks)
        
        # Затем средние
        optimized.extend(medium_tasks)
        
        # В конце длинные
        optimized.extend(long_tasks)
        
        return optimized
    
    def generate(self, output_path: str, template_path: Optional[str] = None):
        """
        Генерирует HTML файл
        
        Args:
            output_path: путь для сохранения HTML
            template_path: путь к шаблону (опционально)
        """
        # Определяем путь к шаблону
        if template_path is None:
            template_path = os.path.join(
                os.path.dirname(__file__), 
                'template.html'
            )
        
        # Читаем шаблон
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
        
        # Оптимизируем расположение задач
        optimized_tasks = self._optimize_layout()
        
        # Генерируем HTML для всех задач
        tasks_html = "\n".join(task.to_html() for task in optimized_tasks)
        
        # Заполняем шаблон
        if self.custom_styles:
             html = template.replace('{{CUSTOM_STYLES}}', self.custom_styles)
        else:
             html = template.replace('{{CUSTOM_STYLES}}', '')

        html = html.replace('{{TITLE}}', self.title)
        html = html.replace('{{AUTHOR}}', self.author)
        html = html.replace('{{DATE}}', self.date)
        html = html.replace('{{TASKS}}', tasks_html)
        
        # Сохраняем файл
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✓ HTML документ сгенерирован: {output_path}")
        print(f"  Всего задач: {len(self.tasks)}")
        print(f"  - Коротких: {len([t for t in self.tasks if t.category == TaskCategory.SHORT])}")
        print(f"  - Средних: {len([t for t in self.tasks if t.category == TaskCategory.MEDIUM])}")
        print(f"  - Длинных: {len([t for t in self.tasks if t.category == TaskCategory.LONG])}")
    
    def generate_density_variants(self, output_dir: str, variant_class: str):
        """
        Generates separate HTML files for density variants.
        Handles grouping and splitting.
        """
        import os
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # CSS Path
        css_path = os.path.join(os.path.dirname(__file__), 'watch_styles.css')
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
            
        base_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Watch Task</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script>
        // AUTO-FIT LOGIC
        window.addEventListener('load', function() {{
            const container = document.querySelector('.watch-container');
            if (!container) return;

            // 1. Adjust Font Size to Fill
            // Only for adaptive layout or generally to prevent overflow
            function autoFit() {{
                let fontSize = 100; // Start percentage
                const minSize = 40;
                
                // Check for overflow
                while (container.scrollHeight > container.clientHeight && fontSize > minSize) {{
                    fontSize -= 2;
                    document.body.style.fontSize = fontSize + '%';
                }}
                
                // If too much space (only for adaptive), grow? 
                // For now, just ensure it fits.
            }}
            
            // Run after MathJax
            if (window.MathJax) {{
                MathJax.startup.promise.then(() => {{
                    setTimeout(autoFit, 500); // Delay for rendering
                }});
            }} else {{
                autoFit();
            }}
        }});
    </script>
    <style>
        {css_content}
    </style>
</head>
<body class="{variant_class}">
    <div class="watch-container">
        {{{{CONTENT}}}}
    </div>
</body>
</html>"""

        # 1. Group Short Tasks (Tasks 1 & 2) - VERTICAL SPLIT / ZIGZAG
        short_tasks = [t for t in self.tasks if t.category == TaskCategory.SHORT]
        if len(short_tasks) >= 2:
            t1, t2 = short_tasks[0], short_tasks[1]
            
            # Choose layout based on variant_class
            if 'zigzag' in variant_class:
                content = f"""
                <div class="layout-zigzag">
                    <div class="zigzag-separator">
                         <svg width="100%" height="100%" viewBox="0 0 100 100" preserveAspectRatio="none">
                             <polyline points="0,0 100,0 100,40 0,100" class="zigzag-line" />
                         </svg>
                    </div>
                    <div class="task-top">
                        <div class="task-id">{t1.number}</div>
                        <div class="math-content">{t1.solution}</div>
                    </div>
                    <div class="task-bottom">
                        <div class="task-id">{t2.number}</div>
                        <div class="math-content">{t2.solution}</div>
                    </div>
                </div>
                """
            else: # Default to Vertical Split for comparison
                content = f"""
                <div class="layout-vertical-split">
                    <div class="task-left">
                        <div class="task-id">#{t1.number}</div>
                        <div class="math-content">{t1.solution}</div>
                    </div>
                    <div class="task-right">
                        <div class="task-id">#{t2.number}</div>
                        <div class="math-content">{t2.solution}</div>
                    </div>
                </div>
                """
            
            with open(os.path.join(output_dir, 'combined_short.html'), 'w', encoding='utf-8') as f:
                f.write(base_template.replace('{{CONTENT}}', content))

        # 2. Medium Task (Single) - ADAPTIVE ZOOM
        medium_tasks = [t for t in self.tasks if t.category == TaskCategory.MEDIUM]
        if medium_tasks:
            t = medium_tasks[0]
            content = f"""
            <div class="layout-adaptive">
                <div class="adaptive-content">
                    <div class="task-id">Task {t.number}</div>
                    <div class="math-content">{t.solution}</div>
                </div>
            </div>
            """
            with open(os.path.join(output_dir, 'medium_single.html'), 'w', encoding='utf-8') as f:
                f.write(base_template.replace('{{CONTENT}}', content))

        # 3. Long Task (Split into 2 parts)
        long_tasks = [t for t in self.tasks if t.category == TaskCategory.LONG]
        if long_tasks:
            t = long_tasks[0]
            parts = t.solution.split('<hr class="split-point">')
            if len(parts) < 2:
                parts = [t.solution, "Continued..."]
            
            # Part 1 (Adaptive)
            content1 = f"""
            <div class="layout-adaptive">
                <div class="adaptive-content">
                    <div class="task-id">Task {t.number} (1/2)</div>
                    <div class="math-content">{parts[0]}</div>
                </div>
            </div>
            """
            with open(os.path.join(output_dir, 'long_split_part1.html'), 'w', encoding='utf-8') as f:
                f.write(base_template.replace('{{CONTENT}}', content1))
                
            # Part 2 (Adaptive)
            content2 = f"""
            <div class="layout-adaptive">
                <div class="adaptive-content">
                    <div class="task-id">Task {t.number} (2/2)</div>
                    <div class="math-content">{parts[1] if len(parts) > 1 else ''}</div>
                </div>
            </div>
            """
            with open(os.path.join(output_dir, 'long_split_part2.html'), 'w', encoding='utf-8') as f:
                f.write(base_template.replace('{{CONTENT}}', content2))

    def generate_standalone(self, output_path: str, template_path: Optional[str] = None, watch_mode: bool = False, theme: str = "dark"):
        """
        Генерирует standalone HTML файл со встроенными стилями
        (не требует внешних файлов CSS)
        
        Args:
            output_path: путь для сохранения HTML
            template_path: путь к шаблону (опционально)
            watch_mode: если True, генерирует версию для часов (по одной задаче на экран)
            theme: тема оформления для watch_mode ('dark', 'light', 'terminal', 'blueprint')
        """
        # Определяем путь к CSS
        if watch_mode:
            css_path = os.path.join(os.path.dirname(__file__), 'watch_styles.css')
        else:
        css_path = os.path.join(os.path.dirname(__file__), 'styles.css')
        
        # Читаем CSS
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Если watch_mode, нам нужно изменить способ генерации HTML
        if watch_mode:
            # Для часов мы генерируем отдельные контейнеры для каждой задачи или используем JS для слайдера
            # Для простоты сейчас сделаем одну длинную ленту, но с разделителями экранов
            # Но лучше генерировать отдельный файл на каждую задачу ИЛИ индексный файл.
            # В рамках текущей задачи "фото", мы сделаем так, чтобы КАЖДАЯ задача была отдельным "экраном" в HTML.
            # Для демонстрации вариантов тем, мы применим класс темы к body
            pass
            
        # Генерируем обычный HTML (базовый метод)
        # Примечание: для watch_mode нам, возможно, нужен другой шаблон или модификация текущего.
        # Используем тот же шаблон, но заменим стили и классы.
        
        self.generate(output_path, template_path)
        
        # Читаем сгенерированный HTML
        with open(output_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Если watch_mode, добавляем класс темы и оборачиваем задачи
        if watch_mode:
             # Внедряем класс темы в body
             html_content = html_content.replace('<body>', f'<body class="theme-{theme}">')
             
             # Убираем старый линк на CSS если он был
             html_content = html_content.replace('<link rel="stylesheet" href="framework/styles.css">', '')
             
             # Меняем структуру задач под часы, если нужно (в styles.css уже есть классы)
             # Для демонстрации просто заменим grid на flex column в стилях (уже сделано в watch_styles.css)
             
             # Добавляем CSS
             html_content = html_content.replace(
                '</head>',
                f'<style>\n{css_content}\n</style>\n</head>'
             )
        else:
             # Заменяем ссылку на CSS на inline стили (старое поведение)
        html_content = html_content.replace(
            '<link rel="stylesheet" href="framework/styles.css">',
            f'<style>\n{css_content}\n</style>'
        )
        
        # Удаляем {{CUSTOM_STYLES}} если он не был заменен
        html_content = html_content.replace('{{CUSTOM_STYLES}}', '')
        
        # Сохраняем standalone версию
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✓ Standalone HTML сгенерирован (все стили встроены). Mode: {'Watch' if watch_mode else 'Standard'}")


def create_task(number: int, 
                category: str, 
                solution: str,
                visualization_svg: Optional[str] = None) -> Task:
    """
    Вспомогательная функция для быстрого создания задачи
    
    Args:
        number: номер задачи
        category: 'short', 'medium', или 'long'
        solution: текст решения
        visualization_svg: SVG визуализация
    
    Returns:
        Task объект
    """
    category_map = {
        'short': TaskCategory.SHORT,
        'medium': TaskCategory.MEDIUM,
        'long': TaskCategory.LONG
    }
    
    task_category = category_map.get(category, TaskCategory.MEDIUM)
    return Task(number, task_category, solution, visualization_svg)


if __name__ == "__main__":
    # Пример использования
    framework = CompactFramework(
        title="Пример работы",
        author="Тестовый студент",
        date="16 ноября 2025 г."
    )
    
    # Добавляем тестовые задачи
    framework.add_task(create_task(
        1, 'short',
        r"Вычислим \( 2 + 2 = 4 \)<br><br><strong class='answer'>Ответ: 4</strong>"
    ))
    
    framework.add_task(create_task(
        2, 'medium',
        r"Решим уравнение \( x^2 - 5x + 6 = 0 \)<br>\[ x_{1,2} = \frac{5 \pm \sqrt{25-24}}{2} = \frac{5 \pm 1}{2} \]<br><strong class='answer'>Ответ: x₁=3, x₂=2</strong>"
    ))
    
    # Генерируем
    framework.generate_standalone('test_output.html')

