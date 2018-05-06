
### DataFrame
## Download & Open
_link = 'https://raw.githubusercontent.com/AlexShkunov/experiments/master/data/deliveryData_2.csv'
_fileName = 'deliveryData.csv'

print('*** Start Demo ***')

!rm _fileName -f
!wget -O $_fileName $_link

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

print('>> Loading CSV=' + _fileName)
fullDF = sqlContext.read.format('csv').options(header='true', inferschema='true').load(_fileName)

print('>> Shaped DataFrame...')
fullDF.show(5)

### WeightDelivery
print('>> Target attributes...')
wd_df = fullDF.select('weight', 'days')
wd_df.show(5)

### VectorAssembly
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import VectorAssembler

assembler_f = VectorAssembler(
    inputCols=["weight"],
    outputCol="features")

features_df = assembler_f.transform(wd_df)
training = features_df.selectExpr("weight as label", "features")

print('>> Assembled...')
training.show(5)

### Model-Train
from pyspark.ml.regression import LinearRegression

lr = LinearRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)

print('>> Train LinearRegression...')
lrModel = lr.fit(training)

# Print the coefficients and intercept for linear regression
print("Coefficients: %s" % str(lrModel.coefficients))
print("Intercept: %s" % str(lrModel.intercept))

# Summarize the model over the training set and print out some metrics
trainingSummary = lrModel.summary
print("numIterations: %d" % trainingSummary.totalIterations)
print("objectiveHistory: %s" % str(trainingSummary.objectiveHistory))
#trainingSummary.residuals.show(5)
print("RMSE: %f" % trainingSummary.rootMeanSquaredError)
print("r2: %f" % trainingSummary.r2)

### Predict
print('>> Predict [12]...')

myList = [0,12,15]
vectorList = []

for val in myList:
    vectorList.append(
        (Vectors.dense(val),)
    )

## Make features Vector
print('>> Pred - input...')
target_w = sqlContext.createDataFrame(vectorList, ["features"])
target_w.show()

print('>> Pred - out...')
target_d = lrModel.transform(target_w)
target_d.show()

### Plot
print('>> Plotting...')
from pyspark.sql import Row

plot_model_rdd = target_d.rdd.map(lambda row: Row(
    weight=float(row.features.toArray()[0]), days=float(row.prediction)
))
#print(plot_model_rdd.take(3))

plot_model_df =sqlContext.createDataFrame(plot_model_rdd)
plot_model_df.show()

## Plot model
from IPython.display import display
import matplotlib
import matplotlib.pyplot as plt

print('>> toPandas..')
model_panda=plot_model_df.toPandas()
input_panda= wd_df.toPandas()
target_panda = plot_model_df.filter(plot_model_df.weight == 12.0).toPandas()

plt.plot(model_panda.weight, model_panda.days, 'g--',
        input_panda.weight, input_panda.days, 'bs',
        target_panda.weight, target_panda.days, 'ro')


