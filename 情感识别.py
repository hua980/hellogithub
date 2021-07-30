import paddlehub as hub
# import paddle
# 加载模型

senta = hub.Module(name="senta_lstm")

# 待分类文本

test_text = [

"你长得真好看",

"《黑色四叶草》是部不错的番"

]

# 情感分类

results = senta.sentiment_classify(data={"text": test_text})

# 得到结果

for result in results:
    print(result)
