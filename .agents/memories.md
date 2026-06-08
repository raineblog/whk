Memories

Add Memory
Enable memories to let Jules use context from your past sessions to improve its responses. Learn more.

Terminology & Style: Consistently use '代入' instead of '带入', '酸碱' instead of '酸减', and '令' instead of '另' for assumptions (e.g., '令 f(x)=0'). Avoid using '一下' and instead use '以下' in formal descriptions per .agents/rules/style.md.


我怀疑你严重违反我的要求，请你审查自己的错误，严格修复！禁止使用任何基于批量大规模替换，我者未经严格审查的替换，你严重违反了我的要求，请你立刻修复！

User avatar

Scientific Accuracy Rules: Trichlorosilane (SiHCl3) is '三氯氢硅'; Black powder composition is S + 2KNO3 + 3C; Aluminum sulfide (Al2S3) produces H2S upon hydrolysis; Gold cyanidation requires 4Au + 8NaCN + O2 + 2H2O.


Repository Context: docs/science/element/fe.md serves as a comprehensive guide for all transition elements, not exclusively iron.


错误范例：有一些 $\ce{}$ 内部的，你也给替换成 $\ce{}$ 了，导致 \ce{} 嵌套，这是绝对禁止的

User avatar

Formatting Rule: 应该用公式没用用数学公式的，应该用 $\ce{}$ 但是没用的（可能的有直接写纯文字、直接 $Fe^{3+}$ 或者用 $\text{}$ 这都是错的，应该用 $\ce{}$ 代替）

User avatar

$\ce{}$ 中沉淀气体，就是 v 和 ^，注意这个符号要和前面后面至少隔一个空格

User avatar

Coding Standard: Markdown files must strictly adhere to the rules defined in .markdownlint.json .autocorrectrc and .agents\rules\style.md.

User avatar

Formatting Rule: LaTeX line breaks within environments like cases or aligned must use \\ (double backslash) to prevent KaTeX rendering failures in the Markdown parser.


Integration Rule: All AI review comments, including those without explicit commit suggestions (text-only hints), must be thoroughly researched and applied to the content.


Workflow Requirement: Before executing large-scale documentation changes, initiate a subagent to collect and catalog specific instances of errors and formatting violations (e.g., frontmatter spacing, list indentation, formula spacing, and quotes) to inform a perfectionist manual audit.


Reporting Requirement: When modifying multiple files, provide a complete list of all modifications specifying exactly what was changed in each file to ensure transparency and review compliance.


Formatting Rule: List indentation must be strictly preserved; removing leading spaces or flattening nested bullet points is considered an erroneous change.


Formatting Rule: YAML frontmatter lists must not contain empty lines between list items; extra newlines in the frontmatter are considered meaningless.


Formatting Rule: Multi-line display math blocks ($$) must be preceded and followed by a blank line, but must not have blank lines immediately inside the opening or closing delimiters.


User Requirement: Chinese main body text must use Chinese quotation marks (“ ”); however, technical attributes (e.g., { width="80%" }) and Markdown links must retain straight English double quotes.


Workflow: A specialized review skill is located at .agents/skills/review-workflow/ with a linting script review.js.


Repository Context: This is RainPPR's WHK (Wenhua Ke) Blog, containing educational notes on subjects like Science (Biology, Chemistry, Physics, Math) and Culture (Chinese writing, philosophy).


Technical Caveat: When performing automated quote replacement, do not alter scientific or mathematical notation such as derivatives (e.g., f', f'') or DNA sequence notation (e.g., 5', 3') as these require single quotes.


Environment: Linting and formatting tools 'autocorrect' and 'markdownlint-cli2' are located in ./node_modules/.bin/.

