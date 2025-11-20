#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates 5 distinct density variants for Watch Math Display.
Creates folders v1_Standard, v2_Grid, etc.
"""

import sys
import os

# Add framework to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../framework'))

from generator import CompactFramework, create_task, TaskCategory

def create_math_tasks():
    tasks = []

    # --- SHORT TASKS (Merged) ---
    tasks.append(create_task(1, 'short', r'''
        \[ \int x e^x dx \]
        \( u=x, dv=e^x dx \)
        \( du=dx, v=e^x \)
        \[ = xe^x - e^x + C \]
    '''))

    tasks.append(create_task(2, 'short', r'''
        \[ \lim_{x\to 0} \frac{\sin 5x}{3x} \]
        \[ = \frac{5}{3} \lim \frac{\sin 5x}{5x} \]
        \[ = \frac{5}{3} \cdot 1 = 1.66 \]
    '''))

    # --- MEDIUM TASK (Single Square) ---
    tasks.append(create_task(3, 'medium', r'''
        <strong>Find Eigenvalues:</strong>
        \[ A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix} \]
        \[ |A - \lambda I| = (4-\lambda)(3-\lambda) - 2 = 0 \]
        \[ \lambda^2 - 7\lambda + 12 - 2 = 0 \]
        \[ \lambda^2 - 7\lambda + 10 = 0 \]
        \[ (\lambda - 5)(\lambda - 2) = 0 \]
        <div style="border: 1px solid white; padding: 5px; margin-top: 10px; text-align: center;">
        \(\lambda_1 = 5, \lambda_2 = 2\)
        </div>
    '''))

    # --- LONG TASK (Split across 2 files) ---
    # We use a special delimiter <hr class="split-point"> to tell the generator where to cut
    tasks.append(create_task(4, 'long', r'''
        <strong>Solve System (Cramer):</strong>
        \[ \begin{cases} 2x + y = 7 \\ x - 3y = -7 \end{cases} \]
        \( \Delta = \begin{vmatrix} 2 & 1 \\ 1 & -3 \end{vmatrix} = -6 - 1 = -7 \)
        <br>
        \( \Delta_x = \begin{vmatrix} 7 & 1 \\ -7 & -3 \end{vmatrix} = -21 - (-7) = -14 \)
        
        <hr class="split-point">
        
        \( \Delta_y = \begin{vmatrix} 2 & 7 \\ 1 & -7 \end{vmatrix} = -14 - 7 = -21 \)
        <br>
        \( x = \frac{\Delta_x}{\Delta} = \frac{-14}{-7} = 2 \)
        <br>
        \( y = \frac{\Delta_y}{\Delta} = \frac{-21}{-7} = 3 \)
        <div style="border: 2px solid white; padding: 10px; margin-top: 20px; text-align: center; font-weight: bold;">
        Ans: (2, 3)
        </div>
    '''))
    
    return tasks

def main():
    print("Generating 5 Math Density Variants...")
    
    variants = [
        ("v1_Standard", "v1-standard"),
        ("v2_Grid", "v2-grid"),
        ("v3_Flow", "v3-flow"),
        ("v4_CompactBox", "v4-compact"),
        ("v5_Sidebar", "v5-sidebar")
    ]
    
    framework = CompactFramework(title="Math Density Test")
    tasks = create_math_tasks()
    for t in tasks:
        framework.add_task(t)
    
    base_output = os.path.join(os.path.dirname(__file__), "density_variants")
    
    for folder_name, css_class in variants:
        output_dir = os.path.join(base_output, folder_name)
        print(f"Generating {folder_name}...")
        framework.generate_density_variants(output_dir, css_class)

    print(f"\nDONE. Check folders in: {base_output}")

if __name__ == "__main__":
    main()

