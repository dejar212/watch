#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates Radical Density Variants using harder problems (Algai Midterm).
Tests: Vertical Split, ZigZag, and Adaptive Zoom.
"""

import sys
import os

# Add framework to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../framework'))

from generator import CompactFramework, create_task, TaskCategory

def create_algai_tasks():
    tasks = []

    # --- SHORT TASK 1 (Merged) ---
    # Recurrence Relation (Master Theorem case)
    tasks.append(create_task(1, 'short', r'''
        <div class="step-desc">Solve recurrence:</div>
        \[ T(n) = 4T(n/2) + n^2 \]
        <div class="step-desc">Master Theorem parameters:</div>
        \( a=4, b=2, f(n)=n^2 \)
        <div class="step-desc">Compare \( n^{\log_b a} \):</div>
        \( \log_2 4 = 2 \implies n^2 \)
        <div class="step-desc">Case 2 (Equal):</div>
        \( T(n) = \Theta(n^2 \log n) \)
        <div class="final-answer">Ans: \Theta(n^2 \log n)</div>
    '''))

    # --- SHORT TASK 2 (Merged) ---
    # Time Complexity Analysis
    tasks.append(create_task(2, 'short', r'''
        <div class="step-desc">Analyze loop complexity:</div>
        <pre style="font-size:0.7em; margin:0;">
for i = 1 to n:
  j = 1
  while j < n:
    j = j * 2
</pre>
        <div class="step-desc">Outer loop runs \( n \) times.</div>
        <div class="step-desc">Inner loop runs \( \log n \) times.</div>
        <div class="step-desc">Multiply:</div>
        \( O(n \cdot \log n) \)
        <div class="final-answer">Ans: O(n \log n)</div>
    '''))

    # --- MEDIUM TASK (Adaptive Zoom) ---
    # Dijkstra's Algorithm Step
    tasks.append(create_task(3, 'medium', r'''
        <div class="step-desc">Run Dijkstra from node S:</div>
        <div class="step-desc">Graph edges: (S,A,4), (S,B,2), (B,A,1), (B,C,5)</div>
        
        <div class="step-desc">1. Init dists:</div>
        \( S=0, A=\infty, B=\infty, C=\infty \)
        
        <div class="step-desc">2. Visit S, update neighbors:</div>
        \( A = \min(\infty, 0+4) = 4 \)
        \( B = \min(\infty, 0+2) = 2 \)
        
        <div class="step-desc">3. Pick min unvisited (B=2):</div>
        \( A = \min(4, 2+1) = 3 \)
        \( C = \min(\infty, 2+5) = 7 \)
        
        <div class="step-desc">4. Pick min unvisited (A=3):</div>
        \( C = \min(7, 3+\infty) = 7 \)
        
        <div class="final-answer">Dists: S:0, A:3, B:2, C:7</div>
    '''))

    # --- LONG TASK (Split) ---
    # Dynamic Programming (Knapsack or Edit Distance)
    tasks.append(create_task(4, 'long', r'''
        <div class="step-desc">DP: Edit Distance "KITTEN" -> "SITTING"</div>
        <div class="step-desc">Recurrence:</div>
        \[ D[i][j] = \min \begin{cases} D[i-1][j]+1 \\ D[i][j-1]+1 \\ D[i-1][j-1] + (0 \text{ if match}) \end{cases} \]
        
        <div class="step-desc">Table (partial):</div>
        <table style="width:100%; border-collapse: collapse; font-size: 0.8em; text-align:center;">
        <tr><td></td><td>""</td><td>S</td><td>I</td><td>T</td></tr>
        <tr><td>""</td><td>0</td><td>1</td><td>2</td><td>3</td></tr>
        <tr><td>K</td><td>1</td><td>1</td><td>2</td><td>3</td></tr>
        <tr><td>I</td><td>2</td><td>2</td><td>1</td><td>2</td></tr>
        </table>
        
        <hr class="split-point">
        
        <div class="step-desc">Calculate remaining cells:</div>
        \( D[3][3] (\text{T vs T}) = D[2][2] = 1 \)
        \( ... \)
        <div class="step-desc">Final cell D[6][7]:</div>
        1. K->S (sub)
        2. E->I (sub)
        3. N->G (sub)
        4. Insert 'G'
        <div class="step-desc">Total operations: 3</div>
        <div class="final-answer">Distance = 3</div>
    '''))
    
    return tasks

def main():
    print("Generating Algai Midterm Variants...")
    
    # 1. Generate ZigZag Layout (Short Tasks)
    print("Generating Layout: ZigZag Split...")
    framework = CompactFramework(title="Algai - ZigZag")
    for t in create_algai_tasks(): framework.add_task(t)
    framework.generate_density_variants(
        os.path.join(os.path.dirname(__file__), "density_variants", "layout_zigzag"), 
        "layout-zigzag"
    )

    # 2. Generate Vertical Split Layout (Short Tasks)
    print("Generating Layout: Vertical Split...")
    framework = CompactFramework(title="Algai - Vertical")
    for t in create_algai_tasks(): framework.add_task(t)
    framework.generate_density_variants(
        os.path.join(os.path.dirname(__file__), "density_variants", "layout_vertical"), 
        "layout-vertical-split"
    )
    
    # 3. Generate Adaptive (Medium/Long) - The generator uses 'layout-adaptive' automatically for medium
    print("Generating Layout: Adaptive Zoom...")
    framework = CompactFramework(title="Algai - Adaptive")
    for t in create_algai_tasks(): framework.add_task(t)
    framework.generate_density_variants(
        os.path.join(os.path.dirname(__file__), "density_variants", "layout_adaptive"), 
        "layout-adaptive"
    )

    print(f"\nDONE. Check 'examples/density_variants/'")

if __name__ == "__main__":
    main()

