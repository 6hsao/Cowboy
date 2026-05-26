# 西部牛仔 (Cowboy)

Unity 3D 潜行射击游戏

## 项目简介

一款以西部荒野为背景的潜行射击游戏，玩家需要在敌人之间穿梭，利用掩体和AI行为机制完成任务。

## 技术栈

- **引擎**: Unity 2022.3 LTS
- **语言**: C#
- **导航系统**: Unity AI Navigation 1.1.6
- **协作**: Unity Collab Proxy 2.7.1

## 项目结构

```
Assets/
├── Prefabs/               # 预制体资源
│   ├── GameManager.prefab # 游戏管理器
│   ├── Player.prefab      # 玩家角色
│   └── Logo.png           # 游戏图标
├── Scenes/                # 场景文件
│   └── MainLevel.unity    # 主关卡
├── Scripts/                # 脚本文件
│   ├── AI Behaviours/      # AI行为系统
│   ├── Characters General/ # 角色通用系统
│   ├── Utilities/          # 工具类
│   └── LevelManager.cs     # 关卡管理
```

## 核心系统

### AI 行为系统 (AI Behaviours)

| 文件 | 功能 |
|------|------|
| `EnemyAI.cs` | 敌人AI主控制器 |
| `AlertBehaviorMain.cs` | 警戒行为 |
| `ChaseBehavior.cs` | 追逐行为 |
| `AttackBehavior.cs` | 攻击行为 |
| `SearchBehavior.cs` | 搜索行为 |
| `RetreatBehavior.cs` | 撤退行为 |
| `AlliesBehavior.cs` | 友军行为 |
| `CommonBehavior.cs` | 通用行为 |
| `PointsOfInterestBehavior.cs` | 兴趣点行为 |

### 角色系统 (Characters General)

| 文件 | 功能 |
|------|------|
| `CharacterStats.cs` | 角色属性数据 |
| `PlayerControl.cs` | 玩家控制 |
| `GameManager.cs` | 游戏管理器 |
| `EnemiesManager.cs` | 敌人管理器 |
| `EnemySightSphere.cs` | 敌人视野范围 |
| `HidingSpot.cs` | 掩体位置 |
| `CoverPositions.cs` | 掩体系统 |
| `PointOfInterest.cs` | 兴趣点基类 |
| `POI_Base.cs` | 兴趣点基础 |
| `POI_Deadbody.cs` | 尸体兴趣点 |

### 工具类 (Utilities)

| 文件 | 功能 |
|------|------|
| `EnemyUI.cs` | 敌人UI显示 |
| `ChangeBoolValue.cs` | 布尔值切换 |
| `ActivateDeactivateRenderers.cs` | 渲染器开关 |



## 版本信息

- 当前版本: 0.2
- 初始提交版本: 0.1
