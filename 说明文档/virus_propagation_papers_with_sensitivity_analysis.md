# 病毒传播仿真建模与参数敏感性分析相关论文

本文档收集了包含参数敏感性分析的病毒传播仿真建模和接触网络病毒传播相关论文。

## 重点推荐论文（含详细的参数敏感性分析）

### 1. Sensitivity analysis of epidemic forecasting and spreading on networks with probability generating functions
- **arXiv ID**: 2506.24103v1
- **发布日期**: 2025-06-30
- **作者**: Mariah C. Boudreau, William H. W. Thompson, Christopher M. Danforth, Jean-Gabriel Young, Laurent Hébert-Dufresne
- **摘要**: 本文使用概率生成函数（PGFs）进行流行病预测和传播建模，并详细介绍了参数敏感性分析方法。主要特点：
  - 使用统计条件估计（SCE - Statistical Condition Estimation）来量化敏感性
  - 分析了负二项分支过程和接触网络渗透模型
  - 发现在同质系统中（k > 0.3），敏感性在临界点R0=1处最大
  - 在异质系统中（k ≤ 0.3），敏感性在R0 > 1时达到最大值
- **URL**: http://arxiv.org/abs/2506.24103v1
- **参数敏感性分析方法**:
  - 使用概率生成函数（PGFs）建模传播过程
  - 通过扰动输入分布来评估敏感性
  - 计算统计条件估计κSCE来衡量输出对输入扰动的敏感性
  - 使用Morris方法（基本效应法）的变体

### 2. Inferring epidemic dynamics using Gaussian process emulation of agent-based simulations
- **arXiv ID**: 2307.12186v2
- **发布日期**: 2023-07-22
- **作者**: Abdulrahman A. Ahmed, M. Amin Rahimian, Mark S. Roberts
- **摘要**: 使用高斯过程模拟（Gaussian process emulation）来处理基于代理的流行病传播仿真模型，帮助决策者理解流行病动力学以优化公共卫生干预。该方法允许在相同人群中比较不同效果或研究干预措施的影响。
- **URL**: http://arxiv.org/abs/2307.12186v2
- **参数敏感性分析方法**: 
  - 使用代理模型（emulator）来替代计算密集的基于代理的仿真
  - 适用于复杂参数空间的敏感性分析

## 其他相关论文

### 3. Cooperative epidemic spreading on a two-layered interconnected network
- **arXiv ID**: 1702.03926v1
- **发布日期**: 2017-02-13
- **作者**: Xiang Wei, Xiaoqun Wu, Shihua Chen, Jun-an Lu, Guanrong Chen
- **摘要**: 研究双层互连网络上的合作流行病传播动力学行为。提出了三个不同层次的模型来描述互连网络上的合作传播过程。
- **URL**: http://arxiv.org/abs/1702.03926v1

### 4. Epidemic Spreading on Weighted Complex Networks
- **arXiv ID**: 1308.4014v2
- **发布日期**: 2013-08-19
- **作者**: Ye Sun, Chuang Liu, Chu-Xu Zhang, Zi-Ke Zhang
- **摘要**: 考虑边权重来表示多角色关系，并详细分析了两种现实场景。
- **URL**: http://arxiv.org/abs/1308.4014v2

### 5. Mathematical models for epidemic spreading on complex networks
- **arXiv ID**: 1307.5503v1
- **发布日期**: 2013-07-21
- **作者**: Wojciech Ganczarek
- **摘要**: 提出了在有限复杂网络上进行流行病传播的模型，限制每个时间步最多一次污染。由于过程的高度离散特性，分析不能使用连续近似。
- **URL**: http://arxiv.org/abs/1307.5503v1

### 6. Virus Propagation in Multiple Profile Networks
- **arXiv ID**: 1504.03306v1
- **发布日期**: 2015-04-13
- **作者**: Angeliki Rapti, Kostas Tsichlas, Spiros Sioutas, Giannis Tzimas
- **摘要**: 研究病毒或竞争性想法/产品在多配置文件（如社交）网络上的传播。可以预测网络中有多大比例会实际被"感染"。
- **URL**: http://arxiv.org/abs/1504.03306v1

### 7. The robustness of interdependent networks under the interplay between cascading failures and virus propagation
- **arXiv ID**: 1608.01037v1
- **发布日期**: 2016-08-03
- **作者**: Dawei Zhao, Zhen Wang, Gaoxi Xiao, Bo Gao, Lianhai Wang
- **摘要**: 研究互依赖网络上的级联故障和流行病动力学的耦合过程，以及它们如何相互影响。
- **URL**: http://arxiv.org/abs/1608.01037v1

### 8. Contact Adaption during Epidemics: A Multilayer Network Formulation Approach
- **arXiv ID**: 1809.06060v1
- **发布日期**: 2018-09-17
- **作者**: Faryad Darabi Sahneh, Aram Vajdi, Joshua Melander, Caterina M. Scoglio
- **摘要**: 提出一个模型，其中每个代理都有一个默认的接触邻居集合，当流行病传播时，代理会根据感知风险动态改变其接触。该模型考虑了疾病传播和接触适应过程的耦合动力学。
- **URL**: http://arxiv.org/abs/1809.06060v1

### 9. Agent-Based Modelling: An Overview with Application to Disease Dynamics
- **arXiv ID**: 2007.04192v1
- **发布日期**: 2020-07-08
- **作者**: Affan Shoukat, Seyed M. Moghadas
- **摘要**: 基于代理的建模综述及其在疾病动力学中的应用。
- **URL**: http://arxiv.org/abs/2007.04192v1

## 参数敏感性分析方法总结

### 方法1: 统计条件估计（Statistical Condition Estimation, SCE）
- **应用论文**: 2506.24103v1
- **核心思想**: 
  - 通过随机扰动输入参数分布
  - 计算输出变化的归一化度量
  - 使用正交采样来减少方差
  - 计算统计条件数κSCE
- **算法步骤**:
  1. 随机扰动输入概率分布p到p̃
  2. 计算相应的输出（如灭绝概率）
  3. 计算归一化的输出变化
  4. 重复多次并计算平均值

### 方法2: 高斯过程模拟（Gaussian Process Emulation）
- **应用论文**: 2307.12186v2
- **核心思想**: 
  - 使用高斯过程作为代理模型替代计算密集的仿真
  - 在参数空间中更高效地进行敏感性分析

### 方法3: Morris方法（基本效应法）
- **在论文2506.24103v1中提到**
- **核心思想**: 
  - 一种全局敏感性分析方法
  - 通过改变一个参数并固定其他参数来评估基本效应

## 研究方向建议

1. **重点关注论文1**（2506.24103v1），它提供了最详细的参数敏感性分析方法
2. 研究统计条件估计（SCE）方法在病毒传播建模中的应用
3. 比较同质系统和异质系统中的敏感性模式
4. 考虑如何将SCE方法应用到自己的研究中

## 参考文献

- Saltelli et al. (2008) - Global sensitivity analysis: The primer
- Morris (1991) - Factorial sampling plans for preliminary computational experiments  
- Kenney and Laub (1994) - Small-sample statistical condition estimates
- Laub and Xia (2008) - Statistical condition estimation for the roots of polynomials
