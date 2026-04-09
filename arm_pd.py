import numpy as np

class ArmPDController:
    """
    基础 PD 控制器，作为算法对比的 Baseline。
    负责将腰部和双臂的关节固定在指定的目标角度。
    """
    def __init__(self, kps, kds):
        """
        初始化控制器
        :param kps: 比例增益数组 (长度 11)
        :param kds: 微分增益数组 (长度 11)
        """
        self.kps = np.array(kps, dtype=np.float32)
        self.kds = np.array(kds, dtype=np.float32)
        
    def compute_tau(self, q, dq, target_q, target_dq=None):
        """
        计算控制力矩
        :param q: 当前关节角度 (长度 11)
        :param dq: 当前关节角速度 (长度 11)
        :param target_q: 期望关节角度 (长度 11)
        :param target_dq: 期望关节角速度 (可选，默认为 0)
        :return: 期望关节力矩 tau (长度 11)
        """
        if target_dq is None:
            target_dq = np.zeros_like(self.kds)
            
        # 标准的 PD 控制律：tau = Kp * (q_des - q) + Kd * (dq_des - dq)
        tau = (target_q - q) * self.kps + (target_dq - dq) * self.kds
        return tau