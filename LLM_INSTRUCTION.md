# LLM Instruction: Watch Framework

This document provides instructions for the LLM to generate compact, square-format technical solutions suitable for smartwatch displays.

## 1. Core Objective
Generate concise, mathematically/technically precise solutions for technical tasks (Math, Physics, Programming, Engineering). The output must be optimized for a square viewport (~1:1 aspect ratio) to be legible on a smartwatch.

## 2. Input Processing
-   **Source**: Tasks will be provided as images/photos in the `inputs/` directory.
-   **Action**:
    1.  Analyze the image in `inputs/`.
    2.  Extract the problem statement accurately.
    3.  Solve the problem.
    4.  Format the output according to the "Square Format" rules below.

## 3. Square Format Rules
The solution must be "Compact but Precise".
-   **Aspect Ratio**: Target a square layout (approx. 450x450px).
-   **Brevity**: Skip verbose explanations ("Let's assume...", "Therefore we can see...").
-   **Precision**: Show key formulas, variable substitutions, and final result.
-   **Density**: Use high information density. Group related equations.
-   **Structure**:
    -   **Header**: Task Number/ID.
    -   **Body**: Mathematical steps / Code snippet / Diagram.
    -   **Footer**: Final Answer (highlighted).

## 4. Task Sizing & Layout
Classify the task to determine layout strategy:

| Category | Description | Watch Layout Strategy |
| :--- | :--- | :--- |
| **SHORT** | Simple calc / 1-step logic | Center vertically, large font. |
| **MEDIUM** | Standard problem (3-5 steps) | Full width, standard font, single view. |
| **LONG** | Complex derivation / multi-part | Split into 2 "pages" or slides (User scrolls). |

## 5. Universal Technical Handling
-   **Mathematics**: Use LaTeX for formulas. Align `=` signs.
-   **Programming**: Use syntax-highlighted code blocks. Remove comments unless critical. Use short variable names if context is clear.
-   **Physics/Engineering**: Include values with units. Show formula $\rightarrow$ substitution $\rightarrow$ result.

## 6. GitHub Upload
**Trigger**: ONLY when explicitly requested by the user with the command "Upload to GitHub".
-   **Repository**: `git@github.com:dejar212/watch.git`
-   **Action**: Commit the generated artifacts (HTML/Images) and push.

## 7. Framework Usage
Use the Python `framework/` to generate the final HTML visual.
1.  Initialize `CompactFramework`.
2.  Create `Task` objects with `category` (short/medium/long).
3.  Generate `standalone` HTML.

