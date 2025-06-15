# 📅 Day 3 – Sliding Window Practice

Another solid day of practicing DSA!  
I focused on applying the **sliding window technique** and got into slightly more complex variations.  
The two problems I worked on today challenged my understanding — especially around how to **track subarrays and prefixes smartly**.

---

## ✅ **Tasks for the Day**

- Deepen understanding of:
  - Variants of sliding window
  - When sliding window **doesn’t work directly**
  - When to use **prefix sums with hash maps**
- Solve:
  - [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
  - [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

---

## 📚 Topics I Studied Today

---

### 🧠 Sliding Window — Refined View

By now, sliding window feels familiar. But today I realized:

👉 **Sliding window doesn't always mean a fixed-size window.**  

Also learned:
- Sometimes **sliding window isn’t the best tool** — we need to think in terms of **prefix sums + HashMap** when we care about sum values over time.

---

## 💡 Logic of Problems Solved

---

### 🔍 **1. Product of Array Except Self**

**Problem**: For every index, return the product of all other elements (without using division).

**Optimized logic (Two Pass Approach)**:

We can't use division, so:
1. First, go **left to right**, and for each index, store the product of all elements to its **left**.
2. Then go **right to left**, and multiply the result with product of all elements to its **right**.

✅ No extra space (except output array), no division, time = O(n)

**What I learned**:  
👉 This isn’t a sliding window question, but it’s a good exercise in **prefix-style thinking**  
👉 Think in **prefix + suffix** instead of recalculating everything

---

### 🔍 **2. Subarray Sum Equals K**

**Problem**: Given an array, find the number of subarrays that sum to exactly `k`.

**Brute-force logic**:  
Try all subarrays and check if their sum = k → O(n²), not ideal.

**Optimized logic (Prefix Sum + HashMap)**:

- Keep a running sum (prefix sum) while going through the array.
- At each step, check:  
  `currentSum - k` → how many times this value has occurred before?



👉 Use a **HashMap to store prefixSum frequencies**.