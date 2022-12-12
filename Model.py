import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import utils as nn_utils

class Bottleneck(nn.Module):#密集连接块的实现过程

    def __init__(self, in_planes, growth_rate):
        super(Bottleneck, self).__init__()
        self.bn1 = nn.BatchNorm2d(in_planes) #数据归一化处理
        self.conv1 = nn.Conv2d(in_planes, 4 * growth_rate, kernel_size=1, bias=False)# 1*1卷积
        self.bn2 = nn.BatchNorm2d(4 * growth_rate)
        self.conv2 = nn.Conv2d(4 * growth_rate, growth_rate, kernel_size=3, padding=1, bias=False) # 3*3卷积

    def forward(self, x):
        out = self.conv1(F.relu(self.bn1(x))) #数据归一化后放入 1*1 卷积
        out = self.conv2(F.relu(self.bn2(out))) # 数据归一化后放入 3*3 卷积
        out = torch.cat([out, x], 1)# 将每一步的处理连接起来
        return out

class Transition(nn.Module): #过渡层，包括一个卷积和一个池化

    def __init__(self, in_planes, out_planes):
        super(Transition, self).__init__()
        self.bn = nn.BatchNorm2d(in_planes)
        self.conv = nn.Conv2d(in_planes, out_planes, kernel_size=1, bias=False)

    def forward(self, x):
        out = self.conv(F.relu(self.bn(x)))
        out = F.avg_pool2d(out, 2)
        return out

class DenseNet(nn.Module): #ncDENSE的实现过程

    def __init__(self, block, nblocks, growth_rate=32, reduction=0.5, num_classes=13):
        super(DenseNet, self).__init__()
        self.BiGRU_profile = nn.GRU(input_size=8, hidden_size=512, num_layers=1, bidirectional=True) #一层的双向GRU，由pytorch包实现，包括了512个隐藏层
        self.growth_rate = growth_rate
        num_planes = 2 * growth_rate
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=num_planes, kernel_size=3, padding=1, bias=False) #
        self.dense1 = self._make_dense_layers(block, num_planes, nblocks[0]) #dense1层实现调用_make_dense_layers
        num_planes += nblocks[0] * growth_rate
        out_planes = int(math.floor(num_planes * reduction))
        self.trans1 = Transition(num_planes, out_planes)#trans1层实现调用Transition
        num_planes = out_planes
        self.dense2 = self._make_dense_layers(block, num_planes, nblocks[1]) #dense2层实现调用_make_dense_layers
        num_planes += nblocks[1] * growth_rate
        out_planes = int(math.floor(num_planes * reduction))
        self.trans2 = Transition(num_planes, out_planes)#trans2层实现调用Transition
        num_planes = out_planes
        self.dense3 = self._make_dense_layers(block, num_planes, nblocks[2])#dense3层实现调用_make_dense_layers
        num_planes += nblocks[2] * growth_rate
        out_planes = int(math.floor(num_planes * reduction))
        self.trans3 = Transition(num_planes, out_planes)#trans3层实现调用Transition
        num_planes = out_planes
        self.dense4 = self._make_dense_layers(block, num_planes, nblocks[3])#dense4层实现调用_make_dense_layers
        num_planes += nblocks[3] * growth_rate
        self.bn = nn.BatchNorm2d(num_planes)
        self.linear = nn.Linear(num_planes, num_classes)

    def _make_dense_layers(self, block, in_planes, nblock): #实现密集连接层
        layers = []
        for i in range(nblock): #设置密集连接块里有多少部分
            layers.append(block(in_planes, self.growth_rate)) #调用上面的Bottleneck实现
            in_planes += self.growth_rate
        return nn.Sequential(*layers)

    def attention_net(self, BiGRU_output, final_state):
        batch_size = len(BiGRU_output) #计算每一个批次的大小
        hidden = final_state.view(batch_size, -1, 1)  # hidden : [batch_size, n_hidden * num_directions(=2), n_layer(=1)]
        attn_weights = torch.bmm(BiGRU_output, hidden).squeeze(2)  # attn_weights : [batch_size, n_step] 计算权重
        soft_attn_weights = F.softmax(attn_weights, 1) #权重列向量归一化处理
        context = torch.bmm(BiGRU_output.transpose(1, 2), soft_attn_weights.unsqueeze(2)).squeeze(2)# 将权重和BiGRU的输出结果相乘之后加权求和
        return context, soft_attn_weights

    def forward(self, x):
        outputs, h_2 = self.BiGRU_profile(x)#outputs为BiGRU的输出结果
        outputs = nn_utils.rnn.pad_packed_sequence(outputs, batch_first=True)#重新填充BiGRU的输出结果
        output = outputs[0]#重新填充后的数据
        length = outputs[1].numpy()#rna序列的原始长度，不算填充的
        out = output[:, -1, :]#reshape一下为了输入到AM中
        out_Put = output[:, 0:200, :]#AM的step设置为200
        for number in range(len(length)):
            out[number] = output[number][length[number] - 1]#给reshape后的out赋值
        attn_output, attention = self.attention_net(out_Put, out)#attn——output为注意力机制输出的结果
        out = attn_output.reshape(-1, 1, 32, 32)#reshape为可以输入到卷积网络的维度
        out = self.conv1(out)# 将结果放进3*3卷积中
        out = self.dense1(out)# 经过dense1
        out = self.trans1(out)# 经过trans1
        out = self.dense2(out)# 经过dense2
        out = self.trans2(out)# 经过trans2
        out = self.dense3(out)# 经过dense3
        out = self.trans3(out)# 经过trans3
        out = self.dense4(out)# 经过dense4
        out = F.avg_pool2d(F.relu(self.bn(out)), 4)# 经过4*4的池化层
        out = out.view(out.size(0), -1)# 将所有数据整合到一起
        out = self.linear(out) # 全联接层分类
        return out


def densenet():
    return DenseNet(Bottleneck, [4, 4, 4, 4])


