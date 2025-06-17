# 📅 Day 4 – Sorting Problems

Today was all about understanding how sorting works — not just using built-in functions, but **thinking like the sorting algorithm itself**.  
I solved two really cool problems that helped me understand **in-place sorting** and **interval merging** — both are super common in interviews!

---

## ✅ **Tasks for the Day**

- Learn:
  - How sorting algorithms work conceptually
  - When to sort before solving a problem
  - Dutch National Flag algorithm (a.k.a. 3-way partitioning)
- Solve:
  - [Sort Colors](https://leetcode.com/problems/sort-colors/)
  - [Merge Intervals](https://leetcode.com/problems/merge-intervals/)

---

## 📚 Topics I Studied Today

---

### 🧠 1. Why Sorting is More Than Just `.sort()`

Most problems that involve **"reordering"** or **"merging"** can be made easier if you sort your data first.

👉 Sorting helps:
- Group similar elements
- Process things in order
- Optimize greedy choices
- Avoid nested loops (sometimes)

But it’s also important to understand **how sorting is happening**, especially for in-place problems.

---

### 🧠 2. Dutch National Flag Algorithm

This is a fancy name for a simple idea — it’s a way to sort an array that only contains **three types of values** (like 0, 1, and 2).

You use **three pointers**:
- `low` for the next 0
- `mid` for the current element
- `high` for the next 2

And you just keep swapping values based on conditions.

---

## 💡 Logic of Problems Solved

---

### 🔍 **1. Sort Colors**

**Problem**: Sort an array of 0s, 1s, and 2s **in-place**, without using sort functions.

**Naive idea**: Count the number of 0s, 1s, 2s → then re-write the array.  
(Works, but needs 2 passes.)

**Better logic (Dutch National Flag algorithm)**:

Use three pointers:
- `low` → boundary for 0s  
- `mid` → the current element  
- `high` → boundary for 2s

Swap based on the value at `mid`.

- If 0 → swap with low, move both
- If 1 → move mid
- If 2 → swap with high, move high only

**Time**: O(n)  
**Space**: O(1)

**What I learned**:  
This is about **classifying things** while moving forward.  
Much faster than sorting, because we only do what’s needed.

---

### 🔍 **2. Merge Intervals**

**Problem**: Given intervals like [[1,3],[2,6],[8,10],[15,18]], merge the ones that overlap.

**Key idea**:  
First, **sort the intervals by start time**.  
Then scan and merge.

How it works:
1. Compare current interval with the last one in the result list.
2. If they **overlap** → update the end of the last interval.
3. If they **don’t overlap** → just add it to the result list.

**Why this works**:  
Because once the list is sorted by start time, any overlapping intervals will be **next to each other**.

**Time**: O(n log n) because of sorting  
**Space**: O(n) for the output list

**What I learned**:  
👉 Sorting first makes merging a **one-pass** job.  
👉 Always ask: "Will sorting make this problem easier to solve?"

---

## ✨ What I Learned Today (Summary)

- Sorting is a powerful pre-processing step that can simplify a lot of logic.
- Not every sorting problem is about using `.sort()` — sometimes you need to **simulate sorting with logic** (like Dutch National Flag).
- Merge Intervals taught me that sorting can **reduce complexity** and **help build greedy solutions**.

---

## 📝 Notes to Myself

- When the problem talks about ranges, overlaps, or intervals — always consider **sorting by start time**.
- Dutch National Flag is a must-know pattern for 3-value classification problems (especially with 0, 1, 2).
- Always simulate on a small example on paper first — it helps catch edge cases!