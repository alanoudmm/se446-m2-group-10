# SE446 – Milestone 2: Spark ML Pipeline

**Group 10**

---

## Team Members

| Name             | Student ID |
| ---------------- | ---------- |
| Alanoud Almeniya | 231385     |
| Lina Dardeer     | 231709     |
| Masa Abara       | 231837     |
| Noura Altuwaijri | 231222     |

---

## Executive Summary

This project analyzes the Chicago Crimes dataset using  Apache Spark. IN milestone 1 MapReduce was used for batch processing, while Spark enabled faster in-memory computation and machine learning modeling. The results show that Spark is more efficient, easier to use, and supports advanced analytics.

---

##  M1 vs M2 Comparison (Tasks 1–4)

### Task 1: Crime Type Analysis

| Rank | Crime Type          | MapReduce (M1) | Spark (M2) 
| ---- | ------------------- | -------------- | ---------- 
| 1    | THEFT               | 2054           | 2054       
| 2    | BATTERY             | 1728           | 1728      
| 3    | CRIMINAL DAMAGE     | 1062           | 1062       
| 4    | MOTOR VEHICLE THEFT | 948            | 948        
| 5    | ASSAULT             | 878            | 878        


---

###  Task 2: Location Hotspots

| Rank | Location    | MapReduce (M1) | Spark (M2) 
| ---- | ----------- | -------------- | ---------- 
| 1    | STREET      | 2737           | 2737       
| 2    | APARTMENT   | 1909           | 1909       
| 3    | RESIDENCE   | 1358           | 1358       
| 4    | SIDEWALK    | 536            | 536        
| 5    | PARKING LOT | 362            | 362        

---
### Task 3: Crime Trend Over Years

|Year|MapReduce (M1)|Spark (M2)|
|-|-|-|
|2001|4|4|
|2005|19|19|
|2010|5|5|
|2015|28|28|
|2017|49|49|



---

### Task 4: Arrest Rate Analysis

**Arrest rate in M1**
false 8717
true  1283

|Metric|MapReduce (M1)|Spark (M2)|
|-|-|-|
|Arrest Rate|\~0.1283|0.1283|

Arrest rate is \~12.83% in both implementations.

---

## Performance Comparison

|Feature|MapReduce|Spark|
|-|-|-|
|Speed|Slow|Fast|

**Conclusion:** Spark is faster, simpler, and more powerful.

---
