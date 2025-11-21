# 📚 Data Structures

This repository provides **C**reate, **R**ead, **U**pdate, and **D**elete (**CRUD**) operations implemented for a comprehensive collection of **linear** and **non-linear** data structures. It serves as a practical resource for learning, implementing, and comparing fundamental data structure concepts.

-----

## 🌟 Features

  * **Complete CRUD Coverage:** Dedicated functions for insertion (Create), retrieval/traversal (Read), modification (Update), and deletion (Delete) for every included data structure.
  * **Broad Structure Support:** Includes both Linear and Non-Linear data structures.
  * **Clear Implementation:** Code is written to be **clean, modular,** and **well-commented** for easy understanding.
  * **Language Agnostic Focus (Specify Language in Codebase):** While implementations are in Python, the conceptual logic is universally applicable.

-----

## 🛠️ Data Structures Included

### 1\. Linear Data Structures

These structures arrange data elements sequentially or in a straight line.

| Data Structure | Description | Key Operations |
| :--- | :--- | :--- |
| **Arrays** | A collection of items stored at contiguous memory locations. | Insertion at index, Deletion at index, Access by index. |
| **Linked Lists** | A sequence of nodes where each node points to the next, offering dynamic memory allocation. | Insert/Delete at head/tail/position, Traversal. |
| **Stack** | A LIFO (Last-In, First-Out) structure. | Push(Create), Pop(Delete), Peek(Read). |
| **Queue** | A FIFO (First-In, First-Out) structure. |Enqueue(Create), Dequeue(Delete), Front(Read). |
| **Deque** (Double-Ended Queue) | Elements can be inserted or deleted from both ends. |Insert/Delete from front/rear. |

### 2\. Non-Linear Data Structures

These structures organize data in a non-sequential manner, often in hierarchies or networks.

| Data Structure | Description | Key Operations |
| :--- | :--- | :--- |
| **Trees** | A hierarchical structure with a root and sub-trees of children. | Insertion, Deletion, Traversal (Inorder, Preorder, Postorder). |
| **Binary Search Trees (BST)** | A tree where the left child key is less than the parent, and the right child key is greater. |Search/Min/Max (Read), Insertion, Deletion. |
| **Heaps** | A specialized tree-based structure satisfying the heap property (Max-Heap or Min-Heap). | Insert, Extract-Max/Min (Delete), Heapify. |
| **Graphs** | A set of vertices (nodes) and edges (connections). | Add Vertex/Edge (Create),Remove Vertex/Edge (Delete),Traversal (BFS/DFS). |
| **Hash Maps / Hash Tables** | Stores key-value pairs using a hash function for fast lookups. | Insert(Create), Get(Read),Update,Remove(Delete). |

-----

## 🚀 Getting Started

### Prerequisites

You will need Python, Annaconda, VS code installed on your machine.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Ankitkumar1141
    cd Data_Structures
    ```
2.  **Navigate to the desired structure's folder:**
    ```bash
    cd linear/linked_lists/
    # or
    cd nonlinear/graphs/
    ```
3.  **Run:**
    ```bash
    python main.py
-----

## 📂 Repository Structure

The code is organized logically into linear and nonlinear directories.

```
.
├── linear/
│   ├── arrays/
│   ├── linked_lists/
│   ├── stacks/
│   └── ...
└── nonlinear/
    ├── trees/
    │   ├── bst/
    │   └── heaps/
    ├── graphs/
    └── hash_tables/
```

-----

## 🤝 Contributing

Contributions are welcome\! If you find a bug or want to add an implementation for another data structure (e.g., Trie, Skip List), please feel free to submit a **Pull Request**.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.
