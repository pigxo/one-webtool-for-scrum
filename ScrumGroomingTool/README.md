项目设计
------------
> 这是一个管理TDD grooming、robot case 以及keyword的网站。
设计目的是能够有效的提高自动化case设计的实现，以期望最终能够实现自动的根据grooming的结果生成有效的robot case。

###网站的主要功能：
    * 能够实现在线编辑Grooming。
    * 能够实现Grooming的上传下载
    * 能够实现Grooming的查询
    * 能够实现通过Grooming产生的ATDD case输出直接产生Robot case并保存以及提供下载功能
    * 能够实现支持case的本地上传，并与Grooming 相关联
    * 能够实现通过Grooming 的相关信息查询robot case
    * 能够实现robot case id 查询Grooming的输出
    * 能够实现robot case的在线编辑
    * 能够实现keyword的查询，查询条件包括keyword name， scli/cli COMMADN, author,keyword 调用关系，以及特殊字段
    * 能够实现robot case在线编辑的自动补全功能
    * 自动补全功能能够按照keyword的使用频度等优化来匹配
    * 能够使用机器学习等算法来归纳keyword的使用，优化自动补全功能
    * 能够记录Grooming ATDD 常用关键字，并记录由该关键字常用的keyword，优化case 编辑的自动补全功能
    * 期望大量训练机器学习算法后，Grooming 的结果能直接生成可以执行的robot case
    * 能够有效对接cci ci等工程，记录case执行结果
    * 能够提供接口分析统计Grooming case keyword以及执行结果的相关数据
    * 用户管理

### 设计理念
     * 开源
     * 简洁易用
            网站前端采用了bootstrap的framwork(目前是如此)，以期望整个网站系统能提供简洁的UI，改网站核心的业务在于文档的编写，查询已经机器学习部分，不过多设计多媒体，所以在文本编辑方面采用markdown的编辑语法，而放弃了富文本编辑（可以讨论更好的设计）
           网站3大功能模块独立实现，降低耦合度
           提供接口，实现扩充
      * 分布式精细化
            用户管理以domain（或者team）建立用户组，以组为维度进行数据的搜索，学习。提供精准度。采用这样设计的原因是，各个domain（team）长期focus固定的模块上，设计case已经实现case的习惯会趋于固定，实现自动匹配keyword的时候更有针对性，提供自动匹配的效率。
           以用户组来实现分布式部署，这样各个组根据自己的需求部署自己的服务器
                   1）更有针对性的灵活的功能扩展
                   2）降低数据增大带来的服务器性能的问题
            首页会设计成所有服务器信息（目前首页用来记录项目信息），采用注册的形式，各个分布式服务器注册自己的地址，各个服务器采用restful api 获取完整的数据。
               
     


PHASE 1 : Grooming Edit -->  Draft Robot case
-------
> 第一阶段，实现Grooming的编辑以及自动产生robot case

####定义Grooming里的字段
    1 定义grooming字段  title sprint ranfeather  S Q A ATTD
    2 增加robot case的tag
    3 定义好atdd的字段

####实现Grooming的编辑功能
     1. 设计编辑的样式

####实现转化robot的功能
     1. 定义转化robot的关键字
     2.定义robotcase的存储路径

PHASE2: Robot Case on-line Edit
-------
> 第二阶段，实现Robot Case的在线编辑功能，该阶段不包含自动补全，该阶段期望能够实现可以demo的版本，在这个版本中基本功能能够实现grooming的编辑，生成robot case， 已经编辑生成的robot case到可执行的case，提供case的上传下载。

####Robot case的打开编辑
     1.robot case可以在线打开
     2.robot case保存更新
 
####Robot case的下载
    1. 生成的case 提供下载功能

####Robot case的上传
     1.本地case可以上传到server，并能打开修改下载
     2.关联grooming

####demo版本的部署
    1.部署到生产环境，能够正常运行
    2.优化前端显示，期望UI更简洁实用（如果时间充足）