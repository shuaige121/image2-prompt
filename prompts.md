# image2 prompt 库 — 人物 / 食物 / 图生图

来源:OpenAI cookbook 官方指南 + Codex 内置 imagegen skill 文档 + 2026-06 多源研究(经对抗性核查)+ 本机实测。
所有片段直接可粘贴。gpt-image **没有 negative_prompt 参数**——一切排除项写成 prompt 内的自然语言句子。

## 通用骨架(官方 schema,只用有帮助的行)

```
Use case: <photorealistic-natural | product-mockup | ads-marketing | ...>
Primary request: <主需求>
Scene/backdrop: <环境>
Subject: <主体>
Style/medium: <photo / illustration / 3D>
Composition/framing: <机位/景别/留白>
Lighting/mood: <光线+情绪>
Materials/textures: <表面细节>
Text (verbatim): "<图内文字逐字>"
Constraints: <必须保留/避免>
```

具体的 prompt 只做规范化,不要乱加内容;泛泛的 prompt 才做克制的增补。

---

## 1. 人物自然 / 反恐怖谷

恐怖谷根因:模型向"理想完美"平均化(无毛孔皮肤、完美对称、死鱼眼、过白牙齿)+ 物理上不可能的默认打光 + gpt-image 偏暖 sepia 底色。修复 = 不完美词汇 + 摄影捕捉式叙述 + 封死风格化出口。

### 按影响力排序的技巧

1. **皮肤纹理词汇**(单项最高收益,OpenAI 官方背书):
   `natural skin texture with visible pores, fine vellus hair, faint blemishes, subtle oiliness and uneven skin tone; no airbrushing, no retouching, no beauty filter`
2. **字面写 "photorealistic" + 当作正在拍真照片来写**:
   `Photorealistic candid photograph, shot like a 35mm film photograph, natural color balance; the image should feel honest and unposed`
3. **防御性反风格化堆叠**(模型偷懒最易滑向插画/CGI):
   `Photorealistic. Real textures, natural skin, real fabric. No illustration, no CGI look. Do not stylise the face, do not cartoonise.`
4. **单一方向性自然光 + 真实阴影/眼神光**(不指定光线→蜡像感;皮肤纹理词在平光下失效):
   `soft window light from camera-left, gentle fill, natural shadow transitions, realistic catchlights`
5. **业余/抓拍美学**对抗职业摄影默认:
   `candid amateur snapshot, slightly off-center framing, mundane background, mild motion blur, no professional bokeh`(更狠:`on-camera flash photo`)
6. **报镜头和胶卷名而非质量词**(35mm 最自然 / 50mm 人眼 / 85mm 头像;gpt-image 对相机参数宽松解释,只影响整体观感):
   `35mm candid shot on Kodak Portra 400, subtle film grain, natural skin tones`
7. **具体的不完美人物描述替代泛美词**(同时破"千人一面"):
   `a 38-year-old man with tired eyes, faint stubble shadow and slightly crooked nose` ← 而不是 "a handsome man, 8k"
8. **非摆拍瞬间**:`caught mid-laugh while glancing off-camera, a few flyaway hairs, unstaged candid moment`
9. **反黄滤镜**(gpt-image 暖 sepia 偏置部分固有,prompt 只能部分缓解;兜底 LAB B 通道后期校正):
   `neutral white balance around 6000-6500K, accurate skin tones, bright whites, no yellow or sepia cast`
   同时避开暖色触发词:`cinematic` `golden hour` `vintage film`。
10. **五官专项**:
    - 牙:默认闭嘴 `relaxed expression, mouth closed` 或 `soft subtle smile, lips barely parted, teeth not prominent`;永不写 "perfect smile"。
    - 手:遮挡/占用最可靠 `hands in jacket pockets` / `one hand loosely wrapped around a coffee mug, fingers naturally curled`;反复失败改 shoulders-up。
    - 眼:`sharp focus on the eyes, realistic catchlights from the window light, slight natural moisture on the lower eyelids`(catchlight 必须与声明光源一致)。
11. (可选增强,社区共识)轻度不对称/疲劳痕迹:`slightly uneven brow line, faint crow's feet, subtle dark circles`

### 人物禁用词(出现即删)

- 美化词:`beautiful` `stunning` `flawless` `perfect skin` `ethereal` `perfect smile`
- 渲染栈:`8k` `ultra-detailed` `hyperreal` `unreal engine` `octane render` `CGI` `masterpiece` `high quality`
- 暖色触发:`cinematic` `golden hour` `vintage film`

### 编辑真人照片(identity lock)

`Do not change her face, facial features, skin tone, or identity in any way. Preserve her exact likeness.`
每轮迭代**逐字重复**,否则身份漂移。

### 实测验证 prompt(本机 2026-06-12,效果自然)

```
Use case: photorealistic-natural
Primary request: candid photo of a woman in her early 30s laughing mid-conversation at an outdoor street cafe, looking slightly away from camera
Style/medium: photorealistic candid photo, shot on 35mm film, Kodak Portra 400
Composition/framing: medium close-up, eye-level, slightly imperfect casual framing
Lighting/mood: natural late-afternoon side light, soft shadows
Materials/textures: real skin texture with visible pores, slight skin tone unevenness, a few flyaway hairs, natural teeth, subtle film grain
Constraints: natural color balance; no heavy retouching; no glamorization; no studio polish
Avoid: plastic skin, perfect symmetry, overly white teeth, dead stare into camera, heavy bokeh
```

---

## 2. 食物自然

根因:模型过度优化"摆拍特征"——对称、高光泽、过饱和、夸张分量。学术研究(Appetite 期刊)证实"差一点真实"的食物比真照片**更**令人不适——目标是物理合理性,不是堆细节。

### 万能骨架(9 槽位)

```
Photorealistic professional food photograph of [菜] on a matte white ceramic plate,
shot at a [机位], soft window light from camera left with gentle shadow fall-off,
[2-3 个具名纹理], [2-3 个真实感锚点], realistic portion size,
palette of [3 colors], shallow depth of field, subtle film grain
— no plastic glaze, no AI-perfect symmetry, no neon reds, no heavy retouching
```

### 要点

1. **约束子句直击已知失败模式**:
   `no plastic-looking glaze, no fake glossy surface, no AI-perfect symmetry, no neon reds, no text on dishes, realistic portion size`
2. **真实感锚点**(最强反 CGI 手段,每图 2-3 个,多了又像摆拍):
   `scattered crumbs` / `a smear of sauce on the plate rim` / `torn bread edge` / `juice pooling` / `uneven char` / `salt crystals` / `flour dusting` / `used fork resting beside the plate` / `fingerprints on glass` / `rumpled linen napkin`
3. **具名纹理替代食欲形容词**:`blistered charred crust, molten mozzarella with a slight oil sheen` ← 而不是 "delicious, mouthwatering"
4. **物理自洽的蒸汽/水珠**:蒸汽只在逆光/侧逆光可见;水珠是细密附着不是流淌:
   `backlit so a thin wisp of steam rises naturally; fine beads of condensation clinging to the cold glass`
5. **色板/道具**:限 3-4 个具名颜色防彩虹配菜;中性陶瓷器皿;背景与食物主色互补(棕橙烘焙物配冷灰蓝背景)。
6. **塑料感触发词照删**:`8k` `masterpiece` `perfect lighting` `smooth` `vibrant` `studio lighting`;负面约束别堆满("no noise, no blur, no shadows" 会逼向渲染感)。

### 机位速查(按菜品几何)

| 菜品 | 机位 | 片段 |
|---|---|---|
| 平铺:披萨/拼盘/寿司盘 | 90° 俯拍 | `overhead flat-lay, 90-degree top-down` |
| 一般摆盘/意面/沙拉/甜点 | 45°(默认) | `45-degree three-quarter hero angle` |
| 高层叠:汉堡/叠层 pancake/饮品 | 0° 平视 | `straight-on eye-level shot showing every layer` |
| 深碗:拉面/汤/咖喱/盖饭 | 30° | `three-quarter 30-degree angle into the bowl, showing surface and depth` |

光线标准答案(全来源一致):`soft natural window light from camera left, gentle shadow fall-off, daylight white balance, no flash`

### 两种具名模式

- **外卖/菜单图**(DoorDash/UberEats 规范;整套菜单同一机位):
  `delivery-app menu photo: single serving exactly as served, white plate on light wood counter, bright soft daylight, plain uncluttered background, 45-degree angle, no props, no text, landscape 16:9`
- **编辑部/杂志图**:
  `editorial food photography in the style of a Bon Appetit feature: dish off-center on a dark weathered wood table, rumpled linen napkin, moody window side-light, shallow depth of field, lived-in scene`

---

## 3. 图生图 / 参考图 prompt 模式

gpt-image-2 输入图行为(已验证):最多 16 张/次;**永远整图重新生成**(edit 不保留像素,"edit" vs "reference" 只是 prompting 上保留多少的区别);**输入图永远 high fidelity**(无参数可调);指令遵循好,详细的角色标注 + lock/vary 长 prompt 划算。

`image2.py --ref` 会自动注入角色标注行(`--ref-mode style|composition|subject|edit`),以下模式用于 spec 正文里进一步精确控制:

- **P1 角色标注**(多图必做,否则模型猜哪张是内容哪张是风格):
  `Image 1: composition reference — match the camera angle, framing, and plating style. Image 2: the actual dish to feature.`
- **P2 三通道点名**(style=色板/纹理/光、composition=布局/机位、identity=脸/产品;"same style" 这种含糊说法表现差):
  `Borrow only the visual language of Image 1: warm side lighting, shallow depth of field, muted earthy palette. Generate a completely new subject: [X].`
- **P3 Borrow / Do-not-borrow**("像但不抄"核心,竞品图安全用法):
  `Image 1 is a mood/lighting reference only. Borrow: the soft window side-light, dark moody backdrop, plating mood. Do not borrow: the dish itself, the plate design, any logos, text, props, or the exact scene. Generate an original photo of [our dish].`
- **P4 Match / Change / Do-not-copy**(构图迁移;多参考图加冲突优先级):
  `Match from Image 1: top-down camera, rule-of-thirds plating. Change: the dish is now [X]. Do not copy the reference's plate, table surface, or garnish. If Image 1 and Image 2 conflict, follow Image 2 for the food's appearance.`
- **P5 反漂移**(编辑迭代时,preserve list 每轮逐字重复):
  `Change only: the garnish. Keep everything else the same: plate, plating arrangement, camera angle, lighting direction, background, color grade.`
- **P6 文字桥两步法**(最大"灵感距离"兜底):先让 vision 描述参考图风格成文字 brief(不描述具体菜品/品牌),再不带图纯文字生成——零像素级复制。

**风格锁死陷阱**(已验证):同一会话里 image 工具会持续复制之前生成图的风格,人脸批量还会趋同。`image2.py` 每张图独立 `codex exec` 新会话,天然免疫——**不要**改成会话内迭代。

**触发词过度解释**:"sunrise" 必出太阳——改写 `sun fully illuminating the side of her face`。

---

## 4. 参考图获取(headless,2026-06-12 全部实测)

首选 `scripts/findref.py`(已内置全部卫生规则):

```bash
python3 ~/.claude/skills/image2/scripts/findref.py "卤肉饭 braised pork rice bowl delivery app photo" --n 3 --out ./refs
```

分层(脚本内已实现 1-2 层;3-4 层手动):

1. **DDG i.js**(默认):无 key、CJK 友好、带宽高。vqd 握手 → `duckduckgo.com/i.js?...&vqd=`。
2. **Bing murl 抓取**(回退):⚠️ URL 必须最简——加 `form=...&first=1` 参数会让 Bing 给 bot 返回缓存的无关结果(实测)。
3. **Pexels API**(如有 key,200 req/hr,许可最干净):`curl -H 'Authorization: KEY' 'https://api.pexels.com/v1/search?query=...'`;无 key 时 `images.pexels.com` CDN 可直接下载已知 URL。Unsplash 页面抓取已死(Anubis 401),CDN 已知 hash 仍可下。
4. **零版权暴露**:Wikimedia Commons API(要求描述性 UA)/ Openverse(匿名 20/min、200/day,逐图带 license);缺点是百科风照片,风格参考偏弱。

**封死路径(勿试)**:大众点评(302 验证墙)、UberEats(307 地理门控)、美团——ToS 禁爬 + 有诉讼先例;同样的照片 DDG/Bing 都能搜到。

**搜索词构造**:`{中文菜名} {英文菜名} delivery app photo`(双语翻倍候选多样性;意图词把结果从菜谱步骤图拉向商业美图)。

**卫生规则**(findref.py 已内置):magic-byte 校验(死链返回 HTML)、水印图库域名黑名单(`shutterstock|dreamstime|alamy|istockphoto|gettyimages`,污染风格且法律风险最高)、最小宽度 ≥600、浏览器 UA + DDG Referer、每菜 3 张即停。

**法律姿态**(非法律意见):参考图私用不发布是低风险灰区;真正的风险在**输出端**——生成图与参考实质性相似(同构图/道具/摆盘)则输出本身可侵权。缓解:① 优先 CC/免费图库;② 竞品图混 2-3 张而非单张;③ prompt 强制 restyle(P3/P4 模式,`--ref-mode style` 默认就带);④ 永不用带水印预览图。

---

## 5. 不要写进 prompt 的"伪事实"

- 不引用"人脸 10-15% 不对称"之类百分比(已证伪,无出处)。
- "牙齿 40% 失败率"等单一 SEO 源数字不复述;策略本身(闭嘴)有效。
- web 流传"图像轮次消耗 plan 限额比文字快 3-5 倍"与本机实测矛盾(15 张后 5h 窗口仍 0.0%)——以 `--usage` 实测为准。

---

## 6. 2026-06 研究升级(63 条发现 / 7-agent 汇总 → 并入 §2/§3 实操)

来源:OpenAI Cookbook《image-gen models prompting guide》+ gpt-image-1.5 指南 + Platform Image API + 社区项目。核心结论:**食物真实感来自"把 prompt 写成相机拍摄简报",不是堆质量词**。实测教训(破晓馒包子):`studio product photo / pure white background / high detail` 这类词直接产出平铺、无景深、过饱和的恐怖谷;改用下面的镜头语言后立刻变真实摄影。

### §2 食物配方升级(在 9 槽位基础上加这 4 条)

1. **镜头+光圈写死景深**(单项最高收益):
   `shot on a 50mm lens at f2.0, shallow depth of field with background falloff`
   英雄特写:`85mm lens, f1.8, creamy background bokeh`
2. **前景失焦元素**做景深分层(最易被忽略):
   `a softly out-of-focus herb sprig in the foreground, clear foreground-to-background separation`
3. **胶片色彩科学**(食物用 Portra 400,**禁用 Ektar**——太艳):
   `shot on Kodak Portra 400, muted film-like color science, subtle film grain`
4. **官方反恐怖谷收尾**(整段照抄,OpenAI cookbook 背书):
   `Shot like a 35mm film photograph, framing at eye level, using a 50mm lens. Soft window light, shallow depth of field, subtle film grain, natural color balance. The image should feel honest and unposed, with real texture and everyday detail. No glamorization, no heavy retouching.`

### §3 图生图升级(多图角色协议 + 防"贴图感")

5. **Role-block 默认模板**(多图必写,点名每张图职责):
   `Image 1: dish to preserve. Image 2: lighting/color-grade reference. Image 3: background.`
   `Change: only <X>. Preserve: food, plating, garnish count, plate, portion, colors, camera angle, framing. Constraints: no extra objects, no redesign, no extra utensils, no logos, no watermark.`
6. **防"贴图感"关键句**(把主体放进新背景时必加,collage→photo 的分水岭):
   `Use Image 1 as the dish photo and Image 2 as the background reference. Place the dish into the scene from Image 2. Preserve the dish shape, color, garnish, proportions, and material exactly. Match lighting, scale, shadow, and perspective. Do not restyle it.`
7. **gpt-image-2 机制**(官方/实测):
   - **没有 input_fidelity 参数**——输入图永远 high fidelity。
   - **mask 只命中第一张输入图**——要被 mask/编辑的图务必排成 Image 1。
   - 一次最多 16 张输入图。
8. **系列一致性 = baseline + style-bible 循环**:冻结一段 STYLE 块逐字复用,并把上一张 baseline 图传进每次调用:
   `STYLE: soft window light from camera-left, 50mm at f2.0, matte stoneware plates, muted earthy palette, subtle film grain`

### 食物禁用词补充(踩了就出 AI 味)
`8k` `masterpiece` `studio lighting` `vibrant` `smooth` `perfect lighting` `hyper-detailed` `Ektar`(过艳)。

### 相关项目/资源(2026-06 研究)
- **OpenAI Cookbook — image-gen prompting guide**(权威,photoreal 收尾 + 多图协议 + 机制):https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide
- GitHub `wuyoscar/GPT-Image2-Skill`(gpt-image-2 prompt/skill 参考)
- 参考图源:Pexels API / Wikimedia / Openverse(见 §4);食物按图检索 = Food-101 + CLIP+FAISS。
- 其它社区源(fal.ai / EvoLinkAI / peterRooo 等)在研究 angle JSON 里,需要再深挖。
