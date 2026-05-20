# ============================================
# SE446 - Milestone 2: Spark ML Pipeline
# Group 10
#
# Task 1-2:  Alanoud Almeniya (231385)
# Task 3-4:  Lina Dardeer (231709)
# Task 5-7:  Masa Abara (231837)
# Task 8-11: Noura Altuwaijri (231222)
# ============================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, to_timestamp, when
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import BinaryClassificationEvaluator, MulticlassClassificationEvaluator
import time

# ==============================
# Spark Session
# ==============================
spark = SparkSession.builder \
    .appName("M2 Spark ML") \
    .getOrCreate()

print("Spark Session Started")

# ==============================
# Load Data (USE SAMPLE FOR SAFETY)
# ==============================
df = spark.read.csv("hdfs:///data/chicago_crimes_sample.csv", header=True, inferSchema=True)

print("Total Rows:", df.count())

# ==============================
# Fix Date Column (IMPORTANT FIX)
# ==============================
df = df.withColumn(
    "Date_TS",
    to_timestamp(col("Date"), "MM/dd/yyyy hh:mm:ss a")
)

# Drop bad rows
df = df.dropna(subset=["Date_TS"])

# ==============================
# Feature Engineering
# ==============================
df = df.withColumn("Hour", hour(col("Date_TS")))

# Convert Domestic (Boolean → Int)
df = df.withColumn(
    "Domestic_int",
    when(col("Domestic") == True, 1).otherwise(0)
)

# Label (Arrest)
df = df.withColumn(
    "label",
    when(col("Arrest") == True, 1).otherwise(0)
)

print("Feature Engineering Done")

# ==============================
# Indexing
# ==============================
crime_indexer = StringIndexer(inputCol="Primary Type", outputCol="crime_index")

# ==============================
# Feature Vector
# ==============================
assembler = VectorAssembler(
    inputCols=["crime_index", "Domestic_int", "Hour"],
    outputCol="features"
)

# ==============================
# Model (Lightweight for cluster)
# ==============================
rf = RandomForestClassifier(
    featuresCol="features",
    labelCol="label",
    numTrees=10,
    maxDepth=5
)

# ==============================
# Pipeline
# ==============================
pipeline = Pipeline(stages=[crime_indexer, assembler, rf])

# ==============================
# Train/Test Split
# ==============================
train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

# ==============================
# Training
# ==============================
print("Training Model...")
start_time = time.time()

model = pipeline.fit(train_df)

training_time = time.time() - start_time
print("Training Time:", training_time, "seconds")

# ==============================
# Predictions
# ==============================
pred = model.transform(test_df)

# ==============================
# Evaluation Metrics
# ==============================
evaluator_auc = BinaryClassificationEvaluator(labelCol="label", metricName="areaUnderROC")
auc = evaluator_auc.evaluate(pred)

evaluator_acc = MulticlassClassificationEvaluator(labelCol="label", metricName="accuracy")
accuracy = evaluator_acc.evaluate(pred)

evaluator_f1 = MulticlassClassificationEvaluator(labelCol="label", metricName="f1")
f1 = evaluator_f1.evaluate(pred)

evaluator_precision = MulticlassClassificationEvaluator(labelCol="label", metricName="weightedPrecision")
precision = evaluator_precision.evaluate(pred)

evaluator_recall = MulticlassClassificationEvaluator(labelCol="label", metricName="weightedRecall")
recall = evaluator_recall.evaluate(pred)

print("\n===== MODEL METRICS =====")
print("AUC-ROC:", auc)
print("Accuracy:", accuracy)
print("F1 Score:", f1)
print("Precision:", precision)
print("Recall:", recall)

# ==============================
# Confusion Matrix
# ==============================
cm = pred.groupBy("label", "prediction").count()
print("\n===== CONFUSION MATRIX =====")
cm.show()

# ==============================
# Stop Spark
# ==============================
spark.stop()
