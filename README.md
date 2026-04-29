# FloraGenius_Agent
# FloraGenius 自动化代码包

这是一套针对观赏植物高通量 3D 表型解析的独立代码。可以完美对接下游的遗传分析管道。

## 内容目录
1. `phenotype_engine.py`: 核心算法引擎。已内置动态缩放因子计算逻辑，并严格锁死了输出参数的浮点数精度，不破坏任何原始文件名。器官划分逻辑已精简，直接提取整体叶面积。
2. `agent_pipeline.py`: 批处理启动脚本。
3. `data_sync.sh`: 辅助脚本。用于将本地系统重建完毕的批量数据快速 rsync 传输至 Linux 服务器进行后续计算。

## 运行说明
如果你正在处理这 200 份种质的抗旱分析数据，可以将点云文件统一放入当前目录的 `data` 文件夹下，然后执行：
```bash
python agent_pipeline.py
```
生成的 CSV 可以直接作为表型数据（Phenotype）送入 GAPIT 等流程中运行多位点模型。
