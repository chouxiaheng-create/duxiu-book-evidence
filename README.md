# duxiu-book-evidence

读秀公知常识书证检索 AI 技能包 —— 面向通用 Agent Skills 格式（WorkBuddy、Claude Code、Codex、DeepSeek Harness、Kimi Code 等均可直接读取）。

从读秀学术搜索（www.duxiu.com）检索并提取**教科书/工具书/技术手册**类书证，用于专利审查中公知常识的证据支撑。

## 核心能力

| 能力 | 说明 |
|---|---|
| **读秀访问** | 通过浏览器自动化（Playwright CLI + Chrome）访问读秀，支持机构 IP 认证 |
| **多层检索** | 精确短语 → 领域组合 → 宽泛检索，三级递进策略 |
| **书证提取** | 自动提取书名、作者、出版社、版次、页码、出版年月、段落原文 |
| **格式化输出** | 按专利审查公知常识证据格式输出，含相关性说明与检索关键词 |

## 目录结构

```
SKILL.md                          技能主文档（工作流、检索技巧、输出格式）
references/
  search_strategies.md            检索策略模式库（工艺参数/材料选型/设备路线/基础原理）
  output_template.md              输出格式模板（单条书证/多条汇总/审查文书引用格式）
scripts/
  extract_book_info.py            从读秀 URL 提取书目信息（页码、dxNumber 等）
```

## 快速开始

```bash
# 打开读秀（必须 --headed --browser=chrome）
npx playwright-cli open --headed --browser=chrome "https://www.duxiu.com/?lsu=ip"

# 搜索
npx playwright-cli open --headed --browser=chrome \
  "https://qw.duxiu.com/getPage?sw=<关键词>&ecode=utf-8&Field=all"

# 提取快照
npx playwright-cli snapshot --filename=results.yml
```

## 证据形式限定（刚性）

仅限审查指南规定的书籍类载体（教科书、工具书、技术手册等）。网页、期刊论文、专利文献**不得**作为公知常识证据，仅可作辅助说理线索。

## 许可

内部工具，不对外发布。
