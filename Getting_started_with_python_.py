# Databricks notebook source
# MAGIC %md
# MAGIC ## Getting started with python- Day1

# COMMAND ----------

Data Type (Immutable)
int
float
string
bool

# COMMAND ----------

a=10
print(a)
print(type(a))

# COMMAND ----------

a=10.5
print(a)
print(type(a))

# COMMAND ----------

print(a)

# COMMAND ----------

s="python"
print(type(s))
print(s)

# COMMAND ----------

n="""databricks is data
and ai company"""
print(type(n))
print(n)

# COMMAND ----------

b=True
print(type(b))
print(b)

# COMMAND ----------

d="10"
print(type(d))

# COMMAND ----------

c="False"
print(c)
print(type(c))

# COMMAND ----------

a=10
print(a)
print(type(a))
print(id(a))

# COMMAND ----------

a=20
print(a)
print(type(a))
print(id(a))

# COMMAND ----------

b=20
print(b)
print(type(b))
print(id(b))

# COMMAND ----------

c=20
print(c)
print(type(c))
print(id(c))

# COMMAND ----------

a=20
print(a)
print(type(a))
print(id(a))

# COMMAND ----------

a=30
print(a)
print(type(a))
print(id(a))

# COMMAND ----------

b=20
print(b)
print(type(b))
print(id(b))

# COMMAND ----------

a=10
b=float(a)
print(b)
print(type(a))
print(type(b))

# COMMAND ----------

a=10
b=str(a)
print(b)
print(type(a))
print(type(b))

# COMMAND ----------

a=0
b=bool(a)
print(b)
print(type(a))
print(type(b))

# COMMAND ----------

s="10"
t=int(s)
print(t)

# COMMAND ----------

s="SQL"
t=int(s)
print(t)

# COMMAND ----------

s="Databricks"
print(s)

# COMMAND ----------

s[0]

# COMMAND ----------

s[-1]

# COMMAND ----------

s[0:5]

# COMMAND ----------

s[:]

# COMMAND ----------

s="AWS" + "Databricks"
print(s)

# COMMAND ----------

s="AWS" + "Databricks"
print(s)

# COMMAND ----------

s="AWS" + 10
print(s)

# COMMAND ----------

s="AWS" * "Databricks"
print(s)

# COMMAND ----------

s="AWS" * 10
print(s)

# COMMAND ----------

# MAGIC %md
# MAGIC plus(+)
# MAGIC str + str
# MAGIC
# MAGIC (*)
# MAGIC str* int

# COMMAND ----------

# MAGIC %md
# MAGIC # List []
# MAGIC
# MAGIC 1.   allows duplicate
# MAGIC 2.   heterogenous  
# MAGIC 3. order is preserverd
# MAGIC 4. indexing & slicing
# MAGIC 5. Mutable

# COMMAND ----------

l=[10,'a',20,10,10.5,10,True,'Python']
print(l)
print(type(l))

# COMMAND ----------

l[-1]

# COMMAND ----------

l=[10,'a',20]
print(l)
print(type(l))
print(id(l))

# COMMAND ----------

l.append(999)
print(l)

# COMMAND ----------

#l.remove(20)
print(l)

# COMMAND ----------

# MAGIC %md
# MAGIC Tuple:
# MAGIC
# MAGIC
# MAGIC 1.   ()
# MAGIC 2.   Exactly same as list except that it is immutable
# MAGIC 3. read only version of list is Tuple
# MAGIC
# MAGIC

# COMMAND ----------


t=(10,'pyhton',10.5,False)
print(t)
print(type(t))

# COMMAND ----------

t[0:3]

# COMMAND ----------

t.append(99)

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC Set
# MAGIC
# MAGIC
# MAGIC 1.   {}
# MAGIC 2.   Duplicate not allowed
# MAGIC 3. order is not preserved
# MAGIC 4. index and slicing is not applicable
# MAGIC 5. Heteogenous objects
# MAGIC 6. Mutable
# MAGIC
# MAGIC

# COMMAND ----------

s={10,10,20,'a',True,10,10.5,99,99,'python'}
print(s)

# COMMAND ----------

s.add(55)
print(s)

# COMMAND ----------

# MAGIC %md
# MAGIC Dict:
# MAGIC 1.   {k:v}
# MAGIC 2.   Duplicates keys are not allowed
# MAGIC 3. duplicate values are allowed
# MAGIC 4. Heterogneous objects
# MAGIC 5. Mutable
# MAGIC

# COMMAND ----------

d={1:'a',2:'b',3:'a',4:True,5:10.9}
print(d)
print(type(d))

# COMMAND ----------

d[3]='Naval'

# COMMAND ----------

print(d)

# COMMAND ----------

Range: sequnce of number

# COMMAND ----------

r=range(10)
print(r)
print(type(r))

# COMMAND ----------

for i in range(5):
  print(i)

# COMMAND ----------

for i in range(5,11):
  print(i)

# COMMAND ----------

for i in range(2,21,2):
  print(i)

# COMMAND ----------


