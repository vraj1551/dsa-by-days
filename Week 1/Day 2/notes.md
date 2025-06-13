# 📅 Day 2 – Sliding Window & Prefix Sum

Day 2 — today I explored some super useful techniques that help make many array problems MUCH faster:

👉 **Sliding Window**  
👉 **Prefix Sum**

Also solved a couple of fun problems using these techniques!

---

## ✅ **Tasks for the Day**

- Understand:
  - Sliding Window technique
  - Prefix Sum technique
- Solve:
  - [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
  - [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- Practice Question:
  - [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

---

## 📚 Topics I Studied Today

---

### 🧠 1. Sliding Window

**Very easy idea once you get it!**

Imagine a **window** moving over an array.  
Instead of calculating things from scratch every time, you "slide" the window and update the result.

👉 Works great when you need:
- sum of a subarray
- max/min of a subarray
- check for valid subarrays

**Example**:  
Finding the **maximum sum of a subarray of size k** → instead of summing the whole subarray again and again, you just add the new number entering the window and subtract the number leaving.

---

### 🧠 2. Prefix Sum

Another magical technique!  
You create an extra array where:
- `prefixSum[i] = sum of first i numbers of original array`

👉 This allows you to get the **sum of any subarray** in O(1) time.

**Example**:  
Want sum of elements between index 3 and 7? → Just do:


---

## 💡 Logic of Problems Solved

---

### 🔍 **1. Maximum Subarray** (Kadane’s Algorithm)

**Problem**: Find the **contiguous subarray** with the largest sum.

**Brute Force**:  
Try all possible subarrays → very slow (O(n²)).

**Better logic (Kadane’s Algorithm)**:

👉 At each index, ask:
- Should I continue the current subarray?
- Or should I start fresh with this number?

**Formula**:  

**Sliding window mindset** → "carry forward good sums, reset when it’s better."

---

### 🔍 **2. Best Time to Buy and Sell Stock**

**Problem**: Given prices over days, buy on one day and sell on a future day to get max profit.

**Brute Force**:  
Try every pair of days → again slow.

**Better logic (Sliding window style)**:

👉 Loop through the array once:

- Keep track of **minimum price seen so far**.
- At each day, check: if I sell today, what’s the profit?


Keep updating **maxProfit** as you go.

---

### 🔍 **Practice Question: Contains Duplicate II**

**Problem**: Check if the same number appears within k distance.

**Sliding window idea + HashSet**:

- Maintain a window of size k using a set.
- For each element:
  - If already in set → duplicate found!
  - Else → add to set.
  - If window size > k → remove the oldest element.

👉 Super neat use of **sliding window + hashing**.

---

## ✨ What I Learned Today (Summary)

- **Sliding window** is like having a smart moving view of an array — saves tons of computation.
- **Prefix sums** are awesome when dealing with repeated subarray sum queries.
- Many problems that look tricky become simple when you think:  
  👉 *“Can I slide a window or use prefix sums?”*
- Practiced combining **HashSet** with **windowing** (Contains Duplicate II).

---

That’s it for Day 2! 🎯  
Tomorrow → I’ll go deeper into **Prefix Sums + more Sliding Window problems**.