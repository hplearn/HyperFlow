import logging

import pandas as pd


from hyperflow.pipeline.components.preprocessing.operate.drop import DropAll
from hyperflow.pipeline.components.preprocessing.operate.split.cat import SplitCat
from hyperflow.pipeline.dataframe import GenericDataFrame
from hyperflow.pipeline.pipeline import GenericPipeline

df = pd.read_csv("../examples/classification/train_classification.csv")
y = df.pop("Survived").values
df = df.loc[:, ["Sex", "Ticket", "Pclass"]]

df2 = GenericDataFrame(df, feat_grp=["cat", "cat", "num"])

split_cat = SplitCat()
split_cat.in_feat_grp = "cat"
split_cat.update_hyperparams({
    "highR": "highR_cat",
    "lowR": "lowR_cat",
    "threshold": 0.5
})
result = split_cat.fit_transform(df2)
logging.info(result)

df2 = GenericDataFrame(df, feat_grp=["cat", "cat", "num"])
drop_all = DropAll()
drop_all.in_feat_grp = ["cat", "num"]
drop_all.out_feat_grp="drop"

split_cat = SplitCat()
split_cat.in_feat_grp = "cat"

pipeline = GenericPipeline([
    ("drop_all", drop_all),
    ("split_cat", split_cat)
])
result=pipeline.fit_transform(df2)
logging.info(result)



