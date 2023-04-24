本仓库存储本人的本科毕业设计相关的文档、代码和开发日志。

# 开发日程

# 基于geth1的出租车调度系统复现

# 英文文献翻译工作

# 树状区块链跨链转账测试

# 讨论纪要

## 2023-04-??的讨论

1. 最终的版图：将区块链作为一个系统服务，能够像调用CreateProcess那样的API供用户使用
2. 作为系统服务的难度仍然很大，那么作为平替，让区块链作为一个可以在浏览器中能运行的服务，只要有浏览器就能运行，也是一个很好的设想
3. 在浏览器中运行的虚拟机就是WASM，也就是说，我们应该尝试将现有的、基于EVM的区块链应用给迁移到WASM上，这要求我们不使用Solidity，而是使用像Rust这样能够编译为WASM支持的高级语言来写合约
4. 至此，引出本科毕设的自主研究内容，使用支持编译为WASM可运行的区块链平台（例如Substrate），用可编译为WASM的高级语言翻译现有合约（不必要求全翻译完）
5. 参考资料如下：
   - [WebAssembly 概念 - WebAssembly | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/WebAssembly/Concepts)
   - [一文读懂 WebAssembly （WASM）智能合约_Rust (sohu.com)](https://www.sohu.com/a/462896257_100217347)
   - [了解区块链虚拟机：EVM、HVM、WASM、MOVE - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/596991126)
   - [Ethereum WebAssembly (ewasm) - Ethereum WebAssembly](https://ewasm.readthedocs.io/en/mkdocs/)
   - [以太坊2.0-Ewasm | 登链社区 | 区块链技术社区 (learnblockchain.cn)](https://learnblockchain.cn/article/716)

## 2023-04-24的讨论

1. 把修改区块链底层，为交易引入“地理位置”的新属性；这项工作在现在做不现实，跨度太大
2. Substrate链和链外应用有暴露接口，可以从这个方面入手，研究链外的请求是如何一步步地被送入区块链的
   - 可以参考[Offchain HTTP Requests](https://docs.substrate.io/reference/how-to-guides/offchain-workers/offchain-http-requests/)和[PolkaDot{.js}](https://polkadot.js.org/)
3. 接下来可以翻译Substrate文档的Tutorials部分，先从get-started开始翻译，后续可以部署成网站
