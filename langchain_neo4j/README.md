# 使用圖形資料庫與向量資料庫查詢電影資料

本專案示範如何使用 LangChain 與 Neo4j 建立電影知識圖譜與向量查詢系統，並透過 Agent 整合兩種查詢工具回應使用者問題。

## 模組一覽

| 檔案 | 說明 |
|------|------|
| `config.py` | 載入 API 金鑰與模型初始化 |
| `graph_setup.py` | 連接並匯入 Neo4j 圖形資料庫 |
| `vector_setup.py` | 建立評論向量資料庫 |
| `qa_chain.py` | 建立問答鏈與查詢鏈 |
| `tools.py` | LangChain 工具封裝 |
| `agent_runner.py` | 整合工具與互動代理 |
| `main.py` | 啟動 CLI 互動模式 |

## 啟動方式

1. 建立 `.env` 檔，輸入金鑰：
```
OPENAI_API_KEY=your_openai_key
NEO4J_URI=your_neo4j_uri
NEO4J_PASSWORD=your_password
```

2. 執行主程式：
```bash
python main.py
```

## QA範本:
1. 請問陳玉勳的導了哪些電影?
2. 總舖師的演員有哪些人?
3. 總舖師的影評幾分?
4. 全面啟動的影評幾分?

