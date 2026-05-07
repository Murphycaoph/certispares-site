# CertiSpares Commercial Content Audit

Date: 2026-05-06

Scope: non-blog pages only. Blog articles are excluded, but homepage sections that promote blog content are considered as part of the homepage experience.

Core positioning being audited:

> Commercial Vehicle & Industrial Aftermarket Sourcing Partner from China

Audit lens: buyer trust, RFQ conversion, sourcing execution, and whether the site feels like it is run by people who actually coordinate China aftermarket supply.

## 1. 全站总体评价

### 当前网站像什么

现在的 CertiSpares 已经不像普通中国外贸模板站，也不像低质量 SEO 目录站。它更像一个正在从“能看的网站”进入“RFQ-first sourcing system”的 B2B 网站。

优点很明确：全站反复强调 RFQ、OE number、VIN、photos、supplier comparison、QC、packing、documents、shipment coordination。这些词不是装饰，它们基本构成了网站的业务骨架。

但问题也很明确：网站还没有完全像“真实接 WhatsApp 询盘、整理 OE/车型/照片、和工厂反复确认适配的人”。它更像一个已经理解 sourcing 方法论的人写出来的网站，而不是一个把真实采购桌面摊开给买家看的页面。

### 最大优势

1. **定位大方向正确**：站点明确不是 factory、不是 public catalog、不是 fake SKU database，而是 RFQ-first sourcing support。
2. **Contact 和 How It Works 很强**：这两个页面真的告诉买家该发什么、下一步怎么走、24-48 小时内会发生什么。
3. **系统页比普通 B2B 页面可信**：brake、suspension、air system、cooling、rubber/bushing 等页面写到了 dimensions、chamber type、valve spec、thread size、port size、hardness、core dimensions 等匹配变量，这些是真采购语言。
4. **没有明显中国外贸低端套话**：全站没有大规模出现 `best quality`、`cheap price`、`professional manufacturer`、`one-stop solution` 这类灾难级表达。
5. **商业模型有差异化**：multi-supplier consolidation、balanced multi-SKU sourcing、lower landed cost、inventory turnover 这条线是有战略价值的。

### 最大问题

1. **内容太爱解释“模型”，不够展示“执行现场”**。很多段落讲 sourcing logic、clearer scope、workable flow，但缺少真实 RFQ 例子、澄清问题样式、供应商比较表样式、装箱/包装/文件检查样式。
2. **品牌页模板化最明显**。10 个品牌页几乎共用同一套 hero、pain points、process、FAQ。对 SEO 和转化都有风险：买家会感觉“换个 logo，内容差不多”。
3. **Cases 页面缺失**。用户要求重点关注 Cases，但本地非 blog 页面中没有 Cases 页面。这是信任链路最大缺口之一。
4. **首页后半段有重复**。首页多次讲 sourcing、consolidation、capabilities、workflow，信息增量逐渐降低。
5. **全站缺少“真实询盘前后的样子”**。例如没有 RFQ template、sample comparison sheet、packing mark checklist、QC photo checklist、clarification questions。

## 2. Top Priority 必须优先修复

### P0-1. 新增 Cases / RFQ Examples 页面

当前没有 `cases` 页面。对于 B2B sourcing 站，这是硬伤。

建议新增页面：

- `/cases/` 或 `/rfq-examples/`
- 不写夸张成功案例，不写虚假金额。
- 写 3-5 个匿名真实业务场景：
  - Mixed brake RFQ: chambers + linings + valves + drums
  - Cooling RFQ: radiator/intercooler dimensions mismatch clarification
  - Rubber/bushing RFQ: ID/OD/length/hardness confirmation
  - Multi-supplier container: 3 suppliers, one loading plan, packaging mark alignment
  - Brand-platform RFQ: HOWO/Shacman platform where OE was missing but photos and dimensions helped

每个 case 应该包含：

- Buyer sent
- Risk found
- What we clarified
- Supplier comparison basis
- QC / packing / document checkpoint
- Resulting next step

这会立刻把网站从“讲方法论”推进到“像真实做过单子”。

### P0-2. 重写品牌页 hero 和 FAQ，减少一眼可见的模板感

现状：

所有品牌页基本是：

- `Send your [Brand] parts inquiry and narrow the right platform before you chat with us`
- `Narrow down the right [Brand] platform before you reach out...`
- FAQ 也基本相同。

问题：

这对 buyer trust 不够。尤其 MAN、Volvo Truck、Mercedes-Benz Truck 这类非中国品牌页面，如果和 HOWO、Shacman 用几乎同一种话术，会让人怀疑授权、供应深度和真实边界。

建议：

- P0 中国重点品牌 Sinotruk/HOWO/Shacman/Foton/Dongfeng/FAW/JAC 分别写差异化开头。
- P2 国际品牌页面必须更谨慎：强调 independent aftermarket inquiry support，不暗示授权、不暗示 full coverage。
- 每个品牌页增加 1 个“common RFQ pattern”模块：
  - Example: `Typical HOWO inquiry starts with OE number + old supplier photo + mixed brake/air items.`
  - Example: `For Mercedes-Benz Truck inquiries, we first treat brand/model/OE as identification inputs, not automatic fitment conclusions.`

### P0-3. 将 Contact 从“表单页”升级为“结构化 RFQ 页面”

Contact 已经是全站强项，但还可以变成真正的 RFQ hub。

目前字段不错：name/company/email/destination/info type/qty/parts/files/pack/notes。

缺失：

- VIN / vehicle model 独立字段
- OE number / part number 独立字段
- Incoterms 字段
- preferred contact method
- old supplier reference / target market
- source page context hidden field

建议：

- 页面标题可以从 `Send Your Truck Parts RFQ` 调整为 `Send a Structured Truck Parts RFQ`。
- 加一个 compact checklist：`Minimum useful RFQ`.
- 增加 WhatsApp 快捷文案模板，例如：
  - `Hello, I have a truck parts RFQ. Brand/model: __. OE/part no: __. Qty: __. Destination: __. Photos available: yes/no.`

### P0-4. 首页删除或合并重复 section

首页当前信息方向正确，但过长，后半段开始重复。

建议合并：

- `What We Do`
- `Why Choose Us`
- `How It Works`

可以改成一个更采购化的 section：

`From RFQ to Repeat Shipment`

里面放 4 个块：

- Match: OE / VIN / photo / dimensions
- Compare: supplier options / MOQ / lead time / quality basis
- Control: QC / packing / documents
- Consolidate: mixed suppliers / one shipment / reorder logic

建议删除或压缩：

- `Latest Insights` 在首页可以保留 2-3 个链接，但不应占太多商业页面空间。
- `A Sourcing Page Should Feel Like an Operating Desk` 这个标题很聪明，但它像给网站审稿人看的，不像给采购买家看的。建议改成更买家视角：`What We Check Before a Quote Becomes Useful`.

### P0-5. 修复 BaseLayout 默认 description

`BaseLayout.astro` 默认 description 仍是：

`One-stop automotive parts sourcing from China.`

问题：

这是全站策略中明确要避免的表达之一。虽然多数页面覆盖了 description，但作为默认值它和定位冲突。

建议改成：

`RFQ-first commercial vehicle aftermarket sourcing support from China.`

## 3. Mid Priority 中期优化

### P1-1. Sourcing 页要减少“经济模型感”，增加操作证据

`/sourcing/` 的商业逻辑非常重要，但现在太多内容在解释 container consolidation 和 inventory turnover，容易像咨询文章或 pitch deck。

尤其 `Benchmark Snapshot` 提到：

- April 2026 public-lane benchmark model
- illustrative distributor model
- 50% to 100%
- 1.5x to 3.0x

风险：

如果页面没有展示计算假设、来源、适用条件，这些数字会降低信任。B2B 买家会问：这个 benchmark 是谁算的？适用于哪个港口？20GP 还是 40HQ？货类是什么？

建议：

- 将 benchmark 区块压缩。
- 增加 `What we need to build a consolidation plan`：
  - supplier pickup city
  - SKU carton size / CBM / gross weight
  - MOQ
  - destination port
  - packaging mark rules
  - inspection requirement
- 增加一个 `Consolidation checklist`，比讲 turnover 更像执行方。

### P1-2. Capabilities 页要从“能力列表”变成“交付物证据”

`/capabilities/` 写了 supplier screening、inspection checkpoints、document consistency、consolidation planning，方向对。

但 `What We Do` 部分还是 capability cards，缺少可视化输出。

建议新增模块：

`What You Can Expect to Receive`

具体列：

- RFQ clarification notes
- supplier comparison summary
- sample / pre-shipment photo set
- packing mark confirmation
- PI / CI / PL consistency check
- loading photos or loading status

如果不展示这些，`capabilities` 仍然像服务介绍，不像可执行交付。

### P1-3. Product entry 页要降低 catalog 误会

`/product/` 的思路是对的：brand entry + part-system entry。

问题：

- URL 和导航叫 `Product`，容易让买家以为是 catalog。
- SEO keywords 里有 `truck parts catalog by brand`，这和 RFQ-first 定位不完全一致。

建议：

- 导航标签从 `Product` 改成 `RFQ Entry` 或 `Parts RFQ`。
- 页面标题可从 `Find the right truck parts from China...` 改为 `Start a Truck Parts RFQ by Brand or Part System`。
- keywords 避免 `catalog`，改成 `truck parts RFQ by brand`、`part system RFQ`。

### P1-4. 系统页增加“常见错误输入 vs 更好输入”

系统页已经是最有业务感的一组页面，但还可以更像真实 operator。

例如 brake 页可新增：

| Weak input | Better input |
|---|---|
| brake chamber | chamber type + stroke + port/thread + OE/photo |
| brake drum | OD/height/bolt holes + OE/photo |
| valve | OE/ref no + port size + pressure spec/photo |

每个系统页都可以做类似小表格。这比再写一段 `we compare workable suppliers` 更有转化价值。

### P1-5. 国际品牌页面增加授权与边界说明

MAN、Volvo Truck、Mercedes-Benz Truck 页面必须特别小心。

建议增加统一但清晰的 disclaimer：

`Brand names and model references are used only to identify inquiry scope. CertiSpares is an independent sourcing and RFQ support service unless explicit authorization is stated.`

同时避免“平台支持范围”看起来像官方替代目录。

## 4. Low Priority 后期优化

1. 页脚 `Sourcing Categories` 描述不准。它链接到 `/sourcing/`，但这个页面是 service strategy，不是 category page。建议改成 `Sourcing Strategy`。
2. Header 导航中 `Insights` 可后移，商业转化页优先级应高于 blog。
3. 首页品牌 logo marquee 可以保留，但应考虑加一句独立 sourcing disclaimer，避免品牌授权误解。
4. Thank-you 页可以增强后续行动：提示继续通过 WhatsApp 补照片、补 Excel、补 packing requirements。
5. 可增加 `/rfq/` 目标架构路径，目前项目上下文里已经写了 target architecture，但实际 public path 还是 `/contact/`。

## 5. 最像真实 sourcing operator 的页面

### 1. Contact

最真实。原因：

- 明确要求 OE number、vehicle model、quantity、destination。
- 有 file upload。
- 有 WhatsApp。
- 有 24-48 hour response expectation。
- 有 minimum needed 和 helpful extras。

缺点：

仍然像 contact form，还没完全升级为 RFQ workflow intake。

### 2. How It Works

非常接近真实采购流程：

- Submit RFQ
- Technical matching
- Supplier sourcing & comparison
- Quotation consolidation
- Order execution & delivery

尤其 `What we need from you` 是强模块，应该复用到更多页面。

### 3. 系统页，尤其 brake / air system / cooling / rubber-bushing

这些页面有真实匹配变量：

- chamber type
- valve spec
- thread size
- port size
- pressure spec
- core dimensions
- inlet/outlet position
- hardness
- inner/outer diameter

这是全站最不像泛 SEO 的内容。

## 6. AI 味最重的页面

### 1. 品牌页

不是因为内容错，而是重复太明显。

高风险句式：

- `Send your [Brand] parts inquiry and narrow the right platform before you chat with us`
- `Narrow down the right [Brand] platform before you reach out, so we can start from a clearer scope and move faster on matching and quotation.`
- `We compare suppliers on execution, not only price`
- `We support mixed orders`

这些句子单独看都可以，但 10 个品牌页面重复出现，就会变成模板味。

### 2. About

About 比传统公司介绍好很多，但有些句子太抽象：

- `The company is built around structured sourcing, supplier comparison, and controllable execution rather than broad catalogue presentation or generic trading language.`
- `The underlying logic is simple: clarify the RFQ, compare with discipline, control key risk points, and make the sourcing path easier to repeat.`

这些像定位稿，不像 founder 真实说话。

建议加入更具体的 founder/operator 语气：

- `Most mistakes start before quotation: unclear OE, missing photos, wrong application, or suppliers quoting different scopes. CertiSpares exists to slow that part down before the order speeds up.`

### 3. Sourcing

AI 味不是句式，而是“模型过度完整”。很多内容像战略文章：

- lower landed cost
- balanced multi-SKU sourcing
- inventory turnover
- GMROI effect
- illustrative distributor model

建议保留方向，但压缩模型解释，换成执行 checklist 和真实 RFQ examples。

## 7. 最影响转化的内容问题

1. **没有 Cases / RFQ examples**。这是最大问题。
2. **品牌页同质化**。买家进入具体品牌页后，没有感到“这个品牌有独立经验”。
3. **CTA 仍偏通用**。大量 `Send RFQ`、`Contact Us`，但少了上下文 CTA：
   - `Send brake chamber details`
   - `Send VIN/OE/photos for this platform`
   - `Send mixed SKU list for consolidation review`
4. **没有 WhatsApp 低阻力模板**。WhatsApp 有入口，但没有帮买家组织第一句话。
5. **缺少可预期交付物**。买家不知道最后会收到 comparison sheet、QC photo set、packing check record，还是普通邮件报价。

## 8. 最值得保留的内容结构

1. Contact 的 RFQ 表单结构。
2. How It Works 的 5-step workflow。
3. Product entry 的 brand path / part-system path 双入口。
4. 系统页的 pain points + matching inputs + process + FAQ。
5. Capabilities 的 service boundaries，特别是：
   - We are not a factory
   - No unrealistic claims
   - Clear QC scope
   - Traceable paperwork

这些都符合 RFQ-first positioning，应该保留并继续深化。

## 9. 建议删除或压缩的内容

1. 首页 `Latest Insights` 压缩，不要让 blog 抢商业页面主线。
2. 首页 `What We Do`、`Why Choose Us`、`How It Works` 合并。
3. Sourcing 页 `Benchmark Snapshot` 压缩，除非补充更清晰的计算依据。
4. 品牌页重复 FAQ 应重写，不要 10 个品牌共用同一语气。
5. BaseLayout 默认 `One-stop automotive parts sourcing from China` 删除。

## 10. 建议新增的内容模块

### 全站通用

- `Minimum useful RFQ`
- `What we check before quotation`
- `Common weak input vs better input`
- `What you receive after review`
- `Independent sourcing disclaimer`
- `WhatsApp RFQ starter`

### 首页

- `What We Check Before a Quote Becomes Useful`
- `From RFQ to Repeat Shipment`
- `Send us what you already have`

### About

- `Why most sourcing mistakes start before quotation`
- founder/operator note，用真实业务语境替代定位稿语气

### How It Works

- `Sample clarification questions`
- `What a compared quotation should include`

### Capabilities

- `Sample deliverables`
- `Inspection evidence examples`
- `Document consistency checklist`

### Sourcing

- `Consolidation plan checklist`
- `Mixed-SKU container example`

### Brand pages

- `Typical RFQ pattern for this brand`
- `Common systems requested`
- `Brand-specific matching cautions`
- international brand disclaimer for MAN / Volvo Truck / Mercedes-Benz Truck

### Product system pages

- `Weak input vs better input`
- `Match-critical fields`
- `Common supplier quote mismatch`

## 11. 页面级审计表

| Page type | Current strength | Main issue | Priority |
|---|---|---|---|
| Home | Strong positioning, strong sourcing model, clear RFQ CTA | Too many repeated sections; some titles feel written for auditors, not buyers | P0 |
| About | Good anti-factory positioning, useful founder/audit angle | Too conceptual; not enough real operator voice | P1 |
| How It Works | Clear buyer flow and RFQ inputs | Could add sample clarification questions and expected outputs | P1 |
| Capabilities | Good capability boundaries and QC/document language | Needs proof of deliverables, not only capability claims | P1 |
| Sourcing | Differentiated commercial model | Too model-heavy; benchmark claims need context | P1 |
| Contact | Best RFQ conversion page | Needs more structured RFQ fields and WhatsApp starter | P0 |
| Product entry | Good brand/system RFQ split | `Product` label risks catalog expectation | P1 |
| Brand pages | Useful platform browser and WhatsApp CTA | Template repetition across brands; weak brand-specific trust | P0 |
| System pages | Strongest real sourcing details | Need weak-vs-better input tables and more category-specific CTA | P1 |
| Thank-you | Functional | Could guide buyer to send extra photos/files via WhatsApp/email | P2 |
| Cases | Missing | Major trust gap | P0 |

## Final judgment

CertiSpares is already above the average China aftermarket sourcing website. It avoids most cheap外贸模板 language and has a real RFQ-first architecture.

But the next stage is not “more SEO content”. The next stage is **operational proof**:

- show what buyers send
- show what you clarify
- show how suppliers are compared
- show what QC / packing / document checkpoints look like
- show how a mixed order becomes a workable shipment

The site should sound less like:

> We have a structured sourcing workflow.

And more like:

> Send the OE number if you have it. If not, send the photo, vehicle model, dimensions, and quantity. We will first check whether suppliers are quoting the same scope before you compare price.

That is the voice of a real sourcing operator.
