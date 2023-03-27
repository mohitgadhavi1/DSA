// Define the Node Class

class Node {
	constructor(val) {
		this.val = val;
		this.child = [];
	}
	addChild(node) {
		this.child.push(node);
	}
}

// Define the Tree Class

class Tree {
	constructor(root) {
		this.root = root;
	}
}

//create some nodes

const root = new Node(1);
const child1 = new Node(2);
const child2 = new Node(3);
const grandchild1 = new Node(4);
const grandchild2 = new Node(5);

//Build the tree
root.addChild(child1);
root.addChild(child2);
child1.addChild(grandchild1);
child2.addChild(grandchild2);

//create the tree
const tree = new Tree(root);

console.log(tree);
