学习笔记
1.代码方面，回溯算法的框架：
        result = []
        def backtrack(路径, 选择列表):
            if 满足结束条件:
                result.add(路径)
            return

        for 选择 in 选择列表:
            做选择
            backtrack(路径, 选择列表)
            撤销选择    
2.本周内容较前两周的难度上升不少，看题解理解和做题花很多时间，多看多背多写 多理解视频题解