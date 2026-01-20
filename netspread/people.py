'''
定义 People 类以及与人相关的函数，处理状态之间的转换（例如，从易感者到感染者）。
'''

#%% 导入
import numpy as np
# from collections import defaultdict
# 根据需要添加其他导入


__all__ = ['People']


class People:
    '''
    用于执行所有人群操作的类——通常不直接调用。

    此类通常由 sim 自动创建。唯一必需的输入参数是人口规模，但通常会传递完整的参数字典，
    因为在 People 对象初始化之前就需要这些参数。但是，年龄、接触等需要单独创建——
    请参见 ``make_people()``。

    注意：此类处理实际人群更新的机制。
    请参见基类以获取其他方法。

    参数:
        pars (dict): 模拟参数，例如 sim.pars——或者，如果是数字，则解释为 pop_size
        strict (bool): 是否只创建已存在于 self.meta.person 中的键；否则允许设置任何键
        kwargs (dict): 实际数据，例如来自 popdict 的数据

    **示例**::

        ppl1 = People(2000)

        sim = Sim()
        ppl2 = People(sim.pars)
    '''

    def __init__(self, pars, strict=True, **kwargs):
        '''
        初始化 People 对象。
        
        参数:
            pars (dict): 模拟参数
            strict (bool): 是否强制执行严格的键检查
            kwargs (dict): 其他关键字参数
        '''
        pass


    def init_flows(self):
        '''
        将流（flows）初始化为零。
        '''
        pass


    def initialize(self, sim_pars=None):
        '''
        执行初始化。
        
        参数:
            sim_pars (dict): 模拟参数
        '''
        pass


    def set_prognoses(self):
        '''
        在初始化期间根据年龄为每个人设置预后。
        需要重置随机种子，因为病毒载量是随机抽取的。
        '''
        pass


    def update_states_pre(self, t):
        '''
        在当前时间步执行所有状态更新。
        
        参数:
            t (int): 当前时间步
        '''
        pass


    def update_states_post(self):
        '''
        执行时间步后的更新。
        '''
        pass


    def update_contacts(self):
        '''
        刷新动态接触，例如社区接触。
        
        返回:
            contacts: 更新后的接触字典
        '''
        pass


    #%% 状态更新方法

    def check_inds(self, current, date, filter_inds=None):
        '''
        返回当前状态为 false 且满足日期条件的索引。
        
        参数:
            current (array): 当前状态数组
            date (array): 日期数组
            filter_inds (array): 可选的过滤索引
            
        返回:
            inds (array): 满足条件的索引
        '''
        pass


    def check_infectious(self):
        '''
        检查他们是否变为传染性。
        
        返回:
            inds (array): 变为传染性的人的索引
        '''
        pass


    def check_symptomatic(self):
        '''
        检查是否有新的进展为有症状。
        
        返回:
            inds (array): 变为有症状的人的索引
        '''
        pass


    def check_severe(self):
        '''
        检查是否有新的进展为重症。
        
        返回:
            inds (array): 变为重症的人的索引
        '''
        pass


    def check_critical(self):
        '''
        检查是否有新的进展为危重症。
        
        返回:
            inds (array): 变为危重症的人的索引
        '''
        pass


    def check_recovery(self, inds=None, filter_inds='is_exp'):
        '''
        检查是否恢复。
        
        比其他函数更复杂，允许为指定的索引集手动设置恢复。
        
        参数:
            inds (array): 要检查的可选特定索引
            filter_inds (str/array): 用于检查的索引过滤器
            
        返回:
            inds (array): 恢复的人的索引
        '''
        pass


    def check_death(self):
        '''
        检查此人是否在此时间步死亡。
        
        返回:
            inds (array): 死亡的人的索引
            new_deaths (int): 新死亡人数
            new_known_deaths (int): 新已知死亡人数
        '''
        pass


    def check_diagnosed(self):
        '''
        检查新的诊断。由于大多数数据是在检测日期报告诊断的，此函数报告的计数不是
        一天内收到阳性检测结果的人数，而是在该天接受检测并计划在未来被诊断的人数。
        
        返回:
            test_pos_inds (array): 检测呈阳性的人的索引
        '''
        pass


    def check_quar(self):
        '''
        更新隔离状态。
        
        返回:
            n_quarantined (int): 进入隔离的人数
        '''
        pass


    def check_enter_iso(self):
        '''
        检查进入隔离的人。
        
        返回:
            iso_inds (array): 进入隔离的人的索引
        '''
        pass


    def check_exit_iso(self):
        '''
        结束任何人的隔离。
        
        返回:
            end_inds (array): 退出隔离的人的索引
        '''
        pass


    #%% 使事件发生的方法（感染和诊断）

    def make_naive(self, inds, reset_vx=False):
        '''
        使一组人变为易感状态。这在动态重采样期间使用。
        
        参数:
            inds (array): 要变为易感状态的人的列表
            reset_vx (bool): 是否重置疫苗衍生的免疫力
        '''
        pass


    def make_nonnaive(self, inds, set_recovered=False, date_recovered=0):
        '''
        使一组人变为非易感状态。
        
        可以通过仅设置易感和易感状态来完成，或者通过将他们设置为已感染并恢复来完成。
        
        参数:
            inds (array): 要变为非易感状态的人的索引
            set_recovered (bool): 是否将他们设置为已恢复
            date_recovered (int): 如果 set_recovered 为 True，则为恢复日期
        '''
        pass


    def infect(self, inds, hosp_max=None, icu_max=None, source=None, layer=None, variant=0):
        '''
        感染人群并确定他们的最终结果。
        
        每个被感染的人都可以感染其他人，无论他们是否出现症状。
        出现症状的感染者被分为轻度、重症（=需要住院）和危重症（=需要ICU）。
        每个无症状、轻度有症状和重度有症状的人都会恢复。
        危重症病例要么恢复，要么死亡。
        
        该方法还会对输入数组进行去重，以防一个代理被多次感染，
        并将谁感染了谁存储在 infection_log 列表中。
        
        参数:
            inds (array): 要感染的人的数组
            hosp_max (bool): 是否有急性病床可供此人使用
            icu_max (bool): 是否有 ICU 病床可供此人使用
            source (array): 传播此感染的人的源索引（如果是输入或种子感染则为 None）
            layer (str): 传播此感染的接触层
            variant (int): 人们正在感染的变体
            
        返回:
            inds (array): 被感染的人的数组
        '''
        pass


    def test(self, inds, test_sensitivity=1.0, loss_prob=0.0, test_delay=0):
        '''
        检测人群的方法。通常不直接由用户调用；
        请参见 test_num() 和 test_prob() 干预措施。
        
        参数:
            inds (array): 要检测的人的索引
            test_sensitivity (float): 真阳性的概率
            loss_prob (float): 失访的概率
            test_delay (int): 检测结果准备就绪前的天数
            
        返回:
            final_inds (array): 检测呈阳性并将被诊断的人的索引
        '''
        pass


    def schedule_quarantine(self, inds, start_date=None, period=None):
        '''
        安排隔离。通常不直接由用户调用，除非通过自定义干预；
        请参见 contact_tracing() 干预。
        
        此函数将在 start_date 创建一个隔离请求，持续一段时间。
        他们是否处于现有隔离中（将被延长），或者他们是否不再有资格隔离，
        将在到达 start_date 时进行检查。
        
        参数:
            inds (array): 要隔离的人的索引
            start_date (int): 开始隔离的日期（默认为当前日期，`sim.t`）
            period (int): 隔离持续时间（默认为 ``pars['quar_period']``）
        '''
        pass


    #%% 分析方法

    def plot(self, *args, **kwargs):
        '''
        绘制人群统计信息——年龄分布、接触数量和接触的总权重
        （每个层的接触数量乘以 beta）。
        
        参数:
            bins (arr): 要使用的年龄区间（默认，0-100 一年一个区间）
            width (float): 条形宽度
            font_size (float): 字体大小
            alpha (float): 图表的透明度
            fig_args (dict): 传递给 pl.figure()
            axis_args (dict): 传递给 pl.subplots_adjust()
            plot_args (dict): 传递给 pl.plot()
            do_show (bool): 是否显示图表
            fig (fig): 要绘制到的现有图形句柄
            
        返回:
            fig: 图形句柄
        '''
        pass


    def story(self, uid, *args):
        '''
        打印指定个体的简短事件历史。
        
        参数:
            uid (int/list): 要讲述故事的人或人群
            args (list): 这些人也会讲述他们的故事
        '''
        pass
