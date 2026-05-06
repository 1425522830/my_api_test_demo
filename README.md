# 接口自动化测试框架（Python + Pytest + Allure）

## 项目简介

本项目是一个基于 **Python + Pytest + Requests + Allure** 构建的接口自动化测试框架，针对 DummyJSON 提供的开放 API 进行测试。实现了**登录鉴权（Token）**、**接口依赖**、**数据驱动**、**Allure 报告**、**失败重试**等测试框架的核心功能。

通过这个项目，你可以：
- 学习如何从零搭建一个完整的接口自动化测试框架
- 掌握 pytest 的使用、fixture 共享、参数化测试
- 理解 Token 鉴权与接口关联的处理方式
- 生成美观的 Allure 测试报告，并集成到 CI 环境

技术栈
| 工具/库 | 用途 |
| ------- | ---- |
| Python 3.13 | 编程语言 |
| Requests | 发送 HTTP 请求 |
| Pytest | 测试框架，管理用例、断言 |
| Allure | 生成可视化测试报告 |
| PyYAML | 读取 YAML 格式的测试数据 |
| Tenacity | 实现请求重试机制 |
| Git | 版本控制 |
