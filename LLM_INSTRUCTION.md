# LLM Instruction: Watch Framework

This document provides instructions for the LLM to generate compact yet descriptive technical solutions for smartwatch displays.

## 1. Core Objective
Generate mathematically/technically precise solutions for technical tasks (Math, Physics, Programming, Engineering). The solution must be optimized for a square viewport (~1:1 aspect ratio).

**CRITICAL CHANGE**: Solutions must NOT be just bare formulas. Each major logical step must have a **concise text description** (1-3 words) to guide the user.

## 2. Input Processing
-   **Source**: Tasks will be provided as images/photos in the `inputs/` directory.
-   **Action**:
    1.  Analyze the image in `inputs/`.
    2.  Extract the problem statement accurately.
    3.  Solve the problem.
    4.  Format the output according to the "Square Format" rules below.

## 3. Square Format Rules
-   **Aspect Ratio**: Target a square layout (1125x1125px).
-   **Step Descriptions**: BEFORE writing a formula, write *what* you are doing.
    -   *Bad*: `\int x e^x dx = ...`
    -   *Good*: `Integrate by parts:` `\int x e^x dx`
-   **Precision**: Show variable substitutions and final result clearly.
-   **Density**: Use high information density. Group related equations.

## 4. Task Sizing & Layout
Classify the task to determine layout strategy:

| Category | Description | Watch Layout Strategy |
| :--- | :--- | :--- |
| **SHORT** | Simple calc / 1-step logic | **Merged Split**: Will be paired with another short task. |
| **MEDIUM** | Standard problem (3-5 steps) | **Auto-Fit**: Fills the entire square. Font size maximizes. |
| **LONG** | Complex derivation / multi-part | **Pagination**: Split into multiple "slides" (User swipes). |

## 5. Universal Technical Handling
-   **Mathematics**: Use LaTeX for formulas. Align `=` signs.
-   **Programming**: Use syntax-highlighted code blocks.
-   **Physics/Engineering**: Include values with units.

## 6. GitHub Upload
**Trigger**: ONLY when explicitly requested by the user with the command "Upload to GitHub".
-   **Repository**: `git@github.com:dejar212/watch.git`
-   **Action**: Commit the generated artifacts (HTML/Images) and push.
