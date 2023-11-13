
from basic_pitch.inference import predict_and_save
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
import pandas as pd
import basic_pitch.note_creation
# predict_and_save(
#     ["C:\\Users\\coco\\Desktop\\basic-pitch-main\\jaycd.ogg"],
#     "C:\\Users\\coco\\Desktop\\basic-pitch-main\\myoutput",
#     True,
#     False,
#     False,
#     True,
# )
model_output, midi_data, note_events = predict("./jaycd.ogg")
second_items = [item[2] for item in note_events]

# 打印提取的第二项
print(second_items)
with open('./myoutput/yinfu_data.txt', 'w') as file:  # 替换为你要保存的文件名和路径
    for item in second_items:
        file.write(str(item) + '\n')

print("列表已保存为txt文件")