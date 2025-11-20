# Watch Framework Improvements Proposal

This document outlines the proposed roadmap for evolving the Watch Framework from a Python-script-based generator into a robust, data-driven tool for creating beautiful mathematical documents.

## 1. Data-Driven Workflow

**Current State:**  
Homeworks are defined by writing Python code that instantiates classes and calls methods (e.g., `framework.add_task(create_task(...))`).

**Proposal:**  
Shift to a declarative configuration approach using JSON or YAML files. Users will define the content in a structured file, and the framework will parse it to generate the HTML.

**Example (`homework.yaml`):**
```yaml
meta:
  title: "Homework 7"
  author: "Student Name"
  date: "2025-11-20"
  course: "alg"

tasks:
  - number: 1
    category: short
    solution: |
      We solve the equation \( x^2 = 4 \).
      \[ x = \pm 2 \]
      <div class="answer">Answer: 2</div>

  - number: 2
    category: medium
    visualization:
      type: "vector_2d"
      data: [[1, 2], [3, 4]]
    solution: |
      Vector addition visualization...
```

## 2. CLI Interface

**Current State:**  
Users must write a specific Python script (like `generate_matem.py`) and run it.

**Proposal:**  
Implement a unified Command Line Interface (CLI) to build projects from the config files.

**Commands:**
- `python -m watch init`: Create a new project structure.
- `python -m watch build homework.yaml`: Generate the HTML output.
- `python -m watch serve`: Start a local server with live reload for editing.

## 3. LLM Integration

**Current State:**  
No direct integration.

**Proposal:**  
Design prompt templates and tooling to allow Large Language Models to output the specific JSON/YAML schema required by the framework.

- **Structured Output:** Create a system prompt that describes the `homework.yaml` schema so LLMs can take a raw text or photo of a problem and output the valid YAML block.
- **Auto-Correction:** A validator tool that checks the LLM output for schema violations before generation.

## 4. Enhanced Visualization

**Current State:**  
Basic matplotlib integration for specific cases (vectors, etc.).

**Proposal:**  
Expand the `visualizations.py` module into a rich library of pre-built geometric and algebraic figures that can be configured via the YAML/JSON interface without writing Python code.

- **Geometry:** Triangles, circles, intersecting lines with automatic labeling.
- **Graphs:** Function plotting with automatic domain/range adjustment.
- **Data Structures:** Trees and graphs for algorithmic problems.

