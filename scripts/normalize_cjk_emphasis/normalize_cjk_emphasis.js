import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkCjkFriendly from 'remark-cjk-friendly';
import remarkStringify from 'remark-stringify';
import { visit } from 'unist-util-visit';

const isCJK = (char) => /[\u4e00-\u9fa5\u3400-\u4dbf\u{20000}-\u{2a6df}\u{2a700}-\u{2b73f}\u{2b740}-\u{2b81f}\u{2b820}-\u{2ceaf}\uf900-\ufaff\u3300-\u33ff\ufe30-\ufe4f]/.test(char);

function cjkSpacedEmphasis() {
  return (tree) => {
    visit(tree, (node, index, parent) => {
      if (!parent || index === null || !['strong', 'emphasis'].includes(node.type)) return;

      let insertBefore = false;
      let insertAfter = false;

      // Check before the emphasis/strong
      const prevNode = parent.children[index - 1];
      if (prevNode && prevNode.type === 'text') {
        const lastChar = prevNode.value.slice(-1);
        if (isCJK(lastChar)) {
          prevNode.value += ' ';
        }
      } else if (!prevNode || prevNode.type !== 'text' || !prevNode.value.endsWith(' ')) {
        insertBefore = true;
      }

      // Check after the emphasis/strong
      const firstChild = node.children[0];
      if (firstChild && firstChild.type === 'text') {
        const firstChar = firstChild.value[0];
        if (isCJK(firstChar)) {
          firstChild.value = ' ' + firstChild.value;
        }
      }

      const lastChild = node.children[node.children.length - 1];
      if (lastChild && lastChild.type === 'text') {
        const lastChar = lastChild.value.slice(-1);
        if (isCJK(lastChar)) {
          insertAfter = true;
        }
      }

      if (insertBefore) {
        parent.children.splice(index, 0, { type: 'text', value: ' ' });
      }

      if (insertAfter) {
        const afterIndex = index + (insertBefore ? 2 : 1);
        const nextNode = parent.children[afterIndex];
        if (nextNode && nextNode.type === 'text') {
          nextNode.value = ' ' + nextNode.value;
        } else {
          parent.children.splice(afterIndex, 0, { type: 'text', value: ' ' });
        }
      }
    });
  };
}

const processor = unified()
  .use(remarkParse)
  .use(remarkCjkFriendly)
  .use(cjkSpacedEmphasis)
  .use(remarkStringify, {
    bullet: '-',
    emphasis: '*',
    strong: '**',
    listItemIndent: 'one',
  });

export default processor;
console.log('Script ready. Use processor.processSync(md) to normalize.');