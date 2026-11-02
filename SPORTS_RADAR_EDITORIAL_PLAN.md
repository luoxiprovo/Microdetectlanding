# Millimeter-wave radar in sports: 52-week editorial plan

One edition consists of one Chinese and one English article, with one cover per language. Edition 1 was committed on November 1, 2026. Later editions follow the weekly automation; week numbers are editorial sequence numbers, not fixed dates.

The sports program takes priority. Existing industrial topics 20–36 remain deferred. The previous sports plan is retained in `archivedSportsRadarPrograms` in the progress JSON.

| Week | English title | 中文标题 |
| --- | --- | --- |
| 1 | What Is Millimeter-Wave Radar—and Why Does It Matter in Sports? | 什么是毫米波雷达？它为什么与体育有关？ |
| 2 | How Radar Measures Speed, Distance, and Movement | 雷达如何测量速度、距离与运动 |
| 3 | Radar vs. Cameras vs. Wearables: Which Measures What? | 雷达、摄像头与可穿戴设备分别能测什么？ |
| 4 | What Can Sports Radar Actually Detect? | 体育雷达到底能检测什么？ |
| 5 | Inside an FMCW Radar Sensor | 走进 FMCW 雷达传感器 |
| 6 | Understanding Radar Accuracy in Sports | 理解体育雷达的测量精度 |
| 7 | Why Sensor Placement Can Make or Break a Measurement | 为什么安装位置决定测量质量 |
| 8 | From Radar Signals to Coaching Feedback | 从雷达信号到教练反馈 |
| 9 | Measuring Sprint Speed with Radar | 用雷达测量短跑速度 |
| 10 | Can Radar Track Running Technique? | 雷达能分析跑步技术吗？ |
| 11 | Measuring Jumps: Height, Takeoff, and Landing | 测量跳跃：高度、起跳与落地 |
| 12 | Tracking Changes of Direction | 追踪变向运动 |
| 13 | Baseball Pitch Tracking: Where Radar Fits | 雷达如何参与棒球投球追踪 |
| 14 | Beyond Pitch Speed: Radar for Baseball Training | 不止球速：棒球训练中的雷达 |
| 15 | Golf Radar: Ball Flight and Club Movement | 高尔夫雷达：球飞行与球杆运动 |
| 16 | Building a Useful Golf Practice Setup | 搭建有效的高尔夫练习测量环境 |
| 17 | Tennis Serve Measurement with Radar | 用雷达测量网球发球 |
| 18 | Can Radar Analyze a Racket Swing? | 雷达能分析挥拍动作吗？ |
| 19 | Pickleball and Table Tennis: The Small-Ball Challenge | 匹克球与乒乓球的小球检测挑战 |
| 20 | Cricket Bowling and Batting Through Radar | 雷达视角下的板球投球与击球 |
| 21 | Soccer Shot Speed: Getting Reliable Measurements | 如何可靠测量足球射门速度 |
| 22 | Tracking Players on a Soccer Field | 追踪足球场上的运动员 |
| 23 | American Football: Measuring Throws and Player Movement | 美式橄榄球：传球与球员运动测量 |
| 24 | Basketball: Can Radar Measure Shots and Jumps? | 雷达能测量篮球投篮与跳跃吗？ |
| 25 | Volleyball: Measuring Serves, Spikes, and Approach Jumps | 排球：发球、扣球与助跑起跳测量 |
| 26 | Hockey: Tracking Fast Objects Near the Surface | 冰球：追踪近地高速目标 |
| 27 | Radar in Strength Training: Measuring Rep Velocity | 力量训练雷达：测量动作速度 |
| 28 | Can Radar Count Exercise Repetitions Reliably? | 雷达能可靠统计运动次数吗？ |
| 29 | Contactless Movement Assessment in Rehabilitation | 康复中的非接触运动评估 |
| 30 | Detecting Fatigue: What Radar Might Contribute | 雷达能为疲劳检测提供什么？ |
| 31 | Breathing and Heart Rate Around Exercise | 运动前后的呼吸与心率测量 |
| 32 | Can Radar Support Injury-Prevention Research? | 雷达能支持运动损伤预防研究吗？ |
| 33 | Micro-Doppler: The Signature Hidden in an Athlete’s Motion | 微多普勒：运动员动作中的信号特征 |
| 34 | Using Machine Learning to Recognize Sports Movements | 用机器学习识别体育动作 |
| 35 | Building a Sports Radar Dataset That Holds Up | 构建可靠的体育雷达数据集 |
| 36 | Testing AI Across Different Athletes and Venues | 跨运动员与场馆测试人工智能 |
| 37 | Tracking Multiple Athletes at Once | 同时追踪多名运动员 |
| 38 | Combining Radar and Cameras | 融合雷达与摄像头 |
| 39 | Combining Radar and Wearables | 融合雷达与可穿戴设备 |
| 40 | Edge AI for Sports Radar | 体育雷达的边缘人工智能 |
| 41 | Choosing a Radar Sensor for a Sports Prototype | 如何为体育原型选择雷达传感器 |
| 42 | Building Your First Radar Speed-Measurement Demo | 构建第一个雷达测速演示 |
| 43 | Designing a Radar-Based Jump Test | 设计雷达跳跃测试 |
| 44 | Indoor Radar Problems: Walls, Floors, and Reflections | 室内雷达问题：墙壁、地面与反射 |
| 45 | Outdoor Radar Testing: Weather and Field Conditions | 户外雷达测试：天气与场地条件 |
| 46 | How to Benchmark a Sports Radar Product | 如何评测体育雷达产品 |
| 47 | Privacy in Sports Tracking: Radar Still Needs Rules | 体育追踪隐私：雷达也需要规则 |
| 48 | Radar Regulations and Deployment Basics | 雷达法规与部署基础 |
| 49 | What Coaches Actually Need from Radar Data | 教练真正需要怎样的雷达数据 |
| 50 | The Business Case for Radar in Sports Facilities | 体育场馆雷达的商业价值 |
| 51 | From Prototype to Pilot: A Practical Deployment Playbook | 从原型到试点的部署指南 |
| 52 | Millimeter-Wave Radar in Sports: What We Learned and What Comes Next | 体育毫米波雷达年度回顾与展望 |

## Publishing procedure

1. Pull the latest main branch and read `content/insights/article-plan-progress.json`.
2. Select the lowest pending week in `activeProgram`; check for existing files to avoid duplicates.
3. Research primary sources. Distinguish demonstrated measurements, experimental results, and proposed applications. Do not present generic radar capability as a validated MicroDetect sports product.
4. Write a Chinese MDX file and an English `en-` counterpart in `content/insights/`. Export `meta` with title, description, coverImage, date, category, tags, and readingTime. Include practical examples, limitations, and linked sources.
5. Add language-specific PNG covers in `public/insights/`. Use accurate diagrams for measurement geometry; illustrative images must not imply experimental evidence.
6. Update completedFiles, topic status, updatedAt, completedEditions, and nextTopicId only after both language articles and covers exist.
7. Run `pnpm install --frozen-lockfile`, `pnpm exec tsc --noEmit`, and `pnpm build`. Inspect covers and output.
8. Commit and push articles, covers, and tracker together. Report the commit link. Repository publication does not by itself verify production deployment.
9. End after edition 52. Do not silently resume the industrial backlog.

## Editorial requirements

Each edition should answer a practical sports question, explain the measurement chain, identify relevant reference measurements and limitations, and link authoritative sources. Any performance number must be sourced or clearly labeled as a hypothetical calculation. Clinical claims require appropriate evidence. Research current regulations for the relevant jurisdiction when preparing week 48.

A concurrent November 1 commit added a separate introductory sports article under the previous plan. Its files remain published; its completion records are preserved in the archived program. It does not advance the new 52-week sequence.
