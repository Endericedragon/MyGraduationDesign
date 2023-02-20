# 快速开始指南

所有Substrate教程都是引导您在自己的开发环境中搭建并运行一个Substrate节点的操作教程。为了让您能够快速地设置好开发环境，[Substrate开发中心](https://github.com/substrate-developer-hub/)维护了数份模板任君选择。例如，开发中心提供的[Substrate节点模板](https://github.com/substrate-developer-hub/substrate-node-template/tags/)即是一份Substrate节点模板主程序的快照，它提供了一个可以工作的节点和一系列核心功能，足够您快速上手开发之用了。

这份快速开始指南假定您是第一次搭建开发环境，以试图在本地运行一个单链区块链的节点。为使过程尽可能简单，您将通过网络浏览器连接到您的本地节点，并在一个给定的样本账户库中查询账户余额。

## 开始之前

在您开始之前，请依次执行下列检查：

- 确认拥有互联网连接，并在本地计算机上准备一个交互式终端
- 您对于软件开发和命令行交互界面较为熟悉
- 本地计算机上已经安装Rust编译器和工具链

为检查Rust是否安装，您可以在终端中运行`rustup show`指令。若Rust已经安装，您将看到关于编译器和工具链的版本信息；否则，该指令将不会有任何回显。有关安装Rust的事宜，请参见[安装](https://docs.substrate.io/install/)。

## 构建节点模板

1. 将节点模板的仓库通过下列指令克隆到本地：

    ```bash
    git clone https://github.com/substrate-developer-hub/substrate-node-template
    ```
    在绝大多数情况下，您只需克隆`main`分支即可获得最新的代码。不过，您也可以使用`--branch`选项选择特定分支以搭配特定版本的Polkadot使用。关于不同分支和不同版本的Polkadot的适配情况，请参阅[Tags](https://github.com/substrate-developer-hub/substrate-node-template/tags)。

2. 在终端中，切换工作目录到克隆下来的仓库文件夹中：

    ```bash
    cd substrate-node-template
    ```
    若您想让自己的分支更有辨识度，或是更易于保存属于您自己的修改，您可以使用形如下列指令来创建一个新的分支：
    ```bash
    git switch -c my-branch-v0.9.29
    ```
3. 编译节点模板：
    ```bash
    cargo build --package node-template --release
    ```
    由于所用的软件包数量较多，编译可能花费长达数分钟才能完成。

## 启动节点

1. 运行下列指令，确认您的节点已经就绪，并查看可用的命令行选项：
    ```bash
    ./target/release/node-template --help
    ```

    通过上述命令获得的信息，我们可以知晓用于下列目的的命令行选项：
    - 启动节点
    - 处理账户
    - 修改节点操作

2. 运行下列指令，查看预定义的开发账号`Alice`的信息：

    ```bash
    ./target/release/node-template key inspect //Alice
    ```

    该指令将显示如下信息：

    ```
    Secret Key URI `//Alice` is account:
    Network ID:        substrate 
    Secret seed:       0xe5be9a5092b81bca64be81d212e7f2f9eba183bb7a90954f7b76361f6edb5c0a
    Public key (hex):  0xd43593c715fdd31c61141abd04a99fd6822c8558854ccde39a5684e7a56da27d
    Account ID:        0xd43593c715fdd31c61141abd04a99fd6822c8558854ccde39a5684e7a56da27d
    Public key (SS58): 5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY
    SS58 Address:      5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY
    ```

    

3. 通过下列指令，您可以以开发模式启动节点：

    ```bash
    ./target/release/node-template --dev
    ```

    在该模式下，该区块链不需要任何对等计算机以封装区块。节点启动后，终端将显示其所执行的操作的输出信息。若您看到形如“区块正在被提交/封装”，则说明您的节点已经开始正常运行：

    ```
    ... Idle (0 peers), best: #3 (0xcc78…5cb1), finalized #1 ...
    ... Starting consensus session on top of parent ...
    ... Prepared block for proposing at 4 (0 ms) ...
    ```

## 连接到节点

1.   创建一个内含JavaScript以及[Polkadot-JS API]([Overview | polkadot{.js}](https://polkadot.js.org/docs/))的HTML文件，以和节点互动。

     在本例中，我们将创建一个名为`index.html`的文件，其内含的JavaScript以及HTML代码将可以：

     -   选择一个账号作为输入
     -   使用`onClick`事件来查阅账号信息
     -   作为以上两步骤的输出，显示该账号的余额信息

     这份[示例index.html]([Quick start: Get Balance (substrate.io)](https://docs.substrate.io/assets/quickstart/))提供了使用JS、Polkadot-JS API和HTML进行以上步骤的简单演示。

2.   复制粘贴[上述示例HTML文件的源代码]([substrate-docs/index.html at main · substrate-developer-hub/substrate-docs (github.com)](https://github.com/substrate-developer-hub/substrate-docs/blob/main/static/assets/quickstart/index.html))至您的代码编辑器中，并保存为`index.html`至本地。

3.   在浏览器中打开`index.html`。

4.   复制账号`Alice`的`SS58地址`到网页中的输入框中，然后点击`Get Balance`按钮。

## 关闭节点

1.   找到之前显示区块链操作信息的终端。
2.   键盘输入`Ctrl + C`以终止节点工作。

## 下一步做什么？

在本节快速开始指南中，您学习了在本地计算机上编译并运行一个单链区块链的方法。若想学习各种功能的个性化设置，请参阅以下资源：

-   [架构](https://docs.substrate.io/fundamentals/architecture/)
-   [运行时开发](https://docs.substrate.io/fundamentals/runtime-development/)
-   [为Substrate服务的Rust](https://docs.substrate.io/fundamentals/rust-basics/)