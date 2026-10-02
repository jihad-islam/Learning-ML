# Linear Regression Basics

Linear regression হলো একটি মেশিন লার্নিং মডেল যা regression problem সলভ করতে ব্যবহার করা হয়। এর মূল কাজ হলো ইনপুট ফিচারের ওপর ভিত্তি করে একটি কন্টিনিউয়াস ভ্যালু বা সংখ্যা (যেমন: গাড়ির দাম) প্রেডিক্ট করা।

## 1. The Formula (ফর্মুলা)

ধরা যাক, আমরা একটি গাড়ির দাম প্রেডিক্ট করতে চাই। এর জন্য আমাদের কিছু ডেটা বা ফিচার ($x_i$) দরকার, যেমন: ইঞ্জিন হর্সপাওয়ার, মাইলেজ, পপুলারিটি ইত্যাদি।

মডেলটির বেসিক ফর্মুলা হলো:

$$g(x_i) = w_0 + x_{i1} \cdot w_1 + x_{i2} \cdot w_2 + ... + x_{in} \cdot w_n$$

সংক্ষেপে সামেশন (Summation) ব্যবহার করে লিখলে:

$$g(x_i) = w_0 + \sum_{j=1}^{n} w_j \cdot x_{ij}$$

ভেক্টর (Vector) ফর্মে লিখলে এটি আরও সহজ হয়ে যায়:

$$g(x_i) = w_0 + x_i^T \cdot w$$

### টার্মগুলোর অর্থ:
* **$g(x_i)$**: আমাদের মডেলের প্রেডিকশন (যেমন: গাড়ির দাম)।
* **$x_i$**: ফিচার ভেক্টর (গাড়ির বিভিন্ন বৈশিষ্ট্য)।
* **$w_0$ (Bias term)**: বেইজলাইন প্রেডিকশন। গাড়িটি সম্পর্কে কোনো তথ্য না জানলেও মডেলটি যে প্রাথমিক দাম ধরে নেয়।
* **$w_1, w_2, ..., w_n$ (Weights)**: প্রতিটি ফিচারের গুরুত্ব। যেমন, হর্সপাওয়ার বাড়লে দাম কতটুকু বাড়বে, তা এই weight দ্বারা নির্ধারিত হয়।

---

## 2. Python Implementation

ফর্মুলাটিকে পাইথনে খুব সহজেই ইমপ্লিমেন্ট করা যায়। নিচে একটি সিঙ্গেল গাড়ির (single observation) জন্য কোড দেওয়া হলো:

```python
import numpy as np

# Sample data for one car
xi = [453, 11, 86] # Features: [horsepower, mpg, popularity]
w0 = 7.17          # Bias term
w = [0.01, 0.04, 0.002] # Weights for each feature

def linear_regression(xi):
    n = len(xi)
    
    # Start with the bias term
    pred = w0
    
    # Add (feature * weight) for each feature
    for j in range(n):
        pred = pred + w[j] * xi[j]
        
    return pred

# Make prediction
log_price_prediction = linear_regression(xi)
print("Log Price:", log_price_prediction) # Output: 12.312
```

---

## 3. Interpreting the Prediction (প্রেডিকশন বিশ্লেষণ)

প্রেডিকশনটি কীভাবে তৈরি হলো তার ব্রেকডাউন:
* **$7.17$**: বেইজলাইন দাম (Bias)।
* **$453 \cdot 0.01$**: হর্সপাওয়ারের অবদান।
* **$11 \cdot 0.04$**: মাইলেজের অবদান।
* **$86 \cdot 0.002$**: পপুলারিটির অবদান।

সবগুলো যোগ করে আমরা পাই $12.312$।

---

## 4. Inverse Transformation (Log থেকে আসল ডলারে রূপান্তর)

অনেক সময় ডেটাসেটে আউಟ್‌লায়ার (outliers) বা অনেক বড় ভ্যালু থাকলে আমরা টার্গেট ভেরিয়েবলের ($y$) ওপর `log1p` অ্যাপ্লাই করি। তাই উপরের ফাংশনটি আমাদের যে ভ্যালু দিচ্ছে ($12.312$), সেটি আসলে গাড়ির দামের **লগারিদমিক ভ্যালু**।

আসল ডলারে দাম পেতে হলে আমাদের এর এক্সপোনেনশিয়াল (Exponential) বের করে ইনভার্স ট্রান্সফরমেশন করতে হবে:

```python
# Convert log price back to actual dollars
actual_price = np.expm1(log_price_prediction)

print("Actual Price in Dollars:", actual_price) 
# Output: ~ 222347.22
```

**নোট:** `np.expm1()` হলো `np.log1p()` এর ঠিক বিপরীত ফাংশন।