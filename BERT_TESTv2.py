import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from transformers import BertForSequenceClassification, BertTokenizer, get_linear_schedule_with_warmup, logging
from transformers import MobileBertForSequenceClassification, MobileBertTokenizer
import tensorflow as tf
import torch
from torch.utils.data import TensorDataset, DataLoader, RandomSampler, SequentialSampler
from torch.utils.tensorboard import SummaryWriter
import time
import datetime

def main():
    # 모델명
    model = 'bert_model.pt'
    model = MobileBertForSequenceClassification.from_pretrained(model)
    model.eval()
    # Test
    df = pd.read_csv("third.csv")
    data_X = df['Text'].values
    labels = df['Sentiment'].values

    tokenizer = MobileBertTokenizer.from_pretrained('mobilebert-uncased', do_lower_case=True)
    input_ids = [tokenizer.encode(x, add_special_tokens=True) for x in data_X]
    input_ids = tf.keras.utils.pad_sequences(input_ids,
                                             maxlen=128,
                                             dtype="long",
                                             truncating="post",
                                             padding="post")
    attention_mask = [[float(i > 0) for i in ids] for ids in input_ids]

    batch_size = 8
    test_inputs = torch.tensor(input_ids)
    test_labels = torch.tensor(labels)
    test_masks = torch.tensor(attention_mask)
    test_data = TensorDataset(test_inputs, test_masks, test_labels)
    test_sampler = SequentialSampler(test_data)
    test_dataloader = DataLoader(test_data, sampler=test_sampler, batch_size=batch_size)
    print(test_data)
    t0 = time.time()  # 시간 초기화

    test_loss, test_accuracy, test_steps, test_examples = 0, 0, 0, 0
    for batch in test_dataloader:
        # batch 데이터 추출
        batch_ids, batch_mask, batch_labels = tuple(t for t in batch)
        # gradient 무시
        with torch.no_grad():
            # Forward
            outputs = model(batch_ids, token_type_ids=None, attention_mask=batch_mask)
        # logit
        logits = outputs[0]
        logits = logits.numpy()
        label_ids = batch_labels.numpy()
        # accuracy
        pred_flat = np.argmax(logits, axis=1).flatten()
        labels_flat = label_ids.flatten()
        test_accuracy_temp = np.sum(pred_flat == labels_flat) / len(labels_flat)
        test_accuracy += test_accuracy_temp
        test_steps += 1
        print("test steps : ", test_steps, "Accuracy : ",test_accuracy_temp)
    avg_test_accuracy = test_accuracy / test_steps
    print("Accuracy: {0:.2f}".format(avg_test_accuracy))
    print("test took: {:}".format(str(datetime.timedelta(seconds=(int(round(time.time() - t0)))))))

if __name__ == "__main__":
    main()