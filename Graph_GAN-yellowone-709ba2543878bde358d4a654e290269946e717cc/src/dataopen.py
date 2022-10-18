import csv
import torch
import numpy as np

filename = 'routeall3.txt'
port_to_ix = {'default': 0, '': 1}
lh_to_ix = {}
rcv_to_ix = {}
store_num = []
store_port = []
store_lh = []
store_self = []
store_rcv = []

def str2Number(strParam):
    if strParam == '' or strParam is None:
    	#遇到空字符串和None会自定义一种处理方式，这里设为默认0
        res = 0
    try:
        res = float(strParam)
    except:
    	#如果遇到了非数字字符，可以异常处理。这里设为默认为0
        res = 0
    return res

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row2 in reader:
        temp1 = []
        temp2 = []
        temp3 = []
        temp4 = []
        temp5 = []
        # 构建port词袋模型
        if row2[5] not in port_to_ix:
            port_to_ix[row2[5]] = len(port_to_ix)
        if row2[6] not in port_to_ix:
            port_to_ix[row2[6]] = len(port_to_ix)
        if row2[7] not in port_to_ix:
            port_to_ix[row2[7]] = len(port_to_ix)

        # 构建lh词袋模型
        if row2[8] not in lh_to_ix:
            lh_to_ix[row2[8]] = len(lh_to_ix)

        # 构建receiver_country_code词袋模型
        if row2[10] not in rcv_to_ix:
            rcv_to_ix[row2[10]] = len(rcv_to_ix)

        if row2[9] == '0':
            temp5 = [0]
        else:
            temp5 = [1]

        temp1 = [str2Number(row2[1][-8:]), str2Number(row2[2][-8:]), str2Number(row2[3][-8:]), str2Number(row2[4][-8:])]
        temp2 = [port_to_ix[row2[5]], port_to_ix[row2[6]], port_to_ix[row2[7]]]
        temp3 = [lh_to_ix[row2[8]]]
        temp4 = [rcv_to_ix[row2[10]]]

        store_num.append(temp1)
        store_port.append(temp2)
        store_lh.append(temp3)
        store_rcv.append(temp4)
        store_self.append(temp5)


    store_num_ts = torch.Tensor(store_num)
    # print(store_num_ts)
    store_port_ts = torch.Tensor(store_port)
    # print(store_port_ts)
    store_lh_ts = torch.Tensor(store_lh)
    # print(store_lh_ts)
    store_rcv_ts = torch.Tensor(store_rcv)
    # print(store_rcv_ts)
    store_self_ts = torch.Tensor(store_self)

    # 复杂res_code特征bachnorm embedding
    m = torch.nn.BatchNorm1d(4, affine=True)
    output1 = m(store_num_ts)
    # print(output1)

    # 拼接res_code和其他特征
    embeds = torch.cat([output1, store_port_ts, store_lh_ts,  store_self_ts, store_rcv_ts], dim=1)
    print('feature is:')
    print(embeds)
    # print(embeds.dtype)
    # print(embeds.shape)
    f.close()

# 建立模型
class BiLSTM(torch.nn.Module):
    def __init__(self):
        super(BiLSTM, self).__init__()
        # bidirectional双向LSTM
        self.bilstm = torch.nn.LSTM(10, 10, 1, bidirectional=True)

    def forward(self, input):
        # 调换第一维和第二维度
        embedding_input = input.permute(1, 0, 2)
        output, (h_n, c_n) = self.bilstm(embedding_input)
        # 使用正向LSTM与反向LSTM最后一个输出做拼接
        # print(h_n.shape)
        # print(c_n.shape)
        # print(output.shape)
        return output

model = BiLSTM()
embeds = embeds.unsqueeze(dim=0)
print(embeds.shape)
print('after bilstm embedding:')
pred = model(embeds)
pred = pred.squeeze(1)
pred = pred[:, :10]+pred[:, 10:]
print(pred)
print(pred.shape)
np.savetxt('bilstm_feature3.txt', pred.detach().numpy())


