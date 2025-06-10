# 📅 Day 1 – Arrays & Hashing Basics

Welcome to Day 1 of my DSA journey!  
Today was all about starting slow, building the right mindset, and understanding how to work with arrays and some basic hashing.

---

## ✅ **Tasks for the Day**
- Learn and understand:
  - Arrays (how they work behind the scenes)
  - HashMaps (basic intro)
  - Two Pointers technique
- Solve the following problems:
  - [Two Sum](https://leetcode.com/problems/two-sum/)
  - [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

---

## 📚 Topics I Studied Today

### 🧠 1. What is an Array?

An **array** is like a long row of boxes that store stuff (numbers, letters, etc.).  
Each box has a **number called an index**, starting from 0.

- It's **fixed in size**, meaning once it's created, you can't shrink or grow it.
- Accessing stuff is super fast. If you know the index, you can get the value instantly (O(1) time).

**Example**:  
`arr = [3, 5, 9]`  
To get the first element: `arr[0]` → gives 3

---

### 🧠 2. What is a HashMap?

Think of a **HashMap** as a real-life dictionary.  
You ask: "Hey, what’s the meaning of 'apple'?" → it looks it up fast.

In programming, HashMap stores data in **key → value** format.

- Very useful when we want to **check if something exists** quickly.
- Example: check if a number was already seen before.

---

### 🧠 3. Two Pointers Technique

This is like using **two fingers** to scan through an array from different directions.

- One pointer starts from the beginning, the other from the end (or both move forward).
- Helps in problems like searching pairs, reversing arrays, or sliding windows.

---

## 💡 Logic of Problems Solved

---

### 🔍 **1. Two Sum**

**Problem**: Given an array of numbers and a target, return the indices of two numbers that add up to the target.

**Brute-force logic**:  
Try every pair → takes a lot of time (O(n²))

**Optimized logic**:  
Use a **HashMap** to store previously seen numbers.  
For each number, check if the **target - current number** is already in the map.

**Why this works**:  
Because we're keeping track of numbers we’ve seen, we can instantly know if the matching pair exists!

---

### 🔍 **2. Contains Duplicate**

**Problem**: Check if any value appears at least twice in the array.

**Brute-force logic**:  
Compare every element with every other → again slow (O(n²))

**Better logic**:  
Use a **set** (a collection that only stores unique values).  
Loop through the array, and if the number is already in the set, we found a duplicate.

---

## ✨ What I Learned Today (Summary)

- Arrays are the most basic and powerful data structure — everything builds from here.
- HashMaps (and sets) help us **speed up our searches** dramatically.
- The **Two Pointers technique** is simple but solves many medium-level problems later.
- Writing brute-force logic first helps you **understand the problem** — optimizing comes next.

---

## 📝 Notes to Myself

- Always ask: **Can I solve this faster with a map or set?**
- Think step-by-step, write down edge cases.
- Don't rush — solving 2 questions with deep understanding is way better than 5 blindly.

---

That's all for Day 1! 🎯  
Tomorrow, I’ll dive deeper into more array tricks like **sliding window** and **prefix sums**.

Let’s gooo 🚀