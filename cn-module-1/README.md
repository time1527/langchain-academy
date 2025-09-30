# 课程内容

## 课程 1：动机

LangChain Academy - LangGraph 简介 - Motivation.pdf  

### LangGraph 常见问题

**我需要使用 LangChain 才能使用 LangGraph 吗？有什么区别？**  
不需要。LangGraph 是一个用于复杂智能体系统的编排框架，比 LangChain 的 agent 更底层、可控性更强。另一方面，LangChain 提供了与模型和其他组件交互的标准接口，适合用于直接的链式调用和检索流程。  

**LangGraph 与其他智能体框架有何不同？**  
其他智能体框架适合处理简单的通用任务，但在应对企业独有的复杂任务时会显得不足。LangGraph 提供了一个更具表达力的框架，能够处理企业的独特需求，而不会把用户限制在单一的黑盒认知架构中。  

**LangGraph 会影响我应用的性能吗？**  
不会。LangGraph 不会给你的代码增加任何额外开销，并且它的设计初衷就是针对流式工作流。  

**LangGraph 是开源的吗？免费吗？**  
是的。LangGraph 是一个基于 MIT 许可证的开源库，可以免费使用。  

**LangGraph Platform 是开源的吗？**  
不是。LangGraph Platform 是专有软件，将来会针对某些使用层级提供付费服务。我们会在开始收费前提前通知，并为早期用户提供优惠价格。  

**我该如何启用 LangGraph Platform？**  
目前，LangGraph Platform 处于测试阶段。在测试期间，所有使用 Plus 和 Enterprise 套餐的 LangSmith 用户都可以访问 LangGraph Platform。详情请参考文档。  

**LangGraph 和 LangGraph Platform 有什么不同？**  
LangGraph 是一个有状态的编排框架，能为智能体工作流带来更多控制。LangGraph Platform 是一个用于部署和扩展 LangGraph 应用的服务，内置了 Studio，方便进行原型设计、调试和分享 LangGraph 应用。如果你想了解更多，可以查看本页底部 FAQ 中的对比表。  

**LangGraph 在 LangChain 生态系统中处于什么位置？**  
我们的目标是简化 LLM 应用生命周期中的每个阶段：  
- **开发**：使用 LangChain 的开源组件和第三方集成来构建应用；使用 LangGraph 构建支持一流流式处理和人类参与的有状态智能体。  
- **生产**：使用 LangSmith 检查、监控和评估你的链，从而持续优化并自信地部署。  
- **部署**：使用 LangGraph Platform 将你的 LangGraph 应用转化为生产可用的 API 和智能助手。  

---

## 课程 2：简单图

- Notebook 参考：`simple-graph.ipynb`   

---

## 课程 3：LangGraph Studio

- [LangGraph Studio](https://studio.langchain.com/?_gl=1*1m3wzex*_gcl_au*MjA2MDUwOTUyLjE3NTY0OTAwODY.*_ga*MTM4MDA5OTA4NC4xNzU2NDkwMDg3*_ga_47WX3HKKY2*czE3NTY4MTcxNDAkbzMkZzEkdDE3NTY4MTkyNzAkajYwJGwwJGgw)  
- GitHub: [LangGraph Studio](https://github.com/langchain-ai/langgraph-studio)

```
langgraph dev
```
---

## 课程 4：链

- Notebook 参考：`chain.ipynb`   

---

## 课程 5：路由器

- Notebook 参考：`router.ipynb`    

---

## 课程 6：智能体

- Notebook 参考：`agent.ipynb`  

---

## 课程 7：带记忆的智能体

- Notebook 参考：`agent-memory.ipynb`  

---

## （可选）课程 8：部署

目前，LangGraph Platform 仅对 LangSmith Plus 套餐用户开放。本课程中的第 8 课为可选内容。  

- Notebook 参考：`deployment.ipynb`  

