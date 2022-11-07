# Databricks notebook source

# MAGIC %md
# MAGIC # MLflow Classification Recipe Databricks Notebook
# MAGIC This notebook runs the MLflow Classification Recipe on Databricks and inspects its results.
# MAGIC
# MAGIC For more information about the MLflow Classification Recipe, including usage examples,
# MAGIC see the [Classification Recipe overview documentation](https://mlflow.org/docs/latest/recipes.html#classification-recipe)
# MAGIC and the [Classification Recipe API documentation](https://mlflow.org/docs/latest/python_api/mlflow.recipes.html#module-mlflow.recipes.classification.v1.recipe).

# COMMAND ----------

# MAGIC %pip install -r ../../requirements.txt
# MAGIC %pip install mlflow

# COMMAND ----------

# MAGIC %md ### Create a new recipe with "databricks" profile:

# COMMAND ----------

from mlflow.recipes import Recipe

r = Recipe(profile="databricks")

# COMMAND ----------

r.clean()

# COMMAND ----------

# MAGIC %md ### Inspect a newly created recipe using a graphical representation:

# COMMAND ----------

r.inspect()

# COMMAND ----------

# MAGIC %md ### Ingest the dataset into the recipe:

# COMMAND ----------

r.run("ingest")

# COMMAND ----------

# MAGIC %md ### Split the dataset in train, validation and test data profiles:

# COMMAND ----------

r.run("split")

# COMMAND ----------

r.run("transform")

# COMMAND ----------

# MAGIC %md ### Using training data profile, train the model:

# COMMAND ----------

r.run("train")

# COMMAND ----------

# MAGIC %md ### Evaluate the resulting model using validation data profile:

# COMMAND ----------

r.run("evaluate")

# COMMAND ----------

# MAGIC %md ### Register the trained model in the registry:

# COMMAND ----------

r.run("register")

# COMMAND ----------

r.inspect("train")

# COMMAND ----------

training_data = r.get_artifact("training_data")
training_data.describe()

# COMMAND ----------

trained_model = r.get_artifact("model")
print(trained_model)
